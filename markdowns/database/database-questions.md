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
27. [How do you partition a large table by date?](#q27-how-do-you-partition-a-large-table-by-date) <span class="advanced">Advanced</span>
28. [How do you implement Database Sharding and when should you use it?](#q28-how-do-you-implement-database-sharding-and-when-should-you-use-it) <span class="advanced">Advanced</span>
29. [How do you prevent Phantom Reads in a transaction?](#q29-how-do-you-prevent-phantom-reads-in-a-transaction) <span class="advanced">Advanced</span>
30. [How do you optimize a query using a Covering Index?](#q30-how-do-you-optimize-a-query-using-a-covering-index) <span class="intermediate">Intermediate</span>
31. [How do you handle 'Dirty Reads' and which isolation level prevents them?](#q31-how-do-you-handle-dirty-reads-and-which-isolation-level-prevents-them) <span class="intermediate">Intermediate</span>
32. [How do you implement connection pooling in a Node.js application?](#q32-how-do-you-implement-connection-pooling-in-a-nodejs-application) <span class="intermediate">Intermediate</span>
33. [How do you model a tree structure (Hierarchy) in a Relational Database?](#q33-how-do-you-model-a-tree-structure-hierarchy-in-a-relational-database) <span class="advanced">Advanced</span>
34. [How do you use JSON columns in PostgreSQL vs MySQL?](#q34-how-do-you-use-json-columns-in-postgresql-vs-mysql) <span class="intermediate">Intermediate</span>
35. [How do you implement Row-Level Security (RLS)?](#q35-how-do-you-implement-row-level-security-rls) <span class="advanced">Advanced</span>
36. [How do you use a Materialized View for reporting?](#q36-how-do-you-use-a-materialized-view-for-reporting) <span class="intermediate">Intermediate</span>
37. [How do you generate unique IDs in a distributed system (Snowflake ID)?](#q37-how-do-you-generate-unique-ids-in-a-distributed-system-snowflake-id) <span class="advanced">Advanced</span>
38. [How do you use Foreign Data Wrappers (FDW) in PostgreSQL?](#q38-how-do-you-use-foreign-data-wrappers-fdw-in-postgresql) <span class="advanced">Advanced</span>
39. [How do you optimize a `LIKE` query with wildcards at the beginning?](#q39-how-do-you-optimize-a-like-query-with-wildcards-at-the-beginning) <span class="intermediate">Intermediate</span>
40. [How do you use the `CASE` statement for conditional logic in SQL?](#q40-how-do-you-use-the-case-statement-for-conditional-logic-in-sql) <span class="beginner">Beginner</span>
41. [How do you implement Database Replication (Master-Slave)?](#q41-how-do-you-implement-database-replication-master-slave) <span class="advanced">Advanced</span>
42. [How do you perform a Batch Insert efficiently?](#q42-how-do-you-perform-a-batch-insert-efficiently) <span class="intermediate">Intermediate</span>
43. [How do you use `GROUPING SETS` for multi-level aggregation?](#q43-how-do-you-use-grouping-sets-for-multi-level-aggregation) <span class="advanced">Advanced</span>
44. [How do you store and query time-series data efficiently?](#q44-how-do-you-store-and-query-time-series-data-efficiently) <span class="intermediate">Intermediate</span>
45. [How do you handle 'NoSQL' data modeling in DynamoDB (Single Table Design)?](#q45-how-do-you-handle-nosql-data-modeling-in-dynamodb-single-table-design) <span class="advanced">Advanced</span>
46. [How do you identify and remove duplicate rows from a table?](#q46-how-do-you-identify-and-remove-duplicate-rows-from-a-table) <span class="intermediate">Intermediate</span>
47. [What is ACID?](#q47-what-is-acid) <span class="beginner">Beginner</span>
48. [What is Indexing?](#q48-what-is-indexing) <span class="beginner">Beginner</span>
49. [Types of Indexes?](#q49-types-of-indexes) <span class="intermediate">Intermediate</span>
50. [What is Normalization?](#q50-what-is-normalization) <span class="intermediate">Intermediate</span>
51. [What is Denormalization?](#q51-what-is-denormalization) <span class="intermediate">Intermediate</span>
52. [Inner Join vs Outer Join?](#q52-inner-join-vs-outer-join) <span class="beginner">Beginner</span>
53. [What is a View?](#q53-what-is-a-view) <span class="beginner">Beginner</span>
54. [What is a Stored Procedure?](#q54-what-is-a-stored-procedure) <span class="intermediate">Intermediate</span>
55. [What is a Trigger?](#q55-what-is-a-trigger) <span class="intermediate">Intermediate</span>
56. [SQL vs NoSQL?](#q56-sql-vs-nosql) <span class="beginner">Beginner</span>
57. [What is Sharding?](#q57-what-is-sharding) <span class="advanced">Advanced</span>
58. [What is Replication?](#q58-what-is-replication) <span class="intermediate">Intermediate</span>
59. [What is CAP Theorem?](#q59-what-is-cap-theorem) <span class="intermediate">Intermediate</span>
60. [What is eventual consistency?](#q60-what-is-eventual-consistency) <span class="intermediate">Intermediate</span>
61. [What is a Transaction?](#q61-what-is-a-transaction) <span class="beginner">Beginner</span>
62. [Isolation Levels?](#q62-isolation-levels) <span class="advanced">Advanced</span>
63. [What is Deadlock?](#q63-what-is-deadlock) <span class="intermediate">Intermediate</span>
64. [Optimistic vs Pessimistic Locking?](#q64-optimistic-vs-pessimistic-locking) <span class="advanced">Advanced</span>
65. [What is Connection Pooling?](#q65-what-is-connection-pooling) <span class="intermediate">Intermediate</span>
66. [What is an ORM?](#q66-what-is-an-orm) <span class="beginner">Beginner</span>
67. [N+1 Problem in DB?](#q67-n1-problem-in-db) <span class="intermediate">Intermediate</span>
68. [What is MongoDB?](#q68-what-is-mongodb) <span class="beginner">Beginner</span>
69. [What is Redis?](#q69-what-is-redis) <span class="beginner">Beginner</span>
70. [What is Cassandra?](#q70-what-is-cassandra) <span class="advanced">Advanced</span>
71. [What is a Primary Key?](#q71-what-is-a-primary-key) <span class="beginner">Beginner</span>
72. [What is a Foreign Key?](#q72-what-is-a-foreign-key) <span class="beginner">Beginner</span>
73. [What is Database Migration?](#q73-what-is-database-migration) <span class="intermediate">Intermediate</span>
74. [How to optimize a slow query?](#q74-how-to-optimize-a-slow-query) <span class="intermediate">Intermediate</span>
75. [What is SQL Injection?](#q75-what-is-sql-injection) <span class="beginner">Beginner</span>
76. [What is a Cursor?](#q76-what-is-a-cursor) <span class="intermediate">Intermediate</span>
77. [What is ETL?](#q77-what-is-etl) <span class="intermediate">Intermediate</span>
78. [OLTP vs OLAP?](#q78-oltp-vs-olap) <span class="advanced">Advanced</span>
79. [What is a Time Series DB?](#q79-what-is-a-time-series-db) <span class="intermediate">Intermediate</span>
80. [What is Graph DB?](#q80-what-is-graph-db) <span class="intermediate">Intermediate</span>
81. [What is Partitioning?](#q81-what-is-partitioning) <span class="advanced">Advanced</span>
82. [What is MVCC?](#q82-what-is-mvcc) <span class="advanced">Advanced</span>
83. [What is Write-Ahead Logging (WAL)?](#q83-what-is-write-ahead-logging-wal) <span class="advanced">Advanced</span>
84. [What is a Materialized View?](#q84-what-is-a-materialized-view) <span class="intermediate">Intermediate</span>
85. [What is Soft Delete?](#q85-what-is-soft-delete) <span class="beginner">Beginner</span>
86. [What is Database Mirroring?](#q86-what-is-database-mirroring) <span class="advanced">Advanced</span>
87. [Row-oriented vs Column-oriented storage?](#q87-row-oriented-vs-column-oriented-storage) <span class="advanced">Advanced</span>
88. [What is a Composite Key?](#q88-what-is-a-composite-key) <span class="intermediate">Intermediate</span>
89. [What is a Surrogate Key?](#q89-what-is-a-surrogate-key) <span class="intermediate">Intermediate</span>
90. [What is Referential Integrity?](#q90-what-is-referential-integrity) <span class="beginner">Beginner</span>
91. [What is a Bloom Filter in DB?](#q91-what-is-a-bloom-filter-in-db) <span class="advanced">Advanced</span>
92. [What is Two-Phase Commit (2PC)?](#q92-what-is-two-phase-commit-2pc) <span class="advanced">Advanced</span>
93. [What is CDC (Change Data Capture)?](#q93-what-is-cdc-change-data-capture) <span class="advanced">Advanced</span>
94. [What is Vacuuming?](#q94-what-is-vacuuming) <span class="intermediate">Intermediate</span>
95. [What is a Clustered Index?](#q95-what-is-a-clustered-index) <span class="advanced">Advanced</span>
96. [What is a Non-Clustered Index?](#q96-what-is-a-non-clustered-index) <span class="advanced">Advanced</span>
97. [What is Database Sharding vs Partitioning?](#q97-what-is-database-sharding-vs-partitioning) <span class="advanced">Advanced</span>
98. [What is a Spatial Index?](#q98-what-is-a-spatial-index) <span class="intermediate">Intermediate</span>
99. [What is Full-Text Search?](#q99-what-is-full-text-search) <span class="intermediate">Intermediate</span>
100. [What is B-Tree?](#q100-what-is-b-tree) <span class="advanced">Advanced</span>
101. [What is Hash Index?](#q101-what-is-hash-index) <span class="advanced">Advanced</span>

---

<a id="q1"></a>
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

<a id="q2"></a>
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

<a id="q3"></a>
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

<a id="q4"></a>
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

<a id="q5"></a>
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

<a id="q6"></a>
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

<a id="q7"></a>
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

<a id="q8"></a>
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

<a id="q9"></a>
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

<a id="q10"></a>
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

<a id="q11"></a>
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

<a id="q12"></a>
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

<a id="q13"></a>
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

<a id="q14"></a>
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

<a id="q15"></a>
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

<a id="q16"></a>
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

<a id="q17"></a>
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

<a id="q18"></a>
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

<a id="q19"></a>
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

<a id="q20"></a>
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

<a id="q21"></a>
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

<a id="q22"></a>
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

<a id="q23"></a>
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

<a id="q24"></a>
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

<a id="q25"></a>
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

<a id="q26"></a>
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

<a id="q27"></a>
### Q27: How do you partition a large table by date?

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


<a id="q28"></a>
### Q28: How do you implement Database Sharding and when should you use it?

**Difficulty**: Advanced

**Strategy:**
Sharding splits a large dataset across multiple database instances (shards) to improve scalability. Use it when vertical scaling (upgrading hardware) is no longer sufficient.

**Code Example:**
-- Concept: Sharding by User ID (Application Level)
-- Shard 1 (Users 1-1000000)
SELECT * FROM users_shard_1 WHERE user_id = 500;

-- Shard 2 (Users 1000001-2000000)
SELECT * FROM users_shard_2 WHERE user_id = 1500500;

-- Routing Logic in Application (Pseudocode)
function getShard(userId) {
    if (userId <= 1000000) return connectionShard1;
    return connectionShard2;
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q29"></a>
### Q29: How do you prevent Phantom Reads in a transaction?

**Difficulty**: Advanced

**Strategy:**
Phantom reads occur when a transaction reads a set of rows that match a search condition, but another transaction inserts/deletes rows that match that condition. Prevent this by using the `SERIALIZABLE` isolation level or `REPEATABLE READ` with range locks (Next-Key Locking in MySQL).

**Code Example:**
-- MySQL/InnoDB Example
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
START TRANSACTION;

-- Next-Key Lock prevents insertion into the range
SELECT * FROM orders WHERE amount > 1000 FOR UPDATE;

-- COMMIT;

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q30"></a>
### Q30: How do you optimize a query using a Covering Index?

**Difficulty**: Intermediate

**Strategy:**
A covering index includes all the columns retrieved by the query, allowing the database to fetch data solely from the index structure without accessing the table heap (Index Only Scan).

**Code Example:**
-- Query
SELECT first_name, last_name FROM users WHERE age > 25;

-- Create Covering Index (Composite Index)
-- Includes columns in WHERE clause and SELECT clause
CREATE INDEX idx_users_age_names ON users(age) INCLUDE (first_name, last_name);

-- 'INCLUDE' is PostgreSQL syntax. In MySQL, simply add columns to the key:
-- CREATE INDEX idx_users_age_names ON users(age, first_name, last_name);

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q31"></a>
### Q31: How do you handle 'Dirty Reads' and which isolation level prevents them?

**Difficulty**: Intermediate

**Strategy:**
Dirty reads happen when a transaction reads uncommitted data from another transaction. The `READ COMMITTED` isolation level prevents this.

**Code Example:**
-- Transaction A
START TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
-- (Not committed yet)

-- Transaction B (READ COMMITTED)
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
SELECT balance FROM accounts WHERE id = 1; 
-- Will read the OLD balance, ignoring uncommitted changes from A.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q32"></a>
### Q32: How do you implement connection pooling in a Node.js application?

**Difficulty**: Intermediate

**Strategy:**
Connection pooling reuses active database connections instead of creating a new one for every request, reducing latency and overhead.

**Code Example:**
const { Pool } = require('pg');

const pool = new Pool({
  user: 'dbuser',
  host: 'database.server.com',
  database: 'mydb',
  password: 'secretpassword',
  port: 5432,
  max: 20, // Maximum number of clients in the pool
  idleTimeoutMillis: 30000
});

// Usage
pool.query('SELECT NOW()', (err, res) => {
  console.log(err, res);
  // Connection is automatically returned to the pool
});

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q33"></a>
### Q33: How do you model a tree structure (Hierarchy) in a Relational Database?

**Difficulty**: Advanced

**Strategy:**
Common patterns include Adjacency List (parent_id), Path Enumeration (path string), Nested Sets (lft/rgt), and Closure Table (separate table for all paths).

**Code Example:**
-- Adjacency List (Simple, good for single-level fetch)
CREATE TABLE categories (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    parent_id INT REFERENCES categories(id)
);

-- Recursive Query (Common Table Expression) to fetch full tree
WITH RECURSIVE category_path (id, name, path) AS (
  SELECT id, name, CAST(name AS CHAR(200))
    FROM categories
    WHERE parent_id IS NULL
  UNION ALL
  SELECT c.id, c.name, CONCAT(cp.path, ' > ', c.name)
    FROM category_path cp JOIN categories c
      ON cp.id = c.parent_id
)
SELECT * FROM category_path;

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q34"></a>
### Q34: How do you use JSON columns in PostgreSQL vs MySQL?

**Difficulty**: Intermediate

**Strategy:**
PostgreSQL uses `JSONB` for binary storage and indexing. MySQL uses the `JSON` data type.

**Code Example:**
-- PostgreSQL
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    data JSONB
);
-- Query JSONB
SELECT * FROM products WHERE data->>'category' = 'Electronics';
-- Create Index on JSON path
CREATE INDEX idx_category ON products ((data->>'category'));

-- MySQL
CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    data JSON
);
-- Query JSON
SELECT * FROM products WHERE JSON_EXTRACT(data, '$.category') = 'Electronics';
-- Or shorthand
SELECT * FROM products WHERE data->'$.category' = 'Electronics';

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q35"></a>
### Q35: How do you implement Row-Level Security (RLS)?

**Difficulty**: Advanced

**Strategy:**
RLS restricts access to rows based on the user executing the query. It allows multiple tenants to share the same table securely.

**Code Example:**
-- PostgreSQL Example
ALTER TABLE orders ENABLE ROW LEVEL SECURITY;

-- Create Policy
CREATE POLICY user_orders_policy ON orders
    FOR SELECT
    USING (user_id = current_setting('app.current_user_id')::integer);

-- Usage in App
BEGIN;
SET LOCAL app.current_user_id = '42';
SELECT * FROM orders; -- Only returns orders for user 42
COMMIT;

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q36"></a>
### Q36: How do you use a Materialized View for reporting?

**Difficulty**: Intermediate

**Strategy:**
Materialized Views store the result of a query physically. They are faster for heavy aggregations but need to be refreshed.

**Code Example:**
-- Create Materialized View
CREATE MATERIALIZED VIEW monthly_sales AS
SELECT 
    date_trunc('month', order_date) as month,
    SUM(amount) as total_sales
FROM orders
GROUP BY 1;

-- Create Index for faster access
CREATE INDEX idx_monthly_sales ON monthly_sales(month);

-- Refresh Data (e.g., nightly via Cron)
REFRESH MATERIALIZED VIEW CONCURRENTLY monthly_sales;

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q37"></a>
### Q37: How do you generate unique IDs in a distributed system (Snowflake ID)?

**Difficulty**: Advanced

**Strategy:**
Auto-increment keys don't scale in distributed DBs. Use UUIDs (random, larger) or Snowflake IDs (time-sortable, 64-bit integer composed of timestamp + machine ID + sequence).

**Code Example:**
-- Twitter Snowflake ID Structure (64 bits)
-- | 1 bit sign | 41 bits timestamp | 10 bits machine ID | 12 bits sequence |

-- Implementation Logic (Pseudocode)
class Snowflake {
    nextId() {
        timestamp = currentTimestamp();
        if (timestamp < lastTimestamp) throw Error("Clock moved backwards");
        if (timestamp == lastTimestamp) {
            sequence = (sequence + 1) & 4095;
            if (sequence == 0) timestamp = waitForNextMillis(lastTimestamp);
        } else {
            sequence = 0;
        }
        lastTimestamp = timestamp;
        return ((timestamp - epoch) << 22) | (machineId << 12) | sequence;
    }
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q38"></a>
### Q38: How do you use Foreign Data Wrappers (FDW) in PostgreSQL?

**Difficulty**: Advanced

**Strategy:**
FDW allows you to access data in external data sources (another SQL DB, CSV, MongoDB) as if they were local tables.

**Code Example:**
-- Install extension
CREATE EXTENSION postgres_fdw;

-- Create Server object
CREATE SERVER remote_pg_db
    FOREIGN DATA WRAPPER postgres_fdw
    OPTIONS (host 'remote-host', dbname 'remote_db', port '5432');

-- Create User Mapping
CREATE USER MAPPING FOR local_user
    SERVER remote_pg_db
    OPTIONS (user 'remote_user', password 'secret');

-- Import Schema or Create Foreign Table
IMPORT FOREIGN SCHEMA public 
    FROM SERVER remote_pg_db 
    INTO local_schema;
    
-- Query like a local table
SELECT * FROM local_schema.remote_table;

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q39"></a>
### Q39: How do you optimize a `LIKE` query with wildcards at the beginning?

**Difficulty**: Intermediate

**Strategy:**
Standard B-Tree indexes don't support leading wildcards (`%term`). Use Trigram Indexes (`pg_trgm` in Postgres) or Full-Text Search.

**Code Example:**
-- Query
SELECT * FROM users WHERE name LIKE '%smith%'; -- Slow (Seq Scan)

-- Optimization (PostgreSQL)
CREATE EXTENSION pg_trgm;

CREATE INDEX idx_users_name_trgm ON users USING GIN (name gin_trgm_ops);

-- Now the index can be used
EXPLAIN SELECT * FROM users WHERE name LIKE '%smith%';

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q40"></a>
### Q40: How do you use the `CASE` statement for conditional logic in SQL?

**Difficulty**: Beginner

**Strategy:**
The `CASE` statement acts like an if-else block within a query.

**Code Example:**
SELECT 
    id,
    name,
    salary,
    CASE
        WHEN salary < 30000 THEN 'Junior'
        WHEN salary BETWEEN 30000 AND 70000 THEN 'Mid'
        ELSE 'Senior'
    END AS level
FROM employees;

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q41"></a>
### Q41: How do you implement Database Replication (Master-Slave)?

**Difficulty**: Advanced

**Strategy:**
Replication copies data from a Master (Write) node to Slave (Read) nodes. It improves read scalability and availability.

**Code Example:**
-- PostgreSQL Streaming Replication Setup (simplified)

-- 1. On Master (postgresql.conf)
wal_level = replica
max_wal_senders = 3

-- 2. Allow replication user (pg_hba.conf)
host replication replicator 192.168.1.0/24 md5

-- 3. On Slave
pg_basebackup -h master_host -D /var/lib/postgresql/data -U replicator -P -R

-- 4. Start Slave
-- Application logic: Write to Master, Read from Slave.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q42"></a>
### Q42: How do you perform a Batch Insert efficiently?

**Difficulty**: Intermediate

**Strategy:**
Avoid single-row inserts. Use multi-row `VALUES` syntax or `COPY` command (Postgres) / `LOAD DATA INFILE` (MySQL).

**Code Example:**
-- Bad (Multiple Round Trips)
INSERT INTO logs (msg) VALUES ('Error 1');
INSERT INTO logs (msg) VALUES ('Error 2');

-- Good (Single Transaction, Multi-row)
INSERT INTO logs (msg) VALUES 
    ('Error 1'), 
    ('Error 2'), 
    ('Error 3');

-- Best (PostgreSQL COPY for massive data)
COPY logs (msg) FROM '/path/to/file.csv' DELIMITER ',' CSV;

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q43"></a>
### Q43: How do you use `GROUPING SETS` for multi-level aggregation?

**Difficulty**: Advanced

**Strategy:**
`GROUPING SETS`, `ROLLUP`, and `CUBE` allow generating multiple levels of subtotals in a single query.

**Code Example:**
SELECT 
    region,
    department,
    SUM(sales) 
FROM sales_data
GROUP BY GROUPING SETS (
    (region, department), -- Sales per Region & Dept
    (region),             -- Total per Region
    ()                    -- Grand Total
);

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q44"></a>
### Q44: How do you store and query time-series data efficiently?

**Difficulty**: Intermediate

**Strategy:**
Use specialized extensions (TimescaleDB) or Partitioning by time. Avoid updating old data. Use proper indexing (BRIN index for ordered time data).

**Code Example:**
-- Using PostgreSQL Partitioning for Time Series
CREATE TABLE sensor_data (
    time TIMESTAMP NOT NULL,
    device_id INT,
    value FLOAT
) PARTITION BY RANGE (time);

-- BRIN Index (Block Range Index) is tiny and fast for time-ordered data
CREATE INDEX idx_sensor_time ON sensor_data USING BRIN(time);

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q45"></a>
### Q45: How do you handle 'NoSQL' data modeling in DynamoDB (Single Table Design)?

**Difficulty**: Advanced

**Strategy:**
In DynamoDB, use a Single Table with generic PK/SK (Partition Key/Sort Key) to support multiple access patterns via Overloaded Indexes.

**Code Example:**
// Table: MyTable (PK, SK)

// Entity: User
// PK: USER#123, SK: METADATA

// Entity: Order
// PK: USER#123, SK: ORDER#999

// Query: Get User and all their Orders
KeyConditionExpression: "PK = :pk",
ExpressionAttributeValues: {
    ":pk": "USER#123"
}
// Efficiently fetches heterogeneous items in one request.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q46"></a>
### Q46: How do you identify and remove duplicate rows from a table?

**Difficulty**: Intermediate

**Strategy:**
Use a CTE or self-join to identify duplicates based on specific columns, keeping only the one with the lowest/highest ID.

**Code Example:**
-- Using CTE and Window Function
WITH Duplicates AS (
    SELECT 
        id,
        ROW_NUMBER() OVER (
            PARTITION BY email 
            ORDER BY id ASC
        ) AS row_num
    FROM users
)
DELETE FROM users
WHERE id IN (
    SELECT id FROM Duplicates WHERE row_num > 1
);

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---



---

<a id="q47"></a>
### Q47: What is ACID?

**Difficulty**: Beginner

**Strategy**:
ACID stands for Atomicity, Consistency, Isolation, and Durability. It is a set of properties of database transactions intended to guarantee data validity despite errors, power failures, and other mishaps. Atomicity ensures that each transaction is treated as a single 'unit', which either succeeds completely or fails completely.

**Code Example**:
```javascript
BEGIN; ... COMMIT;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q48"></a>
### Q48: What is Indexing?

**Difficulty**: Beginner

**Strategy**:
Indexing is a data structure technique used to quickly locate and access the data in a database. Indexes are created using a few database columns. They are like a book's index; instead of scanning the whole book (table) to find a topic (row), you look up the index to find the page number (pointer).

**Code Example**:
```javascript
CREATE INDEX idx_name ON users(name);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q49"></a>
### Q49: Types of Indexes?

**Difficulty**: Intermediate

**Strategy**:
B-Tree, Hash, Bitmap, GiST, GIN. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// B-Tree is default
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q50"></a>
### Q50: What is Normalization?

**Difficulty**: Intermediate

**Strategy**:
Normalization is the process of organizing data in a database. This includes creating tables and establishing relationships between those tables according to rules designed both to protect the data and to make the database more flexible by eliminating redundancy and inconsistent dependency.

**Code Example**:
```javascript
// 1NF, 2NF, 3NF
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q51"></a>
### Q51: What is Denormalization?

**Difficulty**: Intermediate

**Strategy**:
Denormalization is a database optimization technique in which we add redundant data to one or more tables. This can help us avoid costly joins in a relational database. Note that denormalization does not mean not doing normalization. It is an optimization strategy applied after normalization.

**Code Example**:
```javascript
// Storing count in parent table
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q52"></a>
### Q52: Inner Join vs Outer Join?

**Difficulty**: Beginner

**Strategy**:
An Inner Join returns records that have matching values in both tables. An Outer Join doesn't require a match in both tables. A Left Outer Join returns all records from the left table, and the matched records from the right table. A Right Outer Join does the reverse. Full Outer Join returns all records when there is a match in either left or right table.

**Code Example**:
```javascript
SELECT * FROM A JOIN B ON A.id = B.id
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q53"></a>
### Q53: What is a View?

**Difficulty**: Beginner

**Strategy**:
Virtual table based on query. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
CREATE VIEW active_users AS ...
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q54"></a>
### Q54: What is a Stored Procedure?

**Difficulty**: Intermediate

**Strategy**:
Code stored in DB. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
CREATE PROCEDURE ...
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q55"></a>
### Q55: What is a Trigger?

**Difficulty**: Intermediate

**Strategy**:
Auto-executes on event. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
CREATE TRIGGER ... BEFORE INSERT ...
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q56"></a>
### Q56: SQL vs NoSQL?

**Difficulty**: Beginner

**Strategy**:
SQL databases are relational, table-based databases, whereas NoSQL databases are non-relational, document, key-value, graph, or wide-column stores. SQL databases have a predefined schema and use structured query language. NoSQL databases have dynamic schemas for unstructured data.

**Code Example**:
```javascript
// MySQL vs MongoDB
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q57"></a>
### Q57: What is Sharding?

**Difficulty**: Advanced

**Strategy**:
Sharding is a method of splitting and storing a single logical dataset in multiple databases. By distributing the data among multiple machines, a cluster of database systems can store larger datasets and handle additional requests. It is a form of horizontal scaling.

**Code Example**:
```javascript
// Shard by UserID
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q58"></a>
### Q58: What is Replication?

**Difficulty**: Intermediate

**Strategy**:
Copying data to multiple nodes. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Master-Slave
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q59"></a>
### Q59: What is CAP Theorem?

**Difficulty**: Intermediate

**Strategy**:
The CAP Theorem states that a distributed computer system can only provide two of the following three guarantees: Consistency (every read receives the most recent write or an error), Availability (every request receives a (non-error) response, without the guarantee that it contains the most recent write), and Partition Tolerance (the system continues to operate despite an arbitrary number of messages being dropped or delayed by the network).

**Code Example**:
```javascript
// Choose 2
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q60"></a>
### Q60: What is eventual consistency?

**Difficulty**: Intermediate

**Strategy**:
Data will become consistent over time. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// DNS, NoSQL
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q61"></a>
### Q61: What is a Transaction?

**Difficulty**: Beginner

**Strategy**:
A transaction is a single unit of work. If a transaction is successful, all of the data modifications made during the transaction are committed and become a permanent part of the database. If a transaction encounters an error and must be canceled or rolled back, then all of the data modifications are erased.

**Code Example**:
```javascript
START TRANSACTION
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q62"></a>
### Q62: Isolation Levels?

**Difficulty**: Advanced

**Strategy**:
Transaction isolation levels control the degree of locking and row versioning used when selecting data. The levels are: Read Uncommitted (lowest), Read Committed, Repeatable Read, and Serializable (highest). Higher isolation levels reduce concurrency effects but increase system overhead and blocking.

**Code Example**:
```javascript
SET TRANSACTION ISOLATION LEVEL ...
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q63"></a>
### Q63: What is Deadlock?

**Difficulty**: Intermediate

**Strategy**:
Two processes waiting for each other. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// A waits for B, B waits for A
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q64"></a>
### Q64: Optimistic vs Pessimistic Locking?

**Difficulty**: Advanced

**Strategy**:
Optimistic Locking assumes that multiple transactions can complete without affecting each other, and checks for conflicts only when committing. Pessimistic Locking locks the record as soon as it is selected for update, preventing others from modifying it until the lock is released.

**Code Example**:
```javascript
// SELECT ... FOR UPDATE
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q65"></a>
### Q65: What is Connection Pooling?

**Difficulty**: Intermediate

**Strategy**:
Reuse open connections. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Improves performance
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q66"></a>
### Q66: What is an ORM?

**Difficulty**: Beginner

**Strategy**:
Object Relational Mapper. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Hibernate, TypeORM
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q67"></a>
### Q67: N+1 Problem in DB?

**Difficulty**: Intermediate

**Strategy**:
The N+1 problem occurs when an application makes one query to retrieve a parent record (1) and then makes N subsequent queries to retrieve child records for each parent. This results in N+1 total database calls, which kills performance. It is usually solved by using JOINs or batch fetching (e.g., `IN` clause).

**Code Example**:
```javascript
// Use JOIN or batching
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q68"></a>
### Q68: What is MongoDB?

**Difficulty**: Beginner

**Strategy**:
Document store (BSON). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
db.users.find()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q69"></a>
### Q69: What is Redis?

**Difficulty**: Beginner

**Strategy**:
Redis is an open source (BSD licensed), in-memory data structure store, used as a database, cache, and message broker. It supports data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs, geospatial indexes, and streams.

**Code Example**:
```javascript
SET key value
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q70"></a>
### Q70: What is Cassandra?

**Difficulty**: Advanced

**Strategy**:
Wide-column store. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// High write throughput
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q71"></a>
### Q71: What is a Primary Key?

**Difficulty**: Beginner

**Strategy**:
Unique identifier. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
id INT PRIMARY KEY
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q72"></a>
### Q72: What is a Foreign Key?

**Difficulty**: Beginner

**Strategy**:
Link to another table. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
user_id INT REFERENCES users(id)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q73"></a>
### Q73: What is Database Migration?

**Difficulty**: Intermediate

**Strategy**:
Database migration is the management of incremental, reversible changes and version control to relational database schemas. A migration is a set of SQL queries that update the database schema to a newer version (e.g. creating a table, adding a column).

**Code Example**:
```javascript
// Flyway, Liquibase
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q74"></a>
### Q74: How to optimize a slow query?

**Difficulty**: Intermediate

**Strategy**:
EXPLAIN, Indexes, select specific columns. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
EXPLAIN SELECT ...
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q75"></a>
### Q75: What is SQL Injection?

**Difficulty**: Beginner

**Strategy**:
SQL injection is a code injection technique that might destroy your database. It is one of the most common web hacking techniques. SQL injection is the placement of malicious code in SQL statements, via web page input. It is prevented by using Prepared Statements (Parameterized Queries).

**Code Example**:
```javascript
// Use Prepared Statements
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q76"></a>
### Q76: What is a Cursor?

**Difficulty**: Intermediate

**Strategy**:
Pointer to result set row. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
FETCH NEXT FROM cursor
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q77"></a>
### Q77: What is ETL?

**Difficulty**: Intermediate

**Strategy**:
Extract, Transform, Load. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Data Warehousing
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q78"></a>
### Q78: OLTP vs OLAP?

**Difficulty**: Advanced

**Strategy**:
OLTP (Online Transaction Processing) captures, stores, and processes data from transactions in real-time. It is characterized by a large number of short on-line transactions (INSERT, UPDATE, DELETE). OLAP (Online Analytical Processing) uses complex queries to analyze aggregated historical data from OLTP systems.

**Code Example**:
```javascript
// Postgres vs Snowflake
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q79"></a>
### Q79: What is a Time Series DB?

**Difficulty**: Intermediate

**Strategy**:
Optimized for time-stamped data. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// InfluxDB
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q80"></a>
### Q80: What is Graph DB?

**Difficulty**: Intermediate

**Strategy**:
Nodes and Edges. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Neo4j
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q81"></a>
### Q81: What is Partitioning?

**Difficulty**: Advanced

**Strategy**:
Splitting table into smaller tables. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// By Range, List, Hash
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q82"></a>
### Q82: What is MVCC?

**Difficulty**: Advanced

**Strategy**:
Multiversion concurrency control (MVCC) is a concurrency control method used by database management systems to provide concurrent access to the database and in programming languages to implement transactional memory. It allows readers to see a snapshot of the data without blocking writers.

**Code Example**:
```javascript
// Readers don't block writers
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q83"></a>
### Q83: What is Write-Ahead Logging (WAL)?

**Difficulty**: Advanced

**Strategy**:
Log changes before writing to disk. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Durability
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q84"></a>
### Q84: What is a Materialized View?

**Difficulty**: Intermediate

**Strategy**:
Physically stored view, refreshed periodically. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
REFRESH MATERIALIZED VIEW
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q85"></a>
### Q85: What is Soft Delete?

**Difficulty**: Beginner

**Strategy**:
Flag as deleted instead of removing. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
UPDATE users SET deleted_at = NOW()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q86"></a>
### Q86: What is Database Mirroring?

**Difficulty**: Advanced

**Strategy**:
Real-time copy for High Availability. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Failover
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q87"></a>
### Q87: Row-oriented vs Column-oriented storage?

**Difficulty**: Advanced

**Strategy**:
Row-oriented databases store data row by row. This is great for transaction processing where you need to access all columns of a specific record. Column-oriented databases store data column by column. This is efficient for analytics where you often compute aggregates over a single column (e.g., average age) but don't need other columns.

**Code Example**:
```javascript
// Parquet files
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q88"></a>
### Q88: What is a Composite Key?

**Difficulty**: Intermediate

**Strategy**:
Key made of multiple columns. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
PRIMARY KEY (a, b)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q89"></a>
### Q89: What is a Surrogate Key?

**Difficulty**: Intermediate

**Strategy**:
Artificial key (e.g. auto-increment ID). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// vs Natural Key
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q90"></a>
### Q90: What is Referential Integrity?

**Difficulty**: Beginner

**Strategy**:
Consistency of relationships. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Foreign keys constraints
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q91"></a>
### Q91: What is a Bloom Filter in DB?

**Difficulty**: Advanced

**Strategy**:
Check if element exists in set (probabilistic). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Avoid disk lookups
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q92"></a>
### Q92: What is Two-Phase Commit (2PC)?

**Difficulty**: Advanced

**Strategy**:
Distributed transaction protocol. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Prepare -> Commit
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q93"></a>
### Q93: What is CDC (Change Data Capture)?

**Difficulty**: Advanced

**Strategy**:
Change Data Capture (CDC) is a set of software design patterns used to determine and track the data that has changed so that action can be taken using the changed data. It is often used to replicate data to a data warehouse or to trigger events in a microservices architecture.

**Code Example**:
```javascript
// Debezium
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q94"></a>
### Q94: What is Vacuuming?

**Difficulty**: Intermediate

**Strategy**:
Reclaiming storage (Postgres). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
VACUUM FULL
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q95"></a>
### Q95: What is a Clustered Index?

**Difficulty**: Advanced

**Strategy**:
Sorts table data physically. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Only one per table
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q96"></a>
### Q96: What is a Non-Clustered Index?

**Difficulty**: Advanced

**Strategy**:
Separate structure pointing to data. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Multiple allowed
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q97"></a>
### Q97: What is Database Sharding vs Partitioning?

**Difficulty**: Advanced

**Strategy**:
Sharding: across servers. Partitioning: within one server.

**Code Example**:
```javascript
// Scaling strategies
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q98"></a>
### Q98: What is a Spatial Index?

**Difficulty**: Intermediate

**Strategy**:
For geo data. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// R-Tree, Quad-Tree
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q99"></a>
### Q99: What is Full-Text Search?

**Difficulty**: Intermediate

**Strategy**:
Searching text docs. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Elasticsearch, tsvector
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q100"></a>
### Q100: What is B-Tree?

**Difficulty**: Advanced

**Strategy**:
Self-balancing tree data structure. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Default index
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q101"></a>
### Q101: What is Hash Index?

**Difficulty**: Advanced

**Strategy**:
O(1) lookups. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Good for equality checks
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>