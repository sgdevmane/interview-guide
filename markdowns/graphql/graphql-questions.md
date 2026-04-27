<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>GraphQL Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [Difference between Query and Mutation?](#q1) <span class="beginner">Beginner</span>
2. [How do you solve the N+1 problem in GraphQL?](#q2) <span class="advanced">Advanced</span>
3. [How do you handle error handling in GraphQL?](#q3) <span class="intermediate">Intermediate</span>
4. [How do you implement pagination in GraphQL?](#q4) <span class="intermediate">Intermediate</span>
5. [How do you secure a GraphQL API?](#q5) <span class="advanced">Advanced</span>
6. [How do you use Fragments?](#q6) <span class="beginner">Beginner</span>
7. [What are Subscriptions?](#q7) <span class="intermediate">Intermediate</span>
8. [How do you handle file uploads?](#q8) <span class="intermediate">Intermediate</span>
9. [Schema First vs Code First?](#q9) <span class="intermediate">Intermediate</span>
10. [How do you deprecate a field?](#q10) <span class="beginner">Beginner</span>
11. [What are Directives in GraphQL?](#q11) <span class="intermediate">Intermediate</span>
12. [What is Over-fetching and Under-fetching?](#q12) <span class="beginner">Beginner</span>
13. [How do you handle Authentication in GraphQL?](#q13) <span class="intermediate">Intermediate</span>
14. [What are Resolvers?](#q14) <span class="beginner">Beginner</span>
15. [What is Introspection?](#q15) <span class="intermediate">Intermediate</span>
16. [How do you handle caching in GraphQL?](#q16) <span class="advanced">Advanced</span>
17. [What is a Union type?](#q17) <span class="intermediate">Intermediate</span>
18. [What is an Interface type?](#q18) <span class="intermediate">Intermediate</span>
19. [How do you version a GraphQL API?](#q19) <span class="intermediate">Intermediate</span>
20. [What are Enums in GraphQL?](#q20) <span class="beginner">Beginner</span>
21. [How do you handle input validation?](#q21) <span class="intermediate">Intermediate</span>
22. [What is Apollo Federation?](#q22) <span class="advanced">Advanced</span>
23. [How do you test GraphQL resolvers?](#q23) <span class="intermediate">Intermediate</span>
24. [What is Schema Stitching?](#q24) <span class="advanced">Advanced</span>
25. [How do you handle aliases?](#q25) <span class="beginner">Beginner</span>
26. [What is a Scalar type?](#q26) <span class="beginner">Beginner</span>
27. [What is an Object type?](#q27) <span class="beginner">Beginner</span>
28. [What is the root Query type?](#q28) <span class="beginner">Beginner</span>
29. [What is the root Mutation type?](#q29) <span class="beginner">Beginner</span>
30. [What is the root Subscription type?](#q30) <span class="intermediate">Intermediate</span>
31. [What are Input types?](#q31) <span class="intermediate">Intermediate</span>
32. [What is Non-Null (!)?](#q32) <span class="beginner">Beginner</span>
33. [What is a List ([])?](#q33) <span class="beginner">Beginner</span>
34. [How do you define arguments?](#q34) <span class="beginner">Beginner</span>
35. [What is GraphiQL?](#q35) <span class="beginner">Beginner</span>
36. [What is GraphQL Playground?](#q36) <span class="beginner">Beginner</span>
37. [What is Apollo Server?](#q37) <span class="intermediate">Intermediate</span>
38. [What is `info` argument in resolver?](#q38) <span class="advanced">Advanced</span>
39. [How do you handle authentication?](#q39) <span class="intermediate">Intermediate</span>
40. [What is `context`?](#q40) <span class="intermediate">Intermediate</span>
41. [How do you batch requests?](#q41) <span class="advanced">Advanced</span>
42. [What is Persisted Queries?](#q42) <span class="advanced">Advanced</span>
43. [What is Schema Stitching?](#q43) <span class="advanced">Advanced</span>
44. [What is Federation?](#q44) <span class="advanced">Advanced</span>
45. [What is a Gateway?](#q45) <span class="advanced">Advanced</span>
46. [How do you mock data?](#q46) <span class="intermediate">Intermediate</span>
47. [What is Schema Directives?](#q47) <span class="advanced">Advanced</span>
48. [How do you handle pagination?](#q48) <span class="intermediate">Intermediate</span>
49. [What is Cursor Pagination?](#q49) <span class="intermediate">Intermediate</span>
50. [What is Connection pattern?](#q50) <span class="intermediate">Intermediate</span>
51. [How do you handle N+1 problem?](#q51) <span class="advanced">Advanced</span>
52. [What is `dataloader` library?](#q52) <span class="advanced">Advanced</span>
53. [How do you upload files?](#q53) <span class="intermediate">Intermediate</span>
54. [What is Apollo Client?](#q54) <span class="beginner">Beginner</span>
55. [What is Relay?](#q55) <span class="advanced">Advanced</span>
56. [What is Urql?](#q56) <span class="intermediate">Intermediate</span>
57. [How do you cache on client?](#q57) <span class="intermediate">Intermediate</span>
58. [What is `__typename`?](#q58) <span class="intermediate">Intermediate</span>
59. [How do you use fragments on client?](#q59) <span class="intermediate">Intermediate</span>
60. [What is Inline Fragment?](#q60) <span class="intermediate">Intermediate</span>
61. [How do you handle errors on client?](#q61) <span class="intermediate">Intermediate</span>
62. [What is Optimistic UI?](#q62) <span class="advanced">Advanced</span>
63. [How do you refetch data?](#q63) <span class="beginner">Beginner</span>
64. [What is Polling?](#q64) <span class="intermediate">Intermediate</span>
65. [What is `network-only` policy?](#q65) <span class="intermediate">Intermediate</span>
66. [What is `cache-first` policy?](#q66) <span class="intermediate">Intermediate</span>
67. [What is `cache-and-network`?](#q67) <span class="intermediate">Intermediate</span>
68. [How do you update cache after mutation?](#q68) <span class="advanced">Advanced</span>
69. [What is `readQuery`?](#q69) <span class="advanced">Advanced</span>
70. [What is `writeQuery`?](#q70) <span class="advanced">Advanced</span>
71. [What is `client` directive?](#q71) <span class="intermediate">Intermediate</span>
72. [How do you manage local state?](#q72) <span class="intermediate">Intermediate</span>
73. [What is Code Generation?](#q73) <span class="intermediate">Intermediate</span>
74. [How do you document schema?](#q74) <span class="beginner">Beginner</span>
75. [What is Deprecation?](#q75) <span class="beginner">Beginner</span>
76. [How do you limit query depth?](#q76) <span class="advanced">Advanced</span>
77. [What is Query Cost Analysis?](#q77) <span class="advanced">Advanced</span>
78. [How do you prevent introspection in prod?](#q78) <span class="intermediate">Intermediate</span>
79. [What is `graphql-tools`?](#q79) <span class="intermediate">Intermediate</span>
80. [How do you merge schemas?](#q80) <span class="advanced">Advanced</span>
81. [What is Type merging?](#q81) <span class="advanced">Advanced</span>
82. [How do you handle timeouts?](#q82) <span class="intermediate">Intermediate</span>
83. [What is Tracing?](#q83) <span class="advanced">Advanced</span>
84. [What is Apollo Studio?](#q84) <span class="intermediate">Intermediate</span>
85. [How do you secure against DoS?](#q85) <span class="advanced">Advanced</span>
86. [What is JSON scalar?](#q86) <span class="intermediate">Intermediate</span>
87. [How do you handle Date?](#q87) <span class="intermediate">Intermediate</span>
88. [What is the difference between REST and GraphQL?](#q88) <span class="beginner">Beginner</span>
89. [When to use GraphQL?](#q89) <span class="beginner">Beginner</span>
90. [When NOT to use GraphQL?](#q90) <span class="intermediate">Intermediate</span>
91. [What is `extensions` field?](#q91) <span class="advanced">Advanced</span>
92. [How do you debug resolvers?](#q92) <span class="beginner">Beginner</span>
93. [What is `parent` argument?](#q93) <span class="beginner">Beginner</span>
94. [How do you resolve abstract types?](#q94) <span class="advanced">Advanced</span>
95. [What are Persisted Queries?](#q95) <span class="advanced">Advanced</span>
96. [Explain the `@defer` directive.](#q96) <span class="advanced">Advanced</span>
97. [How do you limit Query Depth?](#q97) <span class="intermediate">Intermediate</span>
98. [What is Query Complexity Analysis?](#q98) <span class="advanced">Advanced</span>
99. [GraphQL over WebSockets vs HTTP/2 Streams?](#q99) <span class="advanced">Advanced</span>
100. [How to handle N+1 problem with DataLoader?](#q100) <span class="advanced">Advanced</span>
101. [What are the benefits of Code-First vs Schema-First?](#q101) <span class="intermediate">Intermediate</span>

---

<a id="q1"></a>
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

<a id="q2"></a>
### Q2: How do you solve the N+1 problem in GraphQL?

**Difficulty**: Advanced

**Strategy**: The N+1 problem is the most common performance pitfall in GraphQL, where a list query triggers one query per item in the resolver chain. The standard solution is to use Facebook's DataLoader library, which batches and deduplicates database requests within a single execution tick. A common mistake is creating a new DataLoader instance per module instead of per request, which breaks request-scoped caching.

**Code Example**:
```javascript
const userLoader = new DataLoader(keys => db.batchGetUsers(keys));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q3"></a>
### Q3: How do you handle error handling in GraphQL?

**Difficulty**: Intermediate

**Strategy**: Error handling in GraphQL differs from REST because every response returns HTTP 200, so errors must be structured within the response body using the `errors` array. Using Union types for expected business errors gives clients type-safe error handling, while unexpected errors should propagate to the top-level `errors` array. A common pitfall is swallowing errors silently by returning `null` without adding context, which makes debugging production issues extremely difficult.

**Code Example**:
```javascript
union RegisterResult = User | UserError
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q4"></a>
### Q4: How do you implement pagination in GraphQL?

**Difficulty**: Intermediate

**Strategy**: Pagination is a critical GraphQL topic because unbounded list queries can overwhelm both the server and client with massive result sets. The Relay-style cursor-based connection spec (`edges`, `pageInfo`, `cursors`) is the industry standard, offering stable pagination even when data changes between requests. A common mistake is using simple offset-based pagination for frequently changing datasets, which causes items to be skipped or duplicated when rows are inserted or deleted between pages.

**Code Example**:
```javascript
users(first: 10, after: "cursor") { edges { node { name } } }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q5"></a>
### Q5: How do you secure a GraphQL API?

**Difficulty**: Advanced

**Strategy**: GraphQL security is a frequent interview topic because the language's flexibility lets clients craft arbitrarily complex queries that can exhaust server resources. The three pillars of defense are depth limiting to cap nesting, query cost analysis to cap computational expense, and rate limiting to cap request frequency. A common oversight is only applying these guards to public endpoints -- internal APIs also need protection, since a compromised or buggy internal client can cause just as much damage.

**Code Example**:
```javascript
validationRules: [depthLimit(10)]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q6"></a>
### Q6: How do you use Fragments?

**Difficulty**: Beginner

**Strategy**: Fragments are reusable units of GraphQL fields that help you avoid repeating the same field selections across multiple queries and mutations. They are especially valuable in large applications where multiple components need the same shape of data, and they pair well with colocation patterns on the client side. Avoid creating overly large fragments that pull in unnecessary data, as this defeats GraphQL's purpose of fetching only what is needed.

**Code Example**:
```javascript
fragment UserFields on User { id name }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q7"></a>
### Q7: What are Subscriptions?

**Difficulty**: Intermediate

**Strategy**: Subscriptions are GraphQL's mechanism for real-time data pushed from the server to the client, typically implemented over WebSockets. They are essential for features like live chat, notifications, or real-time dashboards where polling would be wasteful. A common pitfall is overusing subscriptions when a simple polling or refetch strategy would suffice, so reserve them for data that truly changes unpredictably in real time.

**Code Example**:
```javascript
subscription { messageAdded { text } }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q8"></a>
### Q8: How do you handle file uploads?

**Difficulty**: Intermediate

**Strategy**: File uploads in GraphQL use the multipart request specification with a custom `Upload` scalar type, allowing files to be sent alongside the query in a single HTTP request. The server parses the multipart boundary and exposes the file stream to resolvers through the `context` or `args`. Avoid encoding large files as base64 in mutations, as this inflates payload size by roughly 33 percent and can hit server body size limits.

**Code Example**:
```javascript
scalar Upload
mutation($file: Upload!) { uploadFile(file: $file) }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q9"></a>
### Q9: Schema First vs Code First?

**Difficulty**: Intermediate

**Strategy**: The Schema First vs Code First decision shapes how your team designs, maintains, and evolves the GraphQL API. Schema First (writing SDL by hand) encourages API-first design and is language-agnostic, while Code First (using TypeScript/JS classes that generate SDL) provides better type safety and refactoring support. The trade-off is that Schema First can become tedious to keep in sync with resolvers, whereas Code First can obscure the actual API contract behind implementation code.

**Code Example**:
```javascript
// Code First
t.field('name', { type: 'String' })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q10"></a>
### Q10: How do you deprecate a field?

**Difficulty**: Beginner

**Strategy**: Deprecation in GraphQL is done using the built-in `@deprecated` directive with an optional reason, which signals to clients that a field will be removed in the future without breaking existing queries. This is a core part of GraphQL's schema evolution model, which favors continuous evolution over versioned endpoints. A best practice is to monitor usage of deprecated fields through tooling before actually removing them to avoid breaking active consumers.

**Code Example**:
```javascript
fullname: String @deprecated(reason: "Use 'name' instead")
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q11"></a>
### Q11: What are Directives in GraphQL?

**Difficulty**: Intermediate

**Strategy**: Directives are a powerful mechanism in GraphQL that let you conditionally include or skip fields, attach metadata for server-side processing, or modify execution behavior without changing the query structure. The spec provides `@include`, `@skip`, and `@deprecated` as built-in directives, but custom directives enable patterns like auth guards, rate limiting, and field-level caching. A common mistake is confusing client-side directives (which affect query shape) with server-side schema directives (which affect resolver behavior), as they serve entirely different purposes.

**Code Example**:
```javascript
query { hero(episode: JEDI) { name @include(if: $withFriends) } }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q12"></a>
### Q12: What is Over-fetching and Under-fetching?

**Difficulty**: Beginner

**Strategy**: Over-fetching and under-fetching are the two core problems GraphQL was designed to solve, making this a fundamental interview question. Over-fetching wastes bandwidth and processing time when the server returns more data than needed, while under-fetching forces multiple round-trips to assemble the required data. GraphQL addresses both by letting the client specify exactly which fields it needs in a single request, but a pitfall is creating schemas with massive monolithic types that inadvertently encourage over-fetching if clients are not disciplined.

**Code Example**:
```javascript
// REST might return full User object. GraphQL returns only { name } if requested.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q13"></a>
### Q13: How do you handle Authentication in GraphQL?

**Difficulty**: Intermediate

**Strategy**: Authentication in GraphQL is a frequent interview topic because the spec deliberately omits an auth mechanism, leaving it to the implementor. The standard approach is to extract tokens from HTTP headers in the context function and attach the decoded user to the shared context, where resolvers or directive-based guards can enforce authorization. A common pitfall is scattering authentication checks across individual resolvers instead of centralizing them in the context setup, which leads to duplicated logic and security gaps.

**Code Example**:
```javascript
const context = ({ req }) => { const user = getUser(req); return { user }; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q14"></a>
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

<a id="q15"></a>
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

<a id="q16"></a>
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

<a id="q17"></a>
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

<a id="q18"></a>
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

<a id="q19"></a>
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

<a id="q20"></a>
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

<a id="q21"></a>
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

<a id="q22"></a>
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

<a id="q23"></a>
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

<a id="q24"></a>
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

<a id="q25"></a>
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

<a id="q26"></a>
### Q26: What is a Scalar type?

**Difficulty**: Beginner

**Strategy**: Scalar types are the leaf nodes of a GraphQL query -- they represent concrete data values like `Int`, `Float`, `String`, `Boolean`, and `ID` that cannot contain sub-fields. Understanding scalars is fundamental because every field in a schema eventually resolves to a scalar. You can also define custom scalars (e.g., `Date`, `Email`) with serialization, parsing, and validation logic to enforce domain-specific constraints.

**Code Example**:
```javascript
type User { id: ID! }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q27"></a>
### Q27: What is an Object type?

**Difficulty**: Beginner

**Strategy**: Object types are the building blocks of a GraphQL schema, representing entities with named fields that each resolve to a scalar or another object type. They form the graph structure that clients traverse in queries, and interviewers often ask about them to verify you understand how type composition works. A common mistake is creating deeply nested object hierarchies that make queries verbose and resolvers harder to maintain.

**Code Example**:
```javascript
type User { name: String }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q28"></a>
### Q28: What is the root Query type?

**Difficulty**: Beginner

**Strategy**: The root Query type is the entry point for all read operations in a GraphQL schema -- every GraphQL query starts from one of its fields. It acts as the public API surface for data fetching, and each field maps to a resolver function that retrieves data from your data sources. A best practice is to keep the root Query type organized by domain and delegate actual data fetching to field-specific resolvers rather than putting logic in a single massive resolver.

**Code Example**:
```javascript
type Query { me: User }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q29"></a>
### Q29: What is the root Mutation type?

**Difficulty**: Beginner

**Strategy**: The root Mutation type is the entry point for all data-modifying operations in GraphQL, serving as the equivalent of POST, PUT, PATCH, and DELETE in REST. Unlike queries, mutations are executed sequentially (not in parallel), which guarantees that side effects happen in a predictable order. A common pitfall is placing read-only fields on the Mutation type; only operations that modify server-side state should live here.

**Code Example**:
```javascript
type Mutation { save: Boolean }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q30"></a>
### Q30: What is the root Subscription type?

**Difficulty**: Intermediate

**Strategy**: The root Subscription type defines the entry points for real-time, event-driven data pushed from the server to subscribed clients. Each subscription field sets up a persistent connection (usually over WebSocket) and an async iterator that yields results when triggered events occur. Be mindful that subscriptions can be resource-intensive on the server, so implement cleanup logic and consider connection limits to avoid scalability issues.

**Code Example**:
```javascript
type Subscription { onAdd: User }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q31"></a>
### Q31: What are Input types?

**Difficulty**: Intermediate

**Strategy**: Input types define the structure of arguments passed into mutations or queries, acting as the schema-level equivalent of request body DTOs. They differ from output object types in that they cannot contain resolvers or reference other output types, keeping them strictly data-transfer vessels. A best practice is to create dedicated input types per mutation rather than reusing output types as inputs, which keeps the API contract clear and avoids coupling.

**Code Example**:
```javascript
input UserInput { name: String }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q32"></a>
### Q32: What is Non-Null (!)?

**Difficulty**: Beginner

**Strategy**: The Non-Null modifier (`!`) guarantees that a field will never return `null`, and the server will throw an error if the resolver fails to produce a value. This is critical for schema design because it propagates errors up to the nearest nullable parent, affecting how partial data is returned to clients. Be cautious when marking fields Non-Null, as changing a field from non-null to nullable is a breaking change for generated client types.

**Code Example**:
```javascript
name: String!
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q33"></a>
### Q33: What is a List ([])?

**Difficulty**: Beginner

**Strategy**: The List type modifier (`[]`) indicates that a field returns an ordered collection of the specified type, similar to arrays in most programming languages. Lists can be combined with Non-Null modifiers (e.g., `[String!]!`) to enforce different levels of strictness on the array itself versus its elements. A common source of confusion is the difference between `[String]`, `[String!]`, `[String]!`, and `[String!]!`, so be prepared to explain each variation in interviews.

**Code Example**:
```javascript
tags: [String]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q34"></a>
### Q34: How do you define arguments?

**Difficulty**: Beginner

**Strategy**: Arguments allow clients to pass parameters into fields and directives, enabling filtered, paginated, or parameterized queries. They can be defined on any field in the schema using built-in scalar types, enums, or custom input types for complex structures. A best practice is to use input types rather than many individual arguments when a field needs more than three or four parameters, keeping the schema clean and maintainable.

**Code Example**:
```javascript
user(id: ID!): User
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q35"></a>
### Q35: What is GraphiQL?

**Difficulty**: Beginner

**Strategy**: GraphiQL is an in-browser IDE for exploring and testing GraphQL APIs, providing features like syntax highlighting, auto-completion, and inline documentation powered by schema introspection. It is the go-to tool during development for iterating on queries and debugging resolver behavior interactively. Be aware that GraphiQL should be disabled in production environments, as exposing an interactive query explorer can leak schema details to attackers.

**Code Example**:
```javascript
// Browser tool
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q36"></a>
### Q36: What is GraphQL Playground?

**Difficulty**: Beginner

**Strategy**: GraphQL Playground is an enhanced GraphQL IDE built by Prisma (now part of Apollo Studio) that extends GraphiQL with features like tabs for multiple operations, HTTP headers configuration, and subscription support. It was widely used with Apollo Server v2 as the default landing page but has since been deprecated in favor of Apollo Sandbox. Interviewers may ask about it to check whether you understand the evolution of GraphQL developer tooling.

**Code Example**:
```javascript
// Similar to GraphiQL
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q37"></a>
### Q37: What is Apollo Server?

**Difficulty**: Intermediate

**Strategy**: Apollo Server is the most popular open-source GraphQL server implementation for JavaScript, providing a production-ready setup with features like automatic persisted queries, tracing, and federation support out of the box. It abstracts away much of the boilerplate involved in setting up a spec-compliant GraphQL server, making it a common choice in real-world projects. Be prepared to discuss its context function, plugin system, and how it integrates with various Node.js frameworks like Express or Fastify.

**Code Example**:
```javascript
new ApolloServer({ typeDefs, resolvers })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q38"></a>
### Q38: What is `info` argument in resolver?

**Difficulty**: Advanced

**Strategy**: The `info` argument is the fourth parameter in every resolver and contains the AST representation of the incoming query, including field selections, fragments, and directives. Advanced use cases include dynamic field-level authorization, selective database projection (only fetching fields the client requested), and custom directive processing. Avoid over-relying on the info argument for business logic, as traversing the AST manually can make resolvers fragile and hard to test.

**Code Example**:
```javascript
resolve(parent, args, ctx, info)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q39"></a>
### Q39: How do you handle authentication?

**Difficulty**: Intermediate

**Strategy**: Authentication in GraphQL is typically handled at the HTTP transport layer rather than inside resolvers, with tokens extracted from headers and the decoded user attached to the shared context object. Individual resolvers or directive-based guards can then check the context to enforce authorization rules per field. A common mistake is trying to authenticate inside individual resolvers instead of centralizing it in the context setup, which leads to duplicated logic and security gaps.

**Code Example**:
```javascript
context: ({ req }) => ({ user: verify(req) })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q40"></a>
### Q40: What is `context`?

**Difficulty**: Intermediate

**Strategy**: The context object is a shared dictionary passed to every resolver in a single GraphQL request, commonly used to hold authenticated user data, database connections, and service instances. It is created once per request by a context function (often extracting auth headers) and remains immutable throughout query execution. A best practice is to keep the context lightweight and avoid storing request-specific mutable state, as parallel resolver execution can lead to race conditions.

**Code Example**:
```javascript
// Access DB, User info
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q41"></a>
### Q41: How do you batch requests?

**Difficulty**: Advanced

**Strategy**: Request batching sends multiple GraphQL operations in a single HTTP request as an array, reducing network overhead when a client needs to execute several independent queries at once. This is different from query batching at the resolver level (DataLoader), and instead works at the transport layer to amortize connection costs. Be careful with batch size limits on the server side, as very large batches can cause long response times that block the entire array.

**Code Example**:
```javascript
// [ { query: ... }, { query: ... } ]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q42"></a>
### Q42: What is Persisted Queries?

**Difficulty**: Advanced

**Strategy**: Persisted queries replace full query strings with a hash identifier, dramatically reducing request payload sizes and enabling server-side query whitelisting for security. Apollo's automatic persisted queries (APQ) protocol sends the full query only on the first request and uses the hash on subsequent calls. This technique is especially valuable for mobile clients on high-latency networks, but ensure your CDN or gateway is configured to cache the persisted query map.

**Code Example**:
```javascript
// Saves bandwidth
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q43"></a>
### Q43: What is Schema Stitching?

**Difficulty**: Advanced

**Strategy**: Schema Stitching is the process of combining multiple independent GraphQL schemas into a single unified gateway schema, allowing clients to query across services as if they were one graph. It differs from Federation in that it merges schemas at the gateway level without requiring subgraphs to follow a specific specification. While powerful, it can become complex to maintain as services grow, which is why Apollo Federation has become the more popular choice for large-scale microservice architectures.

**Code Example**:
```javascript
stitchSchemas({ subschemas: [...] })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q44"></a>
### Q44: What is Federation?

**Difficulty**: Advanced

**Strategy**: Federation is Apollo's architecture for building a distributed graph where multiple independently owned subgraph services compose into a single supergraph accessible through a gateway. Each subgraph defines its own schema and can extend types owned by other subgraphs using the `@key` and `@external` directives. The key advantage over stitching is that subgraph teams can work autonomously, but the trade-off is adopting Apollo's federation specification and managing gateway deployment complexity.

**Code Example**:
```javascript
buildSubgraphSchema(...) 
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q45"></a>
### Q45: What is a Gateway?

**Difficulty**: Advanced

**Strategy**: A GraphQL Gateway is a single entry-point server that receives client queries, decomposes them into sub-queries for the relevant subgraphs, and stitches the results back together. In a federated architecture, the gateway reads the composed supergraph schema to understand how to route each field to its owning service. A common operational concern is gateway uptime -- since all traffic flows through it, implement health checks, caching, and failover strategies to avoid a single point of failure.

**Code Example**:
```javascript
new ApolloGateway(...) 
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q46"></a>
### Q46: How do you mock data?

**Difficulty**: Intermediate

**Strategy**: Mocking in GraphQL allows you to generate fake data from your schema without writing real resolvers, which is invaluable for frontend development before the backend is complete. Apollo Server provides a built-in mocking system where you can supply default values per type or use functions that generate dynamic data. Avoid relying on mocks too long in the development cycle, as the transition to real resolvers can surface edge cases that mocks hide.

**Code Example**:
```javascript
mocks: { Int: () => 6 }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q47"></a>
### Q47: What is Schema Directives?

**Difficulty**: Advanced

**Strategy**: Schema directives are server-side annotations that modify the behavior of schema elements at build or execution time, enabling cross-cutting concerns like auth, rate limiting, or field transformation. Unlike client-side directives (`@skip`, `@include`), schema directives are implemented as transformer functions or resolver wrappers applied during schema construction. A best practice is to use directives to encapsulate reusable logic rather than scattering authorization and validation checks across individual resolvers.

**Code Example**:
```javascript
field: String @upper
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q48"></a>
### Q48: How do you handle pagination?

**Difficulty**: Intermediate

**Strategy**: Pagination in GraphQL is typically implemented using cursor-based connections (the Relay specification), where clients pass a cursor and a page size to navigate through result sets. This approach is more stable than offset-based pagination for datasets that change frequently, as cursors remain valid even when items are added or removed. A common mistake is returning unpaginated lists for large collections, which leads to performance issues and memory problems on both server and client.

**Code Example**:
```javascript
users(first: 10, after: "abc")
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q49"></a>
### Q49: What is Cursor Pagination?

**Difficulty**: Intermediate

**Strategy**: Cursor pagination uses an opaque token (cursor) to mark a specific position in the result set, typically an encoded timestamp or database ID, rather than numeric offsets. This makes pagination resilient to data changes between requests, as the cursor always points to the exact position regardless of insertions or deletions. Avoid exposing internal database IDs directly as cursors; instead, encode them (e.g., base64) to maintain an opaque contract that lets you change the underlying implementation later.

**Code Example**:
```javascript
edges { cursor node { ... } }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q50"></a>
### Q50: What is Connection pattern?

**Difficulty**: Intermediate

**Strategy**: The Connection pattern, formalized in the Relay cursor connections specification, wraps paginated results in a standardized structure of `edges` (containing `node` and `cursor`) and `pageInfo` (containing `hasNextPage` and `hasPreviousPage`). This pattern provides a consistent contract for pagination across all list fields in your schema, simplifying client-side pagination logic. A common oversight is omitting `totalCount` from connections when clients need it for UI displays like page counters, so consider adding it as an optional field.

**Code Example**:
```javascript
type UserConnection { edges: [UserEdge] }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q51"></a>
### Q51: How do you handle N+1 problem?

**Difficulty**: Advanced

**Strategy**: The N+1 problem occurs when a resolver fetching a list triggers a separate database call for each item, turning a single list query into dozens or hundreds of queries. The primary solution is batching via DataLoader, which collects individual loads within the same event loop tick and dispatches them as a single batched request. Avoid the trap of creating DataLoader instances at module scope; they must be created per request to prevent cross-user data leaks.

**Code Example**:
```javascript
loader.load(id)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q52"></a>
### Q52: What is `dataloader` library?

**Difficulty**: Advanced

**Strategy**: DataLoader is a utility by Facebook that batches and caches database (or API) calls per request, collecting individual `load(key)` calls made during a single execution tick and executing them as one batch function. It also provides per-request memoization, meaning the same key loaded twice in one request returns the cached result without an additional call. A key detail to mention in interviews is that the batch function must return results in the same order as the input keys, which is why index-based mapping is critical.

**Code Example**:
```javascript
new DataLoader(batchFn)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q53"></a>
### Q53: How do you upload files?

**Difficulty**: Intermediate

**Strategy**: File uploads in GraphQL use the `Upload` scalar and the multipart request spec, where files are sent as parts of a multipart HTTP request alongside the GraphQL operation. The resolver receives a file stream that can be piped to storage services like S3 without buffering the entire file in memory. For very large files or multi-gigabyte uploads, consider using presigned URLs and direct-to-storage uploads instead of routing through the GraphQL server.

**Code Example**:
```javascript
scalar Upload
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q54"></a>
### Q54: What is Apollo Client?

**Difficulty**: Beginner

**Strategy**: Apollo Client is a comprehensive GraphQL client library that handles querying, caching, state management, and error handling in frontend applications. Its normalized cache (`InMemoryCache`) automatically deduplicates entities by `__typename` and `id`, keeping the UI in sync when the same data appears in multiple queries. A common pitfall is not including `id` fields in queries, which prevents the cache from normalizing and updating entities correctly across the application.

**Code Example**:
```javascript
useQuery(GET_DOGS)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q55"></a>
### Q55: What is Relay?

**Difficulty**: Advanced

**Strategy**: Relay is Facebook's GraphQL client framework designed for high-performance applications at scale, enforcing strict conventions like the Relay cursor connections specification and colocated fragment declarations per component. Its compiler pre-processes queries at build time, generating optimized artifacts that reduce runtime overhead and enable dead-code elimination. The trade-off is a steeper learning curve and more boilerplate compared to Apollo Client, so it is best suited for large teams that need its rigorous structure and performance guarantees.

**Code Example**:
```javascript
// Optimized for performance
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q56"></a>
### Q56: What is Urql?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
// Simple & extensible
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q57"></a>
### Q57: How do you cache on client?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
// cache-first, network-only
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q58"></a>
### Q58: What is `__typename`?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
{ name __typename }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q59"></a>
### Q59: How do you use fragments on client?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
fragment Name on User { name }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q60"></a>
### Q60: What is Inline Fragment?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
... on Droid { primaryFunction }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q61"></a>
### Q61: How do you handle errors on client?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
const { error } = useQuery(...)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q62"></a>
### Q62: What is Optimistic UI?

**Difficulty**: Advanced

**Strategy**:

**Code Example**:
```javascript
optimisticResponse: { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q63"></a>
### Q63: How do you refetch data?

**Difficulty**: Beginner

**Strategy**:

**Code Example**:
```javascript
const { refetch } = useQuery(...)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q64"></a>
### Q64: What is Polling?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
pollInterval: 500
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q65"></a>
### Q65: What is `network-only` policy?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
fetchPolicy: 'network-only'
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q66"></a>
### Q66: What is `cache-first` policy?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
fetchPolicy: 'cache-first'
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q67"></a>
### Q67: What is `cache-and-network`?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
fetchPolicy: 'cache-and-network'
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q68"></a>
### Q68: How do you update cache after mutation?

**Difficulty**: Advanced

**Strategy**:

**Code Example**:
```javascript
update(cache, { data }) { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q69"></a>
### Q69: What is `readQuery`?

**Difficulty**: Advanced

**Strategy**:

**Code Example**:
```javascript
cache.readQuery({ query })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q70"></a>
### Q70: What is `writeQuery`?

**Difficulty**: Advanced

**Strategy**:

**Code Example**:
```javascript
cache.writeQuery({ query, data })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q71"></a>
### Q71: What is `client` directive?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
isLoggedIn @client
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q72"></a>
### Q72: How do you manage local state?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
makeVar(false)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q73"></a>
### Q73: What is Code Generation?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
graphql-codegen
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q74"></a>
### Q74: How do you document schema?

**Difficulty**: Beginner

**Strategy**:

**Code Example**:
```javascript
""" Description """
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q75"></a>
### Q75: What is Deprecation?

**Difficulty**: Beginner

**Strategy**:

**Code Example**:
```javascript
@deprecated(reason: "...")
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q76"></a>
### Q76: How do you limit query depth?

**Difficulty**: Advanced

**Strategy**:

**Code Example**:
```javascript
depthLimit(5)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q77"></a>
### Q77: What is Query Cost Analysis?

**Difficulty**: Advanced

**Strategy**:

**Code Example**:
```javascript
// Prevent expensive queries
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q78"></a>
### Q78: How do you prevent introspection in prod?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
introspection: false
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q79"></a>
### Q79: What is `graphql-tools`?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
makeExecutableSchema
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q80"></a>
### Q80: How do you merge schemas?

**Difficulty**: Advanced

**Strategy**:

**Code Example**:
```javascript
mergeSchemas({ schemas })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q81"></a>
### Q81: What is Type merging?

**Difficulty**: Advanced

**Strategy**:

**Code Example**:
```javascript
// Federation feature
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q82"></a>
### Q82: How do you handle timeouts?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
// HTTP timeout
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q83"></a>
### Q83: What is Tracing?

**Difficulty**: Advanced

**Strategy**:

**Code Example**:
```javascript
tracing: true
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q84"></a>
### Q84: What is Apollo Studio?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
// Schema registry, metrics
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q85"></a>
### Q85: How do you secure against DoS?

**Difficulty**: Advanced

**Strategy**:

**Code Example**:
```javascript
// Security best practices
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q86"></a>
### Q86: What is JSON scalar?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
scalar JSON
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q87"></a>
### Q87: How do you handle Date?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
scalar Date
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q88"></a>
### Q88: What is the difference between REST and GraphQL?

**Difficulty**: Beginner

**Strategy**:

**Code Example**:
```javascript
// GraphQL is flexible
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q89"></a>
### Q89: When to use GraphQL?

**Difficulty**: Beginner

**Strategy**:

**Code Example**:
```javascript
// Efficient data loading
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q90"></a>
### Q90: When NOT to use GraphQL?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
// REST might be simpler
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q91"></a>
### Q91: What is `extensions` field?

**Difficulty**: Advanced

**Strategy**:

**Code Example**:
```javascript
{ data, extensions: { tracing } }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q92"></a>
### Q92: How do you debug resolvers?

**Difficulty**: Beginner

**Strategy**:

**Code Example**:
```javascript
console.log(args)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q93"></a>
### Q93: What is `parent` argument?

**Difficulty**: Beginner

**Strategy**:

**Code Example**:
```javascript
parent.id
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q94"></a>
### Q94: How do you resolve abstract types?

**Difficulty**: Advanced

**Strategy**:

**Code Example**:
```javascript
__resolveType(obj) { return 'User' }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div><a id="q95"></a>

### Q95: What are Persisted Queries?

**Difficulty**: Advanced

**Strategy**: Persisted queries are a technique where the query string is sent to the server once, hashed, and stored. subsequent requests send only the hash. This improves performance by reducing payload size and allows whitelisting queries for security.

**Code Example**: 
```javascript
// Client sends hash instead of full query string
// GET /graphql?extensions={"persistedQuery":{"version":1,"sha256Hash":"..."}}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q96"></a>

### Q96: Explain the `@defer` directive.

**Difficulty**: Advanced

**Strategy**: `@defer` allows you to delay the delivery of certain fields in the response. This is useful for fields that are slow to resolve (like expensive computations or third-party API calls) but are not critical for the initial render. It enables incremental delivery of data.

**Code Example**: 
```javascript
query {
  user(id: "1") {
    name
    ... @defer {
      purchaseHistory # Slow field
    }
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q97"></a>

### Q97: How do you limit Query Depth?

**Difficulty**: Intermediate

**Strategy**: Query depth limiting prevents malicious or expensive recursive queries (like A -> B -> A -> B...) by rejecting queries that are nested too deeply. This is usually implemented using a validation rule in the GraphQL server setup.

**Code Example**: 
```javascript
import depthLimit from 'graphql-depth-limit';

const server = new ApolloServer({
  schema,
  validationRules: [depthLimit(5)] // Max depth of 5
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q98"></a>

### Q98: What is Query Complexity Analysis?

**Difficulty**: Advanced

**Strategy**: Query complexity analysis assigns a 'cost' to each field and rejects queries that exceed a total cost threshold. This is more sophisticated than depth limiting as it accounts for the computational expense of specific fields.

**Code Example**: 
```javascript
// Example cost configuration
// simpleField: 1
// complexField: 10
// listField: 5 * limit
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q99"></a>

### Q99: GraphQL over WebSockets vs HTTP/2 Streams?

**Difficulty**: Advanced

**Strategy**: Traditionally, Subscriptions used WebSockets for persistent connections. However, HTTP/2 Streams (and Server-Sent Events) are becoming popular as they are easier to manage through firewalls/proxies and don't require a separate protocol handshake. `@stream` and `@defer` typically use multipart HTTP responses.

**Code Example**: 
```javascript
// SSE (Server-Sent Events) is often preferred now for simple unidirectional streams over managing full WebSocket connections.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q100"></a>

### Q100: How to handle N+1 problem with DataLoader?

**Difficulty**: Advanced

**Strategy**: DataLoader batches multiple requests for data into a single request to the database. It uses a tick-based batching mechanism. Instead of executing a SQL query for each resolver, it collects all IDs and executes `SELECT * FROM table WHERE id IN (...)`.

**Code Example**: 
```javascript
const userLoader = new DataLoader(async keys => {
  const users = await getUsers(keys);
  return keys.map(key => users.find(user => user.id === key));
});

// Resolver
resolve(parent) {
  return userLoader.load(parent.userId);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q101"></a>

### Q101: What are the benefits of Code-First vs Schema-First?

**Difficulty**: Intermediate

**Strategy**: **Schema-First**: Good for API design discussions, language agnostic. 
**Code-First** (e.g., Nexus, Pothos): Better type safety in implementation, code acts as source of truth, easier to refactor. The choice often depends on team preference and tooling.

**Code Example**: 
```javascript
// Code-First (Nexus)
objectType({
  name: 'User',
  definition(t) {
    t.string('name')
  }
})
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

