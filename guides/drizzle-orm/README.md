# Drizzle ORM Guide

TypeScript-first SQL toolkit for type-safe database access with zero-abstraction overhead.

## Source

Based on [Drizzle ORM official documentation](https://orm.drizzle.team/docs/overview) and production patterns.

## Categories

| Priority | Category | Impact |
|----------|----------|--------|
| 1 | Schema Definition | CRITICAL |
| 2 | Query Building | CRITICAL |
| 3 | Migrations (drizzle-kit) | CRITICAL |
| 4 | Type-Safe Queries | HIGH |
| 5 | Joins & Relations | HIGH |
| 6 | Transactions | HIGH |
| 7 | Performance Patterns | MEDIUM |
| 8 | Common Pitfalls | MEDIUM |

## Quick Reference

### Supported Databases

| Database | Package | Driver |
|----------|---------|--------|
| PostgreSQL | `drizzle-orm/pg-core` | `postgres`, `@neondatabase/serverless`, `@vercel/postgres` |
| MySQL | `drizzle-orm/mysql-core` | `mysql2` |
| SQLite | `drizzle-orm/sqlite-core` | `better-sqlite3`, `@libsql/client` |

### Installation

```bash
# Core ORM + Kit (migration tool)
npm install drizzle-orm
npm install -D drizzle-kit

# PostgreSQL example
npm install drizzle-orm postgres
npm install -D drizzle-kit
```

---

## 1. Schema Definition

### Tables and Columns

```typescript
// src/db/schema.ts
import {
  pgTable,
  serial,
  text,
  varchar,
  integer,
  boolean,
  timestamp,
  jsonb,
  uuid,
  pgEnum,
} from "drizzle-orm/pg-core";

// Enums
export const roleEnum = pgEnum("role", ["admin", "user", "guest"]);

// Users table
export const users = pgTable("users", {
  id: serial("id").primaryKey(),
  name: varchar("name", { length: 255 }).notNull(),
  email: varchar("email", { length: 255 }).notNull().unique(),
  role: roleEnum("role").default("user").notNull(),
  isActive: boolean("is_active").default(true).notNull(),
  metadata: jsonb("metadata").$type<{ preferences: Record<string, string> }>(),
  createdAt: timestamp("created_at").defaultNow().notNull(),
  updatedAt: timestamp("updated_at").defaultNow().notNull(),
});

// Posts table
export const posts = pgTable("posts", {
  id: uuid("id").defaultRandom().primaryKey(),
  title: varchar("title", { length: 500 }).notNull(),
  content: text("content"),
  authorId: integer("author_id")
    .notNull()
    .references(() => users.id, { onDelete: "cascade" }),
  publishedAt: timestamp("published_at"),
  createdAt: timestamp("created_at").defaultNow().notNull(),
});
```

### Column Type Quick Reference

| TypeScript | PostgreSQL | MySQL | SQLite |
|------------|------------|-------|--------|
| `serial` | `SERIAL` | `INT AUTO_INCREMENT` | `INTEGER` |
| `integer` | `INTEGER` | `INT` | `INTEGER` |
| `text` | `TEXT` | `TEXT` | `TEXT` |
| `varchar` | `VARCHAR(n)` | `VARCHAR(n)` | `TEXT` |
| `boolean` | `BOOLEAN` | `BOOLEAN` | `INTEGER` |
| `timestamp` | `TIMESTAMP` | `TIMESTAMP` | `TEXT` |
| `jsonb` | `JSONB` | `JSON` | `TEXT` |
| `uuid` | `UUID` | `VARCHAR(36)` | `TEXT` |
| `real` | `REAL` | `FLOAT` | `REAL` |
| `numeric` | `NUMERIC` | `DECIMAL` | `NUMERIC` |

### Indexes and Constraints

```typescript
import { pgTable, serial, varchar, integer, index, uniqueIndex } from "drizzle-orm/pg-core";

export const products = pgTable(
  "products",
  {
    id: serial("id").primaryKey(),
    name: varchar("name", { length: 255 }).notNull(),
    sku: varchar("sku", { length: 100 }).notNull(),
    categoryId: integer("category_id").notNull(),
    price: integer("price").notNull(), // Store as cents
  },
  (table) => [
    uniqueIndex("products_sku_idx").on(table.sku),
    index("products_category_idx").on(table.categoryId),
    index("products_name_search_idx").on(table.name),
  ]
);
```

### Relations (Relational Query Builder)

```typescript
import { relations } from "drizzle-orm";

export const usersRelations = relations(users, ({ many }) => ({
  posts: many(posts),
}));

export const postsRelations = relations(posts, ({ one }) => ({
  author: one(users, {
    fields: [posts.authorId],
    references: [users.id],
  }),
}));
```

**Important**: Relations are for the relational query builder (`db.query.*`) only. They do not create foreign keys in the database. Use `.references()` on columns for actual foreign key constraints.

---

## 2. Database Connection

```typescript
// src/db/index.ts
import { drizzle } from "drizzle-orm/postgres-js";
import postgres from "postgres";
import * as schema from "./schema";

// Connection string from environment
const connectionString = process.env.DATABASE_URL!;

// For query usage (connection pool)
const client = postgres(connectionString, {
  max: 10,           // Max pool size
  idle_timeout: 20,  // Close idle connections after 20s
  max_lifetime: 60 * 30, // Max connection lifetime 30 min
});

export const db = drizzle(client, { schema });
```

### Serverless / Edge

```typescript
// Neon serverless
import { neon } from "@neondatabase/serverless";
import { drizzle } from "drizzle-orm/neon-http";

const sql = neon(process.env.DATABASE_URL!);
export const db = drizzle(sql, { schema });

// Vercel Postgres
import { sql } from "@vercel/postgres";
import { drizzle } from "drizzle-orm/vercel-postgres";

export const db = drizzle(sql, { schema });
```

---

## 3. Query Building

### Select

```typescript
import { eq, ne, gt, lt, gte, lte, like, ilike, and, or, not, inArray, isNull, between, sql } from "drizzle-orm";

// Basic select
const allUsers = await db.select().from(users);

// Select specific columns
const userNames = await db
  .select({ id: users.id, name: users.name })
  .from(users);

// Where clause
const activeAdmins = await db
  .select()
  .from(users)
  .where(and(eq(users.role, "admin"), eq(users.isActive, true)));

// Multiple conditions
const filteredUsers = await db
  .select()
  .from(users)
  .where(
    or(
      eq(users.role, "admin"),
      and(eq(users.role, "user"), gt(users.createdAt, new Date("2024-01-01")))
    )
  );

// LIKE / ILIKE
const searchResults = await db
  .select()
  .from(users)
  .where(ilike(users.name, `%${searchTerm}%`));

// IN array
const specificUsers = await db
  .select()
  .from(users)
  .where(inArray(users.id, [1, 2, 3]));

// NULL check
const unverifiedUsers = await db
  .select()
  .from(users)
  .where(isNull(users.metadata));

// Ordering
const sortedUsers = await db
  .select()
  .from(users)
  .orderBy(users.createdAt)    // ASC default
  .limit(10)
  .offset(20);

// DESC ordering
import { desc, asc } from "drizzle-orm";
const recentUsers = await db
  .select()
  .from(users)
  .orderBy(desc(users.createdAt));
```

### Insert

```typescript
// Single insert
const newUser = await db
  .insert(users)
  .values({
    name: "Alice",
    email: "alice@example.com",
    role: "user",
  })
  .returning(); // Returns inserted row(s)

// Batch insert
const newUsers = await db
  .insert(users)
  .values([
    { name: "Bob", email: "bob@example.com" },
    { name: "Carol", email: "carol@example.com" },
  ])
  .returning({ id: users.id, email: users.email });

// Upsert (INSERT ... ON CONFLICT)
await db
  .insert(users)
  .values({ name: "Alice", email: "alice@example.com" })
  .onConflictDoUpdate({
    target: users.email,
    set: { name: "Alice Updated", updatedAt: new Date() },
  });

// INSERT ... ON CONFLICT DO NOTHING
await db
  .insert(users)
  .values({ name: "Alice", email: "alice@example.com" })
  .onConflictDoNothing({ target: users.email });
```

### Update

```typescript
// Update with condition
const updated = await db
  .update(users)
  .set({
    isActive: false,
    updatedAt: new Date(),
  })
  .where(eq(users.id, 1))
  .returning();

// Update with SQL expression
await db
  .update(products)
  .set({
    price: sql`${products.price} * 1.1`, // 10% price increase
  })
  .where(eq(products.categoryId, 5));
```

### Delete

```typescript
// Delete with condition
const deleted = await db
  .delete(users)
  .where(eq(users.id, 1))
  .returning();

// Bulk delete
await db
  .delete(users)
  .where(
    and(
      eq(users.isActive, false),
      lt(users.createdAt, new Date("2023-01-01"))
    )
  );
```

### Aggregations

```typescript
import { count, sum, avg, min, max } from "drizzle-orm";

// Count
const [{ total }] = await db
  .select({ total: count() })
  .from(users);

// Count with condition
const [{ activeCount }] = await db
  .select({ activeCount: count() })
  .from(users)
  .where(eq(users.isActive, true));

// Group by with aggregation
const postsByAuthor = await db
  .select({
    authorId: posts.authorId,
    postCount: count(),
  })
  .from(posts)
  .groupBy(posts.authorId)
  .having(gt(count(), 5));
```

---

## 4. Relational Queries

The relational query builder provides a type-safe way to load related data without manual joins.

```typescript
// Requires relations to be defined (see Schema Definition section)
// Requires schema passed to drizzle(): drizzle(client, { schema })

// Find many with relations
const usersWithPosts = await db.query.users.findMany({
  with: {
    posts: true,
  },
});

// Nested relations
const usersWithPostsAndComments = await db.query.users.findMany({
  with: {
    posts: {
      with: {
        comments: true,
      },
    },
  },
});

// Select specific columns
const userPreviews = await db.query.users.findMany({
  columns: {
    id: true,
    name: true,
    email: true,
  },
  with: {
    posts: {
      columns: {
        id: true,
        title: true,
      },
      limit: 5,
      orderBy: (posts, { desc }) => [desc(posts.createdAt)],
    },
  },
});

// Find first
const user = await db.query.users.findFirst({
  where: (users, { eq }) => eq(users.id, 1),
  with: {
    posts: true,
  },
});

// Filter on relations
const usersWithRecentPosts = await db.query.users.findMany({
  where: (users, { eq }) => eq(users.isActive, true),
  with: {
    posts: {
      where: (posts, { gt }) => gt(posts.publishedAt, new Date("2024-01-01")),
      orderBy: (posts, { desc }) => [desc(posts.publishedAt)],
    },
  },
});
```

---

## 5. Joins

```typescript
// Inner join
const usersWithPosts = await db
  .select({
    userName: users.name,
    postTitle: posts.title,
  })
  .from(users)
  .innerJoin(posts, eq(users.id, posts.authorId));

// Left join
const allUsersWithPosts = await db
  .select({
    userName: users.name,
    postTitle: posts.title, // nullable due to left join
  })
  .from(users)
  .leftJoin(posts, eq(users.id, posts.authorId));

// Multiple joins
const fullData = await db
  .select({
    userName: users.name,
    postTitle: posts.title,
    commentText: comments.text,
  })
  .from(users)
  .leftJoin(posts, eq(users.id, posts.authorId))
  .leftJoin(comments, eq(posts.id, comments.postId));

// Self join (using aliases)
import { alias } from "drizzle-orm/pg-core";

const parent = alias(categories, "parent");
const categoriesWithParent = await db
  .select({
    name: categories.name,
    parentName: parent.name,
  })
  .from(categories)
  .leftJoin(parent, eq(categories.parentId, parent.id));
```

### Joins vs Relations: When to Use Which

| Feature | SQL Joins (`db.select()...join()`) | Relations (`db.query.*`) |
|---------|-------------------------------------|--------------------------|
| Flat result | Yes | No (nested objects) |
| Aggregations | Yes (`count`, `sum`, etc.) | No |
| Complex conditions | Full SQL flexibility | Limited to `where` |
| N+1 prevention | Manual (single query) | Automatic |
| Type safety | Column-level | Relation-level |
| Best for | Reports, analytics, complex queries | CRUD, API responses |

---

## 6. Transactions

```typescript
// Basic transaction
const result = await db.transaction(async (tx) => {
  const [newUser] = await tx
    .insert(users)
    .values({ name: "Alice", email: "alice@example.com" })
    .returning();

  await tx.insert(posts).values({
    title: "First Post",
    content: "Hello world",
    authorId: newUser.id,
  });

  return newUser;
});

// Transaction with rollback
await db.transaction(async (tx) => {
  await tx.update(accounts).set({ balance: sql`balance - 100` }).where(eq(accounts.id, fromId));
  await tx.update(accounts).set({ balance: sql`balance + 100` }).where(eq(accounts.id, toId));

  const [sender] = await tx.select().from(accounts).where(eq(accounts.id, fromId));
  if (sender.balance < 0) {
    tx.rollback(); // Rolls back all changes in this transaction
  }
});

// Nested transactions (savepoints)
await db.transaction(async (tx) => {
  await tx.insert(users).values({ name: "Alice", email: "alice@example.com" });

  try {
    await tx.transaction(async (nestedTx) => {
      await nestedTx.insert(posts).values({ title: "Post", authorId: 1 });
      // If this fails, only the nested transaction is rolled back
    });
  } catch {
    // Nested transaction failed, outer continues
  }
});
```

### Transaction Isolation Levels (PostgreSQL)

```typescript
await db.transaction(async (tx) => {
  // ... transactional work
}, {
  isolationLevel: "serializable",  // "read committed" | "repeatable read" | "serializable"
  accessMode: "read write",       // "read only" | "read write"
});
```

---

## 7. Migrations with drizzle-kit

### Configuration

```typescript
// drizzle.config.ts
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  schema: "./src/db/schema.ts",
  out: "./drizzle",              // Migration output directory
  dialect: "postgresql",         // "postgresql" | "mysql" | "sqlite"
  dbCredentials: {
    url: process.env.DATABASE_URL!,
  },
  verbose: true,
  strict: true,
});
```

### Commands

```bash
# Generate migration from schema changes
npx drizzle-kit generate

# Apply migrations
npx drizzle-kit migrate

# Push schema directly (development only, no migration files)
npx drizzle-kit push

# Open Drizzle Studio (GUI)
npx drizzle-kit studio

# Drop migration
npx drizzle-kit drop

# Introspect existing database into schema
npx drizzle-kit introspect
```

### Migration Workflow

```
1. Edit schema.ts
2. npx drizzle-kit generate    → Creates SQL migration file
3. Review generated SQL         → Check for destructive changes
4. npx drizzle-kit migrate     → Apply to database
```

### Custom Migration

```sql
-- drizzle/0001_add_index.sql
-- Custom: Add partial index not supported by schema DSL
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_active_users
  ON users (email) WHERE is_active = true;
```

---

## 8. Type-Safe Patterns

### Inferred Types

```typescript
import { InferSelectModel, InferInsertModel } from "drizzle-orm";

// Infer types from schema
type User = InferSelectModel<typeof users>;
type NewUser = InferInsertModel<typeof users>;

// Use in functions
async function createUser(data: NewUser): Promise<User> {
  const [user] = await db.insert(users).values(data).returning();
  return user;
}

async function getUserById(id: number): Promise<User | undefined> {
  return db.query.users.findFirst({
    where: (users, { eq }) => eq(users.id, id),
  });
}
```

### Partial Selects with Type Safety

```typescript
// Define a reusable partial select
const userPublicFields = {
  id: users.id,
  name: users.name,
  role: users.role,
} as const;

type PublicUser = typeof userPublicFields;

const publicUsers = await db.select(userPublicFields).from(users);
// Result type: { id: number; name: string; role: "admin" | "user" | "guest" }[]
```

### Dynamic Query Building

```typescript
function buildUserQuery(filters: {
  role?: string;
  isActive?: boolean;
  search?: string;
}) {
  let query = db.select().from(users).$dynamic();

  const conditions = [];

  if (filters.role) {
    conditions.push(eq(users.role, filters.role));
  }
  if (filters.isActive !== undefined) {
    conditions.push(eq(users.isActive, filters.isActive));
  }
  if (filters.search) {
    conditions.push(ilike(users.name, `%${filters.search}%`));
  }

  if (conditions.length > 0) {
    query = query.where(and(...conditions));
  }

  return query;
}
```

### Prepared Statements

```typescript
import { placeholder } from "drizzle-orm";

// Prepare a parameterized query
const getUserByEmail = db
  .select()
  .from(users)
  .where(eq(users.email, placeholder("email")))
  .prepare("get_user_by_email");

// Execute with parameters
const user = await getUserByEmail.execute({ email: "alice@example.com" });
```

---

## 9. Performance Patterns

### Pagination

```typescript
// Offset-based (simple, slower for deep pages)
const page = await db
  .select()
  .from(users)
  .orderBy(users.id)
  .limit(20)
  .offset((pageNum - 1) * 20);

// Cursor-based (efficient for large datasets)
const page = await db
  .select()
  .from(users)
  .where(gt(users.id, lastSeenId))
  .orderBy(users.id)
  .limit(20);
```

### Batch Operations

```typescript
// Batch insert (chunk large arrays)
const BATCH_SIZE = 1000;
for (let i = 0; i < records.length; i += BATCH_SIZE) {
  const chunk = records.slice(i, i + BATCH_SIZE);
  await db.insert(users).values(chunk);
}

// Batch insert in transaction
await db.transaction(async (tx) => {
  for (let i = 0; i < records.length; i += BATCH_SIZE) {
    const chunk = records.slice(i, i + BATCH_SIZE);
    await tx.insert(users).values(chunk);
  }
});
```

### Select Only Needed Columns

```typescript
// Avoid: selects all columns, including large text/jsonb
const users = await db.select().from(users);

// Prefer: select only what you need
const users = await db
  .select({ id: users.id, name: users.name, email: users.email })
  .from(users);
```

### Raw SQL Escape Hatch

```typescript
import { sql } from "drizzle-orm";

// Complex query with raw SQL
const result = await db.execute(
  sql`SELECT u.id, u.name, COUNT(p.id) as post_count
      FROM ${users} u
      LEFT JOIN ${posts} p ON u.id = p.author_id
      GROUP BY u.id, u.name
      HAVING COUNT(p.id) > ${minPosts}
      ORDER BY post_count DESC`
);
```

---

## 10. Common Pitfalls

### Pitfall: `sql` Template Column References in Subqueries

When using Drizzle's `sql` template literals, `${table.column}` generates a **bare column name without the table qualifier**. This causes silent semantic errors inside aliased subqueries.

#### Symptom

```typescript
// Code
sql`SELECT ${agentInvocations.errorSummary} as sub_es
    FROM ${agentInvocations} AS ai2
    WHERE ai2.agent_type = ${agentInvocations.agentType}`

// Generated SQL (WRONG)
// "agent_type" becomes a literal string — always true!
SELECT "error_summary" as sub_es
FROM "agent_invocations" AS ai2
WHERE ai2.agent_type = "agent_type"
```

#### Fix: Use Raw SQL for Subquery Internal References

```typescript
// CORRECT: raw SQL column references inside aliased subquery
sql`SELECT ai2.error_summary as sub_es
    FROM ${agentInvocations} AS ai2
    WHERE ai2.agent_type = ${agentInvocations}.agent_type`
```

#### Decision Table

| Context | Pattern | Safe? |
|---------|---------|-------|
| Top-level `FROM` clause | `${table}` | Yes |
| Top-level `WHERE` with parameterized value | `${value}` | Yes (auto-parameterized) |
| Top-level `SELECT` column | `${table.column}` | Yes |
| Inside aliased subquery `SELECT` | `${table.column}` | **No** — bare column name |
| Inside aliased subquery `WHERE` comparison | `${table.column}` | **No** — string literal |
| Inside aliased subquery (fixed) | `alias.column_name` | Yes |

**Always use `.toSQL()` to inspect generated SQL before running complex queries.**

### Pitfall: Missing `schema` in `drizzle()` Call

```typescript
// WRONG: relational queries will not work
const db = drizzle(client);
await db.query.users.findMany(); // Error: "users" not found

// CORRECT: pass schema for relational queries
const db = drizzle(client, { schema });
await db.query.users.findMany(); // Works
```

### Pitfall: Confusing Relations and Foreign Keys

```typescript
// Relations: for query builder only (no SQL generated)
export const usersRelations = relations(users, ({ many }) => ({
  posts: many(posts),
}));

// Foreign key: actual database constraint
export const posts = pgTable("posts", {
  authorId: integer("author_id")
    .references(() => users.id, { onDelete: "cascade" }), // SQL constraint
});

// You need BOTH for full functionality
```

### Pitfall: Not Handling `null` from Left Joins

```typescript
// Left join makes right-side columns nullable
const result = await db
  .select({
    userName: users.name,
    postTitle: posts.title, // Type: string | null (not string)
  })
  .from(users)
  .leftJoin(posts, eq(users.id, posts.authorId));

// Always check for null
result.forEach((row) => {
  if (row.postTitle !== null) {
    console.log(row.postTitle);
  }
});
```

### Pitfall: Using `push` in Production

```bash
# push applies schema directly WITHOUT migration files
# NEVER use in production — no rollback, no history
npx drizzle-kit push   # Development only

# ALWAYS use generate + migrate in production
npx drizzle-kit generate
npx drizzle-kit migrate
```

---

## 11. Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| `select().from(table)` for large tables | Fetches all columns and rows | Add `.limit()`, select specific columns |
| String concatenation in `sql` | SQL injection risk | Use `sql` template with `${value}` for params |
| N+1 queries in loops | Performance degradation | Use relational queries or joins |
| Schema in application code | Schema and queries in one file | Separate `schema.ts` from query functions |
| Ignoring migration review | Destructive changes slip through | Always review generated SQL before applying |
| Raw `db.execute()` for simple queries | Loses type safety | Use query builder; raw SQL only when needed |
| Shared mutable query builder | Race conditions | Build new query per request |

---

## Usage

This guide is referenced by:
- **Agent**: lang-typescript-expert (TypeScript ORM patterns)
- **Agent**: db-postgres-expert (PostgreSQL-specific Drizzle usage)

## External Resources

- [Drizzle ORM Docs](https://orm.drizzle.team/docs/overview)
- [Drizzle Kit Docs](https://orm.drizzle.team/docs/kit-overview)
- [Drizzle GitHub](https://github.com/drizzle-team/drizzle-orm)
- [Drizzle Studio](https://orm.drizzle.team/drizzle-studio/overview)
- [Drizzle with Neon](https://orm.drizzle.team/docs/get-started-postgresql#neon)
- [Drizzle with Vercel Postgres](https://orm.drizzle.team/docs/get-started-postgresql#vercel-postgres)
