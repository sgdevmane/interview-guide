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
51. [How do you handle Integration state management in large scale applications?](#q51-how-do-you-handle-integration-state-management-in-large-scale-applications) <span class="advanced">Advanced</span>
52. [How do you perform Integration data validation in microservices?](#q52-how-do-you-perform-integration-data-validation-in-microservices) <span class="beginner">Beginner</span>
53. [How do you automate Integration deployment for mobile devices?](#q53-how-do-you-automate-integration-deployment-for-mobile-devices) <span class="advanced">Advanced</span>
54. [How do you handle Integration concurrency issues in legacy systems?](#q54-how-do-you-handle-integration-concurrency-issues-in-legacy-systems) <span class="advanced">Advanced</span>
55. [How do you implement Integration caching in cloud infrastructure?](#q55-how-do-you-implement-integration-caching-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
56. [How do you manage Integration configuration for real-time systems?](#q56-how-do-you-manage-integration-configuration-for-real-time-systems) <span class="beginner">Beginner</span>
57. [How do you handle Integration internationalization (i18n) in distributed systems?](#q57-how-do-you-handle-integration-internationalization-i18n-in-distributed-systems) <span class="intermediate">Intermediate</span>
58. [How do you ensure Integration accessibility (a11y) in high-traffic sites?](#q58-how-do-you-ensure-integration-accessibility-a11y-in-high-traffic-sites) <span class="beginner">Beginner</span>
59. [How do you optimize Integration network requests in embedded systems?](#q59-how-do-you-optimize-integration-network-requests-in-embedded-systems) <span class="advanced">Advanced</span>
60. [How do you handle Integration performance optimization for production environments?](#q60-how-do-you-handle-integration-performance-optimization-for-production-environments) <span class="advanced">Advanced</span>
61. [What are the security implications of Integration in large scale applications?](#q61-what-are-the-security-implications-of-integration-in-large-scale-applications) <span class="intermediate">Intermediate</span>
62. [How do you debug Integration memory leaks in microservices?](#q62-how-do-you-debug-integration-memory-leaks-in-microservices) <span class="advanced">Advanced</span>
63. [Best practices for Integration code organization in mobile devices?](#q63-best-practices-for-integration-code-organization-in-mobile-devices) <span class="beginner">Beginner</span>
64. [How do you implement Integration error handling for legacy systems?](#q64-how-do-you-implement-integration-error-handling-for-legacy-systems) <span class="intermediate">Intermediate</span>
65. [How do you test Integration functionality in cloud infrastructure?](#q65-how-do-you-test-integration-functionality-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
66. [How do you handle Integration state management in real-time systems?](#q66-how-do-you-handle-integration-state-management-in-real-time-systems) <span class="advanced">Advanced</span>
67. [How do you perform Integration data validation in distributed systems?](#q67-how-do-you-perform-integration-data-validation-in-distributed-systems) <span class="beginner">Beginner</span>
68. [How do you automate Integration deployment for high-traffic sites?](#q68-how-do-you-automate-integration-deployment-for-high-traffic-sites) <span class="advanced">Advanced</span>
69. [How do you handle Integration concurrency issues in embedded systems?](#q69-how-do-you-handle-integration-concurrency-issues-in-embedded-systems) <span class="advanced">Advanced</span>
70. [How do you implement Integration caching in production environments?](#q70-how-do-you-implement-integration-caching-in-production-environments) <span class="intermediate">Intermediate</span>
71. [How do you manage Integration configuration for large scale applications?](#q71-how-do-you-manage-integration-configuration-for-large-scale-applications) <span class="beginner">Beginner</span>
72. [How do you handle Integration internationalization (i18n) in microservices?](#q72-how-do-you-handle-integration-internationalization-i18n-in-microservices) <span class="intermediate">Intermediate</span>
73. [How do you ensure Integration accessibility (a11y) in mobile devices?](#q73-how-do-you-ensure-integration-accessibility-a11y-in-mobile-devices) <span class="beginner">Beginner</span>
74. [How do you optimize Integration network requests in legacy systems?](#q74-how-do-you-optimize-integration-network-requests-in-legacy-systems) <span class="advanced">Advanced</span>
75. [How do you handle Integration performance optimization for cloud infrastructure?](#q75-how-do-you-handle-integration-performance-optimization-for-cloud-infrastructure) <span class="advanced">Advanced</span>
76. [What are the security implications of Integration in real-time systems?](#q76-what-are-the-security-implications-of-integration-in-real-time-systems) <span class="intermediate">Intermediate</span>
77. [How do you debug Integration memory leaks in distributed systems?](#q77-how-do-you-debug-integration-memory-leaks-in-distributed-systems) <span class="advanced">Advanced</span>
78. [Best practices for Integration code organization in high-traffic sites?](#q78-best-practices-for-integration-code-organization-in-high-traffic-sites) <span class="beginner">Beginner</span>
79. [How do you implement Integration error handling for embedded systems?](#q79-how-do-you-implement-integration-error-handling-for-embedded-systems) <span class="intermediate">Intermediate</span>
80. [How do you test Integration functionality in production environments?](#q80-how-do-you-test-integration-functionality-in-production-environments) <span class="intermediate">Intermediate</span>
81. [How do you handle Integration state management in large scale applications?](#q81-how-do-you-handle-integration-state-management-in-large-scale-applications) <span class="advanced">Advanced</span>
82. [How do you perform Integration data validation in microservices?](#q82-how-do-you-perform-integration-data-validation-in-microservices) <span class="beginner">Beginner</span>
83. [How do you automate Integration deployment for mobile devices?](#q83-how-do-you-automate-integration-deployment-for-mobile-devices) <span class="advanced">Advanced</span>
84. [How do you handle Integration concurrency issues in legacy systems?](#q84-how-do-you-handle-integration-concurrency-issues-in-legacy-systems) <span class="advanced">Advanced</span>
85. [How do you implement Integration caching in cloud infrastructure?](#q85-how-do-you-implement-integration-caching-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
86. [How do you manage Integration configuration for real-time systems?](#q86-how-do-you-manage-integration-configuration-for-real-time-systems) <span class="beginner">Beginner</span>
87. [How do you handle Integration internationalization (i18n) in distributed systems?](#q87-how-do-you-handle-integration-internationalization-i18n-in-distributed-systems) <span class="intermediate">Intermediate</span>
88. [How do you ensure Integration accessibility (a11y) in high-traffic sites?](#q88-how-do-you-ensure-integration-accessibility-a11y-in-high-traffic-sites) <span class="beginner">Beginner</span>
89. [How do you optimize Integration network requests in embedded systems?](#q89-how-do-you-optimize-integration-network-requests-in-embedded-systems) <span class="advanced">Advanced</span>
90. [How do you handle Integration performance optimization for production environments?](#q90-how-do-you-handle-integration-performance-optimization-for-production-environments) <span class="advanced">Advanced</span>
91. [What are the security implications of Integration in large scale applications?](#q91-what-are-the-security-implications-of-integration-in-large-scale-applications) <span class="intermediate">Intermediate</span>
92. [How do you debug Integration memory leaks in microservices?](#q92-how-do-you-debug-integration-memory-leaks-in-microservices) <span class="advanced">Advanced</span>
93. [Best practices for Integration code organization in mobile devices?](#q93-best-practices-for-integration-code-organization-in-mobile-devices) <span class="beginner">Beginner</span>
94. [How do you implement Integration error handling for legacy systems?](#q94-how-do-you-implement-integration-error-handling-for-legacy-systems) <span class="intermediate">Intermediate</span>
95. [How do you test Integration functionality in cloud infrastructure?](#q95-how-do-you-test-integration-functionality-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
96. [How do you handle Integration state management in real-time systems?](#q96-how-do-you-handle-integration-state-management-in-real-time-systems) <span class="advanced">Advanced</span>
97. [How do you perform Integration data validation in distributed systems?](#q97-how-do-you-perform-integration-data-validation-in-distributed-systems) <span class="beginner">Beginner</span>
98. [How do you automate Integration deployment for high-traffic sites?](#q98-how-do-you-automate-integration-deployment-for-high-traffic-sites) <span class="advanced">Advanced</span>
99. [How do you handle Integration concurrency issues in embedded systems?](#q99-how-do-you-handle-integration-concurrency-issues-in-embedded-systems) <span class="advanced">Advanced</span>
100. [How do you implement Integration caching in production environments?](#q100-how-do-you-implement-integration-caching-in-production-environments) <span class="intermediate">Intermediate</span>

---

<a id="q1"></a>
### Q1: You are integrating a third-party payment gateway (e.g., Stripe) and need to handle asynchronous webhooks. How do you secure and verify them?

**Difficulty**: Intermediate

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

**Strategy:**
Use an algorithm like Twitter Snowflake. It combines Timestamp + Machine ID + Sequence Number to generate sortable, unique 64-bit integers without coordination.

**Code Example:**
// Snowflake Bits: 1 (unused) | 41 (timestamp) | 10 (machine) | 12 (sequence)

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q36"></a>
### Q36: How do you implement Sticky Sessions (Session Affinity)?

**Difficulty**: Intermediate

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

**Strategy:**
Eliminate single points of failure. Use redundancy (multiple instances), Load Balancing, and Multi-AZ/Multi-Region deployment.

**Code Example:**
// Deploy across 3 Availability Zones

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q44"></a>
### Q44: What is the difference between Forward Proxy and Reverse Proxy?

**Difficulty**: Beginner

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

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

**Strategy**:

**Strategy:**
Add a `deleted_at` column or `is_deleted` flag. Filter out these rows in queries. Allows data recovery.

**Code Example:**
SELECT * FROM users WHERE deleted_at IS NULL;

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q49"></a>
### Q49: How do you optimize database queries with Indexes?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Create indexes on columns used in WHERE, JOIN, and ORDER BY clauses. Avoid over-indexing (slows writes). Use Composite Indexes for multi-column queries.

**Code Example:**
CREATE INDEX idx_users_email ON users(email);

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q50"></a>
### Q50: How do you implement Audit Logging?

**Difficulty**: Intermediate

**Strategy**:

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

---


<a id="q51"></a>
### Q51: How do you handle Integration state management in large scale applications?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```javascript
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q52"></a>
### Q52: How do you perform Integration data validation in microservices?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```javascript
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q53"></a>
### Q53: How do you automate Integration deployment for mobile devices?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q54"></a>
### Q54: How do you handle Integration concurrency issues in legacy systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q55"></a>
### Q55: How do you implement Integration caching in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q56"></a>
### Q56: How do you manage Integration configuration for real-time systems?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q57"></a>
### Q57: How do you handle Integration internationalization (i18n) in distributed systems?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```javascript
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q58"></a>
### Q58: How do you ensure Integration accessibility (a11y) in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q59"></a>
### Q59: How do you optimize Integration network requests in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q60"></a>
### Q60: How do you handle Integration performance optimization for production environments?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```javascript
const start = performance.now();
// Integration logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q61"></a>
### Q61: What are the security implications of Integration in large scale applications?

**Difficulty**: Intermediate

**Strategy**:
Validate all inputs. Sanitize data. Use least privilege principle.

**Code Example**:
```javascript
// Sanitize input
const clean = input.replace(/<script>/g, '');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q62"></a>
### Q62: How do you debug Integration memory leaks in microservices?

**Difficulty**: Advanced

**Strategy**:
Use heap snapshots and look for detached DOM nodes or uncleared listeners.

**Code Example**:
```javascript
// Check listeners
process.on('exit', () => cleanup());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q63"></a>
### Q63: Best practices for Integration code organization in mobile devices?

**Difficulty**: Beginner

**Strategy**:
Follow SOLID principles. Keep functions small and focused.

**Code Example**:
```javascript
// Single responsibility
function doOneThing() { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q64"></a>
### Q64: How do you implement Integration error handling for legacy systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```javascript
try {
  await IntegrationOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q65"></a>
### Q65: How do you test Integration functionality in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```javascript
test('Integration works', () => {
  expect(Integration()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q66"></a>
### Q66: How do you handle Integration state management in real-time systems?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```javascript
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q67"></a>
### Q67: How do you perform Integration data validation in distributed systems?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```javascript
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q68"></a>
### Q68: How do you automate Integration deployment for high-traffic sites?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q69"></a>
### Q69: How do you handle Integration concurrency issues in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q70"></a>
### Q70: How do you implement Integration caching in production environments?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q71"></a>
### Q71: How do you manage Integration configuration for large scale applications?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q72"></a>
### Q72: How do you handle Integration internationalization (i18n) in microservices?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```javascript
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q73"></a>
### Q73: How do you ensure Integration accessibility (a11y) in mobile devices?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q74"></a>
### Q74: How do you optimize Integration network requests in legacy systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q75"></a>
### Q75: How do you handle Integration performance optimization for cloud infrastructure?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```javascript
const start = performance.now();
// Integration logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q76"></a>
### Q76: What are the security implications of Integration in real-time systems?

**Difficulty**: Intermediate

**Strategy**:
Validate all inputs. Sanitize data. Use least privilege principle.

**Code Example**:
```javascript
// Sanitize input
const clean = input.replace(/<script>/g, '');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q77"></a>
### Q77: How do you debug Integration memory leaks in distributed systems?

**Difficulty**: Advanced

**Strategy**:
Use heap snapshots and look for detached DOM nodes or uncleared listeners.

**Code Example**:
```javascript
// Check listeners
process.on('exit', () => cleanup());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q78"></a>
### Q78: Best practices for Integration code organization in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Follow SOLID principles. Keep functions small and focused.

**Code Example**:
```javascript
// Single responsibility
function doOneThing() { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q79"></a>
### Q79: How do you implement Integration error handling for embedded systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```javascript
try {
  await IntegrationOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q80"></a>
### Q80: How do you test Integration functionality in production environments?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```javascript
test('Integration works', () => {
  expect(Integration()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q81"></a>
### Q81: How do you handle Integration state management in large scale applications?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```javascript
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q82"></a>
### Q82: How do you perform Integration data validation in microservices?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```javascript
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q83"></a>
### Q83: How do you automate Integration deployment for mobile devices?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q84"></a>
### Q84: How do you handle Integration concurrency issues in legacy systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q85"></a>
### Q85: How do you implement Integration caching in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q86"></a>
### Q86: How do you manage Integration configuration for real-time systems?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q87"></a>
### Q87: How do you handle Integration internationalization (i18n) in distributed systems?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```javascript
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q88"></a>
### Q88: How do you ensure Integration accessibility (a11y) in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q89"></a>
### Q89: How do you optimize Integration network requests in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q90"></a>
### Q90: How do you handle Integration performance optimization for production environments?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```javascript
const start = performance.now();
// Integration logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q91"></a>
### Q91: What are the security implications of Integration in large scale applications?

**Difficulty**: Intermediate

**Strategy**:
Validate all inputs. Sanitize data. Use least privilege principle.

**Code Example**:
```javascript
// Sanitize input
const clean = input.replace(/<script>/g, '');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q92"></a>
### Q92: How do you debug Integration memory leaks in microservices?

**Difficulty**: Advanced

**Strategy**:
Use heap snapshots and look for detached DOM nodes or uncleared listeners.

**Code Example**:
```javascript
// Check listeners
process.on('exit', () => cleanup());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q93"></a>
### Q93: Best practices for Integration code organization in mobile devices?

**Difficulty**: Beginner

**Strategy**:
Follow SOLID principles. Keep functions small and focused.

**Code Example**:
```javascript
// Single responsibility
function doOneThing() { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q94"></a>
### Q94: How do you implement Integration error handling for legacy systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```javascript
try {
  await IntegrationOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q95"></a>
### Q95: How do you test Integration functionality in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```javascript
test('Integration works', () => {
  expect(Integration()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q96"></a>
### Q96: How do you handle Integration state management in real-time systems?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```javascript
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q97"></a>
### Q97: How do you perform Integration data validation in distributed systems?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```javascript
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q98"></a>
### Q98: How do you automate Integration deployment for high-traffic sites?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q99"></a>
### Q99: How do you handle Integration concurrency issues in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q100"></a>
### Q100: How do you implement Integration caching in production environments?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>
