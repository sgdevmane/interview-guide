<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/devops-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Microservices Interview Questions</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [What is Microservices Architecture?](#q1-what-is-microservices-architecture) <span class="beginner">Beginner</span>
2. [Benefits of Microservices?](#q2-benefits-of-microservices) <span class="beginner">Beginner</span>
3. [Drawbacks of Microservices?](#q3-drawbacks-of-microservices) <span class="beginner">Beginner</span>
4. [What is API Gateway?](#q4-what-is-api-gateway) <span class="intermediate">Intermediate</span>
5. [What is Service Discovery?](#q5-what-is-service-discovery) <span class="intermediate">Intermediate</span>
6. [Client-side vs Server-side Discovery?](#q6-client-side-vs-server-side-discovery) <span class="advanced">Advanced</span>
7. [What is Circuit Breaker Pattern?](#q7-what-is-circuit-breaker-pattern) <span class="intermediate">Intermediate</span>
8. [What is Bulkhead Pattern?](#q8-what-is-bulkhead-pattern) <span class="advanced">Advanced</span>
9. [What is Saga Pattern?](#q9-what-is-saga-pattern) <span class="advanced">Advanced</span>
10. [Choreography vs Orchestration?](#q10-choreography-vs-orchestration) <span class="advanced">Advanced</span>
11. [What is Event Sourcing?](#q11-what-is-event-sourcing) <span class="advanced">Advanced</span>
12. [What is CQRS?](#q12-what-is-cqrs) <span class="advanced">Advanced</span>
13. [How do you handle Authentication?](#q13-how-do-you-handle-authentication) <span class="intermediate">Intermediate</span>
14. [What is Distributed Tracing?](#q14-what-is-distributed-tracing) <span class="intermediate">Intermediate</span>
15. [What is Centralized Logging?](#q15-what-is-centralized-logging) <span class="intermediate">Intermediate</span>
16. [Idempotency in Microservices?](#q16-idempotency-in-microservices) <span class="intermediate">Intermediate</span>
17. [How do you handle inter-service communication?](#q17-how-do-you-handle-inter-service-communication) <span class="beginner">Beginner</span>
18. [What is gRPC?](#q18-what-is-grpc) <span class="intermediate">Intermediate</span>
19. [REST vs gRPC?](#q19-rest-vs-grpc) <span class="intermediate">Intermediate</span>
20. [What is a Message Broker?](#q20-what-is-a-message-broker) <span class="beginner">Beginner</span>
21. [Kafka vs RabbitMQ?](#q21-kafka-vs-rabbitmq) <span class="advanced">Advanced</span>
22. [What is API Composition?](#q22-what-is-api-composition) <span class="intermediate">Intermediate</span>
23. [What is Database per Service?](#q23-what-is-database-per-service) <span class="intermediate">Intermediate</span>
24. [What is Shared Database antipattern?](#q24-what-is-shared-database-antipattern) <span class="intermediate">Intermediate</span>
25. [How do you handle data consistency?](#q25-how-do-you-handle-data-consistency) <span class="advanced">Advanced</span>
26. [What is CAP Theorem?](#q26-what-is-cap-theorem) <span class="intermediate">Intermediate</span>
27. [What is 12-Factor App?](#q27-what-is-12-factor-app) <span class="intermediate">Intermediate</span>
28. [How do you version APIs?](#q28-how-do-you-version-apis) <span class="beginner">Beginner</span>
29. [What is Consumer Driven Contracts?](#q29-what-is-consumer-driven-contracts) <span class="advanced">Advanced</span>
30. [What is Chaos Engineering?](#q30-what-is-chaos-engineering) <span class="advanced">Advanced</span>
31. [What is Blue/Green Deployment?](#q31-what-is-blue-green-deployment) <span class="intermediate">Intermediate</span>
32. [What is Canary Release?](#q32-what-is-canary-release) <span class="intermediate">Intermediate</span>
33. [What is Strangler Fig Pattern?](#q33-what-is-strangler-fig-pattern) <span class="advanced">Advanced</span>
34. [What is BFF (Backend for Frontend)?](#q34-what-is-bff-backend-for-frontend) <span class="intermediate">Intermediate</span>
35. [What is Sidecar Pattern?](#q35-what-is-sidecar-pattern) <span class="intermediate">Intermediate</span>
36. [What is Service Mesh?](#q36-what-is-service-mesh) <span class="advanced">Advanced</span>
37. [How to prevent cascading failures?](#q37-how-to-prevent-cascading-failures) <span class="intermediate">Intermediate</span>
38. [What is Rate Limiting?](#q38-what-is-rate-limiting) <span class="beginner">Beginner</span>
39. [What is Throttling?](#q39-what-is-throttling) <span class="beginner">Beginner</span>
40. [Stateless vs Stateful services?](#q40-stateless-vs-stateful-services) <span class="beginner">Beginner</span>
41. [How do you test Microservices?](#q41-how-do-you-test-microservices) <span class="intermediate">Intermediate</span>
42. [What is Containerization?](#q42-what-is-containerization) <span class="beginner">Beginner</span>
43. [What is Orchestration?](#q43-what-is-orchestration) <span class="beginner">Beginner</span>
44. [How to secure microservices?](#q44-how-to-secure-microservices) <span class="intermediate">Intermediate</span>
45. [What is OAuth2?](#q45-what-is-oauth2) <span class="intermediate">Intermediate</span>
46. [What is OpenID Connect (OIDC)?](#q46-what-is-openid-connect-oidc) <span class="intermediate">Intermediate</span>
47. [What is JWT?](#q47-what-is-jwt) <span class="beginner">Beginner</span>
48. [Synchronous vs Asynchronous?](#q48-synchronous-vs-asynchronous) <span class="beginner">Beginner</span>
49. [What is Two-Phase Commit (2PC)?](#q49-what-is-two-phase-commit-2pc) <span class="advanced">Advanced</span>
50. [Why avoid 2PC in Microservices?](#q50-why-avoid-2pc-in-microservices) <span class="advanced">Advanced</span>
51. [What is Dead Letter Queue (DLQ)?](#q51-what-is-dead-letter-queue-dlq) <span class="intermediate">Intermediate</span>
52. [What is a Competing Consumers pattern?](#q52-what-is-a-competing-consumers-pattern) <span class="intermediate">Intermediate</span>
53. [What is Fan-out?](#q53-what-is-fan-out) <span class="intermediate">Intermediate</span>
54. [What is Polyglot Persistence?](#q54-what-is-polyglot-persistence) <span class="intermediate">Intermediate</span>
55. [What is Domain Driven Design (DDD)?](#q55-what-is-domain-driven-design-ddd) <span class="advanced">Advanced</span>
56. [What is a Bounded Context?](#q56-what-is-a-bounded-context) <span class="advanced">Advanced</span>
57. [What is an Aggregate?](#q57-what-is-an-aggregate) <span class="advanced">Advanced</span>
58. [What is Anti-Corruption Layer?](#q58-what-is-anti-corruption-layer) <span class="advanced">Advanced</span>
59. [What is Semantic Versioning?](#q59-what-is-semantic-versioning) <span class="beginner">Beginner</span>
60. [What is Continuous Integration (CI)?](#q60-what-is-continuous-integration-ci) <span class="beginner">Beginner</span>
61. [What is Continuous Deployment (CD)?](#q61-what-is-continuous-deployment-cd) <span class="beginner">Beginner</span>
62. [What is Infrastructure as Code (IaC)?](#q62-what-is-infrastructure-as-code-iac) <span class="intermediate">Intermediate</span>
63. [What is Immutable Infrastructure?](#q63-what-is-immutable-infrastructure) <span class="intermediate">Intermediate</span>
64. [What is Serverless?](#q64-what-is-serverless) <span class="intermediate">Intermediate</span>
65. [Microservices vs Serverless?](#q65-microservices-vs-serverless) <span class="intermediate">Intermediate</span>
66. [What is Cold Start?](#q66-what-is-cold-start) <span class="intermediate">Intermediate</span>
67. [How to handle distributed locking?](#q67-how-to-handle-distributed-locking) <span class="advanced">Advanced</span>
68. [What is Leader Election?](#q68-what-is-leader-election) <span class="advanced">Advanced</span>
69. [What is Sharding?](#q69-what-is-sharding) <span class="advanced">Advanced</span>
70. [What is Replication?](#q70-what-is-replication) <span class="intermediate">Intermediate</span>
71. [What is Auto-scaling?](#q71-what-is-auto-scaling) <span class="beginner">Beginner</span>
72. [What is Log Aggregation?](#q72-what-is-log-aggregation) <span class="intermediate">Intermediate</span>
73. [What is Monitoring vs Observability?](#q73-what-is-monitoring-vs-observability) <span class="advanced">Advanced</span>
74. [What is Alerting?](#q74-what-is-alerting) <span class="beginner">Beginner</span>
75. [What is a Health Check?](#q75-what-is-a-health-check) <span class="beginner">Beginner</span>
76. [What is Graceful Shutdown?](#q76-what-is-graceful-shutdown) <span class="intermediate">Intermediate</span>
77. [What is Retry Pattern?](#q77-what-is-retry-pattern) <span class="beginner">Beginner</span>
78. [What is Exponential Backoff?](#q78-what-is-exponential-backoff) <span class="intermediate">Intermediate</span>
79. [What is Jitter?](#q79-what-is-jitter) <span class="advanced">Advanced</span>
80. [What is load shedding?](#q80-what-is-load-shedding) <span class="advanced">Advanced</span>
81. [What is a Reverse Proxy?](#q81-what-is-a-reverse-proxy) <span class="beginner">Beginner</span>
82. [What is a Forward Proxy?](#q82-what-is-a-forward-proxy) <span class="beginner">Beginner</span>
83. [What is Sticky Sessions?](#q83-what-is-sticky-sessions) <span class="intermediate">Intermediate</span>
84. [Why avoid Sticky Sessions?](#q84-why-avoid-sticky-sessions) <span class="intermediate">Intermediate</span>
85. [What is Shadow Deployment?](#q85-what-is-shadow-deployment) <span class="advanced">Advanced</span>
86. [What is Feature Flag?](#q86-what-is-feature-flag) <span class="beginner">Beginner</span>

---

### Q1: What is Microservices Architecture?

**Difficulty**: Beginner

**Strategy**:
Microservices architecture is a design approach where a single application is composed of many loosely coupled and independently deployable smaller services. Each service runs in its own process and communicates with lightweight mechanisms, often an HTTP resource API.

**Code Example**:
```yaml
# Monolith vs Microservices
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q2: Benefits of Microservices?

**Difficulty**: Beginner

**Strategy**:
Scalability, independent deployment, tech diversity.

**Code Example**:
```yaml
# Agile teams
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q3: Drawbacks of Microservices?

**Difficulty**: Beginner

**Strategy**:
Complexity, network latency, distributed data consistency.

**Code Example**:
```yaml
# Ops overhead
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q4: What is API Gateway?

**Difficulty**: Intermediate

**Strategy**:
An API Gateway acts as a reverse proxy to accept all application programming interface (API) calls, aggregate the various services required to fulfill them, and return the appropriate result. It handles cross-cutting concerns like authentication, SSL termination, and rate limiting.

**Code Example**:
```yaml
path: /api/users -> User Service
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q5: What is Service Discovery?

**Difficulty**: Intermediate

**Strategy**:
Service discovery is the process of automatically detecting devices and services on a network. In microservices, it allows services to find and communicate with each other without hardcoding hostnames and ports. Tools like Consul, Eureka, or Kubernetes DNS are used.

**Code Example**:
```yaml
# Consul, Eureka, K8s DNS
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q6: Client-side vs Server-side Discovery?

**Difficulty**: Advanced

**Strategy**:
Client queries registry vs LB queries registry. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Netflix Ribbon vs AWS ELB
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q7: What is Circuit Breaker Pattern?

**Difficulty**: Intermediate

**Strategy**:
The Circuit Breaker pattern prevents an application from repeatedly trying to execute an operation that's likely to fail. It allows your application to fail fast and gracefully without waiting for TCP connection timeouts, preventing cascading failures across the system.

**Code Example**:
```yaml
if (failures > 5) openCircuit()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q8: What is Bulkhead Pattern?

**Difficulty**: Advanced

**Strategy**:
Isolate resources so one failure doesn't crash whole system.

**Code Example**:
```yaml
# Separate thread pools
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q9: What is Saga Pattern?

**Difficulty**: Advanced

**Strategy**:
A Saga is a sequence of local transactions. Each local transaction updates the database and publishes a message or event to trigger the next local transaction in the saga. If a local transaction fails because it violates a business rule then the saga executes a series of compensating transactions that undo the changes that were made by the preceding local transactions.

**Code Example**:
```yaml
# Choreography vs Orchestration
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q10: Choreography vs Orchestration?

**Difficulty**: Advanced

**Strategy**:
Choreography: Events (Event Bus). Orchestration: Central controller.

**Code Example**:
```yaml
# Kafka events vs Camunda
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q11: What is Event Sourcing?

**Difficulty**: Advanced

**Strategy**:
Event Sourcing ensures that all changes to application state are stored as a sequence of events. We can query these events, we can use them to reconstruct past states, and as a foundation to automatically adjust the state to cope with retroactive changes.

**Code Example**:
```yaml
events: [Created, Updated, Deleted]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q12: What is CQRS?

**Difficulty**: Advanced

**Strategy**:
CQRS stands for Command Query Responsibility Segregation. It's a pattern that separates read and update operations for a data store. Implementing CQRS in your application can maximize its performance, scalability, and security.

**Code Example**:
```yaml
Write DB -> Sync -> Read DB
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q13: How do you handle Authentication?

**Difficulty**: Intermediate

**Strategy**:
Central Auth Service + JWT. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
Authorization: Bearer <token>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q14: What is Distributed Tracing?

**Difficulty**: Intermediate

**Strategy**:
Tracking requests across services. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Jaeger, Zipkin (TraceID)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q15: What is Centralized Logging?

**Difficulty**: Intermediate

**Strategy**:
Aggregating logs from all services. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# ELK Stack
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q16: Idempotency in Microservices?

**Difficulty**: Intermediate

**Strategy**:
Retry safe operations. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
Header: Idempotency-Key
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q17: How do you handle inter-service communication?

**Difficulty**: Beginner

**Strategy**:
Sync (REST/gRPC) vs Async (Message Queue). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# HTTP vs RabbitMQ
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q18: What is gRPC?

**Difficulty**: Intermediate

**Strategy**:
High performance RPC framework using Protobuf. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
service Greeter { rpc SayHello... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q19: REST vs gRPC?

**Difficulty**: Intermediate

**Strategy**:
REST: Text (JSON), Browser friendly. gRPC: Binary, Faster.

**Code Example**:
```yaml
# gRPC for internal comms
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q20: What is a Message Broker?

**Difficulty**: Beginner

**Strategy**:
Intermediary for messages. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# RabbitMQ, Kafka, ActiveMQ
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q21: Kafka vs RabbitMQ?

**Difficulty**: Advanced

**Strategy**:
Kafka: Log stream (replayable). RabbitMQ: Queue (transient).

**Code Example**:
```yaml
# Kafka for event sourcing
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q22: What is API Composition?

**Difficulty**: Intermediate

**Strategy**:
Gateway aggregates results from multiple services.

**Code Example**:
```yaml
{ user, orders, payments }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q23: What is Database per Service?

**Difficulty**: Intermediate

**Strategy**:
Each service owns its DB. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Decoupling data
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q24: What is Shared Database antipattern?

**Difficulty**: Intermediate

**Strategy**:
Services sharing DB creates coupling. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Avoid if possible
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q25: How do you handle data consistency?

**Difficulty**: Advanced

**Strategy**:
Eventual consistency. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# BASE vs ACID
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q26: What is CAP Theorem?

**Difficulty**: Intermediate

**Strategy**:
Consistency, Availability, Partition Tolerance. Pick 2.

**Code Example**:
```yaml
# Microservices usually AP
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q27: What is 12-Factor App?

**Difficulty**: Intermediate

**Strategy**:
The 12-Factor App is a methodology for building software-as-a-service apps. It includes principles like storing config in the environment, keeping dev/prod parity, treating logs as event streams, and handling concurrency via the process model.

**Code Example**:
```yaml
# Config in env, Stateless
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q28: How do you version APIs?

**Difficulty**: Beginner

**Strategy**:
URL path, Header, or Query param. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
/v1/users
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q29: What is Consumer Driven Contracts?

**Difficulty**: Advanced

**Strategy**:
Consumers define expectations. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Pact testing
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q30: What is Chaos Engineering?

**Difficulty**: Advanced

**Strategy**:
Testing resilience by breaking things. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Chaos Monkey
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q31: What is Blue/Green Deployment?

**Difficulty**: Intermediate

**Strategy**:
Zero downtime release. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Switch traffic
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q32: What is Canary Release?

**Difficulty**: Intermediate

**Strategy**:
Rollout to small subset. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# 10% traffic
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q33: What is Strangler Fig Pattern?

**Difficulty**: Advanced

**Strategy**:
Migrate monolith to microservices gradually. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Intercept calls
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q34: What is BFF (Backend for Frontend)?

**Difficulty**: Intermediate

**Strategy**:
Separate API for Mobile vs Web. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Optimized payloads
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q35: What is Sidecar Pattern?

**Difficulty**: Intermediate

**Strategy**:
Offload tasks (ssl, logging) to side container. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Service Mesh
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q36: What is Service Mesh?

**Difficulty**: Advanced

**Strategy**:
Infrastructure layer for service comms. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Istio, Linkerd
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q37: How to prevent cascading failures?

**Difficulty**: Intermediate

**Strategy**:
Timeouts, Circuit Breakers, Bulkheads. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
timeout: 5s
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q38: What is Rate Limiting?

**Difficulty**: Beginner

**Strategy**:
Control traffic flow. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
429 Too Many Requests
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q39: What is Throttling?

**Difficulty**: Beginner

**Strategy**:
Slow down requests. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Leaky bucket
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q40: Stateless vs Stateful services?

**Difficulty**: Beginner

**Strategy**:
Stateless scales easier. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Store state in Redis/DB
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q41: How do you test Microservices?

**Difficulty**: Intermediate

**Strategy**:
Unit, Integration, Contract, E2E. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Mock external services
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q42: What is Containerization?

**Difficulty**: Beginner

**Strategy**:
Packaging app with dependencies. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Docker
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q43: What is Orchestration?

**Difficulty**: Beginner

**Strategy**:
Managing containers. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Kubernetes
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q44: How to secure microservices?

**Difficulty**: Intermediate

**Strategy**:
mTLS, OAuth2, OIDC. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Zero Trust
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q45: What is OAuth2?

**Difficulty**: Intermediate

**Strategy**:
Delegated authorization. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Access Tokens
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q46: What is OpenID Connect (OIDC)?

**Difficulty**: Intermediate

**Strategy**:
Identity layer on OAuth2. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# ID Tokens
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q47: What is JWT?

**Difficulty**: Beginner

**Strategy**:
JSON Web Token. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
header.payload.signature
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q48: Synchronous vs Asynchronous?

**Difficulty**: Beginner

**Strategy**:
Blocking vs Non-blocking. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Async for decoupling
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q49: What is Two-Phase Commit (2PC)?

**Difficulty**: Advanced

**Strategy**:
Distributed transaction protocol. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Prepare -> Commit
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q50: Why avoid 2PC in Microservices?

**Difficulty**: Advanced

**Strategy**:
Blocking, poor scalability. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Use Sagas instead
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q51: What is Dead Letter Queue (DLQ)?

**Difficulty**: Intermediate

**Strategy**:
Queue for failed messages. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# For manual inspection
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q52: What is a Competing Consumers pattern?

**Difficulty**: Intermediate

**Strategy**:
Multiple workers reading same queue. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Load balancing
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q53: What is Fan-out?

**Difficulty**: Intermediate

**Strategy**:
One message to multiple queues. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Pub/Sub
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q54: What is Polyglot Persistence?

**Difficulty**: Intermediate

**Strategy**:
Using different DBs for different needs. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# SQL + Mongo + Redis
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q55: What is Domain Driven Design (DDD)?

**Difficulty**: Advanced

**Strategy**:
Aligning software with business domain. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Bounded Contexts
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q56: What is a Bounded Context?

**Difficulty**: Advanced

**Strategy**:
Boundary where a model applies. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Sales Context vs Support Context
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q57: What is an Aggregate?

**Difficulty**: Advanced

**Strategy**:
Cluster of objects treated as unit. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Order + OrderItems
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q58: What is Anti-Corruption Layer?

**Difficulty**: Advanced

**Strategy**:
Translator between systems. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Adapter
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q59: What is Semantic Versioning?

**Difficulty**: Beginner

**Strategy**:
Major.Minor.Patch. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
v1.0.0
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q60: What is Continuous Integration (CI)?

**Difficulty**: Beginner

**Strategy**:
Merge code frequently + Tests. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Jenkins, GitHub Actions
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q61: What is Continuous Deployment (CD)?

**Difficulty**: Beginner

**Strategy**:
Auto deploy to prod. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Automated pipeline
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q62: What is Infrastructure as Code (IaC)?

**Difficulty**: Intermediate

**Strategy**:
Managing infra via code. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Terraform, Ansible
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q63: What is Immutable Infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Replace servers instead of patching. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# New VM/Container per deploy
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q64: What is Serverless?

**Difficulty**: Intermediate

**Strategy**:
Run code without managing servers. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# AWS Lambda
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q65: Microservices vs Serverless?

**Difficulty**: Intermediate

**Strategy**:
Long running vs Event driven. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Can use both
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q66: What is Cold Start?

**Difficulty**: Intermediate

**Strategy**:
Latency when function starts. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Serverless issue
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q67: How to handle distributed locking?

**Difficulty**: Advanced

**Strategy**:
Redis (Redlock) or Zookeeper. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Prevent race conditions
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q68: What is Leader Election?

**Difficulty**: Advanced

**Strategy**:
Choosing a coordinator. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Zookeeper/etcd
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q69: What is Sharding?

**Difficulty**: Advanced

**Strategy**:
Horizontal data partitioning. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Scale DB
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q70: What is Replication?

**Difficulty**: Intermediate

**Strategy**:
Copying data. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Availability
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q71: What is Auto-scaling?

**Difficulty**: Beginner

**Strategy**:
Dynamic resource adjustment. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Scale out/in
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q72: What is Log Aggregation?

**Difficulty**: Intermediate

**Strategy**:
Centralized logs. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Fluentd
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q73: What is Monitoring vs Observability?

**Difficulty**: Advanced

**Strategy**:
Monitoring: Is it healthy? Observability: Why is it broken?

**Code Example**:
```yaml
# Logs, Metrics, Traces
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q74: What is Alerting?

**Difficulty**: Beginner

**Strategy**:
Notifications on issues. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# PagerDuty
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q75: What is a Health Check?

**Difficulty**: Beginner

**Strategy**:
Endpoint to check status. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
GET /health
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q76: What is Graceful Shutdown?

**Difficulty**: Intermediate

**Strategy**:
Finish requests before stopping. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
server.close()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q77: What is Retry Pattern?

**Difficulty**: Beginner

**Strategy**:
Retry failed request. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
retry(3)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q78: What is Exponential Backoff?

**Difficulty**: Intermediate

**Strategy**:
Increase wait time between retries. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
1s, 2s, 4s, 8s
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q79: What is Jitter?

**Difficulty**: Advanced

**Strategy**:
Randomize retry intervals. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
Avoid thundering herd
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q80: What is load shedding?

**Difficulty**: Advanced

**Strategy**:
Drop requests when overloaded. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
503 Service Unavailable
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q81: What is a Reverse Proxy?

**Difficulty**: Beginner

**Strategy**:
Gateway in front of servers. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Nginx
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q82: What is a Forward Proxy?

**Difficulty**: Beginner

**Strategy**:
Proxy for clients. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# VPN
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q83: What is Sticky Sessions?

**Difficulty**: Intermediate

**Strategy**:
Route user to same server. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Cookie based
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q84: Why avoid Sticky Sessions?

**Difficulty**: Intermediate

**Strategy**:
Uneven load balancing. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
# Use stateless instead
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q85: What is Shadow Deployment?

**Difficulty**: Advanced

**Strategy**:
Run new version with real traffic (ignored response).

**Code Example**:
```yaml
# Test in prod safely
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q86: What is Feature Flag?

**Difficulty**: Beginner

**Strategy**:
Toggle features dynamically. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
if (feature.enabled) ...
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---
