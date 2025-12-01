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

---

### Q1: Design a URL Shortener (TinyURL)?

**Difficulty**: Intermediate

**Strategy**:
- **API:** <code>create(long_url) -> short_url</code>, <code>get(short_url) -> long_url</code>.

    - **DB:** K-V Store (DynamoDB). Key: ShortID, Value: LongURL.

    - **Algorithm:** Base62 encoding of a unique ID.

    - **Unique ID:** Distributed ID Generator (Snowflake) or KGS (Key Generation Service).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q2: Design a Rate Limiter?

**Difficulty**: Intermediate

**Strategy**:
**Token Bucket Algorithm:**


  

  Use Redis `INCR` and `EXPIRE` for distributed counting.

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

### Q3: Design a Chat Application (WhatsApp)?

**Difficulty**: Advanced

**Strategy**:
- **Real-time:** WebSockets or MQTT.

    - **Protocol:** XMPP or Custom binary protocol (Protobuf).

    - **Storage:** Cassandra/HBase for chat history (Write heavy). Redis for presence.

    - **Encryption:** End-to-End using Signal Protocol (Double Ratchet).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q4: Explain CAP Theorem?

**Difficulty**: Beginner

**Strategy**:
Pick two: **Consistency**, **Availability**, **Partition Tolerance**.


  Since Partition Tolerance (P) is mandatory in distributed systems, choice is CP vs AP.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q5: Load Balancing: L4 vs L7?

**Difficulty**: Intermediate

**Strategy**:
**L4:** IP/Port based (TCP). Fast. No packet inspection.
**L7:** Application based (HTTP). Smarter (Routing based on URL/Header). Slower.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q6: SQL vs NoSQL?

**Difficulty**: Beginner

**Strategy**:
**SQL:** ACID, Structured, Complex Queries (Joins). Vertical Scaling.
**NoSQL:** BASE, Unstructured, High Throughput. Horizontal Scaling.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q7: What is Consistent Hashing?

**Difficulty**: Advanced

**Strategy**:
Maps keys and servers to a ring. Minimizes remapping when servers change.

