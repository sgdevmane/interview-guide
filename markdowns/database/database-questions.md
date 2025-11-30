<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/database-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Database Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for backend developers</b></p>
</div>

---

## Table of Contents

1. [How do you optimize a slow SQL query that involves multiple joins and large tables?](#q1-how-do-you-optimize-a-slow-sql-query-that-involves-multiple-joins-and-large-tables) <span class="intermediate">Intermediate</span>
2. [How do you handle database migrations for a high-traffic application with zero downtime?](#q2-how-do-you-handle-database-migrations-for-a-high-traffic-application-with-zero-downtime) <span class="intermediate">Intermediate</span>
3. [How do you prevent SQL Injection vulnerabilities in a raw SQL query?](#q3-how-do-you-prevent-sql-injection-vulnerabilities-in-a-raw-sql-query) <span class="intermediate">Intermediate</span>
4. [How do you design a schema for a 'Many-to-Many' relationship?](#q4-how-do-you-design-a-schema-for-a-many-to-many-relationship) <span class="intermediate">Intermediate</span>
5. [How do you choose between embedding documents and referencing them in MongoDB?](#q5-how-do-you-choose-between-embedding-documents-and-referencing-them-in-mongodb) <span class="intermediate">Intermediate</span>
6. [How do you resolve the N+1 query problem?](#q6-how-do-you-resolve-the-n1-query-problem) <span class="intermediate">Intermediate</span>
7. [How do you use Window Functions to find the top 3 salaries per department?](#q7-how-do-you-use-window-functions-to-find-the-top-3-salaries-per-department) <span class="intermediate">Intermediate</span>
8. [How do you implement optimistic locking to handle concurrent updates?](#q8-how-do-you-implement-optimistic-locking-to-handle-concurrent-updates) <span class="intermediate">Intermediate</span>
9. [How do you ensure data consistency across microservices (Distributed Transaction)?](#q9-how-do-you-ensure-data-consistency-across-microservices-distributed-transaction) <span class="intermediate">Intermediate</span>
10. [How do you use a Redis cache to implement the 'Cache-Aside' pattern?](#q10-how-do-you-use-a-redis-cache-to-implement-the-cache-aside-pattern) <span class="intermediate">Intermediate</span>
11. [How do you structure a composite index to optimize a query with equality and range filters?](#q11-how-do-you-structure-a-composite-index-to-optimize-a-query-with-equality-and-range-filters) <span class="intermediate">Intermediate</span>
12. [How do you handle 'Soft Deletes' to preserve data history?](#q12-how-do-you-handle-soft-deletes-to-preserve-data-history) <span class="intermediate">Intermediate</span>
13. [How do you optimize database writes for a high-ingestion system (e.g., logs)?](#q13-how-do-you-optimize-database-writes-for-a-high-ingestion-system-eg-logs) <span class="intermediate">Intermediate</span>
14. [How do you use Common Table Expressions (CTEs) to simplify complex logic?](#q14-how-do-you-use-common-table-expressions-ctes-to-simplify-complex-logic) <span class="intermediate">Intermediate</span>
15. [How do you maintain ACID properties in a database transaction?](#q15-how-do-you-maintain-acid-properties-in-a-database-transaction) <span class="intermediate">Intermediate</span>
16. [How do you create a Materialized View and refresh it concurrently?](#q16-how-do-you-create-a-materialized-view-and-refresh-it-concurrently) <span class="intermediate">Intermediate</span>
17. [How do you implement an audit log using Database Triggers?](#q17-how-do-you-implement-an-audit-log-using-database-triggers) <span class="advanced">Advanced</span>
18. [How do you query JSONB data efficiently in PostgreSQL?](#q18-how-do-you-query-jsonb-data-efficiently-in-postgresql) <span class="intermediate">Intermediate</span>
19. [How do you perform an Upsert (Insert or Update) in SQL?](#q19-how-do-you-perform-an-upsert-insert-or-update-in-sql) <span class="beginner">Beginner</span>
20. [How do you use Recursive CTEs to query hierarchical data?](#q20-how-do-you-use-recursive-ctes-to-query-hierarchical-data) <span class="advanced">Advanced</span>
21. [How do you use Window Functions to calculate running totals?](#q21-how-do-you-use-window-functions-to-calculate-running-totals) <span class="intermediate">Intermediate</span>
22. [How do you analyze query performance using EXPLAIN ANALYZE?](#q22-how-do-you-analyze-query-performance-using-explain-analyze) <span class="intermediate">Intermediate</span>
23. [How do you choose between UUID and Integer for Primary Keys?](#q23-how-do-you-choose-between-uuid-and-integer-for-primary-keys) <span class="intermediate">Intermediate</span>
24. [How do you prevent Deadlocks in database transactions?](#q24-how-do-you-prevent-deadlocks-in-database-transactions) <span class="advanced">Advanced</span>
25. [How do you use Full-Text Search in PostgreSQL without ElasticSearch?](#q25-how-do-you-use-full-text-search-in-postgresql-without-elasticsearch) <span class="advanced">Advanced</span>
26. [How do you handle transaction isolation levels?](#q26-how-do-you-handle-transaction-isolation-levels) <span class="advanced">Advanced</span>
27. [How do you implement Soft Deletes?](#q27-how-do-you-implement-soft-deletes) <span class="beginner">Beginner</span>
28. [How do you use a Composite Index effectively?](#q28-how-do-you-use-a-composite-index-effectively) <span class="intermediate">Intermediate</span>
29. [How do you identify and fix the N+1 query problem?](#q29-how-do-you-identify-and-fix-the-n1-query-problem) <span class="intermediate">Intermediate</span>
30. [How do you partition a large table by date?](#q30-how-do-you-partition-a-large-table-by-date) <span class="advanced">Advanced</span>

---

### Q1: How do you optimize a slow SQL query that involves multiple joins and large tables?

**Difficulty**: Intermediate

**Strategy:**
1. **Analyze Execution Plan:** Use `EXPLAIN ANALYZE` to identify bottlenecks (sequential scans, high cost loops).
2. **Indexing:** Ensure foreign keys and columns used in `WHERE`, `JOIN`, and `ORDER BY` clauses are indexed.
3. **Selectivity:** Filter data as early as possible to reduce the working set.
4. **Avoid `SELECT *`:** Fetch only necessary columns to reduce I/O.
5. **Join Type:** Check if the optimizer is choosing the right join type (Nested Loop vs Hash Join vs Merge Join).

**Code Example:**
```sql
-- Bad Query
SELECT * FROM orders o
JOIN users u ON o.user_id = u.id
JOIN products p ON o.product_id = p.id
WHERE o.created_at > '2023-01-01';

-- Optimized Query
-- 1. Select specific columns
-- 2. Ensure indexes on orders(created_at), orders(user_id), orders(product_id)
EXPLAIN ANALYZE
SELECT o.id, o.total, u.name, p.title 
FROM orders o
INNER JOIN users u ON o.user_id = u.id
INNER JOIN products p ON o.product_id = p.id
WHERE o.created_at > '2023-01-01';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q2: How do you handle database migrations for a high-traffic application with zero downtime?

**Difficulty**: Intermediate

**Strategy:**
Schema changes must be backward-compatible.
1. **Add Column:** Add new column as nullable (or with default). Code ignores it.
2. **Dual Write:** Deploy code that writes to both old and new columns/tables.
3. **Backfill:** Run a background script to copy old data to new structure.
4. **Switch Read:** Deploy code that reads from the new source.
5. **Cleanup:** Remove the old column/table after verifying everything works.

**Code Example:**
```sql
-- Step 1: Add column safely
ALTER TABLE users ADD COLUMN full_name VARCHAR(255);

-- Step 2: Application writes to both 'first_name'/'last_name' AND 'full_name'

-- Step 3: Backfill data (in batches to avoid locking)
UPDATE users SET full_name = CONCAT(first_name, ' ', last_name) 
WHERE full_name IS NULL LIMIT 1000;

-- Step 4: Deprecate old columns (future migration)
-- ALTER TABLE users DROP COLUMN first_name;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q3: How do you prevent SQL Injection vulnerabilities in a raw SQL query?

**Difficulty**: Intermediate

**Strategy:**
Never concatenate user input directly into SQL strings.
1. **Parameterized Queries (Prepared Statements):** The database treats input as data, not executable code.
2. **Input Validation:** Validate data type and format before reaching the DB.
3. **Principle of Least Privilege:** DB user should only have necessary permissions.

**Code Example:**
```javascript
// VULNERABLE
const query = `SELECT * FROM users WHERE email = '${userInput}'`;
db.query(query);

// SECURE
const query = 'SELECT * FROM users WHERE email = $1';
const values = [userInput];
db.query(query, values);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q4: How do you design a schema for a 'Many-to-Many' relationship?

**Difficulty**: Intermediate

**Strategy:**
Use a **Junction Table** (or Join Table/Associative Entity).
1. Create two main tables (e.g., `Students`, `Courses`).
2. Create a third table (e.g., `Enrollments`) containing foreign keys to both main tables.
3. Add a composite primary key (student_id, course_id) to prevent duplicates.

**Code Example:**
```sql
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100)
);

CREATE TABLE enrollments (
    student_id INT REFERENCES students(id),
    course_id INT REFERENCES courses(id),
    enrolled_at TIMESTAMP DEFAULT NOW(),
    PRIMARY KEY (student_id, course_id)
);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q5: How do you choose between embedding documents and referencing them in MongoDB?

**Difficulty**: Intermediate

**Strategy:**
*   **Embedding:**
    *   **Use when:** Data is "contained" (1-to-few), accessed together, and rarely changes independently.
    *   **Pros:** Single read operation (fast).
    *   **Cons:** Document size limit (16MB), data duplication.
*   **Referencing:**
    *   **Use when:** Data is "related" (1-to-many/infinite), accessed independently, or frequently updated.
    *   **Pros:** Smaller documents, no duplication.
    *   **Cons:** Multiple queries or `$lookup` (slower).

**Code Example:**
```json
// Embedding (User has few addresses)
{
  "_id": 1,
  "name": "John",
  "addresses": [
    { "street": "123 Main St", "city": "NY" },
    { "street": "456 Side St", "city": "LA" }
  ]
}

// Referencing (Book has many reviews)
// Book
{ "_id": 101, "title": "Database Design" }

// Review
{ "_id": 501, "book_id": 101, "text": "Great book!", "user_id": 1 }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q6: How do you resolve the N+1 query problem?

**Difficulty**: Intermediate

**Strategy:**
The N+1 problem happens when you fetch a parent list (1 query) and then execute a query for each child (N queries).
1. **Eager Loading:** Fetch all related data in the initial query using JOINs or `IN` clauses.
2. **Batching:** Collect IDs and fetch all related records in one go (DataLoader pattern).

**Code Example:**
```javascript
// BAD (N+1)
const posts = await Post.findAll(); // 1 query
for (const post of posts) {
  const comments = await Comment.findByPostId(post.id); // N queries
}

// GOOD (Eager Loading)
const posts = await Post.findAll({ include: 'comments' }); 
// SELECT * FROM posts;
// SELECT * FROM comments WHERE post_id IN (1, 2, 3...);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q7: How do you use Window Functions to find the top 3 salaries per department?

**Difficulty**: Intermediate

**Strategy:**
Window functions perform calculations across a set of table rows that are somehow related to the current row.
1. Use `DENSE_RANK()` or `ROW_NUMBER()` to assign a rank to each row within a partition.
2. Partition by `department_id` and Order by `salary DESC`.
3. Filter the result in an outer query.

**Code Example:**
```sql
WITH RankedSalaries AS (
    SELECT 
        name, 
        department_id, 
        salary,
        DENSE_RANK() OVER (
            PARTITION BY department_id 
            ORDER BY salary DESC
        ) as rank
    FROM employees
)
SELECT * FROM RankedSalaries WHERE rank <= 3;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q8: How do you implement optimistic locking to handle concurrent updates?

**Difficulty**: Intermediate

**Strategy:**
Optimistic locking assumes conflicts are rare. It doesn't lock rows during read.
1. Add a `version` column (int or timestamp) to the table.
2. When reading, fetch the current `version`.
3. When updating, add `WHERE version = read_version` and increment the version.
4. If `affected_rows` is 0, the data was modified by someone else; retry or error.

**Code Example:**
```sql
-- 1. Read
SELECT id, name, version FROM products WHERE id = 1; 
-- returns version = 5

-- 2. Update
UPDATE products 
SET name = 'New Name', version = version + 1 
WHERE id = 1 AND version = 5;

-- 3. Check result
-- If row count = 1 -> Success
-- If row count = 0 -> Conflict detected (throw StaleObjectException)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q9: How do you ensure data consistency across microservices (Distributed Transaction)?

**Difficulty**: Intermediate

**Strategy:**
Traditional ACID transactions don't span services.
1. **Saga Pattern:** A sequence of local transactions. If one fails, execute compensating transactions to undo changes.
    *   **Choreography:** Events trigger next steps.
    *   **Orchestration:** Central coordinator directs steps.
2. **Two-Phase Commit (2PC):** (Less common due to blocking) Prepare and Commit phases.

**Code Example:**
```sql
-- Two-Phase Commit (Conceptual)
-- Phase 1: Prepare
PREPARE TRANSACTION 'txn_id';

-- Phase 2: Commit (if all services agree)
COMMIT PREPARED 'txn_id';

-- Or Rollback (if any service fails)
ROLLBACK PREPARED 'txn_id';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q10: How do you use a Redis cache to implement the 'Cache-Aside' pattern?

**Difficulty**: Intermediate

**Strategy:**
The application is responsible for reading/writing from cache.
1. **Read:** App checks cache.
    *   If hit: Return data.
    *   If miss: Read from DB, write to cache, return data.
2. **Write:** App writes to DB, then invalidates (deletes) or updates the cache key.

**Code Example:**
```javascript
async function getUser(id) {
  const cacheKey = `user:${id}`;
  
  // 1. Check Cache
  const cached = await redis.get(cacheKey);
  if (cached) return JSON.parse(cached);
  
  // 2. Read DB
  const user = await db.findUser(id);
  
  // 3. Update Cache (with TTL)
  if (user) {
    await redis.set(cacheKey, JSON.stringify(user), 'EX', 3600);
  }
  
  return user;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q11: How do you structure a composite index to optimize a query with equality and range filters?

**Difficulty**: Intermediate

**Strategy:**
Order of columns in a composite index matters.
Rule: **Equality (=) columns first, then Range (>, <, BETWEEN) columns.**
1. If you have `WHERE category_id = 5 AND price > 100`, the index should be `(category_id, price)`.
2. If you index `(price, category_id)`, the database has to check all prices > 100 and then filter by category, which is less efficient.

**Code Example:**
```sql
-- Query
SELECT * FROM products WHERE status = 'active' AND created_at > '2023-01-01';

-- Optimal Index
CREATE INDEX idx_status_created ON products (status, created_at);

-- Explanation:
-- The DB jumps to the 'active' section of the B-Tree, 
-- then scans the 'created_at' range sequentially.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q12: How do you handle 'Soft Deletes' to preserve data history?

**Difficulty**: Intermediate

**Strategy:**
Instead of `DELETE FROM table`, mark the row as deleted.
1. Add a `deleted_at` (timestamp) or `is_deleted` (boolean) column.
2. Default it to NULL (active).
3. **Delete:** Update `deleted_at` to current timestamp.
4. **Read:** Always filter `WHERE deleted_at IS NULL`.

**Code Example:**
```sql
-- Table
ALTER TABLE users ADD COLUMN deleted_at TIMESTAMP NULL;

-- Soft Delete
UPDATE users SET deleted_at = NOW() WHERE id = 1;

-- Query Active Users
SELECT * FROM users WHERE deleted_at IS NULL;

-- Restore
UPDATE users SET deleted_at = NULL WHERE id = 1;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q13: How do you optimize database writes for a high-ingestion system (e.g., logs)?

**Difficulty**: Intermediate

**Strategy:**
1. **Batch Inserts:** Insert multiple rows in a single transaction/query (`INSERT INTO ... VALUES (...), (...), (...)`).
2. **Remove Indexes:** Disable non-essential indexes during bulk load; rebuild later.
3. **Partitioning:** Write to a specific partition (e.g., current day) to keep index size manageable.
4. **Async Processing:** Write to a queue (Kafka) first, then consume and write to DB in batches.

**Code Example:**
```sql
-- Faster than 3 separate INSERT statements
INSERT INTO logs (level, message, timestamp) VALUES 
('INFO', 'User login', NOW()),
('ERROR', 'DB connection failed', NOW()),
('WARN', 'High latency', NOW());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q14: How do you use Common Table Expressions (CTEs) to simplify complex logic?

**Difficulty**: Intermediate

**Strategy:**
CTEs (`WITH` clause) allow you to define temporary result sets for use within a SELECT, INSERT, UPDATE, or DELETE statement.
1. Improves readability over nested subqueries.
2. Allows recursive queries (e.g., hierarchical data).

**Code Example:**
```sql
WITH RegionalSales AS (
    SELECT region, SUM(amount) as total_sales
    FROM orders
    GROUP BY region
),
TopRegions AS (
    SELECT region
    FROM RegionalSales
    WHERE total_sales > 100000
)
SELECT * 
FROM orders 
WHERE region IN (SELECT region FROM TopRegions);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q15: How do you maintain ACID properties in a database transaction?

**Difficulty**: Intermediate

**Strategy:**
1. **Atomicity:** Use `BEGIN TRANSACTION` and `COMMIT` / `ROLLBACK`. All or nothing.
2. **Consistency:** Constraints (Foreign Keys, Checks) ensure DB rules are valid.
3. **Isolation:** Set appropriate isolation level (`READ COMMITTED`, `SERIALIZABLE`) to handle concurrency.
4. **Durability:** WAL (Write-Ahead Logging) ensures data survives crashes.

**Code Example:**
```sql
BEGIN;

-- Deduct money
UPDATE accounts SET balance = balance - 100 WHERE id = 1;

-- Add money
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

-- If error occurs anywhere here, ROLLBACK;

COMMIT;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q16: How do you create a Materialized View and refresh it concurrently?

**Difficulty**: Intermediate

**Strategy:**
Materialized views store the result of a query physically. Use `REFRESH MATERIALIZED VIEW CONCURRENTLY` to update data without locking the view for reads.

**Code Example:**
```sql
-- Create
CREATE MATERIALIZED VIEW sales_summary AS
SELECT product_id, SUM(amount) as total_sales
FROM sales
GROUP BY product_id;

-- Create Unique Index (Required for Concurrent Refresh)
CREATE UNIQUE INDEX idx_sales_summary_id ON sales_summary(product_id);

-- Refresh without locking
REFRESH MATERIALIZED VIEW CONCURRENTLY sales_summary;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q17: How do you implement an audit log using Database Triggers?

**Difficulty**: Advanced

**Strategy:**
Create a trigger function that inserts old/new values into an audit table whenever an UPDATE or DELETE occurs on the main table.

**Code Example:**
```json
CREATE FUNCTION log_changes() RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO audit_log (table_name, operation, old_data, new_data, changed_at)
  VALUES (TG_TABLE_NAME, TG_OP, row_to_json(OLD), row_to_json(NEW), NOW());
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_audit_users
AFTER UPDATE OR DELETE ON users
FOR EACH ROW EXECUTE FUNCTION log_changes();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q18: How do you query JSONB data efficiently in PostgreSQL?

**Difficulty**: Intermediate

**Strategy:**
Use the `->>` operator to access fields as text. Create a GIN index on the JSONB column to speed up containment queries (`@>`).

**Code Example:**
```sql
-- Query
SELECT * FROM users WHERE data->>'role' = 'admin';

-- Indexing
CREATE INDEX idx_users_data ON users USING GIN (data);

-- Fast query using containment operator
SELECT * FROM users WHERE data @> '{"role": "admin"}';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q19: How do you perform an Upsert (Insert or Update) in SQL?

**Difficulty**: Beginner

**Strategy:**
Use `INSERT ... ON CONFLICT` (Postgres) or `INSERT ... ON DUPLICATE KEY UPDATE` (MySQL) to handle unique constraint violations gracefully.

**Code Example:**
```sql
-- PostgreSQL
INSERT INTO users (id, name, email)
VALUES (1, 'John', 'john@example.com')
ON CONFLICT (id) 
DO UPDATE SET email = EXCLUDED.email, name = EXCLUDED.name;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q20: How do you use Recursive CTEs to query hierarchical data?

**Difficulty**: Advanced

**Strategy:**
Use a `WITH RECURSIVE` CTE. Define a base case (e.g., root nodes) and a recursive step (joining back to the CTE) to traverse trees like organizational charts or category trees.

**Code Example:**
```sql
WITH RECURSIVE employee_tree AS (
  -- Base Case: Top level managers
  SELECT id, name, manager_id, 1 as level
  FROM employees WHERE manager_id IS NULL
  
  UNION ALL
  
  -- Recursive Step: Subordinates
  SELECT e.id, e.name, e.manager_id, et.level + 1
  FROM employees e
  INNER JOIN employee_tree et ON e.manager_id = et.id
)
SELECT * FROM employee_tree;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q21: How do you use Window Functions to calculate running totals?

**Difficulty**: Intermediate

**Strategy:**
Use `SUM(column) OVER (ORDER BY ...)` to calculate a running total (cumulative sum) row by row.

**Code Example:**
```sql
SELECT 
  date,
  amount,
  SUM(amount) OVER (ORDER BY date) as running_total
FROM sales;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q22: How do you analyze query performance using EXPLAIN ANALYZE?

**Difficulty**: Intermediate

**Strategy:**
Prepend `EXPLAIN ANALYZE` to your query to see the execution plan and actual runtimes. Look for 'Seq Scan' on large tables (bad) vs 'Index Scan' (good).

**Code Example:**
```sql
EXPLAIN ANALYZE 
SELECT * FROM orders 
WHERE customer_id = 12345 
AND order_date > '2023-01-01';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q23: How do you choose between UUID and Integer for Primary Keys?

**Difficulty**: Intermediate

**Strategy:**
Integers are smaller (4/8 bytes) and faster for indexing. UUIDs (16 bytes) are globally unique, allowing decentralized ID generation (good for sharding/microservices) but fragment indexes.

**Code Example:**
```sql
-- Integer (Auto Increment)
id SERIAL PRIMARY KEY

-- UUID (Postgres)
id UUID PRIMARY KEY DEFAULT gen_random_uuid()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q24: How do you prevent Deadlocks in database transactions?

**Difficulty**: Advanced

**Strategy:**
Ensure all transactions acquire locks on resources in the same order. Keep transactions short. Use `FOR UPDATE` to lock rows explicitly if needed.

**Code Example:**
```sql
-- Transaction A: Lock User 1 then User 2
BEGIN;
UPDATE users SET balance = balance - 10 WHERE id = 1;
UPDATE users SET balance = balance + 10 WHERE id = 2;
COMMIT;

-- Transaction B MUST also Lock User 1 then User 2 (NOT User 2 then User 1)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q25: How do you use Full-Text Search in PostgreSQL without ElasticSearch?

**Difficulty**: Advanced

**Strategy:**
Use `tsvector` to store lexemes and `tsquery` to search. Create a GIN index on the `tsvector` column for performance.

**Code Example:**
```sql
-- Search
SELECT title 
FROM articles 
WHERE to_tsvector('english', title || ' ' || body) @@ to_tsquery('english', 'database & performance');

-- Index
CREATE INDEX idx_fts ON articles USING GIN (to_tsvector('english', title || ' ' || body));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q26: How do you handle transaction isolation levels?

**Difficulty**: Advanced

**Strategy:**
Set the isolation level to balance consistency vs concurrency. `READ COMMITTED` is default. `SERIALIZABLE` prevents all anomalies but causes high contention.

**Code Example:**
```sql
BEGIN;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
-- This transaction sees a snapshot of data at start time
SELECT * FROM account WHERE id = 1;
COMMIT;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q27: How do you implement Soft Deletes?

**Difficulty**: Beginner

**Strategy:**
Add a `deleted_at` timestamp column. UPDATE this column instead of DELETE. Filter queries with `WHERE deleted_at IS NULL`.

**Code Example:**
```sql
-- Soft Delete
UPDATE users SET deleted_at = NOW() WHERE id = 1;

-- Query active users
SELECT * FROM users WHERE deleted_at IS NULL;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q28: How do you use a Composite Index effectively?

**Difficulty**: Intermediate

**Strategy:**
Order columns in the index based on query usage: Equality columns first, then Range columns. The index `(a, b)` supports queries on `a` and `a, b`, but not just `b`.

**Code Example:**
```sql
-- Index on (last_name, first_name)
CREATE INDEX idx_name ON users (last_name, first_name);

-- Good Usage
SELECT * FROM users WHERE last_name = 'Doe' AND first_name = 'John';
SELECT * FROM users WHERE last_name = 'Doe';

-- Bad Usage (Index scan unlikely)
SELECT * FROM users WHERE first_name = 'John';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q29: How do you identify and fix the N+1 query problem?

**Difficulty**: Intermediate

**Strategy:**
N+1 occurs when fetching a list (1 query) and then fetching related data for each item (N queries). Fix using JOINs or eager loading (fetching all related IDs in one IN clause).

**Code Example:**
```sql
-- BAD (N+1)
-- SELECT * FROM posts;
-- For each post: SELECT * FROM comments WHERE post_id = ?;

-- GOOD (JOIN)
SELECT p.*, c.* 
FROM posts p
LEFT JOIN comments c ON c.post_id = p.id;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q30: How do you partition a large table by date?

**Difficulty**: Advanced

**Strategy:**
Use declarative partitioning. Create a parent table and attach partitions for specific date ranges. This improves query performance for range queries and data management (dropping old partitions).

**Code Example:**
```sql
CREATE TABLE logs (
    id SERIAL,
    log_date DATE NOT NULL
) PARTITION BY RANGE (log_date);

CREATE TABLE logs_2023_01 PARTITION OF logs
    FOR VALUES FROM ('2023-01-01') TO ('2023-02-01');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

