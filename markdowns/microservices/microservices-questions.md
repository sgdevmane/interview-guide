<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/devops-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Microservices Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [What is Microservices Architecture?](#q1) <span class="beginner">Beginner</span>
2. [Benefits of Microservices?](#q2) <span class="beginner">Beginner</span>
3. [Drawbacks of Microservices?](#q3) <span class="beginner">Beginner</span>
4. [What is an API Gateway?](#q4) <span class="intermediate">Intermediate</span>
5. [What is Service Discovery?](#q5) <span class="intermediate">Intermediate</span>
6. [Client-side vs Server-side Discovery?](#q6) <span class="advanced">Advanced</span>
7. [What is Circuit Breaker Pattern?](#q7) <span class="intermediate">Intermediate</span>
8. [What is Bulkhead Pattern?](#q8) <span class="advanced">Advanced</span>
9. [What is Saga Pattern?](#q9) <span class="advanced">Advanced</span>
10. [Choreography vs Orchestration?](#q10) <span class="advanced">Advanced</span>
11. [What is Event Sourcing?](#q11) <span class="advanced">Advanced</span>
12. [What is CQRS?](#q12) <span class="advanced">Advanced</span>
13. [How do you handle Authentication?](#q13) <span class="intermediate">Intermediate</span>
14. [What is Distributed Tracing?](#q14) <span class="intermediate">Intermediate</span>
15. [What is Centralized Logging?](#q15) <span class="intermediate">Intermediate</span>
16. [Idempotency in Microservices?](#q16) <span class="intermediate">Intermediate</span>
17. [Inter-service Communication Styles?](#q17) <span class="beginner">Beginner</span>
18. [What is gRPC?](#q18) <span class="intermediate">Intermediate</span>
19. [REST vs gRPC?](#q19) <span class="intermediate">Intermediate</span>
20. [What is a Message Broker?](#q20) <span class="beginner">Beginner</span>
21. [Kafka vs RabbitMQ?](#q21) <span class="advanced">Advanced</span>
22. [What is API Composition?](#q22) <span class="intermediate">Intermediate</span>
23. [What is Database per Service?](#q23) <span class="intermediate">Intermediate</span>
24. [What is Shared Database Antipattern?](#q24) <span class="intermediate">Intermediate</span>
25. [How do you handle Data Consistency?](#q25) <span class="advanced">Advanced</span>
26. [What is CAP Theorem?](#q26) <span class="intermediate">Intermediate</span>
27. [What is 12-Factor App?](#q27) <span class="intermediate">Intermediate</span>
28. [How do you version APIs?](#q28) <span class="beginner">Beginner</span>
29. [What is Consumer Driven Contracts (CDC)?](#q29) <span class="advanced">Advanced</span>
30. [What is Chaos Engineering?](#q30) <span class="advanced">Advanced</span>
31. [Blue-Green Deployment?](#q31) <span class="intermediate">Intermediate</span>
32. [Canary Release?](#q32) <span class="intermediate">Intermediate</span>
33. [Strangler Fig Pattern?](#q33) <span class="advanced">Advanced</span>
34. [What is BFF (Backend for Frontend)?](#q34) <span class="intermediate">Intermediate</span>
35. [What is Sidecar Pattern?](#q35) <span class="intermediate">Intermediate</span>
36. [What is Service Mesh?](#q36) <span class="advanced">Advanced</span>
37. [How to prevent Cascading Failures?](#q37) <span class="intermediate">Intermediate</span>
38. [What is Rate Limiting?](#q38) <span class="beginner">Beginner</span>
39. [What is Throttling?](#q39) <span class="beginner">Beginner</span>
40. [Stateless vs Stateful Services?](#q40) <span class="beginner">Beginner</span>
41. [Testing Strategies in Microservices?](#q41) <span class="intermediate">Intermediate</span>
42. [What is Containerization (Docker)?](#q42) <span class="beginner">Beginner</span>
43. [What is Orchestration (Kubernetes)?](#q43) <span class="beginner">Beginner</span>
44. [How to secure Microservices?](#q44) <span class="intermediate">Intermediate</span>
45. [OAuth2 Flows?](#q45) <span class="intermediate">Intermediate</span>
46. [What is OIDC (OpenID Connect)?](#q46) <span class="intermediate">Intermediate</span>
47. [What is JWT (JSON Web Token)?](#q47) <span class="beginner">Beginner</span>
48. [Synchronous vs Asynchronous (Deep Dive)?](#q48) <span class="intermediate">Intermediate</span>
49. [What is Two-Phase Commit (2PC)?](#q49) <span class="advanced">Advanced</span>
50. [Why avoid 2PC in Microservices?](#q50) <span class="advanced">Advanced</span>
51. [What is Dead Letter Queue (DLQ)?](#q51) <span class="intermediate">Intermediate</span>
52. [Competing Consumers Pattern?](#q52) <span class="intermediate">Intermediate</span>
53. [What is Fan-out?](#q53) <span class="intermediate">Intermediate</span>
54. [What is Polyglot Persistence?](#q54) <span class="intermediate">Intermediate</span>
55. [What is Domain Driven Design (DDD)?](#q55) <span class="advanced">Advanced</span>
56. [What is a Bounded Context?](#q56) <span class="advanced">Advanced</span>
57. [What is an Aggregate?](#q57) <span class="advanced">Advanced</span>
58. [What is Anti-Corruption Layer?](#q58) <span class="advanced">Advanced</span>
59. [What is Semantic Versioning?](#q59) <span class="beginner">Beginner</span>
60. [What is Continuous Integration (CI)?](#q60) <span class="beginner">Beginner</span>
61. [What is Continuous Deployment (CD)?](#q61) <span class="beginner">Beginner</span>
62. [What is Infrastructure as Code (IaC)?](#q62) <span class="intermediate">Intermediate</span>
63. [What is Immutable Infrastructure?](#q63) <span class="intermediate">Intermediate</span>
64. [What is Serverless?](#q64) <span class="intermediate">Intermediate</span>
65. [Microservices vs Serverless?](#q65) <span class="intermediate">Intermediate</span>
66. [What is Cold Start?](#q66) <span class="intermediate">Intermediate</span>
67. [How to handle Distributed Locking?](#q67) <span class="advanced">Advanced</span>
68. [What is Leader Election?](#q68) <span class="advanced">Advanced</span>
69. [What is Sharding?](#q69) <span class="advanced">Advanced</span>
70. [What is Replication?](#q70) <span class="intermediate">Intermediate</span>
71. [What is Auto-scaling?](#q71) <span class="beginner">Beginner</span>
72. [What is Log Aggregation?](#q72) <span class="intermediate">Intermediate</span>
73. [Monitoring vs Observability?](#q73) <span class="advanced">Advanced</span>
74. [What is Alerting?](#q74) <span class="beginner">Beginner</span>
75. [What is a Health Check?](#q75) <span class="beginner">Beginner</span>
76. [What is Graceful Shutdown?](#q76) <span class="intermediate">Intermediate</span>
77. [What is Retry Pattern?](#q77) <span class="beginner">Beginner</span>
78. [What is Exponential Backoff?](#q78) <span class="intermediate">Intermediate</span>
79. [What is Jitter?](#q79) <span class="advanced">Advanced</span>
80. [What is Load Shedding?](#q80) <span class="advanced">Advanced</span>
81. [What is a Reverse Proxy?](#q81) <span class="beginner">Beginner</span>
82. [What is a Forward Proxy?](#q82) <span class="beginner">Beginner</span>
83. [What is Sticky Sessions?](#q83) <span class="intermediate">Intermediate</span>
84. [Why avoid Sticky Sessions?](#q84) <span class="intermediate">Intermediate</span>
85. [What is Shadow Deployment?](#q85) <span class="advanced">Advanced</span>
86. [What is Feature Flag?](#q86) <span class="beginner">Beginner</span>
87. [What is GitOps?](#q87) <span class="intermediate">Intermediate</span>
88. [What is Helm?](#q88) <span class="intermediate">Intermediate</span>
89. [What is a Pod (K8s)?](#q89) <span class="beginner">Beginner</span>
90. [What is a Namespace?](#q90) <span class="beginner">Beginner</span>
91. [ConfigMaps vs Secrets?](#q91) <span class="intermediate">Intermediate</span>
92. [What is StatefulSet?](#q92) <span class="intermediate">Intermediate</span>
93. [What is DaemonSet?](#q93) <span class="intermediate">Intermediate</span>
94. [What is Ingress Controller?](#q94) <span class="intermediate">Intermediate</span>
95. [What is Persistent Volume (PV)?](#q95) <span class="intermediate">Intermediate</span>
96. [Service Types (ClusterIP, NodePort, LB)?](#q96) <span class="intermediate">Intermediate</span>
97. [Horizontal Pod Autoscaler (HPA)?](#q97) <span class="intermediate">Intermediate</span>
98. [Vertical Pod Autoscaler (VPA)?](#q98) <span class="intermediate">Intermediate</span>
99. [Cluster Autoscaler?](#q99) <span class="intermediate">Intermediate</span>
100. [Multi-Tenancy in Microservices?](#q100) <span class="advanced">Advanced</span>
101. [SOA vs Microservices?](#q101) <span class="intermediate">Intermediate</span>

---

<a id="q1"></a>

### Q1: What is Microservices Architecture?

**Difficulty**: Beginner

**Strategy**:
A style of structuring an application as a collection of small, autonomous services, modeled around a business domain.

**Code Example**:
```text
Monolith: [UI + Logic + DB]
Microservices: [Service A] <-> [Service B]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q2"></a>

### Q2: Benefits of Microservices?

**Difficulty**: Beginner

**Strategy**:
Independent scaling, technology diversity (polyglot), fault isolation, faster time-to-market (independent deployment).

**Code Example**:
```text
Team A -> Java -> Deploy
Team B -> Node.js -> Deploy
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q3"></a>

### Q3: Drawbacks of Microservices?

**Difficulty**: Beginner

**Strategy**:
Complexity (distributed system), network latency, data consistency (eventual), operational overhead (DevOps).

**Code Example**:
```text
Trace: Service A -> B -> C (Debugging is hard)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q4"></a>

### Q4: What is an API Gateway?

**Difficulty**: Intermediate

**Strategy**:
A server that acts as an entry point for clients. Handles routing, composition, auth, rate limiting, and caching.

**Code Example**:
```text
Client -> API Gateway -> [Service A, Service B]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q5"></a>

### Q5: What is Service Discovery?

**Difficulty**: Intermediate

**Strategy**:
Mechanism for services to find each other's dynamic IP addresses. Uses a Service Registry (e.g., Consul, Eureka).

**Code Example**:
```text
Service A -> Registry (Get B's IP) -> Service B
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q6"></a>

### Q6: Client-side vs Server-side Discovery?

**Difficulty**: Advanced

**Strategy**:
Client-side: Client queries registry (Netflix Ribbon). Server-side: Client calls LB, LB queries registry (AWS ELB, K8s Service).

**Code Example**:
```text
Client -> Registry -> Service (Client-side)
Client -> Load Balancer -> Service (Server-side)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q7"></a>

### Q7: What is Circuit Breaker Pattern?

**Difficulty**: Intermediate

**Strategy**:
Prevents cascading failures. If a service fails repeatedly, the circuit 'opens' and returns error instantly without calling the service.

**Code Example**:
```text
if (failures > threshold) open_circuit();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q8"></a>

### Q8: What is Bulkhead Pattern?

**Difficulty**: Advanced

**Strategy**:
Isolating resources (thread pools) so that failure in one part doesn't take down the whole system.

**Code Example**:
```text
ThreadPool A (Service A)
ThreadPool B (Service B)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q9"></a>

### Q9: What is Saga Pattern?

**Difficulty**: Advanced

**Strategy**:
Managing distributed transactions. Sequence of local transactions. If one fails, execute compensating transactions to undo.

**Code Example**:
```text
Order -> Payment -> Stock
If Stock fails -> Refund Payment -> Cancel Order
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q10"></a>

### Q10: Choreography vs Orchestration?

**Difficulty**: Advanced

**Strategy**:
Choreography: Decentralized, event-driven (Kafka). Orchestration: Centralized controller tells services what to do (Camunda).

**Code Example**:
```text
Choreography: A emits event, B listens.
Orchestration: Manager calls A, then B.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q11"></a>

### Q11: What is Event Sourcing?

**Difficulty**: Advanced

**Strategy**:
Storing state as a sequence of events rather than current state. Allows time-travel debugging and audit logs.

**Code Example**:
```text
Events: [Created, Deposited $10, Withdrawn $5]
State: $5
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q12"></a>

### Q12: What is CQRS?

**Difficulty**: Advanced

**Strategy**:
Command Query Responsibility Segregation. Separate models for Write (Command) and Read (Query). Optimizes performance.

**Code Example**:
```text
Write DB (Normalized) -> Sync -> Read DB (Denormalized)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q13"></a>

### Q13: How do you handle Authentication?

**Difficulty**: Intermediate

**Strategy**:
Centralized Identity Provider (IdP). Use OAuth2/OIDC. Pass JWT tokens between services.

**Code Example**:
```text
Header: Authorization: Bearer <JWT>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q14"></a>

### Q14: What is Distributed Tracing?

**Difficulty**: Intermediate

**Strategy**:
Tracking requests across microservices. Assign a Trace ID at ingress and propagate it. Tools: Jaeger, Zipkin.

**Code Example**:
```text
X-Trace-ID: abc-123
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q15"></a>

### Q15: What is Centralized Logging?

**Difficulty**: Intermediate

**Strategy**:
Aggregating logs from all services into one place for searching. ELK Stack (Elasticsearch, Logstash, Kibana).

**Code Example**:
```text
Service -> Fluentd -> Elasticsearch -> Kibana
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q16"></a>

### Q16: Idempotency in Microservices?

**Difficulty**: Intermediate

**Strategy**:
Ensuring replaying a request doesn't change state twice. Use Idempotency Keys.

**Code Example**:
```text
if (processed(key)) return saved_response;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q17"></a>

### Q17: Inter-service Communication Styles?

**Difficulty**: Beginner

**Strategy**:
Synchronous (HTTP/REST, gRPC) vs Asynchronous (Message Queues, Pub/Sub).

**Code Example**:
```text
Sync: A waits for B.
Async: A sends message, B processes later.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q18"></a>

### Q18: What is gRPC?

**Difficulty**: Intermediate

**Strategy**:
High-performance RPC framework. Uses Protobuf (binary) and HTTP/2. Strongly typed.

**Code Example**:
```text
service Greeter { rpc SayHello (HelloRequest) returns (HelloReply) {} }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q19"></a>

### Q19: REST vs gRPC?

**Difficulty**: Intermediate

**Strategy**:
REST: Text (JSON), HTTP/1.1, human readable. gRPC: Binary (Protobuf), HTTP/2, faster, strict contracts.

**Code Example**:
```text
REST: GET /users/1
gRPC: GetUser(id=1)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q20"></a>

### Q20: What is a Message Broker?

**Difficulty**: Beginner

**Strategy**:
Intermediary that translates messages between sender and receiver. Decouples services. Examples: RabbitMQ, Kafka.

**Code Example**:
```text
Producer -> Broker -> Consumer
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q21"></a>

### Q21: Kafka vs RabbitMQ?

**Difficulty**: Advanced

**Strategy**:
Kafka: Log-based, high throughput, replayable, persistent. RabbitMQ: Queue-based, complex routing, ack/nack, transient.

**Code Example**:
```text
Kafka: Stream processing.
RabbitMQ: Task queue.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q22"></a>

### Q22: What is API Composition?

**Difficulty**: Intermediate

**Strategy**:
API Gateway or specific service queries multiple services and combines results.

**Code Example**:
```text
Composite = UserDetails + Orders + Reviews
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q23"></a>

### Q23: What is Database per Service?

**Difficulty**: Intermediate

**Strategy**:
Each service has its own private database. Ensures loose coupling. Data accessible only via API.

**Code Example**:
```text
Service A -> DB A
Service B -> DB B
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q24"></a>

### Q24: What is Shared Database Antipattern?

**Difficulty**: Intermediate

**Strategy**:
Multiple services accessing the same DB. Leads to tight coupling and performance bottlenecks.

**Code Example**:
```text
Service A -> DB <- Service B (Avoid)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q25"></a>

### Q25: How do you handle Data Consistency?

**Difficulty**: Advanced

**Strategy**:
Embrace Eventual Consistency. Use Sagas for distributed transactions. 2PC is rarely used.

**Code Example**:
```text
Update A -> Publish Event -> Update B
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q26"></a>

### Q26: What is CAP Theorem?

**Difficulty**: Intermediate

**Strategy**:
Choose 2: Consistency, Availability, Partition Tolerance. Microservices usually choose AP (Availability + Partition Tolerance).

**Code Example**:
```text
CP: MongoDB (default)
AP: Cassandra
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q27"></a>

### Q27: What is 12-Factor App?

**Difficulty**: Intermediate

**Strategy**:
Methodology for building SaaS apps. Config in env, backing services as resources, stateless processes, dev/prod parity.

**Code Example**:
```text
Config: ENV_VAR
Logs: Stream to stdout
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q28"></a>

### Q28: How do you version APIs?

**Difficulty**: Beginner

**Strategy**:
URI Versioning (/v1/users), Header Versioning (Accept: application/vnd.v1+json).

**Code Example**:
```text
GET /v1/resource
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q29"></a>

### Q29: What is Consumer Driven Contracts (CDC)?

**Difficulty**: Advanced

**Strategy**:
Testing strategy where consumers define expectations (contracts). Providers verify they meet them. Tool: Pact.

**Code Example**:
```text
Consumer defines: 'I expect {id: 1}'
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q30"></a>

### Q30: What is Chaos Engineering?

**Difficulty**: Advanced

**Strategy**:
Testing resilience by intentionally injecting faults (killing pods, latency) in prod/staging.

**Code Example**:
```text
Chaos Monkey: Randomly terminates instances.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q31"></a>

### Q31: Blue-Green Deployment?

**Difficulty**: Intermediate

**Strategy**:
Two identical envs. Blue is live. Deploy to Green. Switch router to Green. Instant rollback.

**Code Example**:
```text
Router -> Blue (v1)
Switch -> Green (v2)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q32"></a>

### Q32: Canary Release?

**Difficulty**: Intermediate

**Strategy**:
Rollout to small % of users first. Monitor. Gradually increase traffic.

**Code Example**:
```text
v1: 90%, v2: 10%
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q33"></a>

### Q33: Strangler Fig Pattern?

**Difficulty**: Advanced

**Strategy**:
Migrating monolith to microservices by gradually replacing specific functionality with new services.

**Code Example**:
```text
Facade -> [New Service, Monolith]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q34"></a>

### Q34: What is BFF (Backend for Frontend)?

**Difficulty**: Intermediate

**Strategy**:
Creating separate backend services for different frontend clients (Mobile, Web) to optimize data.

**Code Example**:
```text
Mobile BFF -> Minimal Data
Web BFF -> Rich Data
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q35"></a>

### Q35: What is Sidecar Pattern?

**Difficulty**: Intermediate

**Strategy**:
Deploying helper container alongside main container to handle cross-cutting concerns (logging, proxy, mTLS).

**Code Example**:
```text
Pod: [App Container] + [Envoy Proxy]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q36"></a>

### Q36: What is Service Mesh?

**Difficulty**: Advanced

**Strategy**:
Infrastructure layer for handling service-to-service communication. Uses sidecars. Features: Traffic mgmt, security, observability.

**Code Example**:
```text
Istio, Linkerd
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q37"></a>

### Q37: How to prevent Cascading Failures?

**Difficulty**: Intermediate

**Strategy**:
Circuit Breakers, Timeouts, Retries with Backoff, Bulkheads.

**Code Example**:
```text
Timeout: 200ms
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q38"></a>

### Q38: What is Rate Limiting?

**Difficulty**: Beginner

**Strategy**:
Controlling the rate of traffic sent or received. Prevents DoS.

**Code Example**:
```text
100 req/min
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q39"></a>

### Q39: What is Throttling?

**Difficulty**: Beginner

**Strategy**:
Intentionally slowing down a service when it's overloaded, or rejecting requests.

**Code Example**:
```text
Queue full -> Reject
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q40"></a>

### Q40: Stateless vs Stateful Services?

**Difficulty**: Beginner

**Strategy**:
Stateless: No session data stored locally. Easy to scale. Stateful: Stores session/data locally. Harder to scale.

**Code Example**:
```text
Stateless: REST API
Stateful: Database
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q41"></a>

### Q41: Testing Strategies in Microservices?

**Difficulty**: Intermediate

**Strategy**:
Unit (Logic), Integration (DB/Queue), Component (Service isolation), Contract (API), E2E (User flow).

**Code Example**:
```text
Pyramid: Unit > Integration > E2E
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q42"></a>

### Q42: What is Containerization (Docker)?

**Difficulty**: Beginner

**Strategy**:
Packaging code and dependencies into a standard unit (Container) that runs anywhere.

**Code Example**:
```text
Dockerfile -> Image -> Container
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q43"></a>

### Q43: What is Orchestration (Kubernetes)?

**Difficulty**: Beginner

**Strategy**:
Automating deployment, scaling, and management of containerized applications.

**Code Example**:
```text
K8s Scheduler -> Nodes
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q44"></a>

### Q44: How to secure Microservices?

**Difficulty**: Intermediate

**Strategy**:
HTTPS/TLS, mTLS (Service-to-Service), OAuth2 (User Auth), API Gateway as firewall.

**Code Example**:
```text
mTLS: Mutual Certificate Auth
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q45"></a>

### Q45: OAuth2 Flows?

**Difficulty**: Intermediate

**Strategy**:
Authorization Code (Web), Client Credentials (M2M), Implicit (Legacy).

**Code Example**:
```text
App -> Auth Server -> Token -> Resource Server
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q46"></a>

### Q46: What is OIDC (OpenID Connect)?

**Difficulty**: Intermediate

**Strategy**:
Identity layer on top of OAuth2. Provides authentication (Who are you?) via ID Token.

**Code Example**:
```text
Scope: openid profile email
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q47"></a>

### Q47: What is JWT (JSON Web Token)?

**Difficulty**: Beginner

**Strategy**:
Compact, URL-safe token for representing claims. Stateless auth.

**Code Example**:
```text
Header.Payload.Signature
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q48"></a>

### Q48: Synchronous vs Asynchronous (Deep Dive)?

**Difficulty**: Intermediate

**Strategy**:
Sync: Tight coupling, blocking. Async: Loose coupling, non-blocking, better resilience.

**Code Example**:
```text
Sync: Request/Response
Async: Event Driven
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q49"></a>

### Q49: What is Two-Phase Commit (2PC)?

**Difficulty**: Advanced

**Strategy**:
Distributed transaction protocol. Prepare phase (vote) + Commit phase. Blocking. Not recommended for microservices.

**Code Example**:
```text
Coordinator -> Prepare -> Commit
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q50"></a>

### Q50: Why avoid 2PC in Microservices?

**Difficulty**: Advanced

**Strategy**:
It blocks resources (locks), reduces availability (if coordinator dies), and increases latency.

**Code Example**:
```text
Use Sagas instead.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q51"></a>

### Q51: What is Dead Letter Queue (DLQ)?

**Difficulty**: Intermediate

**Strategy**:
A queue where messages that cannot be processed (failed consumers) are sent for inspection/replay.

**Code Example**:
```text
Queue -> Consumer (Fail) -> DLQ
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q52"></a>

### Q52: Competing Consumers Pattern?

**Difficulty**: Intermediate

**Strategy**:
Multiple consumers reading from the same queue to process messages concurrently. Load balancing.

**Code Example**:
```text
Queue -> [Consumer A, Consumer B]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q53"></a>

### Q53: What is Fan-out?

**Difficulty**: Intermediate

**Strategy**:
Sending a message to an exchange that broadcasts it to all bound queues (Pub/Sub).

**Code Example**:
```text
Exchange -> [Queue A, Queue B]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q54"></a>

### Q54: What is Polyglot Persistence?

**Difficulty**: Intermediate

**Strategy**:
Using different data storage technologies for different services based on needs (SQL, NoSQL, Graph).

**Code Example**:
```text
UserService (MySQL), CatalogService (Mongo)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q55"></a>

### Q55: What is Domain Driven Design (DDD)?

**Difficulty**: Advanced

**Strategy**:
Software design approach focusing on modelling software to match a domain. Core concepts: Bounded Context, Entities, Aggregates.

**Code Example**:
```text
Domain: E-Commerce -> Contexts: Order, Shipping
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q56"></a>

### Q56: What is a Bounded Context?

**Difficulty**: Advanced

**Strategy**:
A linguistic boundary within which a domain model applies. Ideally maps to a Microservice.

**Code Example**:
```text
Context: Sales (Customer = Buyer)
Context: Support (Customer = Ticket Owner)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q57"></a>

### Q57: What is an Aggregate?

**Difficulty**: Advanced

**Strategy**:
A cluster of domain objects that can be treated as a single unit. Has a Root Entity. Transactions should not cross aggregates.

**Code Example**:
```text
Order (Root) + OrderItems
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q58"></a>

### Q58: What is Anti-Corruption Layer?

**Difficulty**: Advanced

**Strategy**:
A layer that translates between two different domain models (e.g., Legacy Monolith <-> New Microservice) to prevent pollution.

**Code Example**:
```text
New System <-> ACL <-> Legacy System
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q59"></a>

### Q59: What is Semantic Versioning?

**Difficulty**: Beginner

**Strategy**:
Versioning scheme: Major.Minor.Patch (e.g., 1.0.2). Major = Breaking, Minor = Feature, Patch = Fix.

**Code Example**:
```text
v1.0.0 -> v2.0.0 (Breaking Change)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q60"></a>

### Q60: What is Continuous Integration (CI)?

**Difficulty**: Beginner

**Strategy**:
Practice of merging code changes frequently, followed by automated build and test.

**Code Example**:
```text
Git Push -> Jenkins Build -> Test
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q61"></a>

### Q61: What is Continuous Deployment (CD)?

**Difficulty**: Beginner

**Strategy**:
Automated release of code to production after passing CI.

**Code Example**:
```text
CI Pass -> Deploy to Prod
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q62"></a>

### Q62: What is Infrastructure as Code (IaC)?

**Difficulty**: Intermediate

**Strategy**:
Managing infrastructure through code/files rather than manual configuration. Tools: Terraform, Ansible.

**Code Example**:
```text
resource 'aws_instance' 'web' {...}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q63"></a>

### Q63: What is Immutable Infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Servers are never modified after deployment. If update needed, replace with new server.

**Code Example**:
```text
Deploy v2 -> Terminate v1
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q64"></a>

### Q64: What is Serverless?

**Difficulty**: Intermediate

**Strategy**:
Cloud execution model where provider manages servers. Pay per execution. Function as a Service (FaaS).

**Code Example**:
```text
AWS Lambda, Azure Functions
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q65"></a>

### Q65: Microservices vs Serverless?

**Difficulty**: Intermediate

**Strategy**:
Microservices: Long-running processes, control over env. Serverless: Event-driven, ephemeral, no ops.

**Code Example**:
```text
K8s Pod vs Lambda Function
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q66"></a>

### Q66: What is Cold Start?

**Difficulty**: Intermediate

**Strategy**:
Latency experienced when a Serverless function is invoked for the first time (container spin-up).

**Code Example**:
```text
First req: 1s. Subsequent: 50ms.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q67"></a>

### Q67: How to handle Distributed Locking?

**Difficulty**: Advanced

**Strategy**:
Using a shared store (Redis/Zookeeper) to ensure only one process performs an action.

**Code Example**:
```text
Redis: SET resource_name my_random_value NX PX 30000
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q68"></a>

### Q68: What is Leader Election?

**Difficulty**: Advanced

**Strategy**:
Process of designating a single process as the organizer/coordinator. Tools: Zookeeper, Etcd.

**Code Example**:
```text
Nodes vote -> Leader selected
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q69"></a>

### Q69: What is Sharding?

**Difficulty**: Advanced

**Strategy**:
Partitioning data horizontally across databases to scale. Based on Shard Key.

**Code Example**:
```text
User ID % 4 -> Shard 1
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q70"></a>

### Q70: What is Replication?

**Difficulty**: Intermediate

**Strategy**:
Copying data to multiple nodes for redundancy and read scaling.

**Code Example**:
```text
Master (Write) -> Slaves (Read)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q71"></a>

### Q71: What is Auto-scaling?

**Difficulty**: Beginner

**Strategy**:
Automatically adjusting the number of compute resources based on load (CPU/RAM).

**Code Example**:
```text
HPA: Target CPU 50%
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q72"></a>

### Q72: What is Log Aggregation?

**Difficulty**: Intermediate

**Strategy**:
Collecting logs from all services into a central system (ELK, Splunk, Datadog).

**Code Example**:
```text
Log -> Agent -> Central Store
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q73"></a>

### Q73: Monitoring vs Observability?

**Difficulty**: Advanced

**Strategy**:
Monitoring: 'Is the system healthy?' (Known unknowns). Observability: 'Why is it behaving this way?' (Unknown unknowns).

**Code Example**:
```text
Metrics vs Traces/Logs
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q74"></a>

### Q74: What is Alerting?

**Difficulty**: Beginner

**Strategy**:
Notifying humans when metrics cross thresholds.

**Code Example**:
```text
If ErrorRate > 1% -> PageDuty
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q75"></a>

### Q75: What is a Health Check?

**Difficulty**: Beginner

**Strategy**:
Endpoint (/health) that reveals service status. Liveness (Restart if dead) vs Readiness (Don't send traffic until ready).

**Code Example**:
```text
GET /health -> 200 OK
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q76"></a>

### Q76: What is Graceful Shutdown?

**Difficulty**: Intermediate

**Strategy**:
Service stops accepting new requests, finishes current ones, closes connections, then exits.

**Code Example**:
```text
SIGTERM -> Stop Listener -> Drain -> Exit
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q77"></a>

### Q77: What is Retry Pattern?

**Difficulty**: Beginner

**Strategy**:
Automatically retrying a failed operation (transient error).

**Code Example**:
```text
try { call() } catch { retry() }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q78"></a>

### Q78: What is Exponential Backoff?

**Difficulty**: Intermediate

**Strategy**:
Increasing the wait time between retries exponentially (1s, 2s, 4s, 8s) to reduce load.

**Code Example**:
```text
wait = base * 2^attempt
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q79"></a>

### Q79: What is Jitter?

**Difficulty**: Advanced

**Strategy**:
Adding random variation to backoff intervals to prevent Thundering Herd.

**Code Example**:
```text
wait = base * 2^attempt + random()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q80"></a>

### Q80: What is Load Shedding?

**Difficulty**: Advanced

**Strategy**:
Intentionally dropping requests when system is near capacity to prevent total collapse.

**Code Example**:
```text
If CPU > 90% -> Return 503
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q81"></a>

### Q81: What is a Reverse Proxy?

**Difficulty**: Beginner

**Strategy**:
Server sitting in front of backend servers. Client -> Proxy -> Server. Hides backend.

**Code Example**:
```text
Nginx, HAProxy
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q82"></a>

### Q82: What is a Forward Proxy?

**Difficulty**: Beginner

**Strategy**:
Server sitting in front of clients. Client -> Proxy -> Internet. Hides client.

**Code Example**:
```text
VPN, Corporate Proxy
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q83"></a>

### Q83: What is Sticky Sessions?

**Difficulty**: Intermediate

**Strategy**:
Routing all requests from a user to the same specific server instance.

**Code Example**:
```text
Load Balancer (Hash IP) -> Server A
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q84"></a>

### Q84: Why avoid Sticky Sessions?

**Difficulty**: Intermediate

**Strategy**:
Causes uneven load balancing. Makes auto-scaling and failover harder.

**Code Example**:
```text
Use Distributed Cache (Redis) instead.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q85"></a>

### Q85: What is Shadow Deployment?

**Difficulty**: Advanced

**Strategy**:
Replaying live production traffic to a new version (shadow) without returning responses to user. Tests performance/errors.

**Code Example**:
```text
Traffic -> v1 (Live) & v2 (Shadow)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q86"></a>

### Q86: What is Feature Flag?

**Difficulty**: Beginner

**Strategy**:
Toggle functionality on/off at runtime without deploying code.

**Code Example**:
```text
if (feature.isEnabled('dark_mode'))
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q87"></a>

### Q87: What is GitOps?

**Difficulty**: Intermediate

**Strategy**:
Using Git as the single source of truth for infrastructure/deployment. ArgoCD syncs Git state to K8s.

**Code Example**:
```text
Git Commit -> ArgoCD -> K8s Apply
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q88"></a>

### Q88: What is Helm?

**Difficulty**: Intermediate

**Strategy**:
Package manager for Kubernetes. Manages charts (templates).

**Code Example**:
```text
helm install my-app ./chart
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q89"></a>

### Q89: What is a Pod (K8s)?

**Difficulty**: Beginner

**Strategy**:
Smallest deployable unit in K8s. Can contain one or more containers sharing network/storage.

**Code Example**:
```text
Pod = [Container A, Container B]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q90"></a>

### Q90: What is a Namespace?

**Difficulty**: Beginner

**Strategy**:
Virtual cluster inside K8s. Isolates resources between teams/envs.

**Code Example**:
```text
kubectl get pods -n production
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q91"></a>

### Q91: ConfigMaps vs Secrets?

**Difficulty**: Intermediate

**Strategy**:
ConfigMap: Non-sensitive config (URLs). Secret: Sensitive data (passwords, keys), base64 encoded.

**Code Example**:
```text
Env: DB_HOST (ConfigMap), DB_PASS (Secret)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q92"></a>

### Q92: What is StatefulSet?

**Difficulty**: Intermediate

**Strategy**:
K8s controller for stateful apps (DBs). Guarantees ordering and stable network IDs.

**Code Example**:
```text
web-0, web-1, web-2
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q93"></a>

### Q93: What is DaemonSet?

**Difficulty**: Intermediate

**Strategy**:
Ensures a copy of a Pod runs on all (or specific) nodes. Used for logs/monitoring agents.

**Code Example**:
```text
Fluentd on every node
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q94"></a>

### Q94: What is Ingress Controller?

**Difficulty**: Intermediate

**Strategy**:
Manages external access to services (HTTP/HTTPS). Acts as L7 Load Balancer.

**Code Example**:
```text
Internet -> Ingress -> Service
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q95"></a>

### Q95: What is Persistent Volume (PV)?

**Difficulty**: Intermediate

**Strategy**:
Storage resource in the cluster. PVC (Claim) requests storage from PV.

**Code Example**:
```text
Pod -> PVC -> PV -> EBS/Disk
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q96"></a>

### Q96: Service Types (ClusterIP, NodePort, LB)?

**Difficulty**: Intermediate

**Strategy**:
ClusterIP: Internal only. NodePort: Exposes on static port on nodes. LoadBalancer: External Cloud LB.

**Code Example**:
```text
ClusterIP (Default)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q97"></a>

### Q97: Horizontal Pod Autoscaler (HPA)?

**Difficulty**: Intermediate

**Strategy**:
Scales number of pods based on metrics (CPU).

**Code Example**:
```text
Scale 1 -> 10 pods
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q98"></a>

### Q98: Vertical Pod Autoscaler (VPA)?

**Difficulty**: Intermediate

**Strategy**:
Adjusts CPU/Memory requests/limits of containers.

**Code Example**:
```text
Increase RAM 1GB -> 2GB
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q99"></a>

### Q99: Cluster Autoscaler?

**Difficulty**: Intermediate

**Strategy**:
Adds/removes nodes from the cluster when pods cannot be scheduled.

**Code Example**:
```text
Add Node if Pending Pods
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q100"></a>

### Q100: Multi-Tenancy in Microservices?

**Difficulty**: Advanced

**Strategy**:
Serving multiple customers (tenants) from single instance (Shared DB) or isolated instances (Database per Tenant).

**Code Example**:
```text
TenantID in every query
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q101"></a>

### Q101: SOA vs Microservices?

**Difficulty**: Intermediate

**Strategy**:
SOA: Enterprise Service Bus (ESB), smart pipes, larger services. Microservices: Smart endpoints, dumb pipes, smaller scope.

**Code Example**:
```text
SOA: XML/SOAP. Microservices: JSON/REST.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

