<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Integration Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [You are integrating a third-party payment gateway (e.g., Stripe) and need to handle asynchronous webhooks. How do you secure and verify them?](#q1-you-are-integrating-a-third-party-payment-gateway-e.g.-stripe-and-need-to-handle-asynchronous-webhooks.-how-do-you-secure-and-verify-them) <span class="intermediate">Intermediate</span>
2. [Your frontend application needs to aggregate data from multiple microservices (User, Order, Product) efficiently. How do you design this?](#q2-your-frontend-application-needs-to-aggregate-data-from-multiple-microservices-user-order-product-efficiently.-how-do-you-design-this) <span class="intermediate">Intermediate</span>
3. [You are consuming an external REST API that has a strict rate limit (e.g., 100 requests/minute). How do you handle this in your application?](#q3-you-are-consuming-an-external-rest-api-that-has-a-strict-rate-limit-e.g.-100-requestsminute.-how-do-you-handle-this-in-your-application) <span class="intermediate">Intermediate</span>
4. [You need to integrate a legacy SOAP service into a modern React application. The SOAP service uses XML. How do you approach this?](#q4-you-need-to-integrate-a-legacy-soap-service-into-a-modern-react-application.-the-soap-service-uses-xml.-how-do-you-approach-this) <span class="intermediate">Intermediate</span>
5. [Your application integrates with a partner API that is frequently unstable (500 errors, timeouts). How do you prevent this from crashing your system?](#q5-your-application-integrates-with-a-partner-api-that-is-frequently-unstable-500-errors-timeouts.-how-do-you-prevent-this-from-crashing-your-system) <span class="advanced">Advanced</span>
6. [You are designing an API that needs to support multiple versions (v1, v2) simultaneously. How do you implement versioning?](#q6-you-are-designing-an-api-that-needs-to-support-multiple-versions-v1-v2-simultaneously.-how-do-you-implement-versioning) <span class="intermediate">Intermediate</span>
7. [How do you handle Distributed Transactions across multiple microservices (e.g., Order Service, Inventory Service)?](#q7-how-do-you-handle-distributed-transactions-across-multiple-microservices-e.g.-order-service-inventory-service) <span class="advanced">Advanced</span>
8. [You are building a webhook system where your platform sends events to user-defined URLs. How do you handle failures/retries?](#q8-you-are-building-a-webhook-system-where-your-platform-sends-events-to-user-defined-urls.-how-do-you-handle-failuresretries) <span class="intermediate">Intermediate</span>
9. [How do you decide between 'Push' (Webhooks) and 'Pull' (Polling) integration models?](#q9-how-do-you-decide-between-push-webhooks-and-pull-polling-integration-models) <span class="beginner">Beginner</span>
10. [You are integrating with a third-party API that uses OAuth 2.0. Your background worker needs to access data without user interaction. Which flow do you use?](#q10-you-are-integrating-with-a-third-party-api-that-uses-oauth-2.0.-your-background-worker-needs-to-access-data-without-user-interaction.-which-flow-do-you-use) <span class="intermediate">Intermediate</span>
11. [How do you handle 'Idempotency' when building a financial transaction API?](#q11-how-do-you-handle-idempotency-when-building-a-financial-transaction-api) <span class="advanced">Advanced</span>
12. [You need to transfer large files (GBs) between two systems. A standard REST API with Base64 encoding is failing. How do you fix this?](#q12-you-need-to-transfer-large-files-gbs-between-two-systems.-a-standard-rest-api-with-base64-encoding-is-failing.-how-do-you-fix-this) <span class="intermediate">Intermediate</span>
13. [How do you implement 'Contract Testing' to ensure your microservices integration doesn't break when API changes?](#q13-how-do-you-implement-contract-testing-to-ensure-your-microservices-integration-doesnt-break-when-api-changes) <span class="advanced">Advanced</span>
14. [You are designing a public API. How do you implement Offset-based vs Cursor-based Pagination?](#q14-you-are-designing-a-public-api.-how-do-you-implement-offset-based-vs-cursor-based-pagination) <span class="intermediate">Intermediate</span>
15. [How do you secure an internal API that is only meant to be accessed by other internal services within a cluster?](#q15-how-do-you-secure-an-internal-api-that-is-only-meant-to-be-accessed-by-other-internal-services-within-a-cluster) <span class="advanced">Advanced</span>
16. [What is the difference between Orchestration and Choreography in Microservices?](#q16-what-is-the-difference-between-orchestration-and-choreography-in-microservices) <span class="intermediate">Intermediate</span>
17. [How do you implement Authorization Code Flow with PKCE for mobile apps?](#q17-how-do-you-implement-authorization-code-flow-with-pkce-for-mobile-apps) <span class="advanced">Advanced</span>
18. [How do you choose between gRPC, REST, and GraphQL?](#q18-how-do-you-choose-between-grpc-rest-and-graphql) <span class="intermediate">Intermediate</span>
19. [What is the Bulkhead Pattern and why use it?](#q19-what-is-the-bulkhead-pattern-and-why-use-it) <span class="advanced">Advanced</span>
20. [How do you implement Retry with Exponential Backoff and Jitter?](#q20-how-do-you-implement-retry-with-exponential-backoff-and-jitter) <span class="intermediate">Intermediate</span>
21. [JWT vs Session Authentication: When to use which?](#q21-jwt-vs-session-authentication:-when-to-use-which) <span class="intermediate">Intermediate</span>
22. [What are the common Database Sharding strategies?](#q22-what-are-the-common-database-sharding-strategies) <span class="advanced">Advanced</span>
23. [Explain Cache-Aside vs Write-Through caching.](#q23-explain-cache-aside-vs-write-through-caching.) <span class="intermediate">Intermediate</span>
24. [How do you handle Poison Messages in a Queue?](#q24-how-do-you-handle-poison-messages-in-a-queue) <span class="intermediate">Intermediate</span>
25. [How do you ensure Idempotency in a Message Consumer?](#q25-how-do-you-ensure-idempotency-in-a-message-consumer) <span class="advanced">Advanced</span>
26. [How does Distributed Tracing work with Context Propagation?](#q26-how-does-distributed-tracing-work-with-context-propagation) <span class="advanced">Advanced</span>
27. [How do you prevent SQL Injection?](#q27-how-do-you-prevent-sql-injection) <span class="beginner">Beginner</span>
28. [What is the difference between Horizontal and Vertical Scaling?](#q28-what-is-the-difference-between-horizontal-and-vertical-scaling) <span class="beginner">Beginner</span>
29. [How do you implement Content Negotiation?](#q29-how-do-you-implement-content-negotiation) <span class="intermediate">Intermediate</span>
30. [What is Chaos Engineering?](#q30-what-is-chaos-engineering) <span class="advanced">Advanced</span>
31. [Batch Processing vs Stream Processing: When to use which?](#q31-batch-processing-vs-stream-processing:-when-to-use-which) <span class="intermediate">Intermediate</span>
32. [WebSockets vs Server-Sent Events (SSE)?](#q32-websockets-vs-server-sent-events-sse) <span class="intermediate">Intermediate</span>
33. [What is the difference between RBAC and ABAC?](#q33-what-is-the-difference-between-rbac-and-abac) <span class="advanced">Advanced</span>
34. [Why is Connection Pooling important?](#q34-why-is-connection-pooling-important) <span class="intermediate">Intermediate</span>
35. [How do you generate unique IDs in a distributed system (Snowflake)?](#q35-how-do-you-generate-unique-ids-in-a-distributed-system-snowflake) <span class="advanced">Advanced</span>
36. [How do you implement Sticky Sessions (Session Affinity)?](#q36-how-do-you-implement-sticky-sessions-session-affinity) <span class="intermediate">Intermediate</span>
37. [What is a Reverse Proxy and why use it?](#q37-what-is-a-reverse-proxy-and-why-use-it) <span class="beginner">Beginner</span>
38. [How do you handle Cross-Site Request Forgery (CSRF)?](#q38-how-do-you-handle-cross-site-request-forgery-csrf) <span class="intermediate">Intermediate</span>
39. [How do you prevent Cross-Site Scripting (XSS)?](#q39-how-do-you-prevent-cross-site-scripting-xss) <span class="intermediate">Intermediate</span>
40. [What is a Dead Letter Queue (DLQ)?](#q40-what-is-a-dead-letter-queue-dlq) <span class="beginner">Beginner</span>
41. [What is Request Coalescing?](#q41-what-is-request-coalescing) <span class="advanced">Advanced</span>
42. [How do you implement API Rate Limiting with Sliding Window?](#q42-how-do-you-implement-api-rate-limiting-with-sliding-window) <span class="advanced">Advanced</span>
43. [How do you design for High Availability (HA)?](#q43-how-do-you-design-for-high-availability-ha) <span class="intermediate">Intermediate</span>
44. [What is the difference between Forward Proxy and Reverse Proxy?](#q44-what-is-the-difference-between-forward-proxy-and-reverse-proxy) <span class="beginner">Beginner</span>
45. [How do you handle Schema Evolution in Avro/Protobuf?](#q45-how-do-you-handle-schema-evolution-in-avroprotobuf) <span class="advanced">Advanced</span>
46. [How do you implement Distributed Locking?](#q46-how-do-you-implement-distributed-locking) <span class="advanced">Advanced</span>
47. [What is a Bloom Filter and when to use it?](#q47-what-is-a-bloom-filter-and-when-to-use-it) <span class="advanced">Advanced</span>
48. [How do you implement Soft Delete?](#q48-how-do-you-implement-soft-delete) <span class="beginner">Beginner</span>
49. [How do you optimize database queries with Indexes?](#q49-how-do-you-optimize-database-queries-with-indexes) <span class="intermediate">Intermediate</span>
50. [How do you implement Audit Logging?](#q50-how-do-you-implement-audit-logging) <span class="intermediate">Intermediate</span>

---

<a id="q1"></a>
### Q1: You are integrating a third-party payment gateway (e.g., Stripe) and need to handle asynchronous webhooks. How do you secure and verify them?

**Difficulty**: Intermediate

**Strategy**: Webhook security is critical in payment integrations because attackers can forge events to trigger unauthorized actions. The key trade-off is between trusting payloads blindly versus cryptographically verifying each event's origin using a shared secret. Always respond with 200 quickly and process events asynchronously to avoid timeout-related retries from the provider.

**Strategy:**
Verify the webhook signature using the provider's secret to ensure authenticity. Implement **idempotency** to handle duplicate events gracefully.

**Code Example (Node.js/Express):**
```javascript
const stripe = require('stripe')('sk_test_...');
const endpointSecret = "whsec_...";

app.post('/webhook', express.raw({type: 'application/json'}), (request, response) => {
  const sig = request.headers['stripe-signature'];
  let event;

  try {
    // Verify signature
    event = stripe.webhooks.constructEvent(request.body, sig, endpointSecret);
  } catch (err) {
    return response.status(400).send(`Webhook Error: ${err.message}`);
  }

  // Handle event
  if (event.type === 'payment_intent.succeeded') {
    const paymentIntent = event.data.object;
    handlePaymentSuccess(paymentIntent);
  }

  response.send();
});
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q2"></a>
### Q2: Your frontend application needs to aggregate data from multiple microservices (User, Order, Product) efficiently. How do you design this?

**Difficulty**: Intermediate

**Strategy**: Frontend-to-microservice communication is a common interview topic because naive approaches cause over-fetching, high latency, and tight coupling. The BFF (Backend for Frontend) or API Gateway pattern aggregates multiple downstream calls into a single response, reducing round trips. A common pitfall is making serial calls when parallel requests with `Promise.all` would cut latency significantly.

**Strategy:**
Use an **API Gateway** or **BFF (Backend for Frontend)** pattern. The gateway aggregates calls to downstream services and returns a single payload, reducing network chatter.

**Code Example (GraphQL/Apollo):**
```javascript
const resolvers = {
  Query: {
    orderConfig: async (_, { id }) => {
      const [user, order, product] = await Promise.all([
        userService.getUser(id),
        orderService.getOrder(id),
        productService.getProduct(id)
      ]);
      return { user, order, product };
    }
  }
};
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q3"></a>
### Q3: You are consuming an external REST API that has a strict rate limit (e.g., 100 requests/minute). How do you handle this in your application?

**Difficulty**: Intermediate

**Strategy**: Rate limiting is essential when consuming third-party APIs because exceeding limits leads to blocked requests, degraded user experience, and potential account suspension. The token bucket and leaky bucket algorithms each trade off between allowing burst traffic versus maintaining a steady rate. A best practice is to always honor the `Retry-After` header and cache responses locally to reduce unnecessary calls.

**Strategy:**
Implement a **Leaky Bucket** or **Token Bucket** algorithm locally using a queue (e.g., Redis). Respect `Retry-After` headers and implement **Exponential Backoff**.

**Code Example (Redis Rate Limiter):**
```javascript
const redis = require('redis');
const client = redis.createClient();

async function callExternalApi() {
  const key = 'api_limit';
  const current = await client.incr(key);
  
  if (current === 1) {
    await client.expire(key, 60); // Reset every minute
  }
  
  if (current > 100) {
    throw new Error("Rate limit exceeded. Try later.");
  }
  
  return fetch('https://api.external.com/data');
}
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q4"></a>
### Q4: You need to integrate a legacy SOAP service into a modern React application. The SOAP service uses XML. How do you approach this?

**Difficulty**: Intermediate

**Strategy**: Legacy system integration is a real-world reality that interviewers test to see if you can bridge old and new architectures pragmatically. The core approach is building a middleware translation layer that converts between protocols (SOAP/XML to REST/JSON), keeping the frontend clean and modern. Never expose SOAP directly to the browser due to CORS restrictions, XML parsing complexity, and security concerns.

**Strategy:**
Do not call SOAP directly from the browser (CORS/XML issues). Create a **Translation Layer (Middleware)** in Node/Go/Python that converts JSON to XML (SOAP) and vice-versa.

**Code Example (Node.js Proxy):**
```javascript
const soap = require('soap');
const url = 'http://example.com/wsdl?wsdl';

app.post('/api/convert', (req, res) => {
  soap.createClient(url, (err, client) => {
    client.MyFunction({ name: req.body.name }, (err, result) => {
      if (err) return res.status(500).json(err);
      res.json(result); // Return JSON to React
    });
  });
});
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q5"></a>
### Q5: Your application integrates with a partner API that is frequently unstable (500 errors, timeouts). How do you prevent this from crashing your system?

**Difficulty**: Advanced

**Strategy**: Integrating with unreliable external services is inevitable in distributed systems, and failing to isolate their failures can cascade into a full system outage. The Circuit Breaker pattern prevents resource exhaustion by halting calls to a degraded dependency after a failure threshold is reached, then testing recovery with periodic half-open requests. A common mistake is setting the reset timeout too short, which causes constant retry storms against a still-unhealthy service.

**Strategy:**
Implement the **Circuit Breaker Pattern**. If failures exceed a threshold, "open" the circuit to fail fast and prevent resource exhaustion, then periodically check if the service is back.

**Code Example (Hystrix/Resilience4j concept):**
```javascript
const breaker = new CircuitBreaker(callPartnerApi, {
  timeout: 3000, // If function takes longer than 3 seconds, trigger failure
  errorThresholdPercentage: 50, // When 50% of requests fail
  resetTimeout: 30000 // Wait 30 seconds before trying again
});

breaker.fire('some-arg')
  .then(console.log)
  .catch(console.error);
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q6"></a>
### Q6: You are designing an API that needs to support multiple versions (v1, v2) simultaneously. How do you implement versioning?

**Difficulty**: Intermediate

**Strategy**: API versioning is critical because breaking changes are inevitable, yet existing consumers must continue working without disruption. The main trade-offs are between URL path versioning (explicit but changes URLs), header versioning (clean URLs but hidden from casual inspection), and query parameter versioning (simple but less RESTful). A best practice is to maintain at most two active versions and deprecate older ones with clear timelines and migration guides.

**Strategy:**
Use **URL Path Versioning** (`/api/v1/resource`) for clarity or **Header Versioning** (`Accept: application/vnd.myapi.v1+json`) for cleaner URLs.

**Code Example (Express Route):**
```javascript
// v1 Router
app.use('/api/v1', v1Router);

// v2 Router
app.use('/api/v2', v2Router);

// Inside v2Router
router.get('/users', (req, res) => {
  res.json({ data: "New V2 Format" });
});
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q7"></a>
### Q7: How do you handle Distributed Transactions across multiple microservices (e.g., Order Service, Inventory Service)?

**Difficulty**: Advanced

**Strategy**: Distributed transactions are a cornerstone interview topic because maintaining data consistency across services without traditional database transactions is genuinely hard. The Saga pattern replaces Two-Phase Commit by breaking the transaction into a sequence of local transactions, each with a compensating action for rollback. The key pitfall is incomplete compensation logic -- every step must have a well-defined undo operation, or you risk leaving the system in an inconsistent state.

**Strategy:**
Avoid Two-Phase Commit (2PC) due to blocking. Use the **Saga Pattern** (Choreography or Orchestration) with **Compensating Transactions** to undo changes if a step fails.

**Code Example (Saga Logic):**
```javascript
async function createOrder(order) {
  try {
    await inventoryService.reserveStock(order.items);
    await paymentService.charge(order.amount);
    await shippingService.ship(order);
  } catch (error) {
    // Compensating actions
    await paymentService.refund(order.amount);
    await inventoryService.releaseStock(order.items);
    throw new Error("Order failed, rollback complete");
  }
}
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q8"></a>
### Q8: You are building a webhook system where your platform sends events to user-defined URLs. How do you handle failures/retries?

**Difficulty**: Intermediate

**Strategy**: Building a reliable webhook delivery system tests your understanding of at-least-once delivery guarantees and failure handling in distributed systems. The key approach is decoupling event production from delivery using a persistent message queue, combined with exponential backoff retries to avoid overwhelming a temporarily unhealthy subscriber. A common pitfall is retrying indefinitely without a DLQ (Dead Letter Queue), which wastes resources on permanently failing endpoints.

**Strategy:**
Use a **Message Queue** (Kafka/RabbitMQ). If delivery fails, push to a retry queue with **Exponential Backoff**. After N retries, move to a Dead Letter Queue (DLQ).

**Code Example (Concept):**
```javascript
async function sendWebhook(url, payload, attempt = 1) {
  try {
    await axios.post(url, payload);
  } catch (e) {
    if (attempt > 5) return moveToDLQ(payload);
    
    const delay = Math.pow(2, attempt) * 1000;
    setTimeout(() => sendWebhook(url, payload, attempt + 1), delay);
  }
}
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q9"></a>
### Q9: How do you decide between 'Push' (Webhooks) and 'Pull' (Polling) integration models?

**Difficulty**: Beginner

**Strategy**: Choosing between push and pull integration models is a foundational architecture decision that affects latency, resource usage, and system complexity. Push (webhooks) delivers data immediately with minimal overhead, while pull (polling) gives the consumer full control over ingestion rate but wastes resources on empty checks. A common mistake is using polling for real-time requirements when a push model would be far more efficient and responsive.

**Strategy:**
Use **Push (Webhooks)** for real-time updates and to reduce server load (no wasted calls). Use **Pull (Polling)** if the provider doesn't support webhooks or if you need to control the ingestion rate.

**Scenario:**
- **Real-time Chat:** Push (WebSockets/Webhooks)
- **Batch Data Import:** Pull (Cron job polling API)


[⬆️ Back to Top](#table-of-contents)

---

<a id="q10"></a>
### Q10: You are integrating with a third-party API that uses OAuth 2.0. Your background worker needs to access data without user interaction. Which flow do you use?

**Difficulty**: Intermediate

**Strategy**: Machine-to-machine authentication is a frequent requirement in backend integrations where no human user is involved to interactively approve access. The Client Credentials grant type is purpose-built for this scenario, exchanging a static client ID and secret for an access token without any user redirect. A best practice is to store credentials in environment variables or a secrets manager, never in source code, and to use short-lived tokens with automatic refresh.

**Strategy:**
Use the **Client Credentials Grant** flow. The application exchanges its Client ID and Client Secret for an Access Token directly.

**Code Example:**
```javascript
const response = await axios.post('https://api.provider.com/oauth/token', {
  grant_type: 'client_credentials',
  client_id: 'MY_ID',
  client_secret: 'MY_SECRET'
});

const token = response.data.access_token;
// Use token for subsequent requests
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q11"></a>
### Q11: How do you handle 'Idempotency' when building a financial transaction API?

**Difficulty**: Advanced

**Strategy**: Idempotency is non-negotiable in financial systems because duplicate charges or transfers have real monetary consequences and erode customer trust. The idempotency key pattern ensures that replaying the same request produces the same result without side effects, leveraging a store like Redis to cache previous responses. A common pitfall is forgetting to set an expiration on stored keys, which causes the store to grow unbounded over time.

**Strategy:**
Require clients to send a unique `Idempotency-Key` header. Store the key and response in a database (e.g., Redis) with an expiration. If the same key is seen, return the stored response without re-processing.

**Code Example:**
```javascript
const key = req.headers['idempotency-key'];
if (await redis.exists(key)) {
  return res.json(await redis.get(key));
}

// Process transaction
const result = await processPayment(req.body);
await redis.set(key, JSON.stringify(result), 'EX', 86400);
res.json(result);
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q12"></a>
### Q12: You need to transfer large files (GBs) between two systems. A standard REST API with Base64 encoding is failing. How do you fix this?

**Difficulty**: Intermediate

**Strategy**: Large file transfers expose the limits of naive REST APIs, where Base64 encoding inflates payload size by 33% and loading entire files into memory causes out-of-memory crashes. The solution is to use streaming uploads with multipart encoding or presigned URLs that let the client upload directly to object storage, bypassing your server entirely. A best practice is to also implement chunked uploads with resume capability for unreliable networks.

**Strategy:**
Use **Multipart/form-data** streams or **Presigned URLs** (e.g., S3) to upload directly to storage. Avoid loading the entire file into memory.

**Code Example (Node.js Stream):**
```javascript
const fs = require('fs');
const axios = require('axios');

const stream = fs.createReadStream('large-video.mp4');
await axios.post('https://api.upload.com', stream, {
  headers: { 'Content-Type': 'video/mp4' }
});
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q13"></a>
### Q13: How do you implement 'Contract Testing' to ensure your microservices integration doesn't break when API changes?

**Difficulty**: Advanced

**Strategy**: Contract testing catches integration bugs before deployment by verifying that providers and consumers agree on API expectations, making it a critical topic for microservices-heavy organizations. Unlike end-to-end integration tests, contract tests are fast, isolated, and run in CI/CD pipelines on each service independently. A common mistake is writing overly rigid contracts that break on any minor change; focus on testing essential fields and behaviors rather than exact response structures.

**Strategy:**
Use tools like **Pact**. The consumer defines expectations (Pacts), and the provider verifies them during CI/CD. This prevents breaking changes before deployment.

**Code Example (Pact Concept):**
```javascript
// Consumer Test
provider.addInteraction({
  state: 'user 1 exists',
  uponReceiving: 'get user',
  withRequest: { method: 'GET', path: '/user/1' },
  willRespondWith: { status: 200, body: { id: 1, name: 'Alice' } }
});
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q14"></a>
### Q14: You are designing a public API. How do you implement Offset-based vs Cursor-based Pagination?

**Difficulty**: Intermediate

**Strategy**: Pagination is a fundamental API design choice that directly affects performance and user experience, especially with large datasets. Offset-based pagination is simple but suffers from skipped or duplicated items when data changes between pages, while cursor-based pagination uses an indexed column to guarantee consistent results. For public APIs, prefer cursor-based pagination as your default since it scales better and avoids the performance cliff of deep offset queries.

**Strategy:**
Use **Cursor-based** for infinite scrolls and real-time data (avoids duplicates/missed items). Use **Offset-based** for standard static tables.

**Code Example (Cursor):**
```sql
-- Fetch next page where ID > last_seen_id
SELECT * FROM users 
WHERE id > 1050 
ORDER BY id ASC 
LIMIT 10;
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q15"></a>
### Q15: How do you secure an internal API that is only meant to be accessed by other internal services within a cluster?

**Difficulty**: Advanced

**Strategy**: Securing internal service-to-service communication is essential because a compromised pod or malicious actor inside the cluster could otherwise access any internal endpoint freely. Mutual TLS (mTLS) ensures both the client and server authenticate each other via certificates, while a service mesh like Istio enforces fine-grained authorization policies at the network level. A common pitfall is relying solely on network boundaries for security without enforcing identity-based access controls.

**Strategy:**
Use **mTLS (Mutual TLS)**. Both client and server present certificates to authenticate each other. Alternatively, use **Service Mesh** policies (Istio) to allow traffic only from specific service accounts.

**Code Example (Istio Policy):**
```yaml
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: allow-frontend-only
spec:
  selector:
    matchLabels:
      app: backend
  rules:
  - from:
    - source:
        principals: ["cluster.local/ns/default/sa/frontend"]
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q16"></a>
### Q16: What is the difference between Orchestration and Choreography in Microservices?

**Difficulty**: Intermediate

**Strategy**: Understanding orchestration versus choreography is key to designing workflows across microservices, as the wrong choice leads to either brittle coupling or untraceable event chains. Orchestration uses a central coordinator that is easier to monitor and debug but creates a single point of control, while choreography relies on autonomous event-driven services that are loosely coupled but harder to trace end-to-end. Choose orchestration for complex multi-step workflows and choreography for simple, independent reactions to events.

**Strategy:**
**Orchestration:** A central coordinator (conductor) tells services what to do (e.g., Camunda, Step Functions). Tighter coupling, easier monitoring.
**Choreography:** Services react to events (dancers) without a central controller (e.g., Kafka events). Loose coupling, harder to trace.

**Code Example:**
// Choreography Example (Event Bus)
await eventBus.publish('OrderCreated', { orderId: 123 });
// Inventory Service listens and reserves stock
// Payment Service listens and charges card

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q17"></a>
### Q17: How do you implement Authorization Code Flow with PKCE for mobile apps?

**Difficulty**: Advanced

**Strategy**: Mobile apps cannot securely store a client secret because the app binary can be decompiled, making traditional OAuth flows vulnerable to authorization code interception attacks. PKCE solves this by requiring the app to generate a dynamic code verifier and challenge per auth request, so even if the authorization code is intercepted, it cannot be exchanged without the original verifier. A best practice is to always use PKCE for any public client, including SPAs and desktop applications.

**Strategy:**
Use PKCE (Proof Key for Code Exchange) to prevent code interception. Client generates a `code_verifier` and sends a hashed `code_challenge`. The auth server verifies the verifier before issuing tokens.

**Code Example:**
// 1. Client creates verifier & challenge
const verifier = generateRandomString();
const challenge = base64UrlEncode(sha256(verifier));

// 2. Redirect to Auth Server with challenge
window.location = `/authorize?code_challenge=${challenge}`;

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q18"></a>
### Q18: How do you choose between gRPC, REST, and GraphQL?

**Difficulty**: Intermediate

**Strategy**: Selecting the right communication protocol is a high-impact architectural decision that affects performance, developer experience, and ecosystem compatibility. REST is the safest default for public-facing APIs due to universal tooling support, gRPC excels for internal service-to-service calls where binary serialization and strict contracts matter, and GraphQL shines when frontend clients need flexible data fetching. A common mistake is using a single protocol everywhere rather than matching the tool to the specific integration need.

**Strategy:**
- **gRPC:** Internal microservices, high performance (Protobuf), streaming.
- **REST:** Public APIs, standard resource caching, simple integration.
- **GraphQL:** Frontend-facing APIs, flexible data fetching, avoiding over-fetching.

**Code Example:**
// gRPC (Proto)
service OrderService {
  rpc CreateOrder (OrderRequest) returns (OrderResponse);
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q19"></a>
### Q19: What is the Bulkhead Pattern and why use it?

**Difficulty**: Advanced

**Strategy**: The Bulkhead pattern is essential for building resilient systems where a single degraded dependency must not take down the entire application. It works by partitioning resources like thread pools and connection pools per downstream service, so a slow or failing service consumes only its allocated capacity. A common pitfall is sharing a single thread pool across all outbound calls, which means one slow API can starve all other integrations.

**Strategy:**
Isolate resources (thread pools, connections) for different services so that a failure in one (e.g., slow Image Service) doesn't exhaust resources for others (e.g., User Service).

**Code Example:**
// Hystrix/Resilience4j Configuration
const imagePool = new Semaphore(10); // Max 10 concurrent image requests
const userPool = new Semaphore(50); // Max 50 concurrent user requests

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q20"></a>
### Q20: How do you implement Retry with Exponential Backoff and Jitter?

**Difficulty**: Intermediate

**Strategy**: Retry logic is fundamental to building robust integrations, but naive retries without backoff can worsen an already struggling service by flooding it with repeated requests. Exponential backoff progressively increases the wait time between retries, and adding random jitter prevents the thundering herd problem where all clients retry simultaneously. A best practice is to cap the maximum retry count and use a circuit breaker to stop retrying when a service is clearly down.

**Strategy:**
Wait `base * 2^attempt + random_jitter` before retrying. Jitter prevents 'thundering herd' problem where all retries hit the server simultaneously.

**Code Example:**
const delay = Math.min(cap, base * Math.pow(2, attempt));
const jitter = Math.random() * 100;
await sleep(delay + jitter);

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q21"></a>
### Q21: JWT vs Session Authentication: When to use which?

**Difficulty**: Intermediate

**Strategy**: Authentication strategy selection directly impacts scalability, security, and operational complexity, making it a frequent interview topic. Sessions are simpler to revoke and secure but require shared state or sticky sessions in distributed deployments, while JWTs are stateless and self-contained but difficult to invalidate before expiry. A best practice is to use short-lived access tokens with refresh tokens for JWT-based systems, and to never store sensitive data in the JWT payload since it is only encoded, not encrypted.

**Strategy:**
- **Session:** Stateful, easier revocation, better for server-side apps. Cookie-based.
- **JWT:** Stateless, scalable, hard to revoke immediately (requires short expiry + refresh tokens). Good for microservices/mobile.

**Code Example:**
// JWT Payload (Stateless)
{ "userId": 123, "exp": 1710000000 }

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q22"></a>
### Q22: What are the common Database Sharding strategies?

**Difficulty**: Advanced

**Strategy**: Database sharding is a critical scalability topic because single-server databases eventually hit physical limits on storage and compute capacity. Hash-based sharding distributes data evenly but makes resharding expensive, range-based sharding supports efficient range queries but risks hotspots, and directory-based sharding offers flexibility at the cost of an extra lookup. The most common pitfall is choosing a sharding key that leads to uneven data distribution, creating hot shards that defeat the purpose of scaling out.

**Strategy:**
- **Key Based (Hash):** `hash(id) % num_shards`. Even distribution, hard to reshard.
- **Range Based:** `id` 1-1000 in Shard A. Good for range queries, potential hotspots.
- **Directory Based:** Lookup table maps key to shard. Flexible, extra lookup overhead.

**Code Example:**
// Hash Sharding Logic
const shardId = crc32(userId) % totalShards;
const connection = shardConnections[shardId];

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q23"></a>
### Q23: Explain Cache-Aside vs Write-Through caching.

**Difficulty**: Intermediate

**Strategy**: Caching strategy selection has a direct impact on read latency and data consistency, making it one of the most practical topics in system design interviews. Cache-aside is the most common pattern because it is simple and keeps the cache and database decoupled, while write-through guarantees consistency at the cost of higher write latency. A common pitfall with cache-aside is failing to invalidate cached data on writes, leading to stale reads that confuse users.

**Strategy:**
- **Cache-Aside:** App reads cache; if miss, reads DB and updates cache. App updates DB and deletes cache.
- **Write-Through:** App writes to cache; cache writes to DB synchronously. Data always consistent but slower writes.

**Code Example:**
// Cache-Aside (Read)
let value = cache.get(key);
if (!value) {
  value = db.get(key);
  cache.set(key, value);
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q24"></a>
### Q24: How do you handle Poison Messages in a Queue?

**Difficulty**: Intermediate

**Strategy**: Poison message handling is a must-know for any system that relies on message queues, because a single malformed message can block processing for the entire queue. The key approach is to catch processing exceptions, track retry counts per message, and route messages that exceed the threshold to a Dead Letter Queue for investigation. A best practice is to log the full message content and error details when moving to the DLQ so the root cause can be diagnosed without replaying the message.

**Strategy:**
A poison message crashes the consumer repeatedly. Detect invalid messages (catch exceptions) and move them to a **Dead Letter Queue (DLQ)** after N retries for manual inspection.

**Code Example:**
try {
  process(msg);
} catch (e) {
  if (msg.attempts > 3) sendToDLQ(msg);
  else retry(msg);
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q25"></a>
### Q25: How do you ensure Idempotency in a Message Consumer?

**Difficulty**: Advanced

**Strategy**: Message idempotency is critical because most message brokers guarantee at-least-once delivery, meaning consumers will see duplicate messages and must handle them safely. The solution is to track processed message IDs in a persistent store and check for duplicates before processing, ideally within the same database transaction as the business logic. A common pitfall is checking the message ID and performing the work in separate transactions, which creates a race window where duplicates can slip through.

**Strategy:**
Track processed message IDs in a separate store (or DB transaction). If a duplicate message arrives (at-least-once delivery), ignore it.

**Code Example:**
if (await db.exists('processed_msgs', msg.id)) return;

await db.transaction(async () => {
  await processLogic(msg);
  await db.insert('processed_msgs', msg.id);
});

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q26"></a>
### Q26: How does Distributed Tracing work with Context Propagation?

**Difficulty**: Advanced

**Strategy**: Distributed tracing is indispensable for debugging latency and errors in microservice architectures where a single user request may traverse dozens of services. The trace ID is created at the entry point and propagated through HTTP headers or message metadata so every service can attach spans to the same trace. A common mistake is failing to propagate context through asynchronous paths like message queues, which breaks the trace and leaves blind spots in your observability.

**Strategy:**
A unique `Trace ID` is generated at the edge. It is passed (propagated) to downstream services via HTTP headers (e.g., `traceparent` in W3C standard) to correlate logs.

**Code Example:**
// Header Propagation
headers['traceparent'] = `00-${traceId}-${spanId}-01`;
fetch(url, { headers });

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q27"></a>
### Q27: How do you prevent SQL Injection?

**Difficulty**: Beginner

**Strategy**: SQL injection remains one of the most common and devastating web vulnerabilities, allowing attackers to read, modify, or delete entire databases through unsanitized input. The defense is straightforward: always use parameterized queries or an ORM that binds variables, and never interpolate user input directly into SQL strings. A best practice is to also apply the principle of least privilege to database accounts so that even a successful injection cannot drop tables or access unrelated data.

**Strategy:**
Use **Prepared Statements** (Parameterized Queries). Never concatenate user input directly into SQL strings.

**Code Example:**
// Safe
db.query('SELECT * FROM users WHERE id = $1', [userInput]);

// Unsafe
db.query('SELECT * FROM users WHERE id = ' + userInput);

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q28"></a>
### Q28: What is the difference between Horizontal and Vertical Scaling?

**Difficulty**: Beginner

**Strategy**: Scaling strategy is a foundational system design concept that determines whether an application can handle growth in traffic and data volume. Vertical scaling is simpler and faster but has a hard ceiling imposed by hardware limits, while horizontal scaling offers near-infinite capacity but introduces complexity in load balancing, data consistency, and deployment. A common mistake is waiting until vertical scaling hits its limit before designing for horizontal scalability, which forces a painful last-minute rearchitecture.

**Strategy:**
- **Vertical (Scale Up):** Add more power (CPU/RAM) to a single machine. Limited ceiling, downtime to upgrade.
- **Horizontal (Scale Out):** Add more machines (nodes) to the pool. Infinite scale, requires load balancing.

**Code Example:**
// Horizontal Scaling -> Load Balancer + Auto Scaling Group

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q29"></a>
### Q29: How do you implement Content Negotiation?

**Difficulty**: Intermediate

**Strategy**: Content negotiation allows a single API endpoint to serve multiple client types by letting each client declare its preferred response format through Accept headers. The server inspects the header and returns the best matching representation, falling back to a default or returning 406 Not Acceptable when no match exists. A best practice is to always define a default response format and to version your content types when the response structure changes significantly.

**Strategy:**
The client sends `Accept` headers (e.g., `application/json`, `application/xml`). The server responds in the requested format or returns 406 Not Acceptable.

**Code Example:**
const format = req.accepts(['json', 'xml']);
if (format === 'json') res.json(data);
else if (format === 'xml') res.send(toXML(data));

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q30"></a>
### Q30: What is Chaos Engineering?

**Difficulty**: Advanced

**Strategy**: Chaos engineering proactively validates system resilience by injecting controlled failures before real incidents expose weaknesses in production. The approach starts with defining a steady state hypothesis, introducing a controlled fault (like killing a pod or adding latency), and observing whether the system maintains acceptable behavior. A common pitfall is running chaos experiments in production without adequate monitoring or rollback plans, which can cause actual outages rather than prevent them.

**Strategy:**
Intentionally injecting failures (latency, crashes) into a system to verify its resilience and recovery mechanisms (e.g., Netflix Chaos Monkey).

**Code Example:**
// Chaos Experiment
if (Math.random() < 0.1) {
  throw new Error("Chaos: Service Unavailable");
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q31"></a>
### Q31: Batch Processing vs Stream Processing: When to use which?

**Difficulty**: Intermediate

**Strategy**: Choosing between batch and stream processing is a fundamental data architecture decision that affects latency, throughput, and infrastructure cost. Batch processing excels at efficiently handling large datasets with complex transformations on a schedule, while stream processing delivers low-latency results for real-time use cases but requires more sophisticated infrastructure. A common mistake is over-engineering with stream processing when a nightly batch job would meet the business requirements at a fraction of the cost.

**Strategy:**
- **Batch:** Process large volumes of data at scheduled intervals (e.g., Payroll, End-of-day reports). High latency, high throughput.
- **Stream:** Process data in real-time as it arrives (e.g., Fraud detection, Metrics). Low latency.

**Code Example:**
// Stream (Kafka Consumer)
consumer.on('message', processRealTime);

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q32"></a>
### Q32: WebSockets vs Server-Sent Events (SSE)?

**Difficulty**: Intermediate

**Strategy**: Real-time communication choice directly affects user experience and server resource utilization, making it a common topic when discussing interactive application design. WebSockets provide full-duplex communication ideal for collaborative apps, gaming, and chat, while SSE is simpler and more efficient for one-way server-to-client updates like notifications and live feeds. A common pitfall is using WebSockets when SSE would suffice, adding unnecessary complexity for bi-directional channels that are only used in one direction.

**Strategy:**
- **WebSockets:** Bi-directional, binary & text, suitable for chat/games.
- **SSE:** Uni-directional (Server to Client), text only, automatic reconnection, suitable for news feeds/stock tickers.

**Code Example:**
// SSE
const evtSource = new EventSource("/events");
evtSource.onmessage = (e) => console.log(e.data);

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q33"></a>
### Q33: What is the difference between RBAC and ABAC?

**Difficulty**: Advanced

**Strategy**: Authorization model selection determines how flexibly and securely your application can control access to resources as it grows in complexity. RBAC assigns permissions to roles and is simple to implement and audit, while ABAC evaluates dynamic attributes like user location, time, and resource sensitivity for fine-grained control. A common pitfall with RBAC is role explosion -- creating too many highly specific roles that become unmanageable, which is the signal that ABAC may be a better fit.

**Strategy:**
- **RBAC (Role-Based):** Access based on roles (Admin, Editor). Coarse-grained.
- **ABAC (Attribute-Based):** Access based on attributes (User location, Time of day, Resource sensitivity). Fine-grained.

**Code Example:**
// ABAC Policy
if (user.role === 'employee' && resource.owner === user.id && time < 1800) {
  allow();
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q34"></a>
### Q34: Why is Connection Pooling important?

**Difficulty**: Intermediate

**Strategy**: Connection pooling is a simple but high-impact optimization because establishing a database connection involves a TCP handshake, TLS negotiation, and authentication, all of which add significant latency per request. A pool maintains a set of reusable connections that eliminate this overhead, dramatically reducing average response times and database CPU load. A common mistake is setting the pool size too high, which overwhelms the database with too many concurrent connections rather than improving throughput.

**Strategy:**
Establishing DB connections is expensive (handshake). Pooling reuses existing connections, reducing latency and database load.

**Code Example:**
const pool = new Pool({ max: 20 }); // Maintain 20 open connections
const client = await pool.connect();
try { ... } finally { client.release(); }

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q35"></a>
### Q35: How do you generate unique IDs in a distributed system (Snowflake)?

**Difficulty**: Advanced

**Strategy**: Unique ID generation in distributed systems is a foundational problem because auto-incrementing IDs do not work across multiple database instances. The Snowflake approach combines a timestamp, machine identifier, and sequence number into a single sortable 64-bit integer, requiring no coordination between nodes. A best practice is to ensure the machine ID is assigned dynamically via a service discovery mechanism rather than hardcoded, to avoid ID collisions when instances are replaced.

**Strategy:**
Use an algorithm like Twitter Snowflake. It combines Timestamp + Machine ID + Sequence Number to generate sortable, unique 64-bit integers without coordination.

**Code Example:**
// Snowflake Bits: 1 (unused) | 41 (timestamp) | 10 (machine) | 12 (sequence)

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q36"></a>
### Q36: How do you implement Sticky Sessions (Session Affinity)?

**Difficulty**: Intermediate

**Strategy**: Sticky sessions solve the problem of stateful applications where session data is stored locally on one server and would be lost if the user's next request hits a different server. The load balancer routes requests from the same client to the same backend using cookies or IP hashing, maintaining session continuity. The key pitfall is that sticky sessions undermine horizontal scalability -- if one server receives disproportionately sticky traffic, it becomes a hotspot, which is why stateless design with external session storage is generally preferred.

**Strategy:**
Configure the Load Balancer to route requests from the same user (based on Cookie or IP) to the same server. Useful for stateful apps (but stateless is better).

**Code Example:**
// Nginx
upstream backend {
  ip_hash;
  server backend1;
  server backend2;
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q37"></a>
### Q37: What is a Reverse Proxy and why use it?

**Difficulty**: Beginner

**Strategy**: Reverse proxies are a foundational infrastructure component that every developer encounters in production, making this a common early-stage interview question. They sit between clients and backend servers to handle cross-cutting concerns like SSL termination, load balancing, caching, and compression in one place. A best practice is to always use a reverse proxy in production rather than exposing application servers directly, as it provides a security boundary and centralizes traffic management.

**Strategy:**
A server (Nginx, HAProxy) sitting in front of backend servers. Handles SSL termination, Load Balancing, Caching, and Compression.

**Code Example:**
// Nginx Reverse Proxy
location / {
  proxy_pass http://backend_servers;
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q38"></a>
### Q38: How do you handle Cross-Site Request Forgery (CSRF)?

**Difficulty**: Intermediate

**Strategy**: CSRF vulnerabilities exploit the trust a site has in the user's browser by forging authenticated requests without the user's knowledge, making them a critical security concern for any state-changing endpoint. Anti-CSRF tokens work by requiring a server-generated secret that an attacker cannot read due to same-origin policy, ensuring only legitimate forms can submit valid requests. A best practice is to use the SameSite cookie attribute as a defense-in-depth measure alongside tokens, and to always validate the token on the server before processing any state-changing operation.

**Strategy:**
Use **Anti-CSRF Tokens**. The server sends a token (in cookie/HTML). State-changing requests (POST) must include this token in the header, which the server validates.

**Code Example:**
// Client
headers['X-CSRF-Token'] = cookieToken;

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q39"></a>
### Q39: How do you prevent Cross-Site Scripting (XSS)?

**Difficulty**: Intermediate

**Strategy**: XSS is one of the most prevalent web vulnerabilities because it allows attackers to inject malicious scripts that execute in the context of trusted users, potentially stealing session tokens or performing actions on their behalf. The defense combines input sanitization, output encoding, and Content Security Policy headers to create multiple layers of protection. A common pitfall is relying solely on input validation while neglecting output encoding, which leaves the application vulnerable when data passes through different contexts like HTML attributes, JavaScript, or URLs.

**Strategy:**
Escaping/Sanitizing user input before rendering. Use Content Security Policy (CSP). Use frameworks (React/Angular) that auto-escape.

**Code Example:**
// CSP Header
Content-Security-Policy: default-src 'self'; script-src 'self' https://trusted.com

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q40"></a>
### Q40: What is a Dead Letter Queue (DLQ)?

**Difficulty**: Beginner

**Strategy**: Dead Letter Queues are a safety net for any message-driven system, preventing unprocessable messages from blocking the main queue and bringing processing to a halt. They isolate problematic messages so engineers can inspect, debug, and replay them without affecting the healthy flow of traffic. A best practice is to set up monitoring and alerts on the DLQ depth so that a sudden spike in dead letters triggers investigation before it indicates a systemic issue.

**Strategy:**
A queue where messages are moved after they fail to be processed successfully (e.g., after max retries). Allows isolation of bad messages for debugging.

**Code Example:**
// AWS SQS
RedrivePolicy: {
  deadLetterTargetArn: "arn:aws:sqs:...",
  maxReceiveCount: 5
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q41"></a>
### Q41: What is Request Coalescing?

**Difficulty**: Advanced

**Strategy**: Request coalescing prevents backend thundering herd problems by ensuring that multiple simultaneous requests for the same resource result in only one upstream call. This pattern is especially valuable during cache stampedes or thundering herd scenarios where a popular cache entry expires and hundreds of concurrent requests rush to regenerate it. A best practice is to set a reasonable timeout on coalesced waits so that if the primary request fails, waiting callers do not hang indefinitely.

**Strategy:**
Combining multiple identical requests for the same resource into a single request to the backend. The result is shared among all callers.

**Code Example:**
// Nginx Proxy Cache Lock
proxy_cache_lock on;

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q42"></a>
### Q42: How do you implement API Rate Limiting with Sliding Window?

**Difficulty**: Advanced

**Strategy**: Rate limiting is essential for protecting APIs from abuse and ensuring fair resource allocation, and the algorithm choice directly affects accuracy and user experience. Fixed window rate limiting suffers from boundary bursts where traffic doubles at window edges, while sliding window provides smooth, consistent rate enforcement by evaluating the exact count within a rolling time range. A best practice is to use Redis sorted sets for sliding window implementation and to return clear rate limit headers (X-RateLimit-Remaining, X-RateLimit-Reset) so clients can self-regulate.

**Strategy:**
Track request timestamps in a sorted set (Redis). Count elements within the time window `[now - window, now]`. More accurate than fixed window.

**Code Example:**
redis.zadd(key, now, now);
redis.zremrangebyscore(key, 0, now - window);
const count = redis.zcard(key);

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q43"></a>
### Q43: How do you design for High Availability (HA)?

**Difficulty**: Intermediate

**Strategy**: High availability design is critical for systems that cannot tolerate downtime, and interviewers use it to assess whether you think systematically about failure modes. The core principle is eliminating single points of failure through redundancy at every layer -- application instances, databases, load balancers, and availability zones. A common pitfall is building redundant application tiers while neglecting the database layer, which remains a single point of failure that takes the entire system down during a failover.

**Strategy:**
Eliminate single points of failure. Use redundancy (multiple instances), Load Balancing, and Multi-AZ/Multi-Region deployment.

**Code Example:**
// Deploy across 3 Availability Zones

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q44"></a>
### Q44: What is the difference between Forward Proxy and Reverse Proxy?

**Difficulty**: Beginner

**Strategy**: Understanding proxy direction is a fundamental networking concept that clarifies who the proxy is working for -- the client or the server. A forward proxy acts on behalf of the client to access the internet, providing anonymity and enforcing outbound policies, while a reverse proxy acts on behalf of the server to handle incoming traffic with load balancing and caching. A common mistake is confusing the two, especially since the same software (like Nginx) can serve both roles depending on configuration.

**Strategy:**
- **Forward Proxy:** Sits before the Client. Hides client identity (VPN). Enforces outbound policies.
- **Reverse Proxy:** Sits before the Server. Hides server identity. Handles load balancing.

**Code Example:**
// Forward: Client -> Proxy -> Internet
// Reverse: Internet -> Proxy -> Server

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q45"></a>
### Q45: How do you handle Schema Evolution in Avro/Protobuf?

**Difficulty**: Advanced

**Strategy**: Schema evolution is inevitable in long-lived data pipelines, and mishandling it can cause deserialization failures that silently corrupt data across consuming services. The key trade-off is between backward compatibility (new code reads old data) and forward compatibility (old code reads new data), both of which must be maintained in rolling deployments. A best practice is to use a Schema Registry to enforce compatibility rules at deploy time, preventing breaking schema changes from ever reaching production.

**Strategy:**
Follow compatibility rules: Add optional fields, never rename/remove required fields (unless you have a migration plan). Use Schema Registry.

**Code Example:**
// Proto
// Don't change field IDs
string name = 1; // OK
// string full_name = 1; // BAD (if clients expect 'name')

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q46"></a>
### Q46: How do you implement Distributed Locking?

**Difficulty**: Advanced

**Strategy**: Distributed locking is necessary whenever multiple processes or nodes need exclusive access to a shared resource, such as preventing duplicate cron executions or concurrent balance modifications. The challenge is that network partitions and process crashes can leave locks orphaned, so every lock must have a TTL to guarantee eventual release even if the holder dies. A common pitfall is implementing locks without a fencing token, which means a slow holder whose lock expires can still cause conflicts when it resumes execution.

**Strategy:**
Use a lock service (Redis Redlock, Zookeeper, Etcd). Ensure locks have a TTL to prevent deadlocks if the holder crashes.

**Code Example:**
// Redis
SET resource_name my_random_value NX PX 30000

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q47"></a>
### Q47: What is a Bloom Filter and when to use it?

**Difficulty**: Advanced

**Strategy**: Bloom filters are a powerful space-efficient tool for eliminating unnecessary expensive lookups, making them a favorite topic for testing knowledge of probabilistic data structures. They trade a small false positive rate for dramatic memory savings compared to storing the full dataset, which makes them ideal as a pre-check layer before hitting a database or cache. A best practice is to size the bit array based on your expected element count and desired false positive rate, since under-sizing causes the error rate to spike rapidly.

**Strategy:**
A probabilistic data structure that tests if an element is in a set. False positives possible, false negatives impossible. Use to quickly check if a row exists/cache key exists before doing expensive lookup.

**Code Example:**
if (bloom.contains(key)) {
  // Might exist, check DB
} else {
  // Definitely doesn't exist, return 404
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q48"></a>
### Q48: How do you implement Soft Delete?

**Difficulty**: Beginner

**Strategy**: Soft delete is a practical data management pattern that preserves recoverability, which matters because accidental deletions in production are far more common than most engineers expect. Instead of removing rows, it marks them as deleted with a timestamp, allowing administrators to recover data without restoring from backups. A common pitfall is forgetting to add the `WHERE deleted_at IS NULL` filter to new queries, which leaks deleted records into application results and causes confusing bugs.

**Strategy:**
Add a `deleted_at` column or `is_deleted` flag. Filter out these rows in queries. Allows data recovery.

**Code Example:**
SELECT * FROM users WHERE deleted_at IS NULL;

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q49"></a>
### Q49: How do you optimize database queries with Indexes?

**Difficulty**: Intermediate

**Strategy**: Database indexing is one of the highest-impact performance optimizations available, often turning queries that take minutes into millisecond responses. B-tree indexes accelerate lookups, joins, and sorts on specific columns, but every additional index slows down inserts, updates, and deletes because the index must be maintained. A best practice is to analyze slow query logs to identify which columns actually need indexing, and to use composite indexes strategically to cover multi-column WHERE clauses without creating redundant single-column indexes.

**Strategy:**
Create indexes on columns used in WHERE, JOIN, and ORDER BY clauses. Avoid over-indexing (slows writes). Use Composite Indexes for multi-column queries.

**Code Example:**
CREATE INDEX idx_users_email ON users(email);

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q50"></a>
### Q50: How do you implement Audit Logging?

**Difficulty**: Intermediate

**Strategy**: Audit logging is essential for compliance, security investigations, and operational debugging because it provides an immutable record of who did what and when across the system. The key design decision is capturing sufficient context (user identity, action, affected resource, timestamp, and IP address) without logging sensitive data like passwords or personal information. A best practice is to write audit logs to an append-only, tamper-proof store that is separate from application logs, so they survive even if the application is compromised.

**Strategy:**
Log critical actions (Who, What, When, Where) to a tamper-proof store. Use middleware to capture request context.

**Code Example:**
logger.info({
  user: req.user.id,
  action: 'DELETE_ORDER',
  resourceId: 123,
  timestamp: new Date()
});

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>
