# System Design Interview Questions

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

<div id="q1" class="question">1. Design a URL Shortener (TinyURL)? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <ul>
    <li><strong>API:</strong> <code>create(long_url) -> short_url</code>, <code>get(short_url) -> long_url</code>.</li>
    <li><strong>DB:</strong> K-V Store (DynamoDB). Key: ShortID, Value: LongURL.</li>
    <li><strong>Algorithm:</strong> Base62 encoding of a unique ID.</li>
    <li><strong>Unique ID:</strong> Distributed ID Generator (Snowflake) or KGS (Key Generation Service).</li>
  </ul>
</div>

<div id="q2" class="question">2. Design a Rate Limiter? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p><strong>Token Bucket Algorithm:</strong></p>
  <pre><code class="language-python"># Conceptual
bucket_size = 10
refill_rate = 1 # per second
current_tokens = 10
last_refill_timestamp = now()

def allow_request(tokens_needed=1):
refill()
if current_tokens >= tokens_needed:
current_tokens -= tokens_needed
return True
return False</code></pre>

  <p>Use Redis `INCR` and `EXPIRE` for distributed counting.</p>
</div>

<div id="q3" class="question">3. Design a Chat Application (WhatsApp)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <ul>
    <li><strong>Real-time:</strong> WebSockets or MQTT.</li>
    <li><strong>Protocol:</strong> XMPP or Custom binary protocol (Protobuf).</li>
    <li><strong>Storage:</strong> Cassandra/HBase for chat history (Write heavy). Redis for presence.</li>
    <li><strong>Encryption:</strong> End-to-End using Signal Protocol (Double Ratchet).</li>
  </ul>
</div>

<div id="q4" class="question">4. Explain CAP Theorem? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Pick two: <strong>Consistency</strong>, <strong>Availability</strong>, <strong>Partition Tolerance</strong>.</p>
  <p>Since Partition Tolerance (P) is mandatory in distributed systems, choice is CP vs AP.</p>
</div>

<div id="q5" class="question">5. Load Balancing: L4 vs L7? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p><strong>L4:</strong> IP/Port based (TCP). Fast. No packet inspection.<br><strong>L7:</strong> Application based (HTTP). Smarter (Routing based on URL/Header). Slower.</p>
</div>

<div id="q6" class="question">6. SQL vs NoSQL? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p><strong>SQL:</strong> ACID, Structured, Complex Queries (Joins). Vertical Scaling.<br><strong>NoSQL:</strong> BASE, Unstructured, High Throughput. Horizontal Scaling.</p>
</div>

<div id="q7" class="question">7. What is Consistent Hashing? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Maps keys and servers to a ring. Minimizes remapping when servers change.</p>
  <pre><code class="language-text">Ring: 0 ... 2^32-1
Server A at Hash(A)
Server B at Hash(B)
Key K at Hash(K) -> Walk clockwise to find first Server.</code></pre>
</div>

<div id="q8" class="question">8. Design a Key-Value Store (Redis)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>In-memory Hash Map. Persistence via Snapshot (RDB) or Log (AOF). Single-threaded event loop.</p>
</div>

<div id="q9" class="question">9. What is a CDN? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Network of edge servers caching static content close to users to reduce latency.</p>
</div>

<div id="q10" class="question">10. Design a Notification System? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Service -> Message Queue (Kafka) -> Workers -> 3rd Party (FCM/APNS/SendGrid).</p>
</div>

<div id="q11" class="question">11. Sharding vs Replication? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p><strong>Replication:</strong> Copies data (Read scaling, Availability).<br><strong>Sharding:</strong> Splits data (Write scaling, Storage capacity).</p>
</div>

<div id="q12" class="question">12. Design Instagram News Feed? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p><strong>Push Model (Fan-out on Write):</strong> Pre-compute feeds. Fast reads. Complex writes for celebs.</p>
  <p><strong>Pull Model (Fan-out on Read):</strong> Query on demand. Slow reads.</p>
</div>

<div id="q13" class="question">13. What is a Bloom Filter? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Bit array + Hash functions. Checks if item exists. False Positive: Yes. False Negative: No.</p>
</div>