**Code Example**:
```text
Ring: 0 ... 2^32-1
Server A at Hash(A)
Server B at Hash(B)
Key K at Hash(K) -> Walk clockwise to find first Server.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q8: Design a Key-Value Store (Redis)?

**Difficulty**: Advanced

**Strategy**:
In-memory Hash Map. Persistence via Snapshot (RDB) or Log (AOF). Single-threaded event loop.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q9: What is a CDN?

**Difficulty**: Beginner

**Strategy**:
Network of edge servers caching static content close to users to reduce latency.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q10: Design a Notification System?

**Difficulty**: Intermediate

**Strategy**:
Service -> Message Queue (Kafka) -> Workers -> 3rd Party (FCM/APNS/SendGrid).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q11: Sharding vs Replication?

**Difficulty**: Intermediate

**Strategy**:
**Replication:** Copies data (Read scaling, Availability).
**Sharding:** Splits data (Write scaling, Storage capacity).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q12: Design Instagram News Feed?

**Difficulty**: Advanced

**Strategy**:
**Push Model (Fan-out on Write):** Pre-compute feeds. Fast reads. Complex writes for celebs.


  **Pull Model (Fan-out on Read):** Query on demand. Slow reads.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q13: What is a Bloom Filter?

**Difficulty**: Advanced

**Strategy**:
Bit array + Hash functions. Checks if item exists. False Positive: Yes. False Negative: No.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q14: Microservices vs Monolith?

**Difficulty**: Beginner

**Strategy**:
**Monolith:** Single deployable. Simple.
**Microservices:** Distributed. Independent scaling. Complex ops.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q15: Design a Web Crawler?

**Difficulty**: Advanced

**Strategy**:
URL Frontier (Queue) -> Fetcher -> DNS Resolver -> Content Parser -> Dedup -> Storage.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q16: Thundering Herd Problem?

**Difficulty**: Advanced

**Strategy**:
Many clients hit DB simultaneously when cache expires. Fix: Random jitter, Mutex locks, Early expiration.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q17: Design Google Drive (File Sync)?

**Difficulty**: Advanced

**Strategy**:
Chunk files (4MB). Hash chunks. Upload only changed chunks (Differential Sync). Metadata in SQL. Blocks in S3.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q18: What is Backpressure?

**Difficulty**: Advanced

**Strategy**:
Consumer signaling Producer to slow down to prevent overwhelm. Drop, Buffer, or Block.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q19: Design Typeahead (Autocomplete)?

**Difficulty**: Intermediate

**Strategy**:
**Trie** structure. Store top K frequent terms at each node. Cache popular prefixes.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q20: ACID Transactions?

**Difficulty**: Beginner

**Strategy**:
Atomicity, Consistency, Isolation, Durability. Guarantees for relational databases.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q21: Design YouTube (Video Streaming)?

**Difficulty**: Advanced

**Strategy**:
Upload -> Transcode (FFmpeg) to multiple formats/resolutions -> Store in S3 -> CDN. Metadata in SQL.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q22: Design Uber (Ride Sharing)?

**Difficulty**: Advanced

**Strategy**:
**Geospatial Index:** Quadtree or Google S2. Matches riders with drivers in cells. Frequent location updates via WebSocket.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q23: What is Database Normalization?

**Difficulty**: Beginner

**Strategy**:
Organizing data to reduce redundancy and improve integrity (1NF, 2NF, 3NF).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q24: Explain Two-Phase Commit (2PC)?

**Difficulty**: Advanced

**Strategy**:
Distributed transaction protocol. 1. Prepare (Vote). 2. Commit/Abort. Blocking protocol.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q25: Saga Pattern for Distributed Tx?

**Difficulty**: Advanced

**Strategy**:
Sequence of local transactions. If one fails, execute compensating transactions to undo changes.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q26: Circuit Breaker Pattern?

**Difficulty**: Intermediate

**Strategy**:
Prevents cascading failures. If service fails repeatedly, "Open" circuit and fail fast for a timeout period.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q27: API Gateway vs Load Balancer?

**Difficulty**: Intermediate

**Strategy**:
**Gateway:** Entry point. Auth, Rate Limiting, Routing, Aggregation.
**LB:** Distributes traffic to servers.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q28: Polling vs WebSockets vs SSE?

**Difficulty**: Intermediate

**Strategy**:
**Polling:** Client asks repeatedly.
**WebSockets:** Bidirectional.
**SSE:** Server to Client (Unidirectional).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q29: Design Twitter (Timeline)?

**Difficulty**: Advanced

**Strategy**:
Hybrid approach. Push to Redis lists for active users. Pull from DB for inactive/celebrity tweets.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q30: Design Ticketmaster (Booking)?

**Difficulty**: Advanced

**Strategy**:
Consistency is key. Use SQL with locking (SELECT FOR UPDATE) or Redis Lua scripts to reserve seats.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q31: Strong vs Eventual Consistency?

**Difficulty**: Intermediate

**Strategy**:
**Strong:** Reads see latest write (Latency hit).
**Eventual:** Reads may be stale, converges later (High Availability).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q32: What is a Reverse Proxy?

**Difficulty**: Beginner

**Strategy**:
Server sitting in front of backends. Handles SSL termination, Caching, Load Balancing (Nginx, HAProxy).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q33: Service Discovery?

**Difficulty**: Intermediate

**Strategy**:
Registry keeping track of dynamic IP:Ports of services (Consul, Eureka, ZooKeeper, K8s DNS).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q34: Blue-Green vs Canary Deployment?

**Difficulty**: Intermediate

**Strategy**:
**Blue-Green:** Switch traffic 100% from old to new env.
**Canary:** Gradually roll out new version to % of users.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q35: What is a Distributed Lock?

**Difficulty**: Advanced

**Strategy**:
Ensures mutual exclusion across processes/servers. Implementations: Redis (Redlock), ZooKeeper.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q36: Design a Leaderboard?

**Difficulty**: Intermediate

**Strategy**:
Redis Sorted Sets (ZSET). <code>ZADD user score</code>, <code>ZREVRANGE 0 10</code>.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q37: Design a Unique ID Generator?

**Difficulty**: Intermediate

**Strategy**:
**Twitter Snowflake:** 64-bit integer (Timestamp + MachineID + Sequence). Sortable by time.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q38: What is Gossip Protocol?

**Difficulty**: Advanced

**Strategy**:
Peer-to-peer communication. Nodes randomly share info with neighbors. Used in Cassandra ring state.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

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

### Q41: Write-Through vs Write-Back Cache?

**Difficulty**: Intermediate

**Strategy**:
**Through:** Write to Cache and DB synchronously (Safe).
**Back:** Write to Cache, async to DB (Fast, risk of data loss).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

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

### Q44: Design Netflix (Recommendations)?

**Difficulty**: Advanced

**Strategy**:
Collaborative Filtering + Content-based Filtering. Matrix Factorization. Pre-compute recommendations offline.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

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

### Q47: What is a Sidecar Pattern?

**Difficulty**: Intermediate

**Strategy**:
Helper container running alongside main container (e.g., Envoy Proxy in Service Mesh) to handle networking/logs.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q48: Design an API Rate Limiter?

**Difficulty**: Intermediate

**Strategy**:
Middleware using Redis. Identify by API Key or IP. Return 429 Too Many Requests.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q49: What is OAuth 2.0?

**Difficulty**: Intermediate

**Strategy**:
Authorization framework. Allows third-party apps to access user data without sharing passwords. (Access Tokens).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q50: JWT vs Session Cookies?

**Difficulty**: Intermediate

**Strategy**:
**JWT:** Stateless, signed, contains claims. Good for APIs.
**Session:** Stateful, ID stored in cookie, data in server DB.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q51: What is gRPC?

**Difficulty**: Intermediate

**Strategy**:
High-performance RPC framework by Google. Uses Protobuf (binary) and HTTP/2.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

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

### Q54: Vector Clocks?

**Difficulty**: Advanced

**Strategy**:
Algorithm to detect causal ordering of events in distributed systems. Helps resolve conflicts (DynamoDB).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q55: Conflict Resolution Strategies?

**Difficulty**: Advanced

**Strategy**:
Last Write Wins (LWW) or Semantic resolution (Merge shopping carts).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q56: Design Nearby Friends (Location)?

**Difficulty**: Advanced

**Strategy**:
Ephemeral location data. Redis GeoSpatial commands. TTL on location entries.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q57: What is Geohashing?

**Difficulty**: Intermediate

**Strategy**:
Encoding Lat/Long into string. Recursively dividing world into buckets.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q58: Design a Metrics Monitoring System?

**Difficulty**: Advanced

**Strategy**:
Time-Series DB (Prometheus/InfluxDB). Pull vs Push metrics. Downsampling old data.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q59: Pull vs Push Model?

**Difficulty**: Intermediate

**Strategy**:
**Pull:** Consumer requests data (Prometheus).
**Push:** Producer sends data (Graphite).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q60: Batch Processing vs Stream Processing?

**Difficulty**: Intermediate

**Strategy**:
**Batch (Hadoop):** Large volume, high latency.
**Stream (Flink/Kafka):** Real-time, low latency.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q61: Lambda Architecture?

**Difficulty**: Advanced

**Strategy**:
Hybrid. Batch Layer (Accurate, Slow) + Speed Layer (Approx, Fast). Query merges both.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q62: Kappa Architecture?

**Difficulty**: Advanced

**Strategy**:
Stream only. Treat everything as a stream. Simplifies architecture.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q63: What is MapReduce?

**Difficulty**: Intermediate

**Strategy**:
Programming model for processing big data. Map (Filter/Sort) -> Shuffle -> Reduce (Aggregate).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q64: Design a Payment System?

**Difficulty**: Advanced

**Strategy**:
ACID DB mandatory. Idempotency keys to prevent double charge. Distributed Saga for orchestrating steps.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q65: Idempotency in APIs?

**Difficulty**: Intermediate

**Strategy**:
Making multiple identical requests has same effect as single request. Crucial for payments.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q66: What is a Dead Letter Queue?

**Difficulty**: Intermediate

**Strategy**:
Queue for messages that failed processing. Allows debugging and manual retry.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

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

### Q70: Paxos vs Raft Consensus?

**Difficulty**: Advanced

**Strategy**:
Algorithms for agreeing on values in distributed systems. Raft is designed to be more understandable than Paxos.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q71: What is a Merkle Tree?

**Difficulty**: Advanced

**Strategy**:
Tree of hashes. Efficient synchronization (DynamoDB) and integrity check (Blockchain).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

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

### Q73: How HTTPS works?

**Difficulty**: Intermediate

**Strategy**:
TLS Handshake. Asymmetric encryption to exchange symmetric key. Symmetric key for session data.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q74: What is a WAF (Web App Firewall)?

**Difficulty**: Intermediate

**Strategy**:
Protects against SQL Injection, XSS, etc. filters incoming HTTP traffic.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

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

### Q78: Database Isolation Levels?

**Difficulty**: Advanced

**Strategy**:
Read Uncommitted, Read Committed, Repeatable Read, Serializable. Trade-off between consistency and performance.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q79: Optimistic vs Pessimistic Locking?

**Difficulty**: Intermediate

**Strategy**:
**Optimistic:** Version check on save. Good for low contention.
**Pessimistic:** Lock record on read. Good for high contention.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q80: Design Amazon Cart?

**Difficulty**: Advanced

**Strategy**:
DynamoDB (Key-Value). Cart items persisted. Merge local cart after login. Availability over Consistency.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q81: What is PACELC Theorem?

**Difficulty**: Advanced

**Strategy**:
Extension of CAP. If Partition (P), choose A or C. Else (E), choose Latency (L) or Consistency (C).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q82: Design a Flash Sale System?

**Difficulty**: Advanced

**Strategy**:
Redis counters for inventory. Queue to throttle DB writes. Static content on CDN.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q83: What is Content-Based Routing?

**Difficulty**: Intermediate

**Strategy**:
Routing requests to different microservices based on request content (headers/body).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q84: Peer-to-Peer Networks?

**Difficulty**: Intermediate

**Strategy**:
No central server. Peers connect directly (BitTorrent). Resilient but hard to manage.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q85: Design Google Maps?

**Difficulty**: Advanced

**Strategy**:
Graph for routing (Dijkstra/A*). Tiled images for rendering (Quadtree/Zoom levels).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q86: What is Edge Computing?

**Difficulty**: Intermediate

**Strategy**:
Processing data near the source (IoT devices) rather than sending to centralized cloud.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q87: Serverless Architecture?

**Difficulty**: Intermediate

**Strategy**:
FaaS (Lambda). No server management. Scale to zero. Pay per execution.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q88: Design a Collaborative Editor (Google Docs)?

**Difficulty**: Advanced

**Strategy**:
Operational Transformation (OT) or CRDTs to handle concurrent edits without locking.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q89: Operational Transformation (OT)?

**Difficulty**: Advanced

**Strategy**:
Algorithm to transform operations (insert/delete) based on other concurrent operations.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q90: CRDTs (Conflict-free Replicated Data Types)?

**Difficulty**: Advanced

**Strategy**:
Data structures that can be updated independently and merged without conflicts.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q91: Design Tinder (Matching)?

**Difficulty**: Advanced

**Strategy**:
Geospatial query. "Swipes" are heavy writes. Redis for active users. Async processing for matches.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q92: Design a Search Engine?

**Difficulty**: Advanced

**Strategy**:
Crawler -> Indexer (Inverted Index) -> Searcher (Ranking/TF-IDF/PageRank).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q93: What is WebRTC?

**Difficulty**: Intermediate

**Strategy**:
Peer-to-Peer audio/video. Uses UDP. Signaling server needed for handshake.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q94: Design a Distributed Counter?

**Difficulty**: Intermediate

**Strategy**:
Sharded counters. Sum all shards for total. Reduces write contention.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q95: What is a Split-Brain problem?

**Difficulty**: Advanced

**Strategy**:
Cluster splits into two, both thinking they are the master. Leads to data corruption. Fix: Quorum.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q96: Design a Logging System?

**Difficulty**: Intermediate

**Strategy**:
Filebeat (Agent) -> Kafka (Buffer) -> Logstash (Parse) -> Elasticsearch (Index) -> Kibana (UI).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

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

### Q99: Chaos Engineering?

**Difficulty**: Advanced

**Strategy**:
Intentionally introducing faults (latency, crash) to test system resilience (Netflix Chaos Monkey).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q100: Design Facebook Messenger?

**Difficulty**: Advanced

**Strategy**:
One-on-one vs Group. HBase for message storage. Push notifications for offline users.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---
