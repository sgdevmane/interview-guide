# Integration Interview Questions

## Table of Contents

- [Q1: What is the difference between REST and GraphQL for frontend-backend integration?](#q1-what-is-the-difference-between-rest-and-graphql-for-frontend-backend-integration)
- [Q2: How do you handle authentication in a microservices architecture?](#q2-how-do-you-handle-authentication-in-a-microservices-architecture)
- [Q3: What are Webhooks and how do you secure them?](#q3-what-are-webhooks-and-how-do-you-secure-them)
- [Q4: How do you integrate a payment gateway like Stripe?](#q4-how-do-you-integrate-a-payment-gateway-like-stripe)
- [Q5: Explain the Circuit Breaker pattern in integration.](#q5-explain-the-circuit-breaker-pattern-in-integration)
- [Q6: What is CORS and how do you handle it?](#q6-what-is-cors-and-how-do-you-handle-it)
- [Q7: How do you implement Real-time updates (WebSocket vs SSE vs Polling)?](#q7-how-do-you-implement-real-time-updates-websocket-vs-sse-vs-polling)
- [Q8: What is OAuth 2.0 and OpenID Connect (OIDC)?](#q8-what-is-oauth-20-and-openid-connect-oidc)
- [Q9: How do you handle API versioning?](#q9-how-do-you-handle-api-versioning)
- [Q10: What is the difference between synchronous and asynchronous integration?](#q10-what-is-the-difference-between-synchronous-and-asynchronous-integration)
- [Q11: How do you handle Idempotency in API integrations?](#q11-how-do-you-handle-idempotency-in-api-integrations)
- [Q12: What is gRPC and when would you use it?](#q12-what-is-grpc-and-when-would-you-use-it)
- [Q13: How do you implement Rate Limiting?](#q13-how-do-you-implement-rate-limiting)
- [Q14: What is Backend for Frontend (BFF) pattern?](#q14-what-is-backend-for-frontend-bff-pattern)
- [Q15: How do you handle distributed transactions (Saga Pattern)?](#q15-how-do-you-handle-distributed-transactions-saga-pattern)
- [Q16: How do you integrate a third-party library that doesn't have types (TypeScript)?](#q16-how-do-you-integrate-a-third-party-library-that-doesnt-have-types-typescript)
- [Q17: What is Continuous Integration (CI) and Continuous Deployment (CD)?](#q17-what-is-continuous-integration-ci-and-continuous-deployment-cd)
- [Q18: How do you securely store secrets (API Keys) in a project?](#q18-how-do-you-securely-store-secrets-api-keys-in-a-project)
- [Q19: How do you handle long-running tasks (e.g., video processing)?](#q19-how-do-you-handle-long-running-tasks-eg,-video-processing)
- [Q20: What is the role of a Reverse Proxy (Nginx)?](#q20-what-is-the-role-of-a-reverse-proxy-nginx)
- [Q21: What is 'Contract Testing'?](#q21-what-is-contract-testing)
- [Q22: What is Swagger/OpenAPI?](#q22-what-is-swagger-openapi)
- [Q23: Difference between SOAP and REST?](#q23-difference-between-soap-and-rest)
- [Q24: How do you handle database migrations in a CI/CD pipeline?](#q24-how-do-you-handle-database-migrations-in-a-ci-cd-pipeline)
- [Q25: What is Blue-Green Deployment?](#q25-what-is-blue-green-deployment)
- [Q26: What is Canary Deployment?](#q26-what-is-canary-deployment)
- [Q27: How do you monitor integration health?](#q27-how-do-you-monitor-integration-health)
- [Q28: What is Distributed Tracing?](#q28-what-is-distributed-tracing)
- [Q29: How do you handle timezone issues in integration?](#q29-how-do-you-handle-timezone-issues-in-integration)
- [Q30: What is a Dead Letter Queue (DLQ)?](#q30-what-is-a-dead-letter-queue-dlq)
- [Q31: Explain Eventual Consistency.](#q31-explain-eventual-consistency)
- [Q32: What is CAP Theorem?](#q32-what-is-cap-theorem)
- [Q33: How do you integrate Google Maps?](#q33-how-do-you-integrate-google-maps)
- [Q34: How do you handle file uploads to S3?](#q34-how-do-you-handle-file-uploads-to-s3)
- [Q35: What is SSO (Single Sign-On)?](#q35-what-is-sso-single-sign-on)
- [Q36: What is SAML?](#q36-what-is-saml)
- [Q37: How do you implement Feature Flags?](#q37-how-do-you-implement-feature-flags)
- [Q38: What is A/B Testing implementation?](#q38-what-is-a-b-testing-implementation)
- [Q39: How to prevent SQL Injection in integration?](#q39-how-to-prevent-sql-injection-in-integration)
- [Q40: How to prevent XSS (Cross-Site Scripting)?](#q40-how-to-prevent-xss-cross-site-scripting)
- [Q41: What is CSRF (Cross-Site Request Forgery)?](#q41-what-is-csrf-cross-site-request-forgery)
- [Q42: What is Content Delivery Network (CDN)?](#q42-what-is-content-delivery-network-cdn)
- [Q43: How do you invalidate CDN cache?](#q43-how-do-you-invalidate-cdn-cache)
- [Q44: What is Docker?](#q44-what-is-docker)
- [Q45: What is Kubernetes?](#q45-what-is-kubernetes)
- [Q46: What is Service Mesh (Istio)?](#q46-what-is-service-mesh-istio)
- [Q47: How do you handle JSON parsing errors?](#q47-how-do-you-handle-json-parsing-errors)
- [Q48: What is Schema Registry (Kafka)?](#q48-what-is-schema-registry-kafka)
- [Q49: How do you optimize API performance?](#q49-how-do-you-optimize-api-performance)
- [Q50: What is HTTP/2?](#q50-what-is-http-2)
- [Q51: What is HTTP/3?](#q51-what-is-http-3)
- [Q52: How do you handle deprecated APIs?](#q52-how-do-you-handle-deprecated-apis)
- [Q53: What is Semantic Versioning (SemVer)?](#q53-what-is-semantic-versioning-semver)
- [Q54: How do you document APIs?](#q54-how-do-you-document-apis)
- [Q55: What is HATEOAS?](#q55-what-is-hateoas)
- [Q56: What is TDD (Test Driven Development)?](#q56-what-is-tdd-test-driven-development)
- [Q57: What is BDD (Behavior Driven Development)?](#q57-what-is-bdd-behavior-driven-development)
- [Q58: How do you integrate Analytics (Google Analytics)?](#q58-how-do-you-integrate-analytics-google-analytics)
- [Q59: What is a 'Health Check' endpoint?](#q59-what-is-a-health-check-endpoint)
- [Q60: How do you debug CORS errors?](#q60-how-do-you-debug-cors-errors)
- [Q61: What is the difference between Authentication and Authorization?](#q61-what-is-the-difference-between-authentication-and-authorization)
- [Q62: What is RBAC (Role-Based Access Control)?](#q62-what-is-rbac-role-based-access-control)
- [Q63: What is ABAC (Attribute-Based Access Control)?](#q63-what-is-abac-attribute-based-access-control)
- [Q64: How do you handle API timeouts?](#q64-how-do-you-handle-api-timeouts)
- [Q65: What is 'Chaos Engineering'?](#q65-what-is-chaos-engineering)
- [Q66: How do you integration test a file upload?](#q66-how-do-you-integration-test-a-file-upload)
- [Q67: What is 'Mocking' in testing?](#q67-what-is-mocking-in-testing)
- [Q68: What is 'Stubbing'?](#q68-what-is-stubbing)
- [Q69: How do you test Webhooks locally?](#q69-how-do-you-test-webhooks-locally)
- [Q70: What is 'Infrastructure as Code' (IaC)?](#q70-what-is-infrastructure-as-code-iac)
- [Q71: What is 'Serverless'?](#q71-what-is-serverless)
- [Q72: How do you handle 'Cold Start' in Serverless?](#q72-how-do-you-handle-cold-start-in-serverless)
- [Q73: What is Multi-Tenancy?](#q73-what-is-multi-tenancy)
- [Q74: How do you implement Logging in Microservices?](#q74-how-do-you-implement-logging-in-microservices)
- [Q75: What is ELK Stack?](#q75-what-is-elk-stack)
- [Q76: What is Prometheus?](#q76-what-is-prometheus)
- [Q77: How do you secure an API Key in a Mobile App?](#q77-how-do-you-secure-an-api-key-in-a-mobile-app)
- [Q78: What is Certificate Pinning?](#q78-what-is-certificate-pinning)
- [Q79: How do you handle 'Data Seeding' for integration tests?](#q79-how-do-you-handle-data-seeding-for-integration-tests)
- [Q80: What is 'Snapshot Testing'?](#q80-what-is-snapshot-testing)
- [Q81: How do you automate browser testing?](#q81-how-do-you-automate-browser-testing)
- [Q82: What is 'Headless Browser'?](#q82-what-is-headless-browser)
- [Q83: How do you handle 3rd party API downtime?](#q83-how-do-you-handle-3rd-party-api-downtime)
- [Q84: What is 12-Factor App methodology?](#q84-what-is-12-factor-app-methodology)
- [Q85: How do you optimize Docker images?](#q85-how-do-you-optimize-docker-images)
- [Q86: What is 'Shift Left' testing?](#q86-what-is-shift-left-testing)
- [Q87: How do you handle 'Merge Conflicts'?](#q87-how-do-you-handle-merge-conflicts)
- [Q88: What is Git Flow?](#q88-what-is-git-flow)
- [Q89: What is Trunk Based Development?](#q89-what-is-trunk-based-development)
- [Q90: How do you handle API Backward Compatibility?](#q90-how-do-you-handle-api-backward-compatibility)
- [Q91: What is the difference between Forward Proxy and Reverse Proxy?](#q91-what-is-the-difference-between-forward-proxy-and-reverse-proxy)
- [Q92: How do you implement Search?](#q92-how-do-you-implement-search)
- [Q93: What is a 'Bastion Host'?](#q93-what-is-a-bastion-host)
- [Q94: What is 'VPC Peering'?](#q94-what-is-vpc-peering)
- [Q95: How do you back up databases?](#q95-how-do-you-back-up-databases)
- [Q96: What is 'Connection Pooling'?](#q96-what-is-connection-pooling)
- [Q97: What is 'Sticky Sessions'?](#q97-what-is-sticky-sessions)
- [Q98: How do you handle 'Session Replication'?](#q98-how-do-you-handle-session-replication)
- [Q99: What is 'Sharding'?](#q99-what-is-sharding)
- [Q100: What is 'Replication' (Master-Slave)?](#q100-what-is-replication-master-slave)

---

### Q1: What is the difference between REST and GraphQL for frontend-backend integration?

**Difficulty: Beginner**

**Answer:**
**REST (Representational State Transfer):**
- **Architecture:** Resource-based. Endpoints represent resources (e.g., `/users`, `/posts`).
- **Data Fetching:** Fixed data structure per endpoint. Over-fetching (getting too much data) or under-fetching (getting too little, requiring multiple requests) is common.
- **Caching:** Built-in HTTP caching.
- **Versioning:** usually via URL (`v1/users`).

**GraphQL:**
- **Architecture:** Query-based. Single endpoint (usually `/graphql`).
- **Data Fetching:** Client requests exactly what it needs. Solves over/under-fetching.
- **Caching:** Harder, requires client-side caching (Apollo, Relay).
- **Versioning:** Schema evolution (deprecating fields) instead of versioning endpoints.

**Use Cases:**
- **REST:** Simple apps, public APIs, caching is critical.
- **GraphQL:** Complex data requirements, mobile apps (bandwidth efficiency), aggregating multiple sources.

---

### Q2: How do you handle authentication in a microservices architecture?

**Difficulty: Advanced**

**Answer:**
In microservices, you want to avoid authenticating in every service.

**Common Patterns:**

1.  **API Gateway Pattern:**
    - The Gateway handles SSL, AuthN (Authentication).
    - It validates the token (JWT).
    - It forwards the request to downstream services with the User ID/Claims in headers (e.g., `X-User-Id`).

2.  **JWT (JSON Web Tokens):**
    - Stateless. Service A issues a token. Service B validates signature.
    - **Pros:** Scalable, no database lookup needed in Service B.
    - **Cons:** Revocation is hard (short expiry + refresh tokens).

3.  **Centralized Auth Service (OAuth2/OIDC):**
    - Services verify tokens against an Identity Provider (IdP) or use introspection.

**Best Practice:** Terminate Auth at the Gateway. Internal services trust the Gateway.

---

### Q3: What are Webhooks and how do you secure them?

**Difficulty: Intermediate**

**Answer:**
**Webhooks** are user-defined HTTP callbacks. They allow one system to notify another system when an event occurs (e.g., Stripe notifying your server that a payment succeeded).

**How to Secure Webhooks:**

1.  **Signature Verification (HMAC):**
    - The sender signs the payload with a secret key (shared beforehand).
    - The receiver computes the hash of the payload with the same secret and compares it to the signature in the header.
    - **Prevents:** Tampering and Replay attacks (if timestamp included).

2.  **IP Whitelisting:**
    - Only accept requests from known IP ranges of the provider.

3.  **HTTPS:**
    - Ensure the endpoint is HTTPS to encrypt data in transit.

4.  **Idempotency:**
    - Handle duplicate events. Store Event IDs processed to avoid double-charging/processing.

---

### Q4: How do you integrate a payment gateway like Stripe?

**Difficulty: Intermediate**

**Answer:**
**Integration Flow (Stripe Example):**

1.  **Frontend:**
    - User enters card details.
    - Stripe Elements (JS SDK) securely sends card data to Stripe directly.
    - Stripe returns a `PaymentMethodId` (token). **Never** send raw card data to your backend.

2.  **Backend:**
    - Frontend sends `PaymentMethodId` to your backend.
    - Backend calls Stripe API (`PaymentIntents.create`) with amount and currency.
    - Confirm the payment.

3.  **Webhooks:**
    - Stripe notifies your backend via Webhook (`payment_intent.succeeded`) for async confirmation.
    - Backend updates order status in DB.

**Key Concept:** PCI Compliance is handled by Stripe because raw card data never touches your server.

---

### Q5: Explain the Circuit Breaker pattern in integration.

**Difficulty: Advanced**

**Answer:**
**Circuit Breaker** prevents an application from repeatedly trying to execute an operation that's likely to fail (e.g., calling a down service).

**States:**
1.  **Closed:** Normal operation. Requests pass through.
2.  **Open:** Recent failure threshold reached. Requests fail immediately (fast fail) without calling the downstream service.
3.  **Half-Open:** After a timeout, allow a limited number of test requests. If they succeed, reset to **Closed**. If fail, go back to **Open**.

**Benefits:**
- Prevents cascading failures.
- Reduces load on the failing service (giving it time to recover).
- Improves user experience (fast feedback).

---

### Q6: What is CORS and how do you handle it?

**Difficulty: Beginner**

**Answer:**
**CORS (Cross-Origin Resource Sharing)** is a browser security feature that restricts cross-origin HTTP requests.

**Mechanism:**
- Browser sends an `OPTIONS` preflight request.
- Server responds with headers:
    - `Access-Control-Allow-Origin`: `*` or `https://mydomain.com`
    - `Access-Control-Allow-Methods`: `GET, POST`
    - `Access-Control-Allow-Headers`: `Content-Type, Authorization`

**Handling:**
- **Dev:** Proxy requests (e.g., Vite/Webpack proxy) to bypass CORS.
- **Prod:** Configure the backend server (Express/Nginx/AWS API Gateway) to send correct headers.

---

### Q7: How do you implement Real-time updates (WebSocket vs SSE vs Polling)?

**Difficulty: Intermediate**

**Answer:**
1.  **Short Polling:**
    - Client asks server every X seconds.
    - **Pros:** Simple. **Cons:** Wasteful, high latency.

2.  **Long Polling:**
    - Client asks. Server holds connection until data is available.
    - **Pros:** Better than short polling. **Cons:** Server resource heavy.

3.  **Server-Sent Events (SSE):**
    - Unidirectional (Server -> Client) over HTTP.
    - **Use Case:** News feed, stock tickers.
    - **Pros:** Native browser support, auto-reconnect. **Cons:** Text only, unidirectional.

4.  **WebSockets:**
    - Bidirectional (Full-duplex) TCP connection.
    - **Use Case:** Chat, Games.
    - **Pros:** Low latency, bidirectional. **Cons:** Complex load balancing/state management.

---

### Q8: What is OAuth 2.0 and OpenID Connect (OIDC)?

**Difficulty: Intermediate**

**Answer:**
- **OAuth 2.0:** Authorization framework. "I allow App X to access my Photos on Google."
    - **Roles:** Resource Owner (User), Client (App), Authorization Server, Resource Server.
    - **Grant Types:** Authorization Code (server-side), PKCE (mobile/SPA), Client Credentials (machine-to-machine).

- **OIDC:** Authentication layer on top of OAuth 2.0. "I am John Doe."
    - Adds an ID Token (JWT) to the OAuth flow.
    - Standardizes user info endpoint.

**Flow (Auth Code + PKCE):**
1. User redirects to Auth Server.
2. User logs in & approves.
3. Redirect back with `code`.
4. App exchanges `code` + `verifier` for `access_token` + `id_token`.

---

### Q9: How do you handle API versioning?

**Difficulty: Intermediate**

**Answer:**
1.  **URL Versioning:**
    - `GET /api/v1/users`
    - **Pros:** Explicit, easy to cache. **Cons:** URI pollution.

2.  **Header Versioning:**
    - `Accept: application/vnd.myapi.v1+json`
    - **Pros:** Clean URLs. **Cons:** Harder to test in browser, cache fragmentation.

3.  **Query Parameter:**
    - `GET /api/users?version=1`
    - **Pros:** Easy. **Cons:** Generally discouraged for REST.

**Best Practice:** URL versioning is most common and pragmatic.

---

### Q10: What is the difference between synchronous and asynchronous integration?

**Difficulty: Beginner**

**Answer:**
- **Synchronous (REST/gRPC):**
    - Client waits for response.
    - **Pros:** Simple, immediate consistency.
    - **Cons:** Tight coupling, latency sensitive.

- **Asynchronous (Message Queues/Event Bus):**
    - Client sends message and continues. Receiver processes later.
    - **Pros:** Decoupled, scalable, handles bursts (traffic smoothing).
    - **Cons:** Complexity, eventual consistency.

---

### Q11: How do you handle Idempotency in API integrations?

**Difficulty: Advanced**

**Answer:**
**Idempotency:** Making multiple identical requests has the same effect as making a single request.

**Implementation:**
1.  Client generates a unique `Idempotency-Key` (UUID) for sensitive operations (POST payments).
2.  Server checks cache/DB if Key exists.
3.  **If exists:** Return the *cached response* (do NOT re-process).
4.  **If new:** Process, save Key + Response, return response.

**Why:** Network timeouts. Client retries request. Without idempotency, you might charge the user twice.

---

### Q12: What is gRPC and when would you use it?

**Difficulty: Advanced**

**Answer:**
**gRPC (Google Remote Procedure Call):**
- Uses **HTTP/2** for transport.
- Uses **Protocol Buffers (Protobuf)** for binary serialization (smaller, faster than JSON).
- Strong typing with `.proto` contracts.

**Use Cases:**
- **Internal Microservices:** Low latency, high throughput communication.
- **Mobile Clients:** Bandwidth efficiency.
- **Polyglot Environments:** Auto-generate client/server code in any language.

**Cons:** Not natively supported in browsers (requires gRPC-Web proxy). Harder to debug than JSON.

---

### Q13: How do you implement Rate Limiting?

**Difficulty: Intermediate**

**Answer:**
**Rate Limiting** protects APIs from abuse (DDoS, scraping).

**Algorithms:**
1.  **Token Bucket:** Tokens added at rate R. Request consumes token.
2.  **Leaky Bucket:** Requests queue up and process at constant rate.
3.  **Fixed Window:** Max X requests per minute. (Burst issue at minute boundary).
4.  **Sliding Window:** Smoother limit.

**Implementation:**
- **Middleware:** Redis-based counter (key: `ip_address`).
- **Headers:** Return `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `Retry-After`.
- **Response:** 429 Too Many Requests.

---

### Q14: What is Backend for Frontend (BFF) pattern?

**Difficulty: Intermediate**

**Answer:**
**BFF Pattern:** Creating separate backend services for specific frontend interfaces (e.g., Mobile BFF, Web BFF).

**Problem:** Mobile needs less data/different format than Desktop. A general API is too bloated.

**Solution:**
- **Mobile BFF:** Calls microservices, aggregates data, filters fields, formats for mobile.
- **Web BFF:** Does the same for Web.

**Benefits:** Optimized payload, decoupled frontend teams.

---

### Q15: How do you handle distributed transactions (Saga Pattern)?

**Difficulty: Expert**

**Answer:**
In microservices, you can't use ACID transactions across databases.

**Saga Pattern:** A sequence of local transactions.
1.  **Choreography:** Service A publishes event. Service B listens and acts.
2.  **Orchestration:** A central Coordinator service tells A, then B, then C what to do.

**Compensation:** If Step 3 fails, the Saga executes "Compensating Transactions" to undo Steps 2 and 1 (e.g., Refund Payment to undo Charge).

---

### Q16: How do you integrate a third-party library that doesn't have types (TypeScript)?

**Difficulty: Beginner**

**Answer:**
1.  **Check DefinitelyTyped:** `npm install @types/library-name`.
2.  **Declare Module:** Create a `*.d.ts` file:
    ```typescript
    declare module 'library-name' {
      export function doSomething(arg: any): void;
    }
    ```
3.  **Use `any` (Last Resort):** `const lib = require('library-name');`

---

### Q17: What is Continuous Integration (CI) and Continuous Deployment (CD)?

**Difficulty: Beginner**

**Answer:**
- **CI:** Developers merge code frequently (daily). Automated tests run to verify integration. Goal: Detect errors early.
- **CD (Delivery):** Code is automatically built and prepared for release to staging/production.
- **CD (Deployment):** Code is automatically deployed to production without manual intervention.

**Tools:** Jenkins, GitHub Actions, GitLab CI, CircleCI.

---

### Q18: How do you securely store secrets (API Keys) in a project?

**Difficulty: Beginner**

**Answer:**
**NEVER commit secrets to Git.**

1.  **Environment Variables:** Use `.env` files (gitignored).
2.  **CI/CD Secrets:** Inject env vars in the build pipeline (GitHub Secrets).
3.  **Secret Managers:** AWS Secrets Manager, HashiCorp Vault (fetch at runtime).
4.  **Frontend:** Only expose public keys (e.g., Firebase config, Stripe Publishable Key). Proxy private keys through backend.

---

### Q19: How do you handle long-running tasks (e.g., video processing)?

**Difficulty: Intermediate**

**Answer:**
**Async Processing:**
1.  **Client:** Uploads video.
2.  **Server:** Saves to S3. Pushes job to **Message Queue** (SQS/RabbitMQ). Returns `202 Accepted` with a `JobId`.
3.  **Worker:** Pulls job, processes video. Updates DB status to "Done".
4.  **Client:** Polls status endpoint `/jobs/:id` or waits for WebSocket notification / Webhook.

---

### Q20: What is the role of a Reverse Proxy (Nginx)?

**Difficulty: Intermediate**

**Answer:**
A server that sits in front of backend servers.

**Roles:**
1.  **Load Balancing:** Distribute traffic to multiple backend instances.
2.  **Security:** Hide internal IP, handle SSL/TLS termination.
3.  **Caching:** Cache static assets or API responses.
4.  **Compression:** Gzip/Brotli.
5.  **Routing:** Route `/api` to Backend and `/` to Frontend static files.

---

### Q21: What is 'Contract Testing'?

**Difficulty: Advanced**

**Answer:**
Testing integration points by verifying that the Provider meets the contract expected by the Consumer (e.g., Pact).

---

### Q22: What is Swagger/OpenAPI?

**Difficulty: Beginner**

**Answer:**
A specification for documenting REST APIs. Allows auto-generating docs (Swagger UI) and client SDKs.

---

### Q23: Difference between SOAP and REST?

**Difficulty: Intermediate**

**Answer:**
SOAP: XML-based, strict standard, built-in security (WS-Security), stateful. REST: JSON/XML, architectural style, stateless, flexible.

---

### Q24: How do you handle database migrations in a CI/CD pipeline?

**Difficulty: Intermediate**

**Answer:**
Run migration scripts (Flyway/Liquibase/TypeORM) as a step in the deployment pipeline before starting the new app version.

---

### Q25: What is Blue-Green Deployment?

**Difficulty: Advanced**

**Answer:**
Two identical environments. Blue is live. Deploy to Green. Test Green. Switch Router to Green. Blue becomes idle.

---

### Q26: What is Canary Deployment?

**Difficulty: Advanced**

**Answer:**
Roll out update to a small subset of users (e.g., 5%). Monitor metrics. If good, roll out to rest.

---

### Q27: How do you monitor integration health?

**Difficulty: Intermediate**

**Answer:**
Use APM tools (Datadog, New Relic), Distributed Tracing (Jaeger/Zipkin), and Health Check endpoints (`/health`).

---

### Q28: What is Distributed Tracing?

**Difficulty: Advanced**

**Answer:**
Tracking a request as it flows through multiple microservices to identify latency bottlenecks. Uses a Trace ID propagated in headers.

---

### Q29: How do you handle timezone issues in integration?

**Difficulty: Beginner**

**Answer:**
Always store and exchange dates in **UTC** (ISO 8601 format). Convert to local time only on the frontend/UI.

---

### Q30: What is a Dead Letter Queue (DLQ)?

**Difficulty: Intermediate**

**Answer:**
A queue where messages are sent if they cannot be processed successfully after max retries. Allows manual inspection.

---

### Q31: Explain Eventual Consistency.

**Difficulty: Intermediate**

**Answer:**
In distributed systems, data might not be consistent immediately across all nodes, but will become consistent over time.

---

### Q32: What is CAP Theorem?

**Difficulty: Advanced**

**Answer:**
A distributed system can only deliver 2 of 3: Consistency, Availability, Partition Tolerance. Usually choose AP or CP.

---

### Q33: How do you integrate Google Maps?

**Difficulty: Beginner**

**Answer:**
Load Google Maps JS SDK. Secure API Key (restrict by referrer). Initialize Map component.

---

### Q34: How do you handle file uploads to S3?

**Difficulty: Intermediate**

**Answer:**
Generate **Presigned URL** on backend. Frontend uploads directly to S3 using that URL. Avoids burdening backend.

---

### Q35: What is SSO (Single Sign-On)?

**Difficulty: Intermediate**

**Answer:**
User logs in once (Identity Provider) and gains access to multiple applications without re-logging in (e.g., SAML, OIDC).

---

### Q36: What is SAML?

**Difficulty: Advanced**

**Answer:**
XML-based standard for exchanging auth data between IdP and SP (Service Provider). Common in Enterprise SSO.

---

### Q37: How do you implement Feature Flags?

**Difficulty: Intermediate**

**Answer:**
Use a service (LaunchDarkly) or DB config to toggle features on/off at runtime without deploying code.

---

### Q38: What is A/B Testing implementation?

**Difficulty: Intermediate**

**Answer:**
Assign user to Group A or B (randomly or hashed ID). Frontend renders variant. Analytics track conversion. Backend logs group.

---

### Q39: How to prevent SQL Injection in integration?

**Difficulty: Beginner**

**Answer:**
Always use Parameterized Queries or ORMs. Never concatenate strings for SQL.

---

### Q40: How to prevent XSS (Cross-Site Scripting)?

**Difficulty: Beginner**

**Answer:**
Sanitize user input. Escape output. Use Content Security Policy (CSP). Frameworks (Angular/React) auto-escape.

---

### Q41: What is CSRF (Cross-Site Request Forgery)?

**Difficulty: Intermediate**

**Answer:**
Attacker forces user browser to send request to trusted site. Prevention: Anti-CSRF Tokens, SameSite Cookie attribute.

---

### Q42: What is Content Delivery Network (CDN)?

**Difficulty: Beginner**

**Answer:**
Network of distributed servers delivering static content (images, CSS) based on user location for speed.

---

### Q43: How do you invalidate CDN cache?

**Difficulty: Intermediate**

**Answer:**
Version filenames (`main.a1b2.js`). Purge API (slow).

---

### Q44: What is Docker?

**Difficulty: Beginner**

**Answer:**
Platform to containerize applications (code + deps) ensuring consistency across environments.

---

### Q45: What is Kubernetes?

**Difficulty: Advanced**

**Answer:**
Orchestration tool for managing containerized applications (scaling, healing, load balancing).

---

### Q46: What is Service Mesh (Istio)?

**Difficulty: Expert**

**Answer:**
Infrastructure layer for microservice communication. Handles traffic, security (mTLS), observability without code changes.

---

### Q47: How do you handle JSON parsing errors?

**Difficulty: Beginner**

**Answer:**
Use `try-catch` around `JSON.parse()`. Validate schema using libraries like Zod or Joi.

---

### Q48: What is Schema Registry (Kafka)?

**Difficulty: Advanced**

**Answer:**
Central repository for message schemas (Avro). Ensures producers and consumers stay compatible.

---

### Q49: How do you optimize API performance?

**Difficulty: Intermediate**

**Answer:**
Caching (Redis, CDN), Gzip, Pagination, Filtering fields (GraphQL), Database indexing.

---

### Q50: What is HTTP/2?

**Difficulty: Intermediate**

**Answer:**
Major revision of HTTP. Features: Multiplexing (multiple requests over one conn), Header Compression, Server Push.

---

### Q51: What is HTTP/3?

**Difficulty: Advanced**

**Answer:**
Based on QUIC (UDP). Reduces latency, better packet loss handling compared to TCP.

---

### Q52: How do you handle deprecated APIs?

**Difficulty: Intermediate**

**Answer:**
Mark `Deprecated` in docs/headers. Monitor usage. Sunset policy (shutdown date). Email developers.

---

### Q53: What is Semantic Versioning (SemVer)?

**Difficulty: Beginner**

**Answer:**
Major.Minor.Patch (e.g., 1.0.0). Major=Breaking, Minor=Feature, Patch=Fix.

---

### Q54: How do you document APIs?

**Difficulty: Beginner**

**Answer:**
OpenAPI (Swagger), Postman Collections, ReadMe.io.

---

### Q55: What is HATEOAS?

**Difficulty: Advanced**

**Answer:**
REST constraint. Response includes links to related actions/resources. (Hypermedia as the Engine of Application State).

---

### Q56: What is TDD (Test Driven Development)?

**Difficulty: Intermediate**

**Answer:**
Write test first (fail), write code (pass), refactor.

---

### Q57: What is BDD (Behavior Driven Development)?

**Difficulty: Intermediate**

**Answer:**
Tests written in natural language (Gherkin: Given/When/Then). Focus on system behavior.

---

### Q58: How do you integrate Analytics (Google Analytics)?

**Difficulty: Beginner**

**Answer:**
Insert snippet. Track page views (router events). Track custom events (button clicks).

---

### Q59: What is a 'Health Check' endpoint?

**Difficulty: Beginner**

**Answer:**
`/health` or `/status`. Returns 200 OK if app and DB connection are healthy. Used by Load Balancers.

---

### Q60: How do you debug CORS errors?

**Difficulty: Intermediate**

**Answer:**
Check Network tab. Check Origin header vs Allowed Origin. Check if Preflight (OPTIONS) failed.

---

### Q61: What is the difference between Authentication and Authorization?

**Difficulty: Beginner**

**Answer:**
AuthN: Who are you? (Login). AuthZ: What can you do? (Permissions/Roles).

---

### Q62: What is RBAC (Role-Based Access Control)?

**Difficulty: Intermediate**

**Answer:**
Assign permissions to Roles (Admin, User). Assign Roles to Users.

---

### Q63: What is ABAC (Attribute-Based Access Control)?

**Difficulty: Advanced**

**Answer:**
Permissions based on attributes (User Dept, Time of Day, Resource Sensitivity). More fine-grained than RBAC.

---

### Q64: How do you handle API timeouts?

**Difficulty: Intermediate**

**Answer:**
Set timeout limit on client. Implement Retry logic (exponential backoff). Circuit Breaker.

---

### Q65: What is 'Chaos Engineering'?

**Difficulty: Advanced**

**Answer:**
Intentionally injecting failures (kill pods, latency) to test system resilience (e.g., Netflix Simian Army).

---

### Q66: How do you integration test a file upload?

**Difficulty: Intermediate**

**Answer:**
Use `supertest` or `Cypress`. Attach mock file to the form data request.

---

### Q67: What is 'Mocking' in testing?

**Difficulty: Beginner**

**Answer:**
Simulating external dependencies (DB, API) to isolate the unit under test.

---

### Q68: What is 'Stubbing'?

**Difficulty: Beginner**

**Answer:**
Hardcoding a response for a specific method call during test.

---

### Q69: How do you test Webhooks locally?

**Difficulty: Intermediate**

**Answer:**
Use tools like Ngrok to expose local server to internet. Or use Stripe CLI to forward events.

---

### Q70: What is 'Infrastructure as Code' (IaC)?

**Difficulty: Intermediate**

**Answer:**
Managing infrastructure (servers, networks) via code (Terraform, CloudFormation) instead of manual console.

---

### Q71: What is 'Serverless'?

**Difficulty: Intermediate**

**Answer:**
Cloud model where provider manages machine allocation. Pay per execution (AWS Lambda). Integration via triggers (API Gateway, S3).

---

### Q72: How do you handle 'Cold Start' in Serverless?

**Difficulty: Intermediate**

**Answer:**
Keep warm (ping periodically), use lighter runtime, Provisioned Concurrency.

---

### Q73: What is Multi-Tenancy?

**Difficulty: Advanced**

**Answer:**
Single instance serving multiple customers (tenants). Data isolation via separate DBs or Discriminator Column.

---

### Q74: How do you implement Logging in Microservices?

**Difficulty: Intermediate**

**Answer:**
Structured Logging (JSON). Centralized Aggregation (ELK Stack, Splunk). Correlation IDs.

---

### Q75: What is ELK Stack?

**Difficulty: Intermediate**

**Answer:**
Elasticsearch (Search), Logstash (Ingest), Kibana (Visualize). Common for log analysis.

---

### Q76: What is Prometheus?

**Difficulty: Intermediate**

**Answer:**
Monitoring system. Pulls metrics from services. Time-series DB. Often used with Grafana.

---

### Q77: How do you secure an API Key in a Mobile App?

**Difficulty: Intermediate**

**Answer:**
You can't fully. Use Proxy server. Obfuscate code. Restrict key usage by IP/Bundle ID.

---

### Q78: What is Certificate Pinning?

**Difficulty: Advanced**

**Answer:**
Hardcoding the expected server certificate/public key in the client to prevent Man-in-the-Middle attacks.

---

### Q79: How do you handle 'Data Seeding' for integration tests?

**Difficulty: Intermediate**

**Answer:**
Scripts to insert known data state into DB before test suite runs. Clean up after.

---

### Q80: What is 'Snapshot Testing'?

**Difficulty: Beginner**

**Answer:**
Comparing rendered UI or data structure against a stored reference 'snapshot'. Fails if changed unexpectedly.

---

### Q81: How do you automate browser testing?

**Difficulty: Beginner**

**Answer:**
Selenium, Cypress, Playwright, Puppeteer.

---

### Q82: What is 'Headless Browser'?

**Difficulty: Beginner**

**Answer:**
Browser without GUI. Faster for CI/CD testing.

---

### Q83: How do you handle 3rd party API downtime?

**Difficulty: Intermediate**

**Answer:**
Queue requests (DLQ), Circuit Breaker, Fallback UI, Cached data.

---

### Q84: What is 12-Factor App methodology?

**Difficulty: Intermediate**

**Answer:**
Best practices for building SaaS apps (Config in env, Stateless processes, Disposability, etc.).

---

### Q85: How do you optimize Docker images?

**Difficulty: Intermediate**

**Answer:**
Multi-stage builds. Alpine base images. .dockerignore. Minimize layers.

---

### Q86: What is 'Shift Left' testing?

**Difficulty: Intermediate**

**Answer:**
Testing early in the development cycle (Unit/Integration) rather than waiting for QA phase.

---

### Q87: How do you handle 'Merge Conflicts'?

**Difficulty: Beginner**

**Answer:**
Pull latest. Manually resolve overlapping changes. Run tests. Commit.

---

### Q88: What is Git Flow?

**Difficulty: Intermediate**

**Answer:**
Branching model: Master, Develop, Feature branches, Release branches, Hotfix branches.

---

### Q89: What is Trunk Based Development?

**Difficulty: Intermediate**

**Answer:**
Developers merge to main (trunk) frequently. Uses Feature Flags. Avoids 'Merge Hell'. preferred for CI/CD.

---

### Q90: How do you handle API Backward Compatibility?

**Difficulty: Intermediate**

**Answer:**
Never remove fields. Make new fields optional. Use versioning if breaking change is unavoidable.

---

### Q91: What is the difference between Forward Proxy and Reverse Proxy?

**Difficulty: Intermediate**

**Answer:**
Forward: Client -> Proxy -> Internet (Access control). Reverse: Internet -> Proxy -> Server (Load balancing).

---

### Q92: How do you implement Search?

**Difficulty: Intermediate**

**Answer:**
DB 'LIKE' (simple). Full-text Search (Postgres). Dedicated Search Engine (Elasticsearch, Algolia).

---

### Q93: What is a 'Bastion Host'?

**Difficulty: Intermediate**

**Answer:**
Jump server to access private network instances securely.

---

### Q94: What is 'VPC Peering'?

**Difficulty: Advanced**

**Answer:**
Connecting two Virtual Private Clouds so instances can talk as if on same network.

---

### Q95: How do you back up databases?

**Difficulty: Beginner**

**Answer:**
Scheduled dumps (pg_dump), Point-in-Time Recovery (WAL logs), Replication.

---

### Q96: What is 'Connection Pooling'?

**Difficulty: Intermediate**

**Answer:**
Maintaining a cache of open DB connections to reuse, reducing handshake overhead.

---

### Q97: What is 'Sticky Sessions'?

**Difficulty: Intermediate**

**Answer:**
Load balancer routes user to same server instance every time. Good for local session, bad for scaling.

---

### Q98: How do you handle 'Session Replication'?

**Difficulty: Intermediate**

**Answer:**
Store session in shared store (Redis) instead of local memory. Allows stateless servers.

---

### Q99: What is 'Sharding'?

**Difficulty: Advanced**

**Answer:**
Splitting database horizontally across multiple machines based on Shard Key (e.g., UserID).

---

### Q100: What is 'Replication' (Master-Slave)?

**Difficulty: Intermediate**

**Answer:**
Master handles Writes. Slaves replicate data and handle Reads. Increases Read throughput.

---