<div id="q14" class="question">14. Microservices vs Monolith? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p><strong>Monolith:</strong> Single deployable. Simple.<br><strong>Microservices:</strong> Distributed. Independent scaling. Complex ops.</p>
</div>

<div id="q15" class="question">15. Design a Web Crawler? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>URL Frontier (Queue) -> Fetcher -> DNS Resolver -> Content Parser -> Dedup -> Storage.</p>
</div>

<div id="q16" class="question">16. Thundering Herd Problem? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Many clients hit DB simultaneously when cache expires. Fix: Random jitter, Mutex locks, Early expiration.</p>
</div>

<div id="q17" class="question">17. Design Google Drive (File Sync)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Chunk files (4MB). Hash chunks. Upload only changed chunks (Differential Sync). Metadata in SQL. Blocks in S3.</p>
</div>

<div id="q18" class="question">18. What is Backpressure? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Consumer signaling Producer to slow down to prevent overwhelm. Drop, Buffer, or Block.</p>
</div>

<div id="q19" class="question">19. Design Typeahead (Autocomplete)? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p><strong>Trie</strong> structure. Store top K frequent terms at each node. Cache popular prefixes.</p>
</div>

<div id="q20" class="question">20. ACID Transactions? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Atomicity, Consistency, Isolation, Durability. Guarantees for relational databases.</p>
</div>

<div id="q21" class="question">21. Design YouTube (Video Streaming)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Upload -> Transcode (FFmpeg) to multiple formats/resolutions -> Store in S3 -> CDN. Metadata in SQL.</p>
</div>

<div id="q22" class="question">22. Design Uber (Ride Sharing)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p><strong>Geospatial Index:</strong> Quadtree or Google S2. Matches riders with drivers in cells. Frequent location updates via WebSocket.</p>
</div>

<div id="q23" class="question">23. What is Database Normalization? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Organizing data to reduce redundancy and improve integrity (1NF, 2NF, 3NF).</p>
</div>

<div id="q24" class="question">24. Explain Two-Phase Commit (2PC)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Distributed transaction protocol. 1. Prepare (Vote). 2. Commit/Abort. Blocking protocol.</p>
</div>

<div id="q25" class="question">25. Saga Pattern for Distributed Tx? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Sequence of local transactions. If one fails, execute compensating transactions to undo changes.</p>
</div>

<div id="q26" class="question">26. Circuit Breaker Pattern? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Prevents cascading failures. If service fails repeatedly, "Open" circuit and fail fast for a timeout period.</p>
</div>

<div id="q27" class="question">27. API Gateway vs Load Balancer? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p><strong>Gateway:</strong> Entry point. Auth, Rate Limiting, Routing, Aggregation.<br><strong>LB:</strong> Distributes traffic to servers.</p>
</div>

<div id="q28" class="question">28. Polling vs WebSockets vs SSE? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p><strong>Polling:</strong> Client asks repeatedly.<br><strong>WebSockets:</strong> Bidirectional.<br><strong>SSE:</strong> Server to Client (Unidirectional).</p>
</div>

<div id="q29" class="question">29. Design Twitter (Timeline)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Hybrid approach. Push to Redis lists for active users. Pull from DB for inactive/celebrity tweets.</p>
</div>

<div id="q30" class="question">30. Design Ticketmaster (Booking)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Consistency is key. Use SQL with locking (SELECT FOR UPDATE) or Redis Lua scripts to reserve seats.</p>
</div>

<div id="q31" class="question">31. Strong vs Eventual Consistency? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p><strong>Strong:</strong> Reads see latest write (Latency hit).<br><strong>Eventual:</strong> Reads may be stale, converges later (High Availability).</p>
</div>

<div id="q32" class="question">32. What is a Reverse Proxy? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Server sitting in front of backends. Handles SSL termination, Caching, Load Balancing (Nginx, HAProxy).</p>
</div>

<div id="q33" class="question">33. Service Discovery? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Registry keeping track of dynamic IP:Ports of services (Consul, Eureka, ZooKeeper, K8s DNS).</p>
</div>

<div id="q34" class="question">34. Blue-Green vs Canary Deployment? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p><strong>Blue-Green:</strong> Switch traffic 100% from old to new env.<br><strong>Canary:</strong> Gradually roll out new version to % of users.</p>
</div>

