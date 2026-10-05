<div align="center">
  <a href="#" target="_blank">
    <img src="../../assets/icons/interview_guide_logo.png" alt="Interview Guide Logo" width="100" height="100">
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
48. [What is OAuth 2.0?](#q48) <span class="intermediate">Intermediate</span>
49. [JWT vs Session Cookies?](#q49) <span class="intermediate">Intermediate</span>
50. [What is gRPC?](#q50) <span class="intermediate">Intermediate</span>
51. [GraphQL vs REST?](#q51) <span class="beginner">Beginner</span>
52. [Design Dropbox (Deduplication)?](#q52) <span class="advanced">Advanced</span>
53. [Vector Clocks?](#q53) <span class="advanced">Advanced</span>
54. [Conflict Resolution Strategies?](#q54) <span class="advanced">Advanced</span>
55. [Design Nearby Friends (Location)?](#q55) <span class="advanced">Advanced</span>
56. [What is Geohashing?](#q56) <span class="intermediate">Intermediate</span>
57. [Design a Metrics Monitoring System?](#q57) <span class="advanced">Advanced</span>
58. [Pull vs Push Model?](#q58) <span class="intermediate">Intermediate</span>
59. [Batch Processing vs Stream Processing?](#q59) <span class="intermediate">Intermediate</span>
60. [Lambda Architecture?](#q60) <span class="advanced">Advanced</span>
61. [Kappa Architecture?](#q61) <span class="advanced">Advanced</span>
62. [What is MapReduce?](#q62) <span class="intermediate">Intermediate</span>
63. [Design a Payment System?](#q63) <span class="advanced">Advanced</span>
64. [Idempotency in APIs?](#q64) <span class="intermediate">Intermediate</span>
65. [What is a Dead Letter Queue?](#q65) <span class="intermediate">Intermediate</span>
66. [Vertical vs Horizontal Scaling?](#q66) <span class="beginner">Beginner</span>
67. [What is a Stateless Architecture?](#q67) <span class="beginner">Beginner</span>
68. [Design Distributed Job Scheduler?](#q68) <span class="advanced">Advanced</span>
69. [Paxos vs Raft Consensus?](#q69) <span class="advanced">Advanced</span>
70. [What is a Merkle Tree?](#q70) <span class="advanced">Advanced</span>
71. [How HTTPS works?](#q71) <span class="intermediate">Intermediate</span>
72. [What is a WAF (Web App Firewall)?](#q72) <span class="intermediate">Intermediate</span>
73. [Design a Parking Garage?](#q73) <span class="beginner">Beginner</span>
74. [What is a Message Broker?](#q74) <span class="beginner">Beginner</span>
75. [Kafka vs RabbitMQ?](#q75) <span class="intermediate">Intermediate</span>
76. [Database Isolation Levels?](#q76) <span class="advanced">Advanced</span>
77. [Optimistic vs Pessimistic Locking?](#q77) <span class="intermediate">Intermediate</span>
78. [Design Amazon Cart?](#q78) <span class="advanced">Advanced</span>
79. [What is PACELC Theorem?](#q79) <span class="advanced">Advanced</span>
80. [Design a Flash Sale System?](#q80) <span class="advanced">Advanced</span>
81. [What is Content-Based Routing?](#q81) <span class="intermediate">Intermediate</span>
82. [Peer-to-Peer Networks?](#q82) <span class="intermediate">Intermediate</span>
83. [Design Google Maps?](#q83) <span class="advanced">Advanced</span>
84. [What is Edge Computing?](#q84) <span class="intermediate">Intermediate</span>
85. [Serverless Architecture?](#q85) <span class="intermediate">Intermediate</span>
86. [Design a Collaborative Editor (Google Docs)?](#q86) <span class="advanced">Advanced</span>
87. [Operational Transformation (OT)?](#q87) <span class="advanced">Advanced</span>
88. [CRDTs (Conflict-free Replicated Data Types)?](#q88) <span class="advanced">Advanced</span>
89. [Design Tinder (Matching)?](#q89) <span class="advanced">Advanced</span>
90. [Design a Search Engine?](#q90) <span class="advanced">Advanced</span>
91. [What is WebRTC?](#q91) <span class="intermediate">Intermediate</span>
92. [Design a Distributed Counter?](#q92) <span class="intermediate">Intermediate</span>
93. [What is a Split-Brain problem?](#q93) <span class="advanced">Advanced</span>
94. [Design a Logging System?](#q94) <span class="intermediate">Intermediate</span>
95. [What is Structured Logging?](#q95) <span class="beginner">Beginner</span>
96. [Distributed Tracing (Jaeger/Zipkin)?](#q96) <span class="intermediate">Intermediate</span>
97. [Chaos Engineering?](#q97) <span class="advanced">Advanced</span>
98. [Design Facebook Messenger?](#q98) <span class="advanced">Advanced</span>
99. [Design an Elevator System?](#q99) <span class="intermediate">Intermediate</span>
100. [Design a Hotel Booking System?](#q100) <span class="advanced">Advanced</span>
101. [Design an Airline Reservation System?](#q101) <span class="advanced">Advanced</span>
102. [Design a Distributed Job Scheduler?](#q102) <span class="advanced">Advanced</span>
103. [Design a Distributed Log Aggregator (ELK)?](#q103) <span class="advanced">Advanced</span>
104. [Design a Geo-Fencing System?](#q104) <span class="advanced">Advanced</span>
105. [Design a Collaborative Document Editor (Google Docs)?](#q105) <span class="advanced">Advanced</span>
106. [Design Amazon (E-commerce)?](#q106) <span class="advanced">Advanced</span>
107. [Design Netflix (Video on Demand)?](#q107) <span class="advanced">Advanced</span>
108. [Design a Food Delivery App (DoorDash)?](#q108) <span class="advanced">Advanced</span>
109. [Design a Recommendation System?](#q109) <span class="advanced">Advanced</span>
110. [Design a Dating App (Tinder)?](#q110) <span class="advanced">Advanced</span>
111. [Design a News Aggregator?](#q111) <span class="intermediate">Intermediate</span>
112. [Design a Distributed Cache?](#q112) <span class="advanced">Advanced</span>
113. [Design a URL Image Store?](#q113) <span class="intermediate">Intermediate</span>
114. [What is Database Sharding?](#q114) <span class="advanced">Advanced</span>
115. [What is Database Replication?](#q115) <span class="intermediate">Intermediate</span>
116. [What is Checksum?](#q116) <span class="beginner">Beginner</span>
117. [What is a CDN Edge Server?](#q117) <span class="beginner">Beginner</span>
118. [What is a Service Mesh?](#q118) <span class="intermediate">Intermediate</span>
119. [What is the Bulkhead Pattern?](#q119) <span class="advanced">Advanced</span>
120. [What is a Count-Min Sketch?](#q120) <span class="expert">Expert</span>
121. [Quadtree vs. Geohash for Location Search?](#q121) <span class="advanced">Advanced</span>
122. [Token Bucket vs. Leaky Bucket?](#q122) <span class="advanced">Advanced</span>
123. [LSM Tree vs. B-Tree?](#q123) <span class="expert">Expert</span>
124. [What is Write Amplification?](#q124) <span class="expert">Expert</span>
125. [Read Repair vs. Anti-Entropy?](#q125) <span class="advanced">Advanced</span>
126. [What is Split Brain?](#q126) <span class="intermediate">Intermediate</span>
127. [Cache Avalanche vs. Cache Penetration?](#q127) <span class="advanced">Advanced</span>
128. [How to handle Hot Partitions (Data Skew)?](#q128) <span class="advanced">Advanced</span>
129. [Lambda vs. Kappa Architecture?](#q129) <span class="expert">Expert</span>
130. [What is Event Sourcing?](#q130) <span class="advanced">Advanced</span>
131. [What is CQRS?](#q131) <span class="advanced">Advanced</span>
132. [Three-Phase Commit (3PC)?](#q132) <span class="expert">Expert</span>

---

<a id="q1"></a>
### Q1: Design a URL Shortener (TinyURL)?

**Difficulty**: Intermediate

**Strategy**:
**Requirements:** 
*   Functional: Given a long URL, return a unique short URL. Redirect short URL to long URL.
*   Non-Functional: Highly available, low latency, read-heavy (100:1 ratio).

---

<a id="q2"></a>
### Q2: Design a Rate Limiter?

**Difficulty**: Intermediate

**Strategy**:
**Goal:** Restrict the number of requests a user can send within a time window (e.g., 10 requests/sec).

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

---

<a id="q3"></a>
### Q3: Design a Chat Application (WhatsApp)?

**Difficulty**: Advanced

**Strategy**:
**Requirements:** One-on-one chat, Group chat, Online status, Sent/Delivered/Read receipts.

---

<a id="q4"></a>
### Q4: Explain CAP Theorem?

**Difficulty**: Beginner

**Strategy**:
The CAP theorem states that a distributed data store can only guarantee two of the following three properties simultaneously:

1.  **Consistency (C):** Every read receives the most recent write or an error. All nodes see the same data at the same time.
2.  **Availability (A):** Every request receives a (non-error) response, without the guarantee that it contains the most recent write.
3.  **Partition Tolerance (P):** The system continues to operate despite an arbitrary number of messages being dropped or delayed by the network between nodes.

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

---

<a id="q7"></a>
### Q7: What is Consistent Hashing?

**Difficulty**: Advanced

**Strategy**:
In standard hashing (`key % N`), adding/removing a server (N changes) remaps nearly ALL keys, causing massive cache misses.

**Code Example**:
```text
Ring: 0 ... 2^32-1
Server A at Hash(A)
Server B at Hash(B)
Key K at Hash(K) -> Walk clockwise to find first Server.
```

---

<a id="q8"></a>
### Q8: Design a Key-Value Store (Redis)?

**Difficulty**: Advanced

**Strategy**:
**Core Features:**
*   **In-Memory:** Stores data in RAM for sub-millisecond access.
*   **Data Structures:** Supports Strings, Hashes, Lists, Sets, Sorted Sets.
*   **Single-Threaded:** Uses an Event Loop (I/O Multiplexing) to handle requests. No locking overhead, but CPU bound.

---

<a id="q9"></a>
### Q9: What is a CDN?

**Difficulty**: Beginner

**Strategy**:
**Content Delivery Network (CDN):**
A geographically distributed network of proxy servers and data centers.

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

---

<a id="q12"></a>
### Q12: Design Instagram News Feed?

**Difficulty**: Advanced

**Strategy**:
**Core Features:** User posts photos, follows others, sees feed of followed users. Read-heavy.

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

---

<a id="q14"></a>
### Q14: Microservices vs Monolith?

**Difficulty**: Beginner

**Strategy**:
**Monolith:**
*   Single codebase, single deployment unit.
*   **Pros:** Simple to develop/test/deploy initially. Easy refactoring. ACID transactions.
*   **Cons:** Tight coupling, single point of failure, scales poorly (must scale whole app), tech stack lock-in.

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

---

<a id="q17"></a>
### Q17: Design Google Drive (File Sync)?

**Difficulty**: Advanced

**Strategy**:
**Key Challenges:** Large file uploads, sync across devices, consistency.

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

---

<a id="q19"></a>
### Q19: Design Typeahead (Autocomplete)?

**Difficulty**: Intermediate

**Strategy**:
**Requirements:** Low latency (<100ms), Prefix matching, Sorted by popularity.

---

<a id="q20"></a>
### Q20: ACID Transactions?

**Difficulty**: Beginner

**Strategy**:
Atomicity, Consistency, Isolation, Durability. Guarantees for relational databases.

---

<a id="q21"></a>
### Q21: Design YouTube (Video Streaming)?

**Difficulty**: Advanced

**Strategy**:
Upload -> Transcode (FFmpeg) to multiple formats/resolutions -> Store in S3 -> CDN. Metadata in SQL.

---

<a id="q22"></a>
### Q22: Design Uber (Ride Sharing)?

**Difficulty**: Advanced

**Strategy**:
**Geospatial Index:** Quadtree or Google S2. Matches riders with drivers in cells. Frequent location updates via WebSocket.

---

<a id="q23"></a>
### Q23: What is Database Normalization?

**Difficulty**: Beginner

**Strategy**:
Organizing data to reduce redundancy and improve integrity (1NF, 2NF, 3NF).

---

<a id="q24"></a>
### Q24: Explain Two-Phase Commit (2PC)?

**Difficulty**: Advanced

**Strategy**:
Distributed transaction protocol. 1. Prepare (Vote). 2. Commit/Abort. Blocking protocol.

---

<a id="q25"></a>
### Q25: Saga Pattern for Distributed Tx?

**Difficulty**: Advanced

**Strategy**:
Sequence of local transactions. If one fails, execute compensating transactions to undo changes.

---

<a id="q26"></a>
### Q26: Circuit Breaker Pattern?

**Difficulty**: Intermediate

**Strategy**:
Prevents cascading failures. If service fails repeatedly, "Open" circuit and fail fast for a timeout period.

---

<a id="q27"></a>
### Q27: API Gateway vs Load Balancer?

**Difficulty**: Intermediate

**Strategy**:
**Gateway:** Entry point. Auth, Rate Limiting, Routing, Aggregation.
**LB:** Distributes traffic to servers.

---

<a id="q28"></a>
### Q28: Polling vs WebSockets vs SSE?

**Difficulty**: Intermediate

**Strategy**:
**Polling:** Client asks repeatedly.
**WebSockets:** Bidirectional.
**SSE:** Server to Client (Unidirectional).

---

<a id="q29"></a>
### Q29: Design Twitter (Timeline)?

**Difficulty**: Advanced

**Strategy**:
Hybrid approach. Push to Redis lists for active users. Pull from DB for inactive/celebrity tweets.

---

<a id="q30"></a>
### Q30: Design Ticketmaster (Booking)?

**Difficulty**: Advanced

**Strategy**:
Consistency is key. Use SQL with locking (SELECT FOR UPDATE) or Redis Lua scripts to reserve seats.

---

<a id="q31"></a>
### Q31: Strong vs Eventual Consistency?

**Difficulty**: Intermediate

**Strategy**:
**Strong:** Reads see latest write (Latency hit).
**Eventual:** Reads may be stale, converges later (High Availability).

---

<a id="q32"></a>
### Q32: What is a Reverse Proxy?

**Difficulty**: Beginner

**Strategy**:
Server sitting in front of backends. Handles SSL termination, Caching, Load Balancing (Nginx, HAProxy).

---

<a id="q33"></a>
### Q33: Service Discovery?

**Difficulty**: Intermediate

**Strategy**:
Registry keeping track of dynamic IP:Ports of services (Consul, Eureka, ZooKeeper, K8s DNS).

---

<a id="q34"></a>
### Q34: Blue-Green vs Canary Deployment?

**Difficulty**: Intermediate

**Strategy**:
**Blue-Green:** Switch traffic 100% from old to new env.
**Canary:** Gradually roll out new version to % of users.

---

<a id="q35"></a>
### Q35: What is a Distributed Lock?

**Difficulty**: Advanced

**Strategy**:
Ensures mutual exclusion across processes/servers. Implementations: Redis (Redlock), ZooKeeper.

---

<a id="q36"></a>
### Q36: Design a Leaderboard?

**Difficulty**: Intermediate

**Strategy**:
Redis Sorted Sets (ZSET). `ZADD user score`, `ZREVRANGE 0 10`.

---

<a id="q37"></a>
### Q37: Design a Unique ID Generator?

**Difficulty**: Intermediate

**Strategy**:
**Twitter Snowflake:** 64-bit integer (Timestamp + MachineID + Sequence). Sortable by time.

---

<a id="q38"></a>
### Q38: What is Gossip Protocol?

**Difficulty**: Advanced

**Strategy**:
Peer-to-peer communication. Nodes randomly share info with neighbors. Used in Cassandra ring state.

---

<a id="q39"></a>
### Q39: Heartbeat Mechanism?

**Difficulty**: Beginner

**Strategy**:
Periodic signal to indicate a node is alive. If missed, assume failure.

---

<a id="q40"></a>
### Q40: Quorum in Distributed Systems?

**Difficulty**: Advanced

**Strategy**:
Minimum votes required to perform operation. R + W > N ensures strong consistency.

---

<a id="q41"></a>
### Q41: Write-Through vs Write-Back Cache?

**Difficulty**: Intermediate

**Strategy**:
**Through:** Write to Cache and DB synchronously (Safe).
**Back:** Write to Cache, async to DB (Fast, risk of data loss).

---

<a id="q42"></a>
### Q42: What is Database Indexing?

**Difficulty**: Beginner

**Strategy**:
Data structure (B-Tree) improving data retrieval speed at cost of write speed and storage.

---

<a id="q43"></a>
### Q43: Row-Oriented vs Column-Oriented DB?

**Difficulty**: Intermediate

**Strategy**:
**Row (Postgres):** Good for transactional (OLTP).
**Column (Cassandra/Redshift):** Good for analytics/aggregations (OLAP).

---

<a id="q44"></a>
### Q44: Design Netflix (Recommendations)?

**Difficulty**: Advanced

**Strategy**:
Collaborative Filtering + Content-based Filtering. Matrix Factorization. Pre-compute recommendations offline.

---

<a id="q45"></a>
### Q45: What is DNS?

**Difficulty**: Beginner

**Strategy**:
Domain Name System. Phonebook of internet. Translates `google.com` to IP address.

---

<a id="q46"></a>
### Q46: Anycast vs Unicast?

**Difficulty**: Advanced

**Strategy**:
**Unicast:** One-to-One.
**Anycast:** One-to-Nearest. Used by CDNs/DNS to route to closest server.

---

<a id="q47"></a>
### Q47: What is a Sidecar Pattern?

**Difficulty**: Intermediate

**Strategy**:
Helper container running alongside main container (e.g., Envoy Proxy in Service Mesh) to handle networking/logs.

---

<a id="q48"></a>
### Q48: What is OAuth 2.0?

**Difficulty**: Intermediate

**Strategy**:
Authorization framework. Allows third-party apps to access user data without sharing passwords. (Access Tokens).

---

<a id="q49"></a>
### Q49: JWT vs Session Cookies?

**Difficulty**: Intermediate

**Strategy**:
**JWT:** Stateless, signed, contains claims. Good for APIs.
**Session:** Stateful, ID stored in cookie, data in server DB.

---

<a id="q50"></a>
### Q50: What is gRPC?

**Difficulty**: Intermediate

**Strategy**:
High-performance RPC framework by Google. Uses Protobuf (binary) and HTTP/2.

---

<a id="q51"></a>
### Q51: GraphQL vs REST?

**Difficulty**: Beginner

**Strategy**:
<strong>REST:</strong> Multiple endpoints, over/under-fetching.<br><strong>GraphQL:</strong> Single endpoint, client asks exactly what it needs.

---

<a id="q52"></a>
### Q52: Design Dropbox (Deduplication)?

**Difficulty**: Advanced

**Strategy**:
Check hash of file chunks. If hash exists, point to existing chunk instead of uploading again.

---

<a id="q53"></a>
### Q53: Vector Clocks?

**Difficulty**: Advanced

**Strategy**:
Algorithm to detect causal ordering of events in distributed systems. Helps resolve conflicts (DynamoDB).

---

<a id="q54"></a>
### Q54: Conflict Resolution Strategies?

**Difficulty**: Advanced

**Strategy**:
Last Write Wins (LWW) or Semantic resolution (Merge shopping carts).

---

<a id="q55"></a>
### Q55: Design Nearby Friends (Location)?

**Difficulty**: Advanced

**Strategy**:
Ephemeral location data. Redis GeoSpatial commands. TTL on location entries.

---

<a id="q56"></a>
### Q56: What is Geohashing?

**Difficulty**: Intermediate

**Strategy**:
Encoding Lat/Long into string. Recursively dividing world into buckets.

---

<a id="q57"></a>
### Q57: Design a Metrics Monitoring System?

**Difficulty**: Advanced

**Strategy**:
Time-Series DB (Prometheus/InfluxDB). Pull vs Push metrics. Downsampling old data.

---

<a id="q58"></a>
### Q58: Pull vs Push Model?

**Difficulty**: Intermediate

**Strategy**:
**Pull:** Consumer requests data (Prometheus).
**Push:** Producer sends data (Graphite).

---

<a id="q59"></a>
### Q59: Batch Processing vs Stream Processing?

**Difficulty**: Intermediate

**Strategy**:
**Batch (Hadoop):** Large volume, high latency.
**Stream (Flink/Kafka):** Real-time, low latency.

---

<a id="q60"></a>
### Q60: Lambda Architecture?

**Difficulty**: Advanced

**Strategy**:
Hybrid. Batch Layer (Accurate, Slow) + Speed Layer (Approx, Fast). Query merges both.

---

<a id="q61"></a>
### Q61: Kappa Architecture?

**Difficulty**: Advanced

**Strategy**:
Stream only. Treat everything as a stream. Simplifies architecture.

---

<a id="q62"></a>
### Q62: What is MapReduce?

**Difficulty**: Intermediate

**Strategy**:
Programming model for processing big data. Map (Filter/Sort) -> Shuffle -> Reduce (Aggregate).

---

<a id="q63"></a>
### Q63: Design a Payment System?

**Difficulty**: Advanced

**Strategy**:
ACID DB mandatory. Idempotency keys to prevent double charge. Distributed Saga for orchestrating steps.

---

<a id="q64"></a>
### Q64: Idempotency in APIs?

**Difficulty**: Intermediate

**Strategy**:
Making multiple identical requests has same effect as single request. Crucial for payments.

---

<a id="q65"></a>
### Q65: What is a Dead Letter Queue?

**Difficulty**: Intermediate

**Strategy**:
Queue for messages that failed processing. Allows debugging and manual retry.

---

<a id="q66"></a>
### Q66: Vertical vs Horizontal Scaling?

**Difficulty**: Beginner

**Strategy**:
<strong>Vertical:</strong> Bigger machine (CPU/RAM). Limit exists.<br><strong>Horizontal:</strong> More machines. Unlimited scaling.

---

<a id="q67"></a>
### Q67: What is a Stateless Architecture?

**Difficulty**: Beginner

**Strategy**:
Server keeps no session data. Any request can go to any server. Easier to scale.

---

<a id="q68"></a>
### Q68: Design Distributed Job Scheduler?

**Difficulty**: Advanced

**Strategy**:
Leader election (ZooKeeper). Workers pull tasks. Heartbeats. Redis for task status.

---

<a id="q69"></a>
### Q69: Paxos vs Raft Consensus?

**Difficulty**: Advanced

**Strategy**:
Algorithms for agreeing on values in distributed systems. Raft is designed to be more understandable than Paxos.

---

<a id="q70"></a>
### Q70: What is a Merkle Tree?

**Difficulty**: Advanced

**Strategy**:
Tree of hashes. Efficient synchronization (DynamoDB) and integrity check (Blockchain).

---

<a id="q71"></a>
### Q71: How HTTPS works?

**Difficulty**: Intermediate

**Strategy**:
TLS Handshake. Asymmetric encryption to exchange symmetric key. Symmetric key for session data.

---

<a id="q72"></a>
### Q72: What is a WAF (Web App Firewall)?

**Difficulty**: Intermediate

**Strategy**:
Protects against SQL Injection, XSS, etc. filters incoming HTTP traffic.

---

<a id="q73"></a>
### Q73: Design a Parking Garage?

**Difficulty**: Beginner

**Strategy**:
OO Design. Classes: Vehicle, Spot, Level, Garage. Enums: Compact, Large. Strategy Pattern for pricing.

---

<a id="q74"></a>
### Q74: What is a Message Broker?

**Difficulty**: Beginner

**Strategy**:
Intermediary for messaging. Decouples sender and receiver (RabbitMQ, ActiveMQ).

---

<a id="q75"></a>
### Q75: Kafka vs RabbitMQ?

**Difficulty**: Intermediate

**Strategy**:
**Kafka:** Log-based, high throughput, replayable.
**RabbitMQ:** Queue-based, complex routing, ack/nack.

---

<a id="q76"></a>
### Q76: Database Isolation Levels?

**Difficulty**: Advanced

**Strategy**:
Read Uncommitted, Read Committed, Repeatable Read, Serializable. Trade-off between consistency and performance.

---

<a id="q77"></a>
### Q77: Optimistic vs Pessimistic Locking?

**Difficulty**: Intermediate

**Strategy**:
**Optimistic:** Version check on save. Good for low contention.
**Pessimistic:** Lock record on read. Good for high contention.

---

<a id="q78"></a>
### Q78: Design Amazon Cart?

**Difficulty**: Advanced

**Strategy**:
DynamoDB (Key-Value). Cart items persisted. Merge local cart after login. Availability over Consistency.

---

<a id="q79"></a>
### Q79: What is PACELC Theorem?

**Difficulty**: Advanced

**Strategy**:
Extension of CAP. If Partition (P), choose A or C. Else (E), choose Latency (L) or Consistency (C).

---

<a id="q80"></a>
### Q80: Design a Flash Sale System?

**Difficulty**: Advanced

**Strategy**:
Redis counters for inventory. Queue to throttle DB writes. Static content on CDN.

---

<a id="q81"></a>
### Q81: What is Content-Based Routing?

**Difficulty**: Intermediate

**Strategy**:
Routing requests to different microservices based on request content (headers/body).

---

<a id="q82"></a>
### Q82: Peer-to-Peer Networks?

**Difficulty**: Intermediate

**Strategy**:
No central server. Peers connect directly (BitTorrent). Resilient but hard to manage.

---

<a id="q83"></a>
### Q83: Design Google Maps?

**Difficulty**: Advanced

**Strategy**:
Graph for routing (Dijkstra/A*). Tiled images for rendering (Quadtree/Zoom levels).

---

<a id="q84"></a>
### Q84: What is Edge Computing?

**Difficulty**: Intermediate

**Strategy**:
Processing data near the source (IoT devices) rather than sending to centralized cloud.

---

<a id="q85"></a>
### Q85: Serverless Architecture?

**Difficulty**: Intermediate

**Strategy**:
FaaS (Lambda). No server management. Scale to zero. Pay per execution.

---

<a id="q86"></a>
### Q86: Design a Collaborative Editor (Google Docs)?

**Difficulty**: Advanced

**Strategy**:
Operational Transformation (OT) or CRDTs to handle concurrent edits without locking.

---

<a id="q87"></a>
### Q87: Operational Transformation (OT)?

**Difficulty**: Advanced

**Strategy**:
Algorithm to transform operations (insert/delete) based on other concurrent operations.

---

<a id="q88"></a>
### Q88: CRDTs (Conflict-free Replicated Data Types)?

**Difficulty**: Advanced

**Strategy**:
Data structures that can be updated independently and merged without conflicts.

---

<a id="q89"></a>
### Q89: Design Tinder (Matching)?

**Difficulty**: Advanced

**Strategy**:
Geospatial query. "Swipes" are heavy writes. Redis for active users. Async processing for matches.

---

<a id="q90"></a>
### Q90: Design a Search Engine?

**Difficulty**: Advanced

**Strategy**:
Crawler -> Indexer (Inverted Index) -> Searcher (Ranking/TF-IDF/PageRank).

---

<a id="q91"></a>
### Q91: What is WebRTC?

**Difficulty**: Intermediate

**Strategy**:
Peer-to-Peer audio/video. Uses UDP. Signaling server needed for handshake.

---

<a id="q92"></a>
### Q92: Design a Distributed Counter?

**Difficulty**: Intermediate

**Strategy**:
Sharded counters. Sum all shards for total. Reduces write contention.

---

<a id="q93"></a>
### Q93: What is a Split-Brain problem?

**Difficulty**: Advanced

**Strategy**:
Cluster splits into two, both thinking they are the master. Leads to data corruption. Fix: Quorum.

---

<a id="q94"></a>
### Q94: Design a Logging System?

**Difficulty**: Intermediate

**Strategy**:
Filebeat (Agent) -> Kafka (Buffer) -> Logstash (Parse) -> Elasticsearch (Index) -> Kibana (UI).

---

<a id="q95"></a>
### Q95: What is Structured Logging?

**Difficulty**: Beginner

**Strategy**:
Logging in JSON format (key-value) instead of plain text. Easier to query.

---

<a id="q96"></a>
### Q96: Distributed Tracing (Jaeger/Zipkin)?

**Difficulty**: Intermediate

**Strategy**:
Tracking a request across microservices using a Trace ID and Span IDs.

---

<a id="q97"></a>
### Q97: Chaos Engineering?

**Difficulty**: Advanced

**Strategy**:
Intentionally introducing faults (latency, crash) to test system resilience (Netflix Chaos Monkey).

---

<a id="q98"></a>
### Q98: Design Facebook Messenger?

**Difficulty**: Advanced

**Strategy**:
One-on-one vs Group. HBase for message storage. Push notifications for offline users.

---

<a id="q99"></a>
### Q99: Design an Elevator System?

**Difficulty**: Intermediate

**Strategy**:
**
State Machine. Classes: Elevator, Request, Dispatcher. Algorithms: FCFS, SSTF (SCAN), LOOK.

**Code Example**:
```text
Request(Floor 5, Up) -> Dispatcher -> Elevator 2 (Moving Up, at Floor 3)
```

---

<a id="q100"></a>
### Q100: Design a Hotel Booking System?

**Difficulty**: Advanced

**Strategy**:
**
Handling concurrency is key (Double booking). Database locking (Optimistic vs Pessimistic). Search availability by date/room type.

**Code Example**:
```sql
SELECT * FROM rooms WHERE id NOT IN (
  SELECT room_id FROM bookings WHERE start < end_date AND end > start_date
)
```

---

<a id="q101"></a>
### Q101: Design an Airline Reservation System?

**Difficulty**: Advanced

**Strategy**:
**
Similar to Hotel Booking but with Seat Map. High read/write ratio. Caching availability. Queueing for high traffic (flash sales).

**Code Example**:
```text
Redis for seat map cache. Database transaction for final booking.
```

---

<a id="q102"></a>
### Q102: Design a Distributed Job Scheduler?

**Difficulty**: Advanced

**Strategy**:
**
Leader-Follower. Tasks in DB/Queue. Workers poll for tasks. Heartbeats to detect worker failure. Re-assignment of failed tasks.

**Code Example**:
```text
Zookeeper for leader election. Redis/Kafka for task queue.
```

---

<a id="q103"></a>
### Q103: Design a Distributed Log Aggregator (ELK)?

**Difficulty**: Advanced

**Strategy**:
**
Agents (Filebeat) on servers -> Buffer (Kafka) -> Indexer (Logstash) -> Storage/Search (Elasticsearch) -> UI (Kibana).

**Code Example**:
```text
Log -> JSON -> Index -> Search
```

---

<a id="q104"></a>
### Q104: Design a Geo-Fencing System?

**Difficulty**: Advanced

**Strategy**:
**
QuadTrees or Google S2. Check if point is inside polygon (Ray Casting algorithm). Real-time location updates.

**Code Example**:
```text
User enters zone -> Event Trigger -> Notification
```

---

<a id="q105"></a>
### Q105: Design a Collaborative Document Editor (Google Docs)?

**Difficulty**: Advanced

**Strategy**:
**
Operational Transformation (OT) or CRDTs (Conflict-free Replicated Data Types). WebSockets for real-time sync.

**Code Example**:
```text
Client A: Insert 'x' at 0. Client B: Delete at 0.
OT transforms operations to converge.
```

---

<a id="q106"></a>
### Q106: Design Amazon (E-commerce)?

**Difficulty**: Advanced

**Strategy**:
**
Catalog Service, Cart Service, Order Service, User Service. Inventory management (eventual consistency ok for viewing, strong for checkout). Recommendation engine.

**Code Example**:
```text
Cart -> Redis Session. Checkout -> DB Transaction.
```

---

<a id="q107"></a>
### Q107: Design Netflix (Video on Demand)?

**Difficulty**: Advanced

**Strategy**:
**
CDN for video delivery. Adaptive Bitrate Streaming (DASH/HLS). Pre-transcoding videos into multiple formats/resolutions.

**Code Example**:
```text
Upload -> Split -> Transcode -> Store S3 -> Push to CDNs
```

---

<a id="q108"></a>
### Q108: Design a Food Delivery App (DoorDash)?

**Difficulty**: Advanced

**Strategy**:
**
Real-time tracking (Driver location). Matching algorithm (Driver to Restaurant to Customer). State machine for order status.

**Code Example**:
```text
Graph Service for routing. Geo-hashing for matching.
```

---

<a id="q109"></a>
### Q109: Design a Recommendation System?

**Difficulty**: Advanced

**Strategy**:
**
Collaborative Filtering vs Content-Based Filtering. Matrix Factorization. Real-time vs Batch processing (Spark/Hadoop).

**Code Example**:
```text
User-Item Matrix -> Similar Users -> Recommend Items
```

---

<a id="q110"></a>
### Q110: Design a Dating App (Tinder)?

**Difficulty**: Advanced

**Strategy**:
**
Geo-location (Quadtree/Geohash). Swiping logic (Bloom filter for seen profiles). Matching (mutual like).

**Code Example**:
```text
Query: Find users within X km radius who haven't been seen.
```

---

<a id="q111"></a>
### Q111: Design a News Aggregator?

**Difficulty**: Intermediate

**Strategy**:
**
Web Crawlers. Content deduplication (SimHash). Categorization (NLP). Ranking (Time decay + Popularity).

**Code Example**:
```text
Feed Service -> Pulls top ranked articles from cache.
```

---

<a id="q112"></a>
### Q112: Design a Distributed Cache?

**Difficulty**: Advanced

**Strategy**:
**
Eviction policies (LRU/LFU). Consistency (Write-Through vs Write-Back). Partitioning (Consistent Hashing). High Availability (Replication).

**Code Example**:
```text
Client -> Hash(Key) -> Node
```

---

<a id="q113"></a>
### Q113: Design a URL Image Store?

**Difficulty**: Intermediate

**Strategy**:
**
Upload -> Generate Unique ID -> Store Metadata (DB) -> Store Blob (S3) -> Return URL. CDN for serving.

**Code Example**:
```text
GET /img/abc1234 -> Redirect to CDN URL
```

---

<a id="q114"></a>
### Q114: What is Database Sharding?

**Difficulty**: Advanced

**Strategy**:
**
Partitioning data across multiple machines. Horizontal scaling. Strategies: Range based, Hash based, Directory based. Challenges: Joins, Rebalancing.

**Code Example**:
```text
User ID % 4 -> Shard 0, 1, 2, or 3
```

---

<a id="q115"></a>
### Q115: What is Database Replication?

**Difficulty**: Intermediate

**Strategy**:
**
Master-Slave (Write to Master, Read from Slaves) vs Master-Master. Async vs Sync replication. Improves read throughput and availability.

**Code Example**:
```text
Master -> Binlog -> Slave -> Relay Log
```

---

<a id="q116"></a>
### Q116: What is Checksum?

**Difficulty**: Beginner

**Strategy**:
**
A value used to verify data integrity. If data changes, checksum changes. Used in file transfers and hashing.

**Code Example**:
```text
MD5, SHA-256
```

---

<a id="q117"></a>
### Q117: What is a CDN Edge Server?

**Difficulty**: Beginner

**Strategy**:
**
A server located geographically close to the user. It caches static content from the origin server to reduce latency.

**Code Example**:
```text
User (London) -> CDN Edge (London) -> Origin (US)
```

---

<a id="q118"></a>
### Q118: What is a Service Mesh?

**Difficulty**: Intermediate

**Strategy**:
**
A dedicated infrastructure layer for facilitating service-to-service communications between microservices. It often uses a sidecar proxy (e.g., Envoy) to handle traffic, observability, and security.

**Code Example**:
```yaml
# Kubernetes Sidecar injection
apiVersion: v1
kind: Pod
metadata:
  name: my-app
  annotations:
    sidecar.istio.io/inject: "true"
```

---

<a id="q119"></a>
### Q119: What is the Bulkhead Pattern?

**Difficulty**: Advanced

**Strategy**:
**
Isolates elements of an application into pools so if one fails, the others continue to function (like ship bulkheads). Prevents cascading failures.

**Code Example**:
```java
// Hystrix/Resilience4j Thread Pools
ThreadPool-A (Service X)
ThreadPool-B (Service Y)
// If Service X hangs, ThreadPool-B is unaffected.
```

---

<a id="q120"></a>
### Q120: What is a Count-Min Sketch?

**Difficulty**: Expert

**Strategy**:
**
A probabilistic frequency table. Used to count heavy hitters (e.g., top trending topics) in a stream with sub-linear space.

**Code Example**:
```text
Matrix [d x w]. Hash element to one cell in each row and increment.
Min(cells) = Estimated Count.
```

---

<a id="q121"></a>
### Q121: Quadtree vs. Geohash for Location Search?

**Difficulty**: Advanced

**Strategy**:
**

- **Quadtree**: Tree structure where each node has 4 children (NW, NE, SW, SE). Good for dynamic updates.
- **Geohash**: Encodes lat/long into a string. Shared prefix = proximity. Good for static storage/caching.

**Code Example**:
```text
Geohash: "u4pruydqqvj"
Quadtree: Root -> NE -> SW ...
```

---

<a id="q122"></a>
### Q122: Token Bucket vs. Leaky Bucket?

**Difficulty**: Advanced

**Strategy**:
**
Rate limiting algorithms.

- **Token Bucket**: Tokens added at rate `r`. Request needs token. Allows bursts.
- **Leaky Bucket**: Requests enter queue, processed at constant rate. Smooths traffic.

**Code Example**:
```java
// Token Bucket
if (tokens > 0) {
  tokens--;
  process();
} else {
  drop();
}
```

---

<a id="q123"></a>
### Q123: LSM Tree vs. B-Tree?

**Difficulty**: Expert

**Strategy**:
**

- **LSM (Log-Structured Merge)**: Optimizes for writes (append-only). Used in Cassandra, Kafka.
- **B-Tree**: Optimizes for reads (sorted blocks). Used in SQL databases.

**Code Example**:
```text
LSM: MemTable -> Flush to SSTable -> Compaction
```

---

<a id="q124"></a>
### Q124: What is Write Amplification?

**Difficulty**: Expert

**Strategy**:
**
When one logical write results in multiple physical writes to storage (e.g., during LSM compaction or B-Tree page splitting). Reduces SSD lifespan and throughput.

**Code Example**:
```text
Write 1KB data -> Triggers merge -> Rewrites 10MB file.
Amplification = 10MB / 1KB.
```

---

<a id="q125"></a>
### Q125: Read Repair vs. Anti-Entropy?

**Difficulty**: Advanced

**Strategy**:
**

- **Read Repair**: Fix inconsistencies when data is read (Lazy).
- **Anti-Entropy**: Background process (e.g., Merkle Trees) to compare and fix data (Active).

**Code Example**:
```text
Read(Key) -> Get versions from replicas -> If mismatch, update stale replica.
```

---

<a id="q126"></a>
### Q126: What is Split Brain?

**Difficulty**: Intermediate

**Strategy**:
**
When a cluster loses connectivity and splits into two partitions, both believing they are the leader/active. Leads to data corruption. Resolved by Quorum (majority vote).

**Code Example**:
```text
Cluster: 5 nodes.
Partition: 2 nodes vs 3 nodes.
3 nodes (Majority) continue. 2 nodes pause.
```

---

<a id="q127"></a>
### Q127: Cache Avalanche vs. Cache Penetration?

**Difficulty**: Advanced

**Strategy**:
**

- **Avalanche**: Many keys expire at once -> DB overwhelmed. Solution: Randomize TTL.
- **Penetration**: Querying non-existent keys bypasses cache -> DB overwhelmed. Solution: Bloom Filter or cache empty results.

**Code Example**:
```java
// Avoid Avalanche
ttl = base_ttl + random(0, 60s);
```

---

<a id="q128"></a>
### Q128: How to handle Hot Partitions (Data Skew)?

**Difficulty**: Advanced

**Strategy**:
**
When one shard receives disproportionate traffic (e.g., Justin Bieber's tweets).
Solutions: Add salt/random suffix to keys to spread load, or read from replicas.

**Code Example**:
```java
key = "celebrity_id" + random(1, 10);
// Writes go to 10 shards. Reads aggregate from 10 shards.
```

---

<a id="q129"></a>
### Q129: Lambda vs. Kappa Architecture?

**Difficulty**: Expert

**Strategy**:
**

- **Lambda**: Batch layer (Hadoop) + Speed layer (Storm/Flink). Complex to maintain two codebases.
- **Kappa**: Everything is a stream. Single processing framework (e.g., Kafka + Flink).

**Code Example**:
```text
Lambda: Batch(Historical) + Stream(Real-time) -> Merge Query
Kappa: Stream(All Data) -> Query
```

---

<a id="q130"></a>
### Q130: What is Event Sourcing?

**Difficulty**: Advanced

**Strategy**:
**
Storing state as a sequence of events rather than the current snapshot. Allows replaying history to reconstruct state or debug.

**Code Example**:
```sql
Events:
1. AccountCreated(ID=1)
2. Deposited(Amount=100)
3. Withdrawn(Amount=20)
Current Balance = 100 - 20 = 80.
```

---

<a id="q131"></a>
### Q131: What is CQRS?

**Difficulty**: Advanced

**Strategy**:
**
Command Query Responsibility Segregation. Separating Read (Query) and Write (Command) models. Allows optimizing them independently (e.g., NoSQL for reads, SQL for writes).

**Code Example**:
```java
CommandService.updateUser(); // Writes to Master DB
QueryService.getUser();      // Reads from Read Replica/Cache
```

---

<a id="q132"></a>
### Q132: Three-Phase Commit (3PC)?

**Difficulty**: Expert

**Strategy**:
**
Improvement on 2PC to reduce blocking. Adds a "PreCommit" phase. If coordinator fails, participants can timeout and resolve state.

**Code Example**:
```text
CanCommit? -> PreCommit (Lock) -> DoCommit
```

---
