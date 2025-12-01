<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>System Design Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [Design a URL Shortener (TinyURL)?](#q1) <span class="intermediate">Intermediate</span>
2. [Design a Rate Limiter?](#q2) <span class="intermediate">Intermediate</span>
3. [Design a Chat Application (WhatsApp)?](#q3) <span class="advanced">Advanced</span>
4. [Explain CAP Theorem?](#q4) <span class="beginner">Beginner</span>
5. [Load Balancing: L4 vs L7?](#q5) <span class="intermediate">Intermediate</span>
6. [SQL vs NoSQL?](#q6) <span class="beginner">Beginner</span>
7. [What is Consistent Hashing?](#q7) <span class="advanced">Advanced</span>
8. [Design a Key-Value Store (Redis)?](#q8) <span class="advanced">Advanced</span>
9. [What is a CDN?](#q9) <span class="beginner">Beginner</span>
10. [Design a Notification System?](#q10) <span class="intermediate">Intermediate</span>
11. [Sharding vs Replication?](#q11) <span class="intermediate">Intermediate</span>
12. [Design Instagram News Feed?](#q12) <span class="advanced">Advanced</span>
13. [What is a Bloom Filter?](#q13) <span class="advanced">Advanced</span>
14. [Microservices vs Monolith?](#q14) <span class="beginner">Beginner</span>
15. [Design a Web Crawler?](#q15) <span class="advanced">Advanced</span>
16. [Thundering Herd Problem?](#q16) <span class="advanced">Advanced</span>
17. [Design Google Drive (File Sync)?](#q17) <span class="advanced">Advanced</span>
18. [What is Backpressure?](#q18) <span class="advanced">Advanced</span>
19. [Design Typeahead (Autocomplete)?](#q19) <span class="intermediate">Intermediate</span>
20. [ACID Transactions?](#q20) <span class="beginner">Beginner</span>
21. [Design YouTube (Video Streaming)?](#q21) <span class="advanced">Advanced</span>
22. [Design Uber (Ride Sharing)?](#q22) <span class="advanced">Advanced</span>
23. [What is Database Normalization?](#q23) <span class="beginner">Beginner</span>
24. [Explain Two-Phase Commit (2PC)?](#q24) <span class="advanced">Advanced</span>
25. [Saga Pattern for Distributed Tx?](#q25) <span class="advanced">Advanced</span>
26. [Circuit Breaker Pattern?](#q26) <span class="intermediate">Intermediate</span>
27. [API Gateway vs Load Balancer?](#q27) <span class="intermediate">Intermediate</span>
28. [Polling vs WebSockets vs SSE?](#q28) <span class="intermediate">Intermediate</span>
29. [Design Twitter (Timeline)?](#q29) <span class="advanced">Advanced</span>
30. [Design Ticketmaster (Booking)?](#q30) <span class="advanced">Advanced</span>
31. [Strong vs Eventual Consistency?](#q31) <span class="intermediate">Intermediate</span>
32. [What is a Reverse Proxy?](#q32) <span class="beginner">Beginner</span>
33. [Service Discovery?](#q33) <span class="intermediate">Intermediate</span>
34. [Blue-Green vs Canary Deployment?](#q34) <span class="intermediate">Intermediate</span>
35. [What is a Distributed Lock?](#q35) <span class="advanced">Advanced</span>
36. [Design a Leaderboard?](#q36) <span class="intermediate">Intermediate</span>
37. [Design a Unique ID Generator?](#q37) <span class="intermediate">Intermediate</span>
38. [What is Gossip Protocol?](#q38) <span class="advanced">Advanced</span>
39. [Heartbeat Mechanism?](#q39) <span class="beginner">Beginner</span>
40. [Quorum in Distributed Systems?](#q40) <span class="advanced">Advanced</span>
41. [Write-Through vs Write-Back Cache?](#q41) <span class="intermediate">Intermediate</span>
42. [What is Database Indexing?](#q42) <span class="beginner">Beginner</span>
43. [Row-Oriented vs Column-Oriented DB?](#q43) <span class="intermediate">Intermediate</span>
44. [Design Netflix (Recommendations)?](#q44) <span class="advanced">Advanced</span>
45. [What is DNS?](#q45) <span class="beginner">Beginner</span>
46. [Anycast vs Unicast?](#q46) <span class="advanced">Advanced</span>
47. [What is a Sidecar Pattern?](#q47) <span class="intermediate">Intermediate</span>
48. [Design an API Rate Limiter?](#q48) <span class="intermediate">Intermediate</span>
49. [What is OAuth 2.0?](#q49) <span class="intermediate">Intermediate</span>
50. [JWT vs Session Cookies?](#q50) <span class="intermediate">Intermediate</span>
51. [What is gRPC?](#q51) <span class="intermediate">Intermediate</span>
52. [GraphQL vs REST?](#q52) <span class="beginner">Beginner</span>
53. [Design Dropbox (Deduplication)?](#q53) <span class="advanced">Advanced</span>
54. [Vector Clocks?](#q54) <span class="advanced">Advanced</span>
55. [Conflict Resolution Strategies?](#q55) <span class="advanced">Advanced</span>
56. [Design Nearby Friends (Location)?](#q56) <span class="advanced">Advanced</span>
57. [What is Geohashing?](#q57) <span class="intermediate">Intermediate</span>
58. [Design a Metrics Monitoring System?](#q58) <span class="advanced">Advanced</span>
59. [Pull vs Push Model?](#q59) <span class="intermediate">Intermediate</span>
60. [Batch Processing vs Stream Processing?](#q60) <span class="intermediate">Intermediate</span>
61. [Lambda Architecture?](#q61) <span class="advanced">Advanced</span>
62. [Kappa Architecture?](#q62) <span class="advanced">Advanced</span>
63. [What is MapReduce?](#q63) <span class="intermediate">Intermediate</span>
64. [Design a Payment System?](#q64) <span class="advanced">Advanced</span>
65. [Idempotency in APIs?](#q65) <span class="intermediate">Intermediate</span>
66. [What is a Dead Letter Queue?](#q66) <span class="intermediate">Intermediate</span>
67. [Vertical vs Horizontal Scaling?](#q67) <span class="beginner">Beginner</span>
68. [What is a Stateless Architecture?](#q68) <span class="beginner">Beginner</span>
69. [Design Distributed Job Scheduler?](#q69) <span class="advanced">Advanced</span>
70. [Paxos vs Raft Consensus?](#q70) <span class="advanced">Advanced</span>
71. [What is a Merkle Tree?](#q71) <span class="advanced">Advanced</span>
72. [Design a URL Shortener (DB Schema)?](#q72) <span class="intermediate">Intermediate</span>
73. [How HTTPS works?](#q73) <span class="intermediate">Intermediate</span>
74. [What is a WAF (Web App Firewall)?](#q74) <span class="intermediate">Intermediate</span>
75. [Design a Parking Garage?](#q75) <span class="beginner">Beginner</span>
76. [What is a Message Broker?](#q76) <span class="beginner">Beginner</span>
77. [Kafka vs RabbitMQ?](#q77) <span class="intermediate">Intermediate</span>
78. [Database Isolation Levels?](#q78) <span class="advanced">Advanced</span>
79. [Optimistic vs Pessimistic Locking?](#q79) <span class="intermediate">Intermediate</span>
80. [Design Amazon Cart?](#q80) <span class="advanced">Advanced</span>
81. [What is PACELC Theorem?](#q81) <span class="advanced">Advanced</span>
82. [Design a Flash Sale System?](#q82) <span class="advanced">Advanced</span>
83. [What is Content-Based Routing?](#q83) <span class="intermediate">Intermediate</span>
84. [Peer-to-Peer Networks?](#q84) <span class="intermediate">Intermediate</span>
85. [Design Google Maps?](#q85) <span class="advanced">Advanced</span>
86. [What is Edge Computing?](#q86) <span class="intermediate">Intermediate</span>
87. [Serverless Architecture?](#q87) <span class="intermediate">Intermediate</span>
88. [Design a Collaborative Editor (Google Docs)?](#q88) <span class="advanced">Advanced</span>
89. [Operational Transformation (OT)?](#q89) <span class="advanced">Advanced</span>
90. [CRDTs (Conflict-free Replicated Data Types)?](#q90) <span class="advanced">Advanced</span>
91. [Design Tinder (Matching)?](#q91) <span class="advanced">Advanced</span>
92. [Design a Search Engine?](#q92) <span class="advanced">Advanced</span>
93. [What is WebRTC?](#q93) <span class="intermediate">Intermediate</span>
94. [Design a Distributed Counter?](#q94) <span class="intermediate">Intermediate</span>
95. [What is a Split-Brain problem?](#q95) <span class="advanced">Advanced</span>
96. [Design a Logging System?](#q96) <span class="intermediate">Intermediate</span>
97. [What is Structured Logging?](#q97) <span class="beginner">Beginner</span>
98. [Distributed Tracing (Jaeger/Zipkin)?](#q98) <span class="intermediate">Intermediate</span>
99. [Chaos Engineering?](#q99) <span class="advanced">Advanced</span>
100. [Design Facebook Messenger?](#q100) <span class="advanced">Advanced</span>

---

<a id="q1"></a>
### Q1: Design a URL Shortener (TinyURL)?

**Difficulty**: Intermediate

**Strategy**:
**Requirements:** 
*   Functional: Given a long URL, return a unique short URL. Redirect short URL to long URL.
*   Non-Functional: Highly available, low latency, read-heavy (100:1 ratio).

**High-Level Design:**
1.  **API Server:** Handles `create(long_url)` and `get(short_url)`.
2.  **Database:** A NoSQL Key-Value store (like DynamoDB or Cassandra) is ideal for scalability.
    *   Schema: `{ short_key: "abc12", long_url: "...", creation_date: ... }`
3.  **ID Generation:** The core challenge.
    *   **Counter Approach:** Use a distributed counter (Zookeeper/Redis) to get a unique integer ID, then base62 encode it. 
    *   **Key Generation Service (KGS):** Pre-generate keys offline and store them in a database. The API server fetches a unused key. This removes the encoding latency and collision checks.
4.  **Caching:** Use Redis (LRU eviction) to cache popular redirections (20% of URLs generate 80% of traffic).


**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q2"></a>
### Q2: Design a Rate Limiter?

**Difficulty**: Intermediate

**Strategy**:
**Goal:** Restrict the number of requests a user can send within a time window (e.g., 10 requests/sec).

**Algorithms:**
1.  **Token Bucket:** A bucket holds tokens. Tokens are added at a fixed rate. Requests consume tokens. If bucket is empty, request is dropped. Memory efficient.
2.  **Leaky Bucket:** Requests enter a queue processed at a fixed rate. Good for smoothing traffic bursts.
3.  **Fixed Window Counter:** Count requests in `12:00-12:01`. Issue: Traffic spike at edges (double limit).
4.  **Sliding Window Log:** Store timestamps of requests. Precise but expensive (memory).
5.  **Sliding Window Counter:** Hybrid approach. Weighted count of previous window + current window.

**Architecture:**
*   Store counters in **Redis** (fast, supports atomic `INCR`).
*   Rate Limiter can be a Middleware or a separate Service (Sidecar).


**Code Example**:
```python
# Conceptual
bucket_size = 10
refill_rate = 1 # per second
current_tokens = 10
last_refill_timestamp = now()

def allow_request(tokens_needed=1):
refill()
if current_tokens >= tokens_needed:
current_tokens -= tokens_needed
return True
return False
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q3"></a>
### Q3: Design a Chat Application (WhatsApp)?

**Difficulty**: Advanced

**Strategy**:
**Requirements:** One-on-one chat, Group chat, Online status, Sent/Delivered/Read receipts.

**Architecture:**
1.  **Connection:** Use **WebSockets** for persistent bi-directional connection.
2.  **Message Flow:** User A -> Load Balancer -> Chat Server -> Message Queue -> User B.
3.  **Storage:**
    *   **Chat History:** Write-heavy. Use **Cassandra** or **HBase** (LSM-tree based) for efficient writes and range queries (fetch recent messages).
    *   **User Profile:** Relational DB (MySQL).
4.  **Online Status:** Use **Redis** with Heartbeats. If no heartbeat for x seconds, mark offline.
5.  **Group Chat:** Fan-out on write (for small groups) or Fan-out on read (for mega groups).


**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q4"></a>
### Q4: Explain CAP Theorem?

**Difficulty**: Beginner

**Strategy**:
The CAP theorem states that a distributed data store can only guarantee two of the following three properties simultaneously:

1.  **Consistency (C):** Every read receives the most recent write or an error. All nodes see the same data at the same time.
2.  **Availability (A):** Every request receives a (non-error) response, without the guarantee that it contains the most recent write.
3.  **Partition Tolerance (P):** The system continues to operate despite an arbitrary number of messages being dropped or delayed by the network between nodes.

**Choice:**
*   Since network partitions (P) are inevitable in distributed systems, you must choose between **CP** (Consistency) and **AP** (Availability).
*   **CP (e.g., MongoDB, HBase):** Returns error/timeout if data might be inconsistent.
*   **AP (e.g., Cassandra, DynamoDB):** Returns potentially stale data but always responds.


**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q5"></a>
### Q5: Load Balancing: L4 vs L7?

**Difficulty**: Intermediate

**Strategy**:
**Layer 4 (Transport Layer):**
*   Decisions based on IP address and TCP port.
*   Packet-level load balancing.
*   **Pros:** Very fast, low overhead, efficient.
*   **Cons:** Can't inspect content (can't route based on URL path).

**Layer 7 (Application Layer):**
*   Decisions based on HTTP headers, URLs, cookies, or message content.
*   **Pros:** Smarter routing (e.g., `/video` to VideoService, `/chat` to ChatService). Can terminate SSL.
*   **Cons:** More CPU intensive, slower than L4 (needs to decrypt/buffer).


**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q6"></a>
### Q6: SQL vs NoSQL?

**Difficulty**: Beginner

**Strategy**:
**SQL (Relational):**
*   **Structure:** Table-based, predefined schema.
*   **Properties:** ACID compliance (Atomicity, Consistency, Isolation, Durability). Strong consistency.
*   **Scaling:** Vertical (add more CPU/RAM). Harder to scale horizontally (Sharding is complex).
*   **Use Case:** Financial systems, complex relationships, strict data integrity.

**NoSQL (Non-Relational):**
*   **Structure:** Document (JSON), Key-Value, Wide-Column, or Graph. Dynamic schema.
*   **Properties:** BASE (Basically Available, Soft state, Eventual consistency).
*   **Scaling:** Horizontal (add more cheap servers). Built for scale.
*   **Use Case:** Big Data, Real-time analytics, Content management, Social networks.


**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q7"></a>
### Q7: What is Consistent Hashing?

**Difficulty**: Advanced

**Strategy**:
In standard hashing (`key % N`), adding/removing a server (N changes) remaps nearly ALL keys, causing massive cache misses.

**Consistent Hashing** maps both servers and keys to a circular ring (0 to 2^32-1).
*   A key is assigned to the first server encountered moving clockwise on the ring.
*   **Benefit:** Adding/removing a node only affects `K/N` keys (neighbors), not all keys.
*   **Virtual Nodes:** To balance load, each physical server maps to multiple points (virtual nodes) on the ring.


**Code Example**:
```text
Ring: 0 ... 2^32-1
Server A at Hash(A)
Server B at Hash(B)
Key K at Hash(K) -> Walk clockwise to find first Server.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q8"></a>
### Q8: Design a Key-Value Store (Redis)?

**Difficulty**: Advanced

**Strategy**:
**Core Features:**
*   **In-Memory:** Stores data in RAM for sub-millisecond access.
*   **Data Structures:** Supports Strings, Hashes, Lists, Sets, Sorted Sets.
*   **Single-Threaded:** Uses an Event Loop (I/O Multiplexing) to handle requests. No locking overhead, but CPU bound.

**Persistence:**
1.  **RDB (Snapshot):** Periodically saves dataset to disk. Faster startup, but data loss window.
2.  **AOF (Append Only File):** Logs every write operation. Slower replay, but higher durability.

**Scaling:**
*   **Replication:** Master-Slave (Async).
*   **Clustering:** Shards data across multiple nodes using CRC16 hashing.


**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q9"></a>
### Q9: What is a CDN?

**Difficulty**: Beginner

**Strategy**:
**Content Delivery Network (CDN):**
A geographically distributed network of proxy servers and data centers.

**How it works:**
1.  User requests `image.jpg`.
2.  DNS routes request to the nearest CDN Edge Server (PoP).
3.  If cached, Edge returns image (Hit).
4.  If not (Miss), Edge fetches from Origin Server, caches it, and returns it.

**Benefits:**
*   Reduced Latency (physically closer).
*   Reduced Bandwidth costs (offloads Origin).
*   DDoS Protection (absorbs traffic).


**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q10"></a>
### Q10: Design a Notification System?

**Difficulty**: Intermediate

**Strategy**:
**Requirements:**
*   Send notifications via Email, SMS, Push (iOS/Android).
*   Pluggable providers (SendGrid, Twilio, APNS, FCM).
*   Rate limiting (don't spam users).
*   Prioritization (OTP > Marketing).

**Architecture:**
1.  **Notification Service:** Accepts requests. Validates payload.
2.  **User Preferences DB:** Checks if user opted-out.
3.  **Message Queue (Kafka/RabbitMQ):** Decouples reception from processing. Topics: `sms_high`, `sms_low`, `email`.
4.  **Workers:** Pull from queue, call 3rd party APIs.
5.  **Retry Mechanism:** If Twilio fails, retry with exponential backoff.
6.  **Deduplication:** Use Redis to check if msg was already sent recently.


**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q11"></a>
### Q11: Sharding vs Replication?

**Difficulty**: Intermediate

**Strategy**:
**Replication:**
*   **What:** Copying data to multiple nodes.
*   **Why:** High Availability (failover), Read Scaling (distribute reads).
*   **Types:** Master-Slave (Async), Master-Master.
*   **Con:** Does not help with Write Scaling (Master is bottleneck).

**Sharding:**
*   **What:** Partitioning data across multiple nodes (e.g., UserID 1-1000 -> Node A, 1001-2000 -> Node B).
*   **Why:** Write Scaling (parallel writes), Storage Scaling (data exceeds single disk).
*   **Con:** Complex queries (joins across shards), Rebalancing data is hard.


**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q12"></a>
### Q12: Design Instagram News Feed?

**Difficulty**: Advanced

**Strategy**:
**Core Features:** User posts photos, follows others, sees feed of followed users. Read-heavy.

**Feed Generation (Fan-out):**
1.  **Pull Model (Fan-out-on-load):** When user loads feed, query all followees' recent posts and merge.
    *   Pros: Simple write.
    *   Cons: Slow read (N queries).
2.  **Push Model (Fan-out-on-write):** When user posts, push ID to all followers' pre-computed feed lists (Redis Lists).
    *   Pros: Fast read (O(1)).
    *   Cons: Slow write for celebs (Justin Bieber problem).
3.  **Hybrid:** Push for normal users, Pull for celebs.


**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q13"></a>
### Q13: What is a Bloom Filter?

**Difficulty**: Advanced

**Strategy**:
A probabilistic data structure used to test whether an element is a member of a set.
*   **Returns:** "Possibly in set" or "Definitely not in set".
*   **False Positives:** Possible.
*   **False Negatives:** Impossible.
*   **Use Case:** Checking if a username is taken (fast check before DB), reducing disk lookups in Cassandra/HBase.
*   **Mechanism:** Bit array + K hash functions.


**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q14"></a>
### Q14: Microservices vs Monolith?

**Difficulty**: Beginner

**Strategy**:
**Monolith:**
*   Single codebase, single deployment unit.
*   **Pros:** Simple to develop/test/deploy initially. Easy refactoring. ACID transactions.
*   **Cons:** Tight coupling, single point of failure, scales poorly (must scale whole app), tech stack lock-in.

**Microservices:**
*   Suite of small services, communicating via API.
*   **Pros:** Independent scaling/deployment, fault isolation, tech diversity, organizational alignment (Two-pizza teams).
*   **Cons:** Distributed system complexity (network latency, partial failures), eventual consistency, operational overhead (DevOps).


**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q15"></a>
### Q15: Design a Web Crawler?

**Difficulty**: Advanced

**Strategy**:
**Components:**
1.  **Seed URLs:** Starting point.
2.  **URL Frontier:** Priority Queue of URLs to visit (Kafka/Redis). Handles politeness (rate limit per domain).
3.  **DNS Resolver:** Cache IP addresses to avoid latency.
4.  **HTML Downloader:** Fetches page content.
5.  **Content Parser:** Extracts links and validation.
6.  **Dedup:** Bloom Filter or Checksum to avoid re-crawling same page.
7.  **Storage:** Save content to S3/HDFS.


**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q16"></a>
### Q16: Thundering Herd Problem?

**Difficulty**: Advanced

**Strategy**:
Occurs when a large number of processes waiting for an event are woken up at the same time.
*   **Example:** Cache expires. 10,000 requests hit the DB simultaneously to regenerate the cache.
*   **Impact:** DB CPU spikes, system crashes.
*   **Solution:**
    *   **Mutex:** Only one process computes the value.
    *   **Probabilistic Early Expiration:** Re-compute cache slightly before it actually expires.
    *   **Jitter:** Add random delay to retries.


**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q17"></a>
### Q17: Design Google Drive (File Sync)?

**Difficulty**: Advanced

**Strategy**:
**Key Challenges:** Large file uploads, sync across devices, consistency.

**Architecture:**
1.  **Block Storage:** Split files into blocks (e.g., 4MB). Only upload modified blocks (Differential Sync).
2.  **Metadata DB:** Stores file hierarchy, permissions, versions. (SQL).
3.  **Cold Storage:** S3/Glacier for actual blocks.
4.  **Notification Service:** Long polling/WebSockets to notify clients of changes.
5.  **Offline Support:** Local database on client, queue changes, sync when online.


**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q18"></a>
### Q18: What is Backpressure?

**Difficulty**: Advanced

**Strategy**:
Resistance or opposition to the flow of data. In reactive systems, it allows a consumer to signal to the producer that it is overwhelmed.
*   **Scenario:** Fast producer -> Slow consumer. Buffer fills up -> OOM.
*   **Strategies:**
    *   **Control:** Consumer requests N items (Reactive Streams).
    *   **Buffer:** Store temporarily (limited capacity).
    *   **Drop:** Discard new data (sampling).


**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q19"></a>
### Q19: Design Typeahead (Autocomplete)?

**Difficulty**: Intermediate

**Strategy**:
**Requirements:** Low latency (<100ms), Prefix matching, Sorted by popularity.

**Data Structure:** **Trie (Prefix Tree)**.
*   Each node stores top 5 popular search terms ending at that node.

**Architecture:**
1.  **Storage:** Serialize Trie to DB/File.
2.  **Memory:** Load Trie into RAM for speed.
3.  **Optimization:** Limit tree depth.
4.  **Update:** Async offline job (MapReduce) to rebuild Trie hourly based on logs.


**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q20"></a>
### Q20: ACID Transactions?

**Difficulty**: Beginner

**Strategy**:
Atomicity, Consistency, Isolation, Durability. Guarantees for relational databases.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q21"></a>
### Q21: Design YouTube (Video Streaming)?

**Difficulty**: Advanced

**Strategy**:
Upload -> Transcode (FFmpeg) to multiple formats/resolutions -> Store in S3 -> CDN. Metadata in SQL.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q22"></a>
### Q22: Design Uber (Ride Sharing)?

**Difficulty**: Advanced

**Strategy**:
**Geospatial Index:** Quadtree or Google S2. Matches riders with drivers in cells. Frequent location updates via WebSocket.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q23"></a>
### Q23: What is Database Normalization?

**Difficulty**: Beginner

**Strategy**:
Organizing data to reduce redundancy and improve integrity (1NF, 2NF, 3NF).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q24"></a>
### Q24: Explain Two-Phase Commit (2PC)?

**Difficulty**: Advanced

**Strategy**:
Distributed transaction protocol. 1. Prepare (Vote). 2. Commit/Abort. Blocking protocol.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q25"></a>
### Q25: Saga Pattern for Distributed Tx?

**Difficulty**: Advanced

**Strategy**:
Sequence of local transactions. If one fails, execute compensating transactions to undo changes.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q26"></a>
### Q26: Circuit Breaker Pattern?

**Difficulty**: Intermediate

**Strategy**:
Prevents cascading failures. If service fails repeatedly, "Open" circuit and fail fast for a timeout period.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q27"></a>
### Q27: API Gateway vs Load Balancer?

**Difficulty**: Intermediate

**Strategy**:
**Gateway:** Entry point. Auth, Rate Limiting, Routing, Aggregation.
**LB:** Distributes traffic to servers.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q28"></a>
### Q28: Polling vs WebSockets vs SSE?

**Difficulty**: Intermediate

**Strategy**:
**Polling:** Client asks repeatedly.
**WebSockets:** Bidirectional.
**SSE:** Server to Client (Unidirectional).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q29"></a>
### Q29: Design Twitter (Timeline)?

**Difficulty**: Advanced

**Strategy**:
Hybrid approach. Push to Redis lists for active users. Pull from DB for inactive/celebrity tweets.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q30"></a>
### Q30: Design Ticketmaster (Booking)?

**Difficulty**: Advanced

**Strategy**:
Consistency is key. Use SQL with locking (SELECT FOR UPDATE) or Redis Lua scripts to reserve seats.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q31"></a>
### Q31: Strong vs Eventual Consistency?

**Difficulty**: Intermediate

**Strategy**:
**Strong:** Reads see latest write (Latency hit).
**Eventual:** Reads may be stale, converges later (High Availability).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q32"></a>
### Q32: What is a Reverse Proxy?

**Difficulty**: Beginner

**Strategy**:
Server sitting in front of backends. Handles SSL termination, Caching, Load Balancing (Nginx, HAProxy).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q33"></a>
### Q33: Service Discovery?

**Difficulty**: Intermediate

**Strategy**:
Registry keeping track of dynamic IP:Ports of services (Consul, Eureka, ZooKeeper, K8s DNS).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q34"></a>
### Q34: Blue-Green vs Canary Deployment?

**Difficulty**: Intermediate

**Strategy**:
**Blue-Green:** Switch traffic 100% from old to new env.
**Canary:** Gradually roll out new version to % of users.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q35"></a>
### Q35: What is a Distributed Lock?

**Difficulty**: Advanced

**Strategy**:
Ensures mutual exclusion across processes/servers. Implementations: Redis (Redlock), ZooKeeper.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q36"></a>
### Q36: Design a Leaderboard?

**Difficulty**: Intermediate

**Strategy**:
Redis Sorted Sets (ZSET). `ZADD user score`, `ZREVRANGE 0 10`.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q37"></a>
### Q37: Design a Unique ID Generator?

**Difficulty**: Intermediate

**Strategy**:
**Twitter Snowflake:** 64-bit integer (Timestamp + MachineID + Sequence). Sortable by time.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q38"></a>
### Q38: What is Gossip Protocol?

**Difficulty**: Advanced

**Strategy**:
Peer-to-peer communication. Nodes randomly share info with neighbors. Used in Cassandra ring state.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q39"></a>
### Q39: Heartbeat Mechanism? <span class="beginner">Beginner</span></div>
<div class="answer">
  <p>Periodic signal to indicate a node is alive. If missed, assume failure.</p>
</div>

<div id="q40" class="question">40. Quorum in Distributed Systems?

**Difficulty**: Advanced

**Strategy**:
Minimum votes required to perform operation. R + W > N ensures strong consistency.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q41"></a>
### Q41: Write-Through vs Write-Back Cache?

**Difficulty**: Intermediate

**Strategy**:
**Through:** Write to Cache and DB synchronously (Safe).
**Back:** Write to Cache, async to DB (Fast, risk of data loss).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q42"></a>
### Q42: What is Database Indexing? <span class="beginner">Beginner</span></div>
<div class="answer">
  <p>Data structure (B-Tree) improving data retrieval speed at cost of write speed and storage.</p>
</div>

<div id="q43" class="question">43. Row-Oriented vs Column-Oriented DB?

**Difficulty**: Intermediate

**Strategy**:
**Row (Postgres):** Good for transactional (OLTP).
**Column (Cassandra/Redshift):** Good for analytics/aggregations (OLAP).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q44"></a>
### Q44: Design Netflix (Recommendations)?

**Difficulty**: Advanced

**Strategy**:
Collaborative Filtering + Content-based Filtering. Matrix Factorization. Pre-compute recommendations offline.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q45"></a>
### Q45: What is DNS? <span class="beginner">Beginner</span></div>
<div class="answer">
  <p>Domain Name System. Phonebook of internet. Translates `google.com` to IP address.</p>
</div>

<div id="q46" class="question">46. Anycast vs Unicast?

**Difficulty**: Advanced

**Strategy**:
**Unicast:** One-to-One.
**Anycast:** One-to-Nearest. Used by CDNs/DNS to route to closest server.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q47"></a>
### Q47: What is a Sidecar Pattern?

**Difficulty**: Intermediate

**Strategy**:
Helper container running alongside main container (e.g., Envoy Proxy in Service Mesh) to handle networking/logs.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q48"></a>
### Q48: Design an API Rate Limiter?

**Difficulty**: Intermediate

**Strategy**:
Middleware using Redis. Identify by API Key or IP. Return 429 Too Many Requests.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q49"></a>
### Q49: What is OAuth 2.0?

**Difficulty**: Intermediate

**Strategy**:
Authorization framework. Allows third-party apps to access user data without sharing passwords. (Access Tokens).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q50"></a>
### Q50: JWT vs Session Cookies?

**Difficulty**: Intermediate

**Strategy**:
**JWT:** Stateless, signed, contains claims. Good for APIs.
**Session:** Stateful, ID stored in cookie, data in server DB.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q51"></a>
### Q51: What is gRPC?

**Difficulty**: Intermediate

**Strategy**:
High-performance RPC framework by Google. Uses Protobuf (binary) and HTTP/2.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q52"></a>
### Q52: GraphQL vs REST? <span class="beginner">Beginner</span></div>
<div class="answer">
  <p><strong>REST:</strong> Multiple endpoints, over/under-fetching.<br><strong>GraphQL:</strong> Single endpoint, client asks exactly what it needs.</p>
</div>

<div id="q53" class="question">53. Design Dropbox (Deduplication)?

**Difficulty**: Advanced

**Strategy**:
Check hash of file chunks. If hash exists, point to existing chunk instead of uploading again.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q54"></a>
### Q54: Vector Clocks?

**Difficulty**: Advanced

**Strategy**:
Algorithm to detect causal ordering of events in distributed systems. Helps resolve conflicts (DynamoDB).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q55"></a>
### Q55: Conflict Resolution Strategies?

**Difficulty**: Advanced

**Strategy**:
Last Write Wins (LWW) or Semantic resolution (Merge shopping carts).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q56"></a>
### Q56: Design Nearby Friends (Location)?

**Difficulty**: Advanced

**Strategy**:
Ephemeral location data. Redis GeoSpatial commands. TTL on location entries.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q57"></a>
### Q57: What is Geohashing?

**Difficulty**: Intermediate

**Strategy**:
Encoding Lat/Long into string. Recursively dividing world into buckets.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q58"></a>
### Q58: Design a Metrics Monitoring System?

**Difficulty**: Advanced

**Strategy**:
Time-Series DB (Prometheus/InfluxDB). Pull vs Push metrics. Downsampling old data.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q59"></a>
### Q59: Pull vs Push Model?

**Difficulty**: Intermediate

**Strategy**:
**Pull:** Consumer requests data (Prometheus).
**Push:** Producer sends data (Graphite).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q60"></a>
### Q60: Batch Processing vs Stream Processing?

**Difficulty**: Intermediate

**Strategy**:
**Batch (Hadoop):** Large volume, high latency.
**Stream (Flink/Kafka):** Real-time, low latency.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q61"></a>
### Q61: Lambda Architecture?

**Difficulty**: Advanced

**Strategy**:
Hybrid. Batch Layer (Accurate, Slow) + Speed Layer (Approx, Fast). Query merges both.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q62"></a>
### Q62: Kappa Architecture?

**Difficulty**: Advanced

**Strategy**:
Stream only. Treat everything as a stream. Simplifies architecture.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q63"></a>
### Q63: What is MapReduce?

**Difficulty**: Intermediate

**Strategy**:
Programming model for processing big data. Map (Filter/Sort) -> Shuffle -> Reduce (Aggregate).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q64"></a>
### Q64: Design a Payment System?

**Difficulty**: Advanced

**Strategy**:
ACID DB mandatory. Idempotency keys to prevent double charge. Distributed Saga for orchestrating steps.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q65"></a>
### Q65: Idempotency in APIs?

**Difficulty**: Intermediate

**Strategy**:
Making multiple identical requests has same effect as single request. Crucial for payments.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q66"></a>
### Q66: What is a Dead Letter Queue?

**Difficulty**: Intermediate

**Strategy**:
Queue for messages that failed processing. Allows debugging and manual retry.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q67"></a>
### Q67: Vertical vs Horizontal Scaling? <span class="beginner">Beginner</span></div>
<div class="answer">
  <p><strong>Vertical:</strong> Bigger machine (CPU/RAM). Limit exists.<br><strong>Horizontal:</strong> More machines. Unlimited scaling.</p>
</div>

<div id="q68" class="question">68. What is a Stateless Architecture? <span class="beginner">Beginner</span></div>
<div class="answer">
  <p>Server keeps no session data. Any request can go to any server. Easier to scale.</p>
</div>

<div id="q69" class="question">69. Design Distributed Job Scheduler?

**Difficulty**: Advanced

**Strategy**:
Leader election (ZooKeeper). Workers pull tasks. Heartbeats. Redis for task status.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q70"></a>
### Q70: Paxos vs Raft Consensus?

**Difficulty**: Advanced

**Strategy**:
Algorithms for agreeing on values in distributed systems. Raft is designed to be more understandable than Paxos.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q71"></a>
### Q71: What is a Merkle Tree?

**Difficulty**: Advanced

**Strategy**:
Tree of hashes. Efficient synchronization (DynamoDB) and integrity check (Blockchain).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q72"></a>
### Q72: Design a URL Shortener (DB Schema)?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```sql
CREATE TABLE urls (
  short_key VARCHAR(7) PRIMARY KEY,
  original_url VARCHAR(255),
  created_at TIMESTAMP,
  user_id INT
);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q73"></a>
### Q73: How HTTPS works?

**Difficulty**: Intermediate

**Strategy**:
TLS Handshake. Asymmetric encryption to exchange symmetric key. Symmetric key for session data.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q74"></a>
### Q74: What is a WAF (Web App Firewall)?

**Difficulty**: Intermediate

**Strategy**:
Protects against SQL Injection, XSS, etc. filters incoming HTTP traffic.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q75"></a>
### Q75: Design a Parking Garage? <span class="beginner">Beginner</span></div>
<div class="answer">
  <p>OO Design. Classes: Vehicle, Spot, Level, Garage. Enums: Compact, Large. Strategy Pattern for pricing.</p>
</div>

<div id="q76" class="question">76. What is a Message Broker? <span class="beginner">Beginner</span></div>
<div class="answer">
  <p>Intermediary for messaging. Decouples sender and receiver (RabbitMQ, ActiveMQ).</p>
</div>

<div id="q77" class="question">77. Kafka vs RabbitMQ?

**Difficulty**: Intermediate

**Strategy**:
**Kafka:** Log-based, high throughput, replayable.
**RabbitMQ:** Queue-based, complex routing, ack/nack.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q78"></a>
### Q78: Database Isolation Levels?

**Difficulty**: Advanced

**Strategy**:
Read Uncommitted, Read Committed, Repeatable Read, Serializable. Trade-off between consistency and performance.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q79"></a>
### Q79: Optimistic vs Pessimistic Locking?

**Difficulty**: Intermediate

**Strategy**:
**Optimistic:** Version check on save. Good for low contention.
**Pessimistic:** Lock record on read. Good for high contention.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q80"></a>
### Q80: Design Amazon Cart?

**Difficulty**: Advanced

**Strategy**:
DynamoDB (Key-Value). Cart items persisted. Merge local cart after login. Availability over Consistency.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q81"></a>
### Q81: What is PACELC Theorem?

**Difficulty**: Advanced

**Strategy**:
Extension of CAP. If Partition (P), choose A or C. Else (E), choose Latency (L) or Consistency (C).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q82"></a>
### Q82: Design a Flash Sale System?

**Difficulty**: Advanced

**Strategy**:
Redis counters for inventory. Queue to throttle DB writes. Static content on CDN.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q83"></a>
### Q83: What is Content-Based Routing?

**Difficulty**: Intermediate

**Strategy**:
Routing requests to different microservices based on request content (headers/body).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q84"></a>
### Q84: Peer-to-Peer Networks?

**Difficulty**: Intermediate

**Strategy**:
No central server. Peers connect directly (BitTorrent). Resilient but hard to manage.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q85"></a>
### Q85: Design Google Maps?

**Difficulty**: Advanced

**Strategy**:
Graph for routing (Dijkstra/A*). Tiled images for rendering (Quadtree/Zoom levels).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q86"></a>
### Q86: What is Edge Computing?

**Difficulty**: Intermediate

**Strategy**:
Processing data near the source (IoT devices) rather than sending to centralized cloud.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q87"></a>
### Q87: Serverless Architecture?

**Difficulty**: Intermediate

**Strategy**:
FaaS (Lambda). No server management. Scale to zero. Pay per execution.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q88"></a>
### Q88: Design a Collaborative Editor (Google Docs)?

**Difficulty**: Advanced

**Strategy**:
Operational Transformation (OT) or CRDTs to handle concurrent edits without locking.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q89"></a>
### Q89: Operational Transformation (OT)?

**Difficulty**: Advanced

**Strategy**:
Algorithm to transform operations (insert/delete) based on other concurrent operations.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q90"></a>
### Q90: CRDTs (Conflict-free Replicated Data Types)?

**Difficulty**: Advanced

**Strategy**:
Data structures that can be updated independently and merged without conflicts.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q91"></a>
### Q91: Design Tinder (Matching)?

**Difficulty**: Advanced

**Strategy**:
Geospatial query. "Swipes" are heavy writes. Redis for active users. Async processing for matches.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q92"></a>
### Q92: Design a Search Engine?

**Difficulty**: Advanced

**Strategy**:
Crawler -> Indexer (Inverted Index) -> Searcher (Ranking/TF-IDF/PageRank).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q93"></a>
### Q93: What is WebRTC?

**Difficulty**: Intermediate

**Strategy**:
Peer-to-Peer audio/video. Uses UDP. Signaling server needed for handshake.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q94"></a>
### Q94: Design a Distributed Counter?

**Difficulty**: Intermediate

**Strategy**:
Sharded counters. Sum all shards for total. Reduces write contention.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q95"></a>
### Q95: What is a Split-Brain problem?

**Difficulty**: Advanced

**Strategy**:
Cluster splits into two, both thinking they are the master. Leads to data corruption. Fix: Quorum.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q96"></a>
### Q96: Design a Logging System?

**Difficulty**: Intermediate

**Strategy**:
Filebeat (Agent) -> Kafka (Buffer) -> Logstash (Parse) -> Elasticsearch (Index) -> Kibana (UI).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q97"></a>
### Q97: What is Structured Logging? <span class="beginner">Beginner</span></div>
<div class="answer">
  <p>Logging in JSON format (key-value) instead of plain text. Easier to query.</p>
</div>

<div id="q98" class="question">98. Distributed Tracing (Jaeger/Zipkin)?

**Difficulty**: Intermediate

**Strategy**:
Tracking a request across microservices using a Trace ID and Span IDs.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q99"></a>
### Q99: Chaos Engineering?

**Difficulty**: Advanced

**Strategy**:
Intentionally introducing faults (latency, crash) to test system resilience (Netflix Chaos Monkey).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q100"></a>
### Q100: Design Facebook Messenger?

**Difficulty**: Advanced

**Strategy**:
One-on-one vs Group. HBase for message storage. Push notifications for offline users.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---