<div id="q35" class="question">35. What is a Distributed Lock? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Ensures mutual exclusion across processes/servers. Implementations: Redis (Redlock), ZooKeeper.</p>
</div>

<div id="q36" class="question">36. Design a Leaderboard? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Redis Sorted Sets (ZSET). <code>ZADD user score</code>, <code>ZREVRANGE 0 10</code>.</p>
</div>

<div id="q37" class="question">37. Design a Unique ID Generator? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p><strong>Twitter Snowflake:</strong> 64-bit integer (Timestamp + MachineID + Sequence). Sortable by time.</p>
</div>

<div id="q38" class="question">38. What is Gossip Protocol? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Peer-to-peer communication. Nodes randomly share info with neighbors. Used in Cassandra ring state.</p>
</div>

<div id="q39" class="question">39. Heartbeat Mechanism? <span class="beginner">Beginner</span></div>
<div class="answer">
  <p>Periodic signal to indicate a node is alive. If missed, assume failure.</p>
</div>

<div id="q40" class="question">40. Quorum in Distributed Systems? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Minimum votes required to perform operation. R + W > N ensures strong consistency.</p>
</div>

<div id="q41" class="question">41. Write-Through vs Write-Back Cache? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p><strong>Through:</strong> Write to Cache and DB synchronously (Safe).<br><strong>Back:</strong> Write to Cache, async to DB (Fast, risk of data loss).</p>
</div>

<div id="q42" class="question">42. What is Database Indexing? <span class="beginner">Beginner</span></div>
<div class="answer">
  <p>Data structure (B-Tree) improving data retrieval speed at cost of write speed and storage.</p>
</div>

<div id="q43" class="question">43. Row-Oriented vs Column-Oriented DB? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p><strong>Row (Postgres):</strong> Good for transactional (OLTP).<br><strong>Column (Cassandra/Redshift):</strong> Good for analytics/aggregations (OLAP).</p>
</div>

<div id="q44" class="question">44. Design Netflix (Recommendations)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Collaborative Filtering + Content-based Filtering. Matrix Factorization. Pre-compute recommendations offline.</p>
</div>

<div id="q45" class="question">45. What is DNS? <span class="beginner">Beginner</span></div>
<div class="answer">
  <p>Domain Name System. Phonebook of internet. Translates `google.com` to IP address.</p>
</div>

<div id="q46" class="question">46. Anycast vs Unicast? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p><strong>Unicast:</strong> One-to-One.<br><strong>Anycast:</strong> One-to-Nearest. Used by CDNs/DNS to route to closest server.</p>
</div>

<div id="q47" class="question">47. What is a Sidecar Pattern? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Helper container running alongside main container (e.g., Envoy Proxy in Service Mesh) to handle networking/logs.</p>
</div>

<div id="q48" class="question">48. Design an API Rate Limiter? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Middleware using Redis. Identify by API Key or IP. Return 429 Too Many Requests.</p>
</div>

<div id="q49" class="question">49. What is OAuth 2.0? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Authorization framework. Allows third-party apps to access user data without sharing passwords. (Access Tokens).</p>
</div>

<div id="q50" class="question">50. JWT vs Session Cookies? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p><strong>JWT:</strong> Stateless, signed, contains claims. Good for APIs.<br><strong>Session:</strong> Stateful, ID stored in cookie, data in server DB.</p>
</div>

<div id="q51" class="question">51. What is gRPC? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>High-performance RPC framework by Google. Uses Protobuf (binary) and HTTP/2.</p>
</div>

<div id="q52" class="question">52. GraphQL vs REST? <span class="beginner">Beginner</span></div>
<div class="answer">
  <p><strong>REST:</strong> Multiple endpoints, over/under-fetching.<br><strong>GraphQL:</strong> Single endpoint, client asks exactly what it needs.</p>
</div>

<div id="q53" class="question">53. Design Dropbox (Deduplication)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Check hash of file chunks. If hash exists, point to existing chunk instead of uploading again.</p>
</div>

<div id="q54" class="question">54. Vector Clocks? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Algorithm to detect causal ordering of events in distributed systems. Helps resolve conflicts (DynamoDB).</p>
</div>

<div id="q55" class="question">55. Conflict Resolution Strategies? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Last Write Wins (LWW) or Semantic resolution (Merge shopping carts).</p>
</div>

