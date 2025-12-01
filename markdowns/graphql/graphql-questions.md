<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>GraphQL Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [Difference between Query and Mutation?](#q1-difference-between-query-and-mutation) <span class="beginner">Beginner</span>
2. [How do you solve the N+1 problem in GraphQL?](#q2-how-do-you-solve-the-n1-problem-in-graphql) <span class="advanced">Advanced</span>
3. [How do you handle error handling in GraphQL?](#q3-how-do-you-handle-error-handling-in-graphql) <span class="intermediate">Intermediate</span>
4. [How do you implement pagination in GraphQL?](#q4-how-do-you-implement-pagination-in-graphql) <span class="intermediate">Intermediate</span>
5. [How do you secure a GraphQL API?](#q5-how-do-you-secure-a-graphql-api) <span class="advanced">Advanced</span>
6. [How do you use Fragments?](#q6-how-do-you-use-fragments) <span class="beginner">Beginner</span>
7. [What are Subscriptions?](#q7-what-are-subscriptions) <span class="intermediate">Intermediate</span>
8. [How do you handle file uploads?](#q8-how-do-you-handle-file-uploads) <span class="intermediate">Intermediate</span>
9. [Schema First vs Code First?](#q9-schema-first-vs-code-first) <span class="intermediate">Intermediate</span>
10. [How do you deprecate a field?](#q10-how-do-you-deprecate-a-field) <span class="beginner">Beginner</span>
11. [What are Directives in GraphQL?](#q11-what-are-directives-in-graphql) <span class="intermediate">Intermediate</span>
12. [What is Over-fetching and Under-fetching?](#q12-what-is-over-fetching-and-under-fetching) <span class="beginner">Beginner</span>
13. [How do you handle Authentication in GraphQL?](#q13-how-do-you-handle-authentication-in-graphql) <span class="intermediate">Intermediate</span>
14. [What are Resolvers?](#q14-what-are-resolvers) <span class="beginner">Beginner</span>
15. [What is Introspection?](#q15-what-is-introspection) <span class="intermediate">Intermediate</span>
16. [How do you handle caching in GraphQL?](#q16-how-do-you-handle-caching-in-graphql) <span class="advanced">Advanced</span>
17. [What is a Union type?](#q17-what-is-a-union-type) <span class="intermediate">Intermediate</span>
18. [What is an Interface type?](#q18-what-is-an-interface-type) <span class="intermediate">Intermediate</span>
19. [How do you version a GraphQL API?](#q19-how-do-you-version-a-graphql-api) <span class="intermediate">Intermediate</span>
20. [What are Enums in GraphQL?](#q20-what-are-enums-in-graphql) <span class="beginner">Beginner</span>
21. [How do you handle input validation?](#q21-how-do-you-handle-input-validation) <span class="intermediate">Intermediate</span>
22. [What is Apollo Federation?](#q22-what-is-apollo-federation) <span class="advanced">Advanced</span>
23. [How do you test GraphQL resolvers?](#q23-how-do-you-test-graphql-resolvers) <span class="intermediate">Intermediate</span>
24. [What is Schema Stitching?](#q24-what-is-schema-stitching) <span class="advanced">Advanced</span>
25. [How do you handle aliases?](#q25-how-do-you-handle-aliases) <span class="beginner">Beginner</span>
26. [What is a Scalar type?](#q26-what-is-a-scalar-type) <span class="beginner">Beginner</span>
27. [What is an Object type?](#q27-what-is-an-object-type) <span class="beginner">Beginner</span>
28. [What is the root Query type?](#q28-what-is-the-root-query-type) <span class="beginner">Beginner</span>
29. [What is the root Mutation type?](#q29-what-is-the-root-mutation-type) <span class="beginner">Beginner</span>
30. [What is the root Subscription type?](#q30-what-is-the-root-subscription-type) <span class="intermediate">Intermediate</span>
31. [What are Input types?](#q31-what-are-input-types) <span class="intermediate">Intermediate</span>
32. [What is Non-Null (!)?](#q32-what-is-non-null-) <span class="beginner">Beginner</span>
33. [What is a List ([])?](#q33-what-is-a-list-) <span class="beginner">Beginner</span>
34. [How do you define arguments?](#q34-how-do-you-define-arguments) <span class="beginner">Beginner</span>
35. [What is GraphiQL?](#q35-what-is-graphiql) <span class="beginner">Beginner</span>
36. [What is GraphQL Playground?](#q36-what-is-graphql-playground) <span class="beginner">Beginner</span>
37. [What is Apollo Server?](#q37-what-is-apollo-server) <span class="intermediate">Intermediate</span>
38. [What is `info` argument in resolver?](#q38-what-is-info-argument-in-resolver) <span class="advanced">Advanced</span>
39. [How do you handle authentication?](#q39-how-do-you-handle-authentication) <span class="intermediate">Intermediate</span>
40. [What is `context`?](#q40-what-is-context) <span class="intermediate">Intermediate</span>
41. [How do you batch requests?](#q41-how-do-you-batch-requests) <span class="advanced">Advanced</span>
42. [What is Persisted Queries?](#q42-what-is-persisted-queries) <span class="advanced">Advanced</span>
43. [What is Schema Stitching?](#q43-what-is-schema-stitching) <span class="advanced">Advanced</span>
44. [What is Federation?](#q44-what-is-federation) <span class="advanced">Advanced</span>
45. [What is a Gateway?](#q45-what-is-a-gateway) <span class="advanced">Advanced</span>
46. [How do you mock data?](#q46-how-do-you-mock-data) <span class="intermediate">Intermediate</span>
47. [What is Schema Directives?](#q47-what-is-schema-directives) <span class="advanced">Advanced</span>
48. [How do you handle pagination?](#q48-how-do-you-handle-pagination) <span class="intermediate">Intermediate</span>
49. [What is Cursor Pagination?](#q49-what-is-cursor-pagination) <span class="intermediate">Intermediate</span>
50. [What is Connection pattern?](#q50-what-is-connection-pattern) <span class="intermediate">Intermediate</span>
51. [How do you handle N+1 problem?](#q51-how-do-you-handle-n1-problem) <span class="advanced">Advanced</span>
52. [What is `dataloader` library?](#q52-what-is-dataloader-library) <span class="advanced">Advanced</span>
53. [How do you upload files?](#q53-how-do-you-upload-files) <span class="intermediate">Intermediate</span>
54. [What is Apollo Client?](#q54-what-is-apollo-client) <span class="beginner">Beginner</span>
55. [What is Relay?](#q55-what-is-relay) <span class="advanced">Advanced</span>
56. [What is Urql?](#q56-what-is-urql) <span class="intermediate">Intermediate</span>
57. [How do you cache on client?](#q57-how-do-you-cache-on-client) <span class="intermediate">Intermediate</span>
58. [What is `__typename`?](#q58-what-is-typename) <span class="intermediate">Intermediate</span>
59. [How do you use fragments on client?](#q59-how-do-you-use-fragments-on-client) <span class="intermediate">Intermediate</span>
60. [What is Inline Fragment?](#q60-what-is-inline-fragment) <span class="intermediate">Intermediate</span>
61. [How do you handle errors on client?](#q61-how-do-you-handle-errors-on-client) <span class="intermediate">Intermediate</span>
62. [What is Optimistic UI?](#q62-what-is-optimistic-ui) <span class="advanced">Advanced</span>
63. [How do you refetch data?](#q63-how-do-you-refetch-data) <span class="beginner">Beginner</span>
64. [What is Polling?](#q64-what-is-polling) <span class="intermediate">Intermediate</span>
65. [What is `network-only` policy?](#q65-what-is-network-only-policy) <span class="intermediate">Intermediate</span>
66. [What is `cache-first` policy?](#q66-what-is-cache-first-policy) <span class="intermediate">Intermediate</span>
67. [What is `cache-and-network`?](#q67-what-is-cache-and-network) <span class="intermediate">Intermediate</span>
68. [How do you update cache after mutation?](#q68-how-do-you-update-cache-after-mutation) <span class="advanced">Advanced</span>
69. [What is `readQuery`?](#q69-what-is-readquery) <span class="advanced">Advanced</span>
70. [What is `writeQuery`?](#q70-what-is-writequery) <span class="advanced">Advanced</span>
71. [What is `client` directive?](#q71-what-is-client-directive) <span class="intermediate">Intermediate</span>
72. [How do you manage local state?](#q72-how-do-you-manage-local-state) <span class="intermediate">Intermediate</span>
73. [What is Code Generation?](#q73-what-is-code-generation) <span class="intermediate">Intermediate</span>
74. [How do you document schema?](#q74-how-do-you-document-schema) <span class="beginner">Beginner</span>
75. [What is Deprecation?](#q75-what-is-deprecation) <span class="beginner">Beginner</span>
76. [How do you limit query depth?](#q76-how-do-you-limit-query-depth) <span class="advanced">Advanced</span>
77. [What is Query Cost Analysis?](#q77-what-is-query-cost-analysis) <span class="advanced">Advanced</span>
78. [How do you prevent introspection in prod?](#q78-how-do-you-prevent-introspection-in-prod) <span class="intermediate">Intermediate</span>
79. [What is `graphql-tools`?](#q79-what-is-graphql-tools) <span class="intermediate">Intermediate</span>
80. [How do you merge schemas?](#q80-how-do-you-merge-schemas) <span class="advanced">Advanced</span>
81. [What is Type merging?](#q81-what-is-type-merging) <span class="advanced">Advanced</span>
82. [How do you handle timeouts?](#q82-how-do-you-handle-timeouts) <span class="intermediate">Intermediate</span>
83. [What is Tracing?](#q83-what-is-tracing) <span class="advanced">Advanced</span>
84. [What is Apollo Studio?](#q84-what-is-apollo-studio) <span class="intermediate">Intermediate</span>
85. [How do you secure against DoS?](#q85-how-do-you-secure-against-dos) <span class="advanced">Advanced</span>
86. [What is JSON scalar?](#q86-what-is-json-scalar) <span class="intermediate">Intermediate</span>
87. [How do you handle Date?](#q87-how-do-you-handle-date) <span class="intermediate">Intermediate</span>
88. [What is the difference between REST and GraphQL?](#q88-what-is-the-difference-between-rest-and-graphql) <span class="beginner">Beginner</span>
89. [When to use GraphQL?](#q89-when-to-use-graphql) <span class="beginner">Beginner</span>
90. [When NOT to use GraphQL?](#q90-when-not-to-use-graphql) <span class="intermediate">Intermediate</span>
91. [What is `extensions` field?](#q91-what-is-extensions-field) <span class="advanced">Advanced</span>
92. [How do you debug resolvers?](#q92-how-do-you-debug-resolvers) <span class="beginner">Beginner</span>
93. [What is `parent` argument?](#q93-what-is-parent-argument) <span class="beginner">Beginner</span>
94. [How do you resolve abstract types?](#q94-how-do-you-resolve-abstract-types) <span class="advanced">Advanced</span>

---

### Q1: Difference between Query and Mutation?

**Difficulty**: Beginner

**Strategy**:
Query reads data (GET). Mutation modifies data (POST/PUT/DELETE).

**Code Example**:
```javascript
query { user(id: 1) { name } }
mutation { createUser(name: "Bob") { id } }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q2: How do you solve the N+1 problem in GraphQL?

**Difficulty**: Advanced

**Strategy**:
Use **DataLoaders** to batch and cache requests. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const userLoader = new DataLoader(keys => db.batchGetUsers(keys));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q3: How do you handle error handling in GraphQL?

**Difficulty**: Intermediate

**Strategy**:
Return `null` for the field and populate the `errors` array. Or use Union types for expected errors.

**Code Example**:
```javascript
union RegisterResult = User | UserError
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q4: How do you implement pagination in GraphQL?

**Difficulty**: Intermediate

**Strategy**:
Use Cursor-based pagination (Relay style) with `edges` and `pageInfo`.

**Code Example**:
```javascript
users(first: 10, after: "cursor") { edges { node { name } } }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q5: How do you secure a GraphQL API?

**Difficulty**: Advanced

**Strategy**:
Implement Depth Limiting, Query Cost Analysis, and Rate Limiting.

**Code Example**:
```javascript
validationRules: [depthLimit(10)]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q6: How do you use Fragments?

**Difficulty**: Beginner

**Strategy**:
Fragments allow reusing parts of a query. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
fragment UserFields on User { id name }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q7: What are Subscriptions?

**Difficulty**: Intermediate

**Strategy**:
Real-time updates using WebSockets. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
subscription { messageAdded { text } }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q8: How do you handle file uploads?

**Difficulty**: Intermediate

**Strategy**:
Use `graphql-upload` scalar. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
scalar Upload
mutation($file: Upload!) { uploadFile(file: $file) }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q9: Schema First vs Code First?

**Difficulty**: Intermediate

**Strategy**:
Schema First: Write SDL then resolvers. Code First: Write TS/JS classes that generate SDL.

**Code Example**:
```javascript
// Code First
t.field('name', { type: 'String' })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q10: How do you deprecate a field?

**Difficulty**: Beginner

**Strategy**:
Use the `@deprecated` directive. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
fullname: String @deprecated(reason: "Use 'name' instead")
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q11: What are Directives in GraphQL?

**Difficulty**: Intermediate

**Strategy**:
Directives allow you to attach metadata to fields or arguments to alter execution behavior (e.g., `@include`, `@skip`).

**Code Example**:
```javascript
query { hero(episode: JEDI) { name @include(if: $withFriends) } }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q12: What is Over-fetching and Under-fetching?

**Difficulty**: Beginner

**Strategy**:
Over-fetching: Downloading more data than needed. Under-fetching: Downloading less data, requiring multiple requests. GraphQL solves this by fetching exactly what is asked.

**Code Example**:
```javascript
// REST might return full User object. GraphQL returns only { name } if requested.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q13: How do you handle Authentication in GraphQL?

**Difficulty**: Intermediate

**Strategy**:
Pass the auth token in HTTP headers (e.g., Authorization: Bearer). Validate it in the context setup.

**Code Example**:
```javascript
const context = ({ req }) => { const user = getUser(req); return { user }; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q14: What are Resolvers?

**Difficulty**: Beginner

**Strategy**:
Functions that provide the instructions for turning a GraphQL operation into data. They resolve the value for a type or field.

**Code Example**:
```javascript
const resolvers = { Query: { user: (parent, args) => db.getUser(args.id) } }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q15: What is Introspection?

**Difficulty**: Intermediate

**Strategy**:
The ability to query a GraphQL schema for information about itself (types, fields, etc.).

**Code Example**:
```javascript
query { __schema { types { name } } }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q16: How do you handle caching in GraphQL?

**Difficulty**: Advanced

**Strategy**:
Since GraphQL uses POST, standard HTTP caching doesn't work well. Use client-side caching (Apollo Client) or persisted queries with CDNs.

**Code Example**:
```javascript
// Apollo Client uses InMemoryCache by default
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q17: What is a Union type?

**Difficulty**: Intermediate

**Strategy**:
A type that represents one of several other types.

**Code Example**:
```javascript
union SearchResult = Human | Droid | Starship
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q18: What is an Interface type?

**Difficulty**: Intermediate

**Strategy**:
An abstract type that includes a certain set of fields that a type must include to implement the interface.

**Code Example**:
```javascript
interface Character { id: ID! name: String! }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q19: How do you version a GraphQL API?

**Difficulty**: Intermediate

**Strategy**:
GraphQL promotes a continuous evolution of the schema (adding new fields, deprecating old ones) rather than version numbers (v1, v2).

**Code Example**:
```javascript
// Just add new fields and @deprecated old ones
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q20: What are Enums in GraphQL?

**Difficulty**: Beginner

**Strategy**:
A special scalar type that is restricted to a particular set of allowed values.

**Code Example**:
```javascript
enum Episode { NEWHOPE EMPIRE JEDI }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q21: How do you handle input validation?

**Difficulty**: Intermediate

**Strategy**:
Use custom scalars or throw errors inside resolvers.

**Code Example**:
```javascript
if (args.age < 0) throw new Error('Age must be positive');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q22: What is Apollo Federation?

**Difficulty**: Advanced

**Strategy**:
An architecture for composing multiple GraphQL services (subgraphs) into a single graph.

**Code Example**:
```javascript
// Subgraph 1: Users, Subgraph 2: Products -> Federated Gateway
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q23: How do you test GraphQL resolvers?

**Difficulty**: Intermediate

**Strategy**:
Treat resolvers as pure functions. Mock the context and arguments.

**Code Example**:
```javascript
const result = await resolvers.Query.user(null, { id: 1 }, mockContext);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q24: What is Schema Stitching?

**Difficulty**: Advanced

**Strategy**:
The process of creating a single GraphQL schema from multiple underlying GraphQL APIs. (Older alternative to Federation).

**Code Example**:
```javascript
const gatewaySchema = stitchSchemas({ subschemas: [schema1, schema2] });
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q25: How do you handle aliases?

**Difficulty**: Beginner

**Strategy**:
Aliases let you rename the result of a field to avoid conflicts.

**Code Example**:
```javascript
{ empireHero: hero(episode: EMPIRE) { name } jediHero: hero(episode: JEDI) { name } }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q26: What is a Scalar type?

**Difficulty**: Beginner

**Strategy**:
Primitive type (Int, Float, String, Boolean, ID). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
type User { id: ID! }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q27: What is an Object type?

**Difficulty**: Beginner

**Strategy**:
Type with fields. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
type User { name: String }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q28: What is the root Query type?

**Difficulty**: Beginner

**Strategy**:
Entry point for reads. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
type Query { me: User }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q29: What is the root Mutation type?

**Difficulty**: Beginner

**Strategy**:
Entry point for writes. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
type Mutation { save: Boolean }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q30: What is the root Subscription type?

**Difficulty**: Intermediate

**Strategy**:
Entry point for streams. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
type Subscription { onAdd: User }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q31: What are Input types?

**Difficulty**: Intermediate

**Strategy**:
Complex objects as arguments. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
input UserInput { name: String }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q32: What is Non-Null (!)?

**Difficulty**: Beginner

**Strategy**:
Field cannot be null. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
name: String!
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q33: What is a List ([])?

**Difficulty**: Beginner

**Strategy**:
Array of items. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
tags: [String]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q34: How do you define arguments?

**Difficulty**: Beginner

**Strategy**:
Inside parentheses. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
user(id: ID!): User
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q35: What is GraphiQL?

**Difficulty**: Beginner

**Strategy**:
IDE for testing GraphQL. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Browser tool
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q36: What is GraphQL Playground?

**Difficulty**: Beginner

**Strategy**:
Another IDE (by Prisma). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Similar to GraphiQL
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q37: What is Apollo Server?

**Difficulty**: Intermediate

**Strategy**:
Library to build GraphQL servers. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
new ApolloServer({ typeDefs, resolvers })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q38: What is `info` argument in resolver?

**Difficulty**: Advanced

**Strategy**:
AST of the query. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
resolve(parent, args, ctx, info)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q39: How do you handle authentication?

**Difficulty**: Intermediate

**Strategy**:
In context function. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
context: ({ req }) => ({ user: verify(req) })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q40: What is `context`?

**Difficulty**: Intermediate

**Strategy**:
Shared object passed to all resolvers. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Access DB, User info
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q41: How do you batch requests?

**Difficulty**: Advanced

**Strategy**:
Query batching (array of queries) or DataLoaders. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// [ { query: ... }, { query: ... } ]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q42: What is Persisted Queries?

**Difficulty**: Advanced

**Strategy**:
Send hash instead of full query string. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Saves bandwidth
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q43: What is Schema Stitching?

**Difficulty**: Advanced

**Strategy**:
Combine schemas. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
stitchSchemas({ subschemas: [...] })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q44: What is Federation?

**Difficulty**: Advanced

**Strategy**:
Microservices architecture for GraphQL. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
buildSubgraphSchema(...) 
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q45: What is a Gateway?

**Difficulty**: Advanced

**Strategy**:
Entry point for federated graph. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
new ApolloGateway(...) 
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q46: How do you mock data?

**Difficulty**: Intermediate

**Strategy**:
Use `mocks` option in Apollo. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
mocks: { Int: () => 6 }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q47: What is Schema Directives?

**Difficulty**: Advanced

**Strategy**:
Custom logic on schema elements. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
field: String @upper
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q48: How do you handle pagination?

**Difficulty**: Intermediate

**Strategy**:
Limit/Offset or Cursors. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
users(first: 10, after: "abc")
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q49: What is Cursor Pagination?

**Difficulty**: Intermediate

**Strategy**:
Pagination based on pointer. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
edges { cursor node { ... } }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q50: What is Connection pattern?

**Difficulty**: Intermediate

**Strategy**:
Standard for cursor pagination. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
type UserConnection { edges: [UserEdge] }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q51: How do you handle N+1 problem?

**Difficulty**: Advanced

**Strategy**:
DataLoaders. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
loader.load(id)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q52: What is `dataloader` library?

**Difficulty**: Advanced

**Strategy**:
Batching and caching utility. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
new DataLoader(batchFn)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q53: How do you upload files?

**Difficulty**: Intermediate

**Strategy**:
Multipart request spec. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
scalar Upload
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q54: What is Apollo Client?

**Difficulty**: Beginner

**Strategy**:
Client library. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
useQuery(GET_DOGS)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q55: What is Relay?

**Difficulty**: Advanced

**Strategy**:
Facebook's client library. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Optimized for performance
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q56: What is Urql?

**Difficulty**: Intermediate

**Strategy**:
Lightweight client. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Simple & extensible
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q57: How do you cache on client?

**Difficulty**: Intermediate

**Strategy**:
Normalization (InMemoryCache). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// cache-first, network-only
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q58: What is `__typename`?

**Difficulty**: Intermediate

**Strategy**:
Meta field for type name. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
{ name __typename }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q59: How do you use fragments on client?

**Difficulty**: Intermediate

**Strategy**:
Reuse query parts. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
fragment Name on User { name }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q60: What is Inline Fragment?

**Difficulty**: Intermediate

**Strategy**:
Fragment without name, for unions. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
... on Droid { primaryFunction }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q61: How do you handle errors on client?

**Difficulty**: Intermediate

**Strategy**:
Check `error` object. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const { error } = useQuery(...)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q62: What is Optimistic UI?

**Difficulty**: Advanced

**Strategy**:
Update UI before server responds. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
optimisticResponse: { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q63: How do you refetch data?

**Difficulty**: Beginner

**Strategy**:
Call `refetch`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const { refetch } = useQuery(...)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q64: What is Polling?

**Difficulty**: Intermediate

**Strategy**:
Periodically fetch data. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
pollInterval: 500
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q65: What is `network-only` policy?

**Difficulty**: Intermediate

**Strategy**:
Ignore cache. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
fetchPolicy: 'network-only'
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q66: What is `cache-first` policy?

**Difficulty**: Intermediate

**Strategy**:
Default. Use cache if available. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
fetchPolicy: 'cache-first'
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q67: What is `cache-and-network`?

**Difficulty**: Intermediate

**Strategy**:
Show cache, then update from network. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
fetchPolicy: 'cache-and-network'
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q68: How do you update cache after mutation?

**Difficulty**: Advanced

**Strategy**:
Use `update` function. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
update(cache, { data }) { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q69: What is `readQuery`?

**Difficulty**: Advanced

**Strategy**:
Read direct from cache. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
cache.readQuery({ query })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q70: What is `writeQuery`?

**Difficulty**: Advanced

**Strategy**:
Write direct to cache. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
cache.writeQuery({ query, data })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q71: What is `client` directive?

**Difficulty**: Intermediate

**Strategy**:
Client-only field. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
isLoggedIn @client
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q72: How do you manage local state?

**Difficulty**: Intermediate

**Strategy**:
Reactive variables or cache. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
makeVar(false)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q73: What is Code Generation?

**Difficulty**: Intermediate

**Strategy**:
Generate types from schema. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
graphql-codegen
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q74: How do you document schema?

**Difficulty**: Beginner

**Strategy**:
Comments/Descriptions. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
""" Description """
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q75: What is Deprecation?

**Difficulty**: Beginner

**Strategy**:
Mark field as old. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
@deprecated(reason: "...")
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q76: How do you limit query depth?

**Difficulty**: Advanced

**Strategy**:
Validation rule. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
depthLimit(5)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q77: What is Query Cost Analysis?

**Difficulty**: Advanced

**Strategy**:
Calculate complexity score. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Prevent expensive queries
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q78: How do you prevent introspection in prod?

**Difficulty**: Intermediate

**Strategy**:
Disable in server config. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
introspection: false
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q79: What is `graphql-tools`?

**Difficulty**: Intermediate

**Strategy**:
Utilities for schema building. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
makeExecutableSchema
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q80: How do you merge schemas?

**Difficulty**: Advanced

**Strategy**:
mergeSchemas tool. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
mergeSchemas({ schemas })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q81: What is Type merging?

**Difficulty**: Advanced

**Strategy**:
Merge types from different subgraphs. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Federation feature
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q82: How do you handle timeouts?

**Difficulty**: Intermediate

**Strategy**:
Server config or context cancellation. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// HTTP timeout
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q83: What is Tracing?

**Difficulty**: Advanced

**Strategy**:
Performance metrics. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
tracing: true
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q84: What is Apollo Studio?

**Difficulty**: Intermediate

**Strategy**:
Cloud dashboard. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Schema registry, metrics
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q85: How do you secure against DoS?

**Difficulty**: Advanced

**Strategy**:
Rate limiting, timeouts, complexity limits. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Security best practices
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q86: What is JSON scalar?

**Difficulty**: Intermediate

**Strategy**:
Arbitrary JSON blob. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
scalar JSON
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q87: How do you handle Date?

**Difficulty**: Intermediate

**Strategy**:
Custom scalar. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
scalar Date
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q88: What is the difference between REST and GraphQL?

**Difficulty**: Beginner

**Strategy**:
Endpoint vs Schema, Overfetching fix. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// GraphQL is flexible
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q89: When to use GraphQL?

**Difficulty**: Beginner

**Strategy**:
Complex data requirements, mobile apps. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Efficient data loading
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q90: When NOT to use GraphQL?

**Difficulty**: Intermediate

**Strategy**:
Simple APIs, file heavy, binary protocols. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// REST might be simpler
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q91: What is `extensions` field?

**Difficulty**: Advanced

**Strategy**:
Extra metadata in response. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
{ data, extensions: { tracing } }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q92: How do you debug resolvers?

**Difficulty**: Beginner

**Strategy**:
Console log or debugger. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
console.log(args)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q93: What is `parent` argument?

**Difficulty**: Beginner

**Strategy**:
Result of previous resolver. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
parent.id
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q94: How do you resolve abstract types?

**Difficulty**: Advanced

**Strategy**:
`__resolveType`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
__resolveType(obj) { return 'User' }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>