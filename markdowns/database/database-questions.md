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
6. [How do you resolve the N+1 query problem?](#q6-how-do-you-resolve-the-n+1-query-problem) <span class="intermediate">Intermediate</span>
7. [How do you use Window Functions to find the top 3 salaries per department?](#q7-how-do-you-use-window-functions-to-find-the-top-3-salaries-per-department) <span class="intermediate">Intermediate</span>
8. [How do you implement optimistic locking to handle concurrent updates?](#q8-how-do-you-implement-optimistic-locking-to-handle-concurrent-updates) <span class="intermediate">Intermediate</span>
9. [How do you ensure data consistency across microservices (Distributed Transaction)?](#q9-how-do-you-ensure-data-consistency-across-microservices-distributed-transaction) <span class="intermediate">Intermediate</span>
10. [How do you use a Redis cache to implement the 'Cache-Aside' pattern?](#q10-how-do-you-use-a-redis-cache-to-implement-the-cache-aside-pattern) <span class="intermediate">Intermediate</span>
11. [How do you structure a composite index to optimize a query with equality and range filters?](#q11-how-do-you-structure-a-composite-index-to-optimize-a-query-with-equality-and-range-filters) <span class="intermediate">Intermediate</span>
12. [How do you handle 'Soft Deletes' to preserve data history?](#q12-how-do-you-handle-soft-deletes-to-preserve-data-history) <span class="intermediate">Intermediate</span>
13. [How do you optimize database writes for a high-ingestion system (e.g., logs)?](#q13-how-do-you-optimize-database-writes-for-a-high-ingestion-system-e.g.-logs) <span class="intermediate">Intermediate</span>
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
29. [How do you identify and fix the N+1 query problem?](#q29-how-do-you-identify-and-fix-the-n+1-query-problem) <span class="intermediate">Intermediate</span>
30. [How do you partition a large table by date?](#q30-how-do-you-partition-a-large-table-by-date) <span class="advanced">Advanced</span>
31. [How do you implement Database Sharding and when should you use it?](#q31-how-do-you-implement-database-sharding-and-when-should-you-use-it) <span class="advanced">Advanced</span>
32. [How do you prevent Phantom Reads in a transaction?](#q32-how-do-you-prevent-phantom-reads-in-a-transaction) <span class="advanced">Advanced</span>
33. [How do you optimize a query using a Covering Index?](#q33-how-do-you-optimize-a-query-using-a-covering-index) <span class="intermediate">Intermediate</span>
34. [How do you handle 'Dirty Reads' and which isolation level prevents them?](#q34-how-do-you-handle-dirty-reads-and-which-isolation-level-prevents-them) <span class="intermediate">Intermediate</span>
35. [How do you implement connection pooling in a Node.js application?](#q35-how-do-you-implement-connection-pooling-in-a-node.js-application) <span class="intermediate">Intermediate</span>
36. [How do you model a tree structure (Hierarchy) in a Relational Database?](#q36-how-do-you-model-a-tree-structure-hierarchy-in-a-relational-database) <span class="advanced">Advanced</span>
37. [How do you use JSON columns in PostgreSQL vs MySQL?](#q37-how-do-you-use-json-columns-in-postgresql-vs-mysql) <span class="intermediate">Intermediate</span>
38. [How do you implement Row-Level Security (RLS)?](#q38-how-do-you-implement-row-level-security-rls) <span class="advanced">Advanced</span>
39. [How do you use a Materialized View for reporting?](#q39-how-do-you-use-a-materialized-view-for-reporting) <span class="intermediate">Intermediate</span>
40. [How do you generate unique IDs in a distributed system (Snowflake ID)?](#q40-how-do-you-generate-unique-ids-in-a-distributed-system-snowflake-id) <span class="advanced">Advanced</span>
41. [How do you use Foreign Data Wrappers (FDW) in PostgreSQL?](#q41-how-do-you-use-foreign-data-wrappers-fdw-in-postgresql) <span class="advanced">Advanced</span>
42. [How do you optimize a `LIKE` query with wildcards at the beginning?](#q42-how-do-you-optimize-a-like-query-with-wildcards-at-the-beginning) <span class="intermediate">Intermediate</span>
43. [How do you handle Deadlocks in a database?](#q43-how-do-you-handle-deadlocks-in-a-database) <span class="advanced">Advanced</span>
44. [How do you use the `CASE` statement for conditional logic in SQL?](#q44-how-do-you-use-the-case-statement-for-conditional-logic-in-sql) <span class="beginner">Beginner</span>
45. [How do you implement Database Replication (Master-Slave)?](#q45-how-do-you-implement-database-replication-master-slave) <span class="advanced">Advanced</span>
46. [How do you perform a Batch Insert efficiently?](#q46-how-do-you-perform-a-batch-insert-efficiently) <span class="intermediate">Intermediate</span>
47. [How do you use `GROUPING SETS` for multi-level aggregation?](#q47-how-do-you-use-grouping-sets-for-multi-level-aggregation) <span class="advanced">Advanced</span>
48. [How do you store and query time-series data efficiently?](#q48-how-do-you-store-and-query-time-series-data-efficiently) <span class="intermediate">Intermediate</span>
49. [How do you handle 'NoSQL' data modeling in DynamoDB (Single Table Design)?](#q49-how-do-you-handle-nosql-data-modeling-in-dynamodb-single-table-design) <span class="advanced">Advanced</span>
50. [How do you identify and remove duplicate rows from a table?](#q50-how-do-you-identify-and-remove-duplicate-rows-from-a-table) <span class="intermediate">Intermediate</span>
51. [How do you handle Database state management in large scale applications?](#q51-how-do-you-handle-database-state-management-in-large-scale-applications) <span class="advanced">Advanced</span>
52. [How do you perform Database data validation in microservices?](#q52-how-do-you-perform-database-data-validation-in-microservices) <span class="beginner">Beginner</span>
53. [How do you automate Database deployment for mobile devices?](#q53-how-do-you-automate-database-deployment-for-mobile-devices) <span class="advanced">Advanced</span>
54. [How do you handle Database concurrency issues in legacy systems?](#q54-how-do-you-handle-database-concurrency-issues-in-legacy-systems) <span class="advanced">Advanced</span>
55. [How do you implement Database caching in cloud infrastructure?](#q55-how-do-you-implement-database-caching-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
56. [How do you manage Database configuration for real-time systems?](#q56-how-do-you-manage-database-configuration-for-real-time-systems) <span class="beginner">Beginner</span>
57. [How do you handle Database internationalization (i18n) in distributed systems?](#q57-how-do-you-handle-database-internationalization-i18n-in-distributed-systems) <span class="intermediate">Intermediate</span>
58. [How do you ensure Database accessibility (a11y) in high-traffic sites?](#q58-how-do-you-ensure-database-accessibility-a11y-in-high-traffic-sites) <span class="beginner">Beginner</span>
59. [How do you optimize Database network requests in embedded systems?](#q59-how-do-you-optimize-database-network-requests-in-embedded-systems) <span class="advanced">Advanced</span>
60. [How do you handle Database performance optimization for production environments?](#q60-how-do-you-handle-database-performance-optimization-for-production-environments) <span class="advanced">Advanced</span>
61. [What are the security implications of Database in large scale applications?](#q61-what-are-the-security-implications-of-database-in-large-scale-applications) <span class="intermediate">Intermediate</span>
62. [How do you debug Database memory leaks in microservices?](#q62-how-do-you-debug-database-memory-leaks-in-microservices) <span class="advanced">Advanced</span>
63. [Best practices for Database code organization in mobile devices?](#q63-best-practices-for-database-code-organization-in-mobile-devices) <span class="beginner">Beginner</span>
64. [How do you implement Database error handling for legacy systems?](#q64-how-do-you-implement-database-error-handling-for-legacy-systems) <span class="intermediate">Intermediate</span>
65. [How do you test Database functionality in cloud infrastructure?](#q65-how-do-you-test-database-functionality-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
66. [How do you handle Database state management in real-time systems?](#q66-how-do-you-handle-database-state-management-in-real-time-systems) <span class="advanced">Advanced</span>
67. [How do you perform Database data validation in distributed systems?](#q67-how-do-you-perform-database-data-validation-in-distributed-systems) <span class="beginner">Beginner</span>
68. [How do you automate Database deployment for high-traffic sites?](#q68-how-do-you-automate-database-deployment-for-high-traffic-sites) <span class="advanced">Advanced</span>
69. [How do you handle Database concurrency issues in embedded systems?](#q69-how-do-you-handle-database-concurrency-issues-in-embedded-systems) <span class="advanced">Advanced</span>
70. [How do you implement Database caching in production environments?](#q70-how-do-you-implement-database-caching-in-production-environments) <span class="intermediate">Intermediate</span>
71. [How do you manage Database configuration for large scale applications?](#q71-how-do-you-manage-database-configuration-for-large-scale-applications) <span class="beginner">Beginner</span>
72. [How do you handle Database internationalization (i18n) in microservices?](#q72-how-do-you-handle-database-internationalization-i18n-in-microservices) <span class="intermediate">Intermediate</span>
73. [How do you ensure Database accessibility (a11y) in mobile devices?](#q73-how-do-you-ensure-database-accessibility-a11y-in-mobile-devices) <span class="beginner">Beginner</span>
74. [How do you optimize Database network requests in legacy systems?](#q74-how-do-you-optimize-database-network-requests-in-legacy-systems) <span class="advanced">Advanced</span>
75. [How do you handle Database performance optimization for cloud infrastructure?](#q75-how-do-you-handle-database-performance-optimization-for-cloud-infrastructure) <span class="advanced">Advanced</span>
76. [What are the security implications of Database in real-time systems?](#q76-what-are-the-security-implications-of-database-in-real-time-systems) <span class="intermediate">Intermediate</span>
77. [How do you debug Database memory leaks in distributed systems?](#q77-how-do-you-debug-database-memory-leaks-in-distributed-systems) <span class="advanced">Advanced</span>
78. [Best practices for Database code organization in high-traffic sites?](#q78-best-practices-for-database-code-organization-in-high-traffic-sites) <span class="beginner">Beginner</span>
79. [How do you implement Database error handling for embedded systems?](#q79-how-do-you-implement-database-error-handling-for-embedded-systems) <span class="intermediate">Intermediate</span>
80. [How do you test Database functionality in production environments?](#q80-how-do-you-test-database-functionality-in-production-environments) <span class="intermediate">Intermediate</span>
81. [How do you handle Database state management in large scale applications?](#q81-how-do-you-handle-database-state-management-in-large-scale-applications) <span class="advanced">Advanced</span>
82. [How do you perform Database data validation in microservices?](#q82-how-do-you-perform-database-data-validation-in-microservices) <span class="beginner">Beginner</span>
83. [How do you automate Database deployment for mobile devices?](#q83-how-do-you-automate-database-deployment-for-mobile-devices) <span class="advanced">Advanced</span>
84. [How do you handle Database concurrency issues in legacy systems?](#q84-how-do-you-handle-database-concurrency-issues-in-legacy-systems) <span class="advanced">Advanced</span>
85. [How do you implement Database caching in cloud infrastructure?](#q85-how-do-you-implement-database-caching-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
86. [How do you manage Database configuration for real-time systems?](#q86-how-do-you-manage-database-configuration-for-real-time-systems) <span class="beginner">Beginner</span>
87. [How do you handle Database internationalization (i18n) in distributed systems?](#q87-how-do-you-handle-database-internationalization-i18n-in-distributed-systems) <span class="intermediate">Intermediate</span>
88. [How do you ensure Database accessibility (a11y) in high-traffic sites?](#q88-how-do-you-ensure-database-accessibility-a11y-in-high-traffic-sites) <span class="beginner">Beginner</span>
89. [How do you optimize Database network requests in embedded systems?](#q89-how-do-you-optimize-database-network-requests-in-embedded-systems) <span class="advanced">Advanced</span>
90. [How do you handle Database performance optimization for production environments?](#q90-how-do-you-handle-database-performance-optimization-for-production-environments) <span class="advanced">Advanced</span>
91. [What are the security implications of Database in large scale applications?](#q91-what-are-the-security-implications-of-database-in-large-scale-applications) <span class="intermediate">Intermediate</span>
92. [How do you debug Database memory leaks in microservices?](#q92-how-do-you-debug-database-memory-leaks-in-microservices) <span class="advanced">Advanced</span>
93. [Best practices for Database code organization in mobile devices?](#q93-best-practices-for-database-code-organization-in-mobile-devices) <span class="beginner">Beginner</span>
94. [How do you implement Database error handling for legacy systems?](#q94-how-do-you-implement-database-error-handling-for-legacy-systems) <span class="intermediate">Intermediate</span>
95. [How do you test Database functionality in cloud infrastructure?](#q95-how-do-you-test-database-functionality-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
96. [How do you handle Database state management in real-time systems?](#q96-how-do-you-handle-database-state-management-in-real-time-systems) <span class="advanced">Advanced</span>
97. [How do you perform Database data validation in distributed systems?](#q97-how-do-you-perform-database-data-validation-in-distributed-systems) <span class="beginner">Beginner</span>
98. [How do you automate Database deployment for high-traffic sites?](#q98-how-do-you-automate-database-deployment-for-high-traffic-sites) <span class="advanced">Advanced</span>
99. [How do you handle Database concurrency issues in embedded systems?](#q99-how-do-you-handle-database-concurrency-issues-in-embedded-systems) <span class="advanced">Advanced</span>
100. [How do you implement Database caching in production environments?](#q100-how-do-you-implement-database-caching-in-production-environments) <span class="intermediate">Intermediate</span>

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


### Q31: How do you implement Database Sharding and when should you use it?

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

### Q32: How do you prevent Phantom Reads in a transaction?

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

### Q33: How do you optimize a query using a Covering Index?

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

### Q34: How do you handle 'Dirty Reads' and which isolation level prevents them?

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

### Q35: How do you implement connection pooling in a Node.js application?

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

### Q36: How do you model a tree structure (Hierarchy) in a Relational Database?

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

### Q37: How do you use JSON columns in PostgreSQL vs MySQL?

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

### Q38: How do you implement Row-Level Security (RLS)?

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

### Q39: How do you use a Materialized View for reporting?

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

### Q40: How do you generate unique IDs in a distributed system (Snowflake ID)?

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

### Q41: How do you use Foreign Data Wrappers (FDW) in PostgreSQL?

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

### Q42: How do you optimize a `LIKE` query with wildcards at the beginning?

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

### Q43: How do you handle Deadlocks in a database?

**Difficulty**: Advanced

**Strategy:**
Deadlocks occur when two transactions block each other. Handle them by: 1. Ordering updates consistently. 2. Keeping transactions short. 3. Using retry logic in the application.

**Code Example:**
-- Scenario causing Deadlock
-- Tx1: Locks Row A, needs Row B
-- Tx2: Locks Row B, needs Row A

-- Solution: Consistent Ordering
-- Always lock tables/rows in the same order (e.g., by ID)

-- Tx1
UPDATE accounts SET balance = balance - 10 WHERE id = 1;
UPDATE accounts SET balance = balance + 10 WHERE id = 2;

-- Tx2 (Must follow same order: 1 then 2)
UPDATE accounts SET balance = balance - 20 WHERE id = 1;
UPDATE accounts SET balance = balance + 20 WHERE id = 2;

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q44: How do you use the `CASE` statement for conditional logic in SQL?

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

### Q45: How do you implement Database Replication (Master-Slave)?

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

### Q46: How do you perform a Batch Insert efficiently?

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

### Q47: How do you use `GROUPING SETS` for multi-level aggregation?

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

### Q48: How do you store and query time-series data efficiently?

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

### Q49: How do you handle 'NoSQL' data modeling in DynamoDB (Single Table Design)?

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

### Q50: How do you identify and remove duplicate rows from a table?

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


### Q51: How do you handle Database state management in large scale applications?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```sql
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q52: How do you perform Database data validation in microservices?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```sql
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q53: How do you automate Database deployment for mobile devices?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application.

**Code Example**:
```sql
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q54: How do you handle Database concurrency issues in legacy systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations.

**Code Example**:
```sql
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q55: How do you implement Database caching in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches.

**Code Example**:
```sql
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q56: How do you manage Database configuration for real-time systems?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files.

**Code Example**:
```sql
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q57: How do you handle Database internationalization (i18n) in distributed systems?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```sql
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q58: How do you ensure Database accessibility (a11y) in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles.

**Code Example**:
```sql
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q59: How do you optimize Database network requests in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL.

**Code Example**:
```sql
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q60: How do you handle Database performance optimization for production environments?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```sql
const start = performance.now();
// Database logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q61: What are the security implications of Database in large scale applications?

**Difficulty**: Intermediate

**Strategy**:
Validate all inputs. Sanitize data. Use least privilege principle.

**Code Example**:
```sql
// Sanitize input
const clean = input.replace(/<script>/g, '');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q62: How do you debug Database memory leaks in microservices?

**Difficulty**: Advanced

**Strategy**:
Use heap snapshots and look for detached DOM nodes or uncleared listeners.

**Code Example**:
```sql
// Check listeners
process.on('exit', () => cleanup());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q63: Best practices for Database code organization in mobile devices?

**Difficulty**: Beginner

**Strategy**:
Follow SOLID principles. Keep functions small and focused.

**Code Example**:
```sql
// Single responsibility
function doOneThing() { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q64: How do you implement Database error handling for legacy systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```sql
try {
  await DatabaseOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q65: How do you test Database functionality in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```sql
test('Database works', () => {
  expect(Database()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q66: How do you handle Database state management in real-time systems?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```sql
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q67: How do you perform Database data validation in distributed systems?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```sql
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q68: How do you automate Database deployment for high-traffic sites?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application.

**Code Example**:
```sql
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q69: How do you handle Database concurrency issues in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations.

**Code Example**:
```sql
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q70: How do you implement Database caching in production environments?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches.

**Code Example**:
```sql
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q71: How do you manage Database configuration for large scale applications?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files.

**Code Example**:
```sql
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q72: How do you handle Database internationalization (i18n) in microservices?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```sql
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q73: How do you ensure Database accessibility (a11y) in mobile devices?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles.

**Code Example**:
```sql
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q74: How do you optimize Database network requests in legacy systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL.

**Code Example**:
```sql
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q75: How do you handle Database performance optimization for cloud infrastructure?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```sql
const start = performance.now();
// Database logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q76: What are the security implications of Database in real-time systems?

**Difficulty**: Intermediate

**Strategy**:
Validate all inputs. Sanitize data. Use least privilege principle.

**Code Example**:
```sql
// Sanitize input
const clean = input.replace(/<script>/g, '');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q77: How do you debug Database memory leaks in distributed systems?

**Difficulty**: Advanced

**Strategy**:
Use heap snapshots and look for detached DOM nodes or uncleared listeners.

**Code Example**:
```sql
// Check listeners
process.on('exit', () => cleanup());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q78: Best practices for Database code organization in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Follow SOLID principles. Keep functions small and focused.

**Code Example**:
```sql
// Single responsibility
function doOneThing() { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q79: How do you implement Database error handling for embedded systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```sql
try {
  await DatabaseOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q80: How do you test Database functionality in production environments?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```sql
test('Database works', () => {
  expect(Database()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q81: How do you handle Database state management in large scale applications?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```sql
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q82: How do you perform Database data validation in microservices?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```sql
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q83: How do you automate Database deployment for mobile devices?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application.

**Code Example**:
```sql
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q84: How do you handle Database concurrency issues in legacy systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations.

**Code Example**:
```sql
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q85: How do you implement Database caching in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches.

**Code Example**:
```sql
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q86: How do you manage Database configuration for real-time systems?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files.

**Code Example**:
```sql
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q87: How do you handle Database internationalization (i18n) in distributed systems?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```sql
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q88: How do you ensure Database accessibility (a11y) in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles.

**Code Example**:
```sql
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q89: How do you optimize Database network requests in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL.

**Code Example**:
```sql
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q90: How do you handle Database performance optimization for production environments?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```sql
const start = performance.now();
// Database logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q91: What are the security implications of Database in large scale applications?

**Difficulty**: Intermediate

**Strategy**:
Validate all inputs. Sanitize data. Use least privilege principle.

**Code Example**:
```sql
// Sanitize input
const clean = input.replace(/<script>/g, '');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q92: How do you debug Database memory leaks in microservices?

**Difficulty**: Advanced

**Strategy**:
Use heap snapshots and look for detached DOM nodes or uncleared listeners.

**Code Example**:
```sql
// Check listeners
process.on('exit', () => cleanup());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q93: Best practices for Database code organization in mobile devices?

**Difficulty**: Beginner

**Strategy**:
Follow SOLID principles. Keep functions small and focused.

**Code Example**:
```sql
// Single responsibility
function doOneThing() { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q94: How do you implement Database error handling for legacy systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```sql
try {
  await DatabaseOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q95: How do you test Database functionality in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```sql
test('Database works', () => {
  expect(Database()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q96: How do you handle Database state management in real-time systems?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```sql
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q97: How do you perform Database data validation in distributed systems?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```sql
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q98: How do you automate Database deployment for high-traffic sites?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application.

**Code Example**:
```sql
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q99: How do you handle Database concurrency issues in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations.

**Code Example**:
```sql
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q100: How do you implement Database caching in production environments?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches.

**Code Example**:
```sql
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---