<div id="q56" class="question">56. Design Nearby Friends (Location)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Ephemeral location data. Redis GeoSpatial commands. TTL on location entries.</p>
</div>

<div id="q57" class="question">57. What is Geohashing? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Encoding Lat/Long into string. Recursively dividing world into buckets.</p>
</div>

<div id="q58" class="question">58. Design a Metrics Monitoring System? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Time-Series DB (Prometheus/InfluxDB). Pull vs Push metrics. Downsampling old data.</p>
</div>

<div id="q59" class="question">59. Pull vs Push Model? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p><strong>Pull:</strong> Consumer requests data (Prometheus).<br><strong>Push:</strong> Producer sends data (Graphite).</p>
</div>

<div id="q60" class="question">60. Batch Processing vs Stream Processing? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p><strong>Batch (Hadoop):</strong> Large volume, high latency.<br><strong>Stream (Flink/Kafka):</strong> Real-time, low latency.</p>
</div>

<div id="q61" class="question">61. Lambda Architecture? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Hybrid. Batch Layer (Accurate, Slow) + Speed Layer (Approx, Fast). Query merges both.</p>
</div>

<div id="q62" class="question">62. Kappa Architecture? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Stream only. Treat everything as a stream. Simplifies architecture.</p>
</div>

<div id="q63" class="question">63. What is MapReduce? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Programming model for processing big data. Map (Filter/Sort) -> Shuffle -> Reduce (Aggregate).</p>
</div>

<div id="q64" class="question">64. Design a Payment System? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>ACID DB mandatory. Idempotency keys to prevent double charge. Distributed Saga for orchestrating steps.</p>
</div>

<div id="q65" class="question">65. Idempotency in APIs? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Making multiple identical requests has same effect as single request. Crucial for payments.</p>
</div>

<div id="q66" class="question">66. What is a Dead Letter Queue? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Queue for messages that failed processing. Allows debugging and manual retry.</p>
</div>

<div id="q67" class="question">67. Vertical vs Horizontal Scaling? <span class="beginner">Beginner</span></div>
<div class="answer">
  <p><strong>Vertical:</strong> Bigger machine (CPU/RAM). Limit exists.<br><strong>Horizontal:</strong> More machines. Unlimited scaling.</p>
</div>

<div id="q68" class="question">68. What is a Stateless Architecture? <span class="beginner">Beginner</span></div>
<div class="answer">
  <p>Server keeps no session data. Any request can go to any server. Easier to scale.</p>
</div>

<div id="q69" class="question">69. Design Distributed Job Scheduler? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Leader election (ZooKeeper). Workers pull tasks. Heartbeats. Redis for task status.</p>
</div>

<div id="q70" class="question">70. Paxos vs Raft Consensus? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Algorithms for agreeing on values in distributed systems. Raft is designed to be more understandable than Paxos.</p>
</div>

<div id="q71" class="question">71. What is a Merkle Tree? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Tree of hashes. Efficient synchronization (DynamoDB) and integrity check (Blockchain).</p>
</div>

<div id="q72" class="question">72. Design a URL Shortener (DB Schema)? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-sql">CREATE TABLE urls (
  short_key VARCHAR(7) PRIMARY KEY,
  original_url VARCHAR(255),
  created_at TIMESTAMP,
  user_id INT
);</code></pre>
</div>

<div id="q73" class="question">73. How HTTPS works? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>TLS Handshake. Asymmetric encryption to exchange symmetric key. Symmetric key for session data.</p>
</div>

<div id="q74" class="question">74. What is a WAF (Web App Firewall)? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Protects against SQL Injection, XSS, etc. filters incoming HTTP traffic.</p>
</div>

<div id="q75" class="question">75. Design a Parking Garage? <span class="beginner">Beginner</span></div>
<div class="answer">
  <p>OO Design. Classes: Vehicle, Spot, Level, Garage. Enums: Compact, Large. Strategy Pattern for pricing.</p>
</div>

<div id="q76" class="question">76. What is a Message Broker? <span class="beginner">Beginner</span></div>
<div class="answer">
  <p>Intermediary for messaging. Decouples sender and receiver (RabbitMQ, ActiveMQ).</p>
</div>

<div id="q77" class="question">77. Kafka vs RabbitMQ? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p><strong>Kafka:</strong> Log-based, high throughput, replayable.<br><strong>RabbitMQ:</strong> Queue-based, complex routing, ack/nack.</p>
</div>

<div id="q78" class="question">78. Database Isolation Levels? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Read Uncommitted, Read Committed, Repeatable Read, Serializable. Trade-off between consistency and performance.</p>
</div>

<div id="q79" class="question">79. Optimistic vs Pessimistic Locking? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p><strong>Optimistic:</strong> Version check on save. Good for low contention.<br><strong>Pessimistic:</strong> Lock record on read. Good for high contention.</p>
</div>

<div id="q80" class="question">80. Design Amazon Cart? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>DynamoDB (Key-Value). Cart items persisted. Merge local cart after login. Availability over Consistency.</p>
</div>

<div id="q81" class="question">81. What is PACELC Theorem? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Extension of CAP. If Partition (P), choose A or C. Else (E), choose Latency (L) or Consistency (C).</p>
</div>

<div id="q82" class="question">82. Design a Flash Sale System? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Redis counters for inventory. Queue to throttle DB writes. Static content on CDN.</p>
</div>

<div id="q83" class="question">83. What is Content-Based Routing? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Routing requests to different microservices based on request content (headers/body).</p>
</div>

<div id="q84" class="question">84. Peer-to-Peer Networks? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>No central server. Peers connect directly (BitTorrent). Resilient but hard to manage.</p>
</div>

<div id="q85" class="question">85. Design Google Maps? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Graph for routing (Dijkstra/A*). Tiled images for rendering (Quadtree/Zoom levels).</p>
</div>

<div id="q86" class="question">86. What is Edge Computing? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Processing data near the source (IoT devices) rather than sending to centralized cloud.</p>
</div>

<div id="q87" class="question">87. Serverless Architecture? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>FaaS (Lambda). No server management. Scale to zero. Pay per execution.</p>
</div>

<div id="q88" class="question">88. Design a Collaborative Editor (Google Docs)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Operational Transformation (OT) or CRDTs to handle concurrent edits without locking.</p>
</div>

<div id="q89" class="question">89. Operational Transformation (OT)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Algorithm to transform operations (insert/delete) based on other concurrent operations.</p>
</div>

<div id="q90" class="question">90. CRDTs (Conflict-free Replicated Data Types)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Data structures that can be updated independently and merged without conflicts.</p>
</div>

<div id="q91" class="question">91. Design Tinder (Matching)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Geospatial query. "Swipes" are heavy writes. Redis for active users. Async processing for matches.</p>
</div>

<div id="q92" class="question">92. Design a Search Engine? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Crawler -> Indexer (Inverted Index) -> Searcher (Ranking/TF-IDF/PageRank).</p>
</div>

<div id="q93" class="question">93. What is WebRTC? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Peer-to-Peer audio/video. Uses UDP. Signaling server needed for handshake.</p>
</div>

<div id="q94" class="question">94. Design a Distributed Counter? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Sharded counters. Sum all shards for total. Reduces write contention.</p>
</div>

<div id="q95" class="question">95. What is a Split-Brain problem? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Cluster splits into two, both thinking they are the master. Leads to data corruption. Fix: Quorum.</p>
</div>

<div id="q96" class="question">96. Design a Logging System? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Filebeat (Agent) -> Kafka (Buffer) -> Logstash (Parse) -> Elasticsearch (Index) -> Kibana (UI).</p>
</div>

<div id="q97" class="question">97. What is Structured Logging? <span class="beginner">Beginner</span></div>
<div class="answer">
  <p>Logging in JSON format (key-value) instead of plain text. Easier to query.</p>
</div>

<div id="q98" class="question">98. Distributed Tracing (Jaeger/Zipkin)? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Tracking a request across microservices using a Trace ID and Span IDs.</p>
</div>

<div id="q99" class="question">99. Chaos Engineering? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Intentionally introducing faults (latency, crash) to test system resilience (Netflix Chaos Monkey).</p>
</div>

<div id="q100" class="question">100. Design Facebook Messenger? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>One-on-one vs Group. HBase for message storage. Push notifications for offline users.</p>
</div>
