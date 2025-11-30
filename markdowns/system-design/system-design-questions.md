# System Design Interview Questions

## Table of Contents

1. [Design a URL Shortener (TinyURL)?](#q1-design-a-url-shortener-tinyurl) <span class="intermediate">Intermediate</span>
2. [Design a Rate Limiter?](#q2-design-a-rate-limiter) <span class="intermediate">Intermediate</span>
3. [Design a Chat Application (WhatsApp/Slack)?](#q3-design-a-chat-application-whatsappslack) <span class="advanced">Advanced</span>
4. [Explain CAP Theorem?](#q4-explain-cap-theorem) <span class="beginner">Beginner</span>
5. [Load Balancing: L4 vs L7?](#q5-load-balancing-l4-vs-l7) <span class="intermediate">Intermediate</span>
6. [SQL vs NoSQL: When to choose which?](#q6-sql-vs-nosql-when-to-choose-which) <span class="beginner">Beginner</span>
7. [What is Consistent Hashing?](#q7-what-is-consistent-hashing) <span class="advanced">Advanced</span>
8. [Design a Key-Value Store (like Redis)?](#q8-design-a-key-value-store-like-redis) <span class="advanced">Advanced</span>
9. [What is a CDN and how does it work?](#q9-what-is-a-cdn-and-how-does-it-work) <span class="beginner">Beginner</span>
10. [Design a Notification System?](#q10-design-a-notification-system) <span class="intermediate">Intermediate</span>
11. [Database Sharding vs Replication?](#q11-database-sharding-vs-replication) <span class="intermediate">Intermediate</span>
12. [Design Instagram News Feed?](#q12-design-instagram-news-feed) <span class="advanced">Advanced</span>
13. [What is a Bloom Filter?](#q13-what-is-a-bloom-filter) <span class="advanced">Advanced</span>
14. [Explain Microservices vs Monolith?](#q14-explain-microservices-vs-monolith) <span class="beginner">Beginner</span>
15. [Design a Web Crawler?](#q15-design-a-web-crawler) <span class="advanced">Advanced</span>
16. [How to handle the "Thundering Herd" problem?](#q16-how-to-handle-the-thundering-herd-problem) <span class="advanced">Advanced</span>
17. [Design Google Drive (File Upload/Sync)?](#q17-design-google-drive-file-uploadsync) <span class="advanced">Advanced</span>
18. [What is Backpressure?](#q18-what-is-backpressure) <span class="advanced">Advanced</span>
19. [Design Typeahead Suggestion (Autocomplete)?](#q19-design-typeahead-suggestion-autocomplete) <span class="intermediate">Intermediate</span>
20. [Explain ACID transactions?](#q20-explain-acid-transactions) <span class="beginner">Beginner</span>

---

<div id="q1-design-a-url-shortener-tinyurl" class="question">
  1. Design a URL Shortener (TinyURL)?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <ul>
    <li><strong>Requirements:</strong> Shorten long URLs, redirect short URLs to original, high availability.</li>
    <li><strong>Back-of-envelope:</strong> 100M new URLs/month. 100:1 read/write ratio.</li>
    <li><strong>Database:</strong> NoSQL (K-V store like DynamoDB/Cassandra) is better for scalability.</li>
    <li><strong>Hashing:</strong>
      <ul>
        <li>Use Base62 encoding (a-z, A-Z, 0-9).</li>
        <li>6 characters = 62^6 = ~56 billion combinations.</li>
      </ul>
    </li>
    <li><strong>Collision Handling:</strong> Use a distributed ID generator (Snowflake) or a pre-generated key service (KGS) to ensure unique IDs before encoding.</li>
  </ul>
</div>

<div id="q2-design-a-rate-limiter" class="question">
  2. Design a Rate Limiter?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <ul>
    <li><strong>Goal:</strong> Limit the number of requests a user can send in a time window (e.g., 10 req/sec).</li>
    <li><strong>Algorithms:</strong>
      <ul>
        <li><strong>Token Bucket:</strong> Tokens are added at a constant rate. Request consumes a token. Good for bursty traffic.</li>
        <li><strong>Leaky Bucket:</strong> Requests enter a queue and are processed at a constant rate. Smooths out traffic.</li>
        <li><strong>Fixed Window Counter:</strong> Simple, but has edge case issues at window boundaries.</li>
      </ul>
    </li>
    <li><strong>Implementation:</strong> Redis (fast in-memory store) with `INCR` and expiration.</li>
  </ul>
</div>

<div id="q3-design-a-chat-application-whatsappslack" class="question">
  3. Design a Chat Application (WhatsApp/Slack)?
  <span class="difficulty advanced">Advanced</span>
</div>

<div class="answer">
  <ul>
    <li><strong>Protocol:</strong> WebSockets (persistent connection) for real-time bidirectional communication.</li>
    <li><strong>Message Storage:</strong>
      <ul>
        <li>Ephemeral (just for delivery): Redis.</li>
        <li>Persistent (History): Cassandra or HBase (write-heavy, time-series data).</li>
      </ul>
    </li>
    <li><strong>Status:</strong> "Sent", "Delivered", "Read". Handled via acknowledgments (ACKs).</li>
    <li><strong>Group Chat:</strong> Fan-out on write (for small groups) or Fan-out on read (for huge channels).</li>
  </ul>
</div>

<div id="q4-explain-cap-theorem" class="question">
  4. Explain CAP Theorem?
  <span class="difficulty beginner">Beginner</span>
</div>

<div class="answer">
  <p>In a distributed system, you can only satisfy two of the following three guarantees:</p>
  <ul>
    <li><strong>Consistency (C):</strong> Every read receives the most recent write or an error.</li>
    <li><strong>Availability (A):</strong> Every request receives a (non-error) response, without the guarantee that it contains the most recent write.</li>
    <li><strong>Partition Tolerance (P):</strong> The system continues to operate despite an arbitrary number of messages being dropped/delayed by the network.</li>
  </ul>
  <p>Since network partitions (P) are inevitable, you must choose between <strong>CP</strong> (Banking) or <strong>AP</strong> (Social Media).</p>
</div>

<div id="q5-load-balancing-l4-vs-l7" class="question">
  5. Load Balancing: L4 vs L7?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <ul>
    <li><strong>L4 (Transport Layer):</strong> Routes based on IP and Port.
      <ul>
        <li>Pros: Very fast, efficient, packet-level.</li>
        <li>Cons: No insight into content (cannot route based on URL path).</li>
      </ul>
    </li>
    <li><strong>L7 (Application Layer):</strong> Routes based on HTTP content (URL, Headers, Cookies).
      <ul>
        <li>Pros: Smart routing (e.g., `/api` to Backend service, `/static` to CDN).</li>
        <li>Cons: More CPU intensive (requires decrypting HTTPS).</li>
      </ul>
    </li>
  </ul>
</div>

<div id="q6-sql-vs-nosql-when-to-choose-which" class="question">
  6. SQL vs NoSQL: When to choose which?
  <span class="difficulty beginner">Beginner</span>
</div>

<div class="answer">
  <ul>
    <li><strong>Choose SQL (Relational):</strong>
      <ul>
        <li>You need ACID compliance (Financial transactions).</li>
        <li>Your data is structured and has strict schemas.</li>
        <li>You need complex joins.</li>
      </ul>
    </li>
    <li><strong>Choose NoSQL (Non-Relational):</strong>
      <ul>
        <li>You need extremely high write throughput.</li>
        <li>Your data is unstructured or semi-structured (JSON).</li>
        <li>You need horizontal scaling (sharding is native).</li>
        <li>Examples: Analytics, Real-time feeds, Caching.</li>
      </ul>
    </li>
  </ul>
</div>

<div id="q7-what-is-consistent-hashing" class="question">
  7. What is Consistent Hashing?
  <span class="difficulty advanced">Advanced</span>
</div>

<div class="answer">
  <p>A technique to distribute keys across a dynamic number of servers (nodes).</p>
  <ul>
    <li><strong>Problem:</strong> With `hash(key) % N`, if N changes (server dies/added), almost ALL keys get remapped.</li>
    <li><strong>Solution:</strong> Map both servers and keys to a "Hash Ring" (0 to 2^32).</li>
    <li>A key is assigned to the first server found moving clockwise on the ring.</li>
    <li><strong>Benefit:</strong> When a server is added/removed, only `K/N` keys need to be moved.</li>
    <li>Used in: DynamoDB, Cassandra, Discord.</li>
  </ul>
</div>

<div id="q8-design-a-key-value-store-like-redis" class="question">
  8. Design a Key-Value Store (like Redis)?
  <span class="difficulty advanced">Advanced</span>
</div>

<div class="answer">
  <ul>
    <li><strong>Data Structure:</strong> Hash Map (in-memory) for O(1) access.</li>
    <li><strong>Persistence:</strong>
      <ul>
        <li>Snapshotting (RDB): Periodically save DB to disk.</li>
        <li>AOF (Append Only File): Log every write operation.</li>
      </ul>
    </li>
    <li><strong>Eviction Policy:</strong> LRU (Least Recently Used) when memory is full.</li>
    <li><strong>Concurrency:</strong> Single-threaded event loop (avoids locking overhead) or highly granular locking.</li>
  </ul>
</div>

<div id="q9-what-is-a-cdn-and-how-does-it-work" class="question">
  9. What is a CDN and how does it work?
  <span class="difficulty beginner">Beginner</span>
</div>

<div class="answer">
  <p><strong>Content Delivery Network (CDN):</strong> A network of geographically distributed servers used to deliver static content (images, CSS, JS, videos) closer to the user.</p>
  <ul>
    <li><strong>How it works:</strong>
      <ol>
        <li>User requests image.</li>
        <li>DNS routes user to nearest Edge Server.</li>
        <li>If content is cached, return it.</li>
        <li>If miss, fetch from Origin, cache it, and return it.</li>
      </ol>
    </li>
    <li><strong>Benefits:</strong> Reduced latency, reduced load on origin servers.</li>
  </ul>
</div>

<div id="q10-design-a-notification-system" class="question">
  10. Design a Notification System?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <ul>
    <li><strong>Components:</strong>
      <ul>
        <li><strong>Notification Service:</strong> Exposes API to trigger notifications.</li>
        <li><strong>Message Queue (Kafka/RabbitMQ):</strong> Decouples triggering from sending. Buffers bursts.</li>
        <li><strong>Workers:</strong> Pull from queue and call 3rd party providers.</li>
        <li><strong>3rd Party Providers:</strong> APNS/FCM (Mobile), SendGrid (Email), Twilio (SMS).</li>
      </ul>
    </li>
    <li><strong>Reliability:</strong> Retry mechanism with exponential backoff for failed sends.</li>
  </ul>
</div>

<div id="q11-database-sharding-vs-replication" class="question">
  11. Database Sharding vs Replication?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <ul>
    <li><strong>Replication:</strong> Copying data to multiple nodes.
      <ul>
        <li>Pros: High Availability, Read Scalability (read from replicas).</li>
        <li>Cons: Write latency (if sync), eventual consistency. Does not solve storage limits.</li>
      </ul>
    </li>
    <li><strong>Sharding:</strong> Partitioning data across multiple nodes (e.g., Users A-M on DB1, N-Z on DB2).
      <ul>
        <li>Pros: Horizontal scaling of Write throughput and Storage capacity.</li>
        <li>Cons: Complex queries (joins across shards), re-sharding is painful.</li>
      </ul>
    </li>
  </ul>
</div>

<div id="q12-design-instagram-news-feed" class="question">
  12. Design Instagram News Feed?
  <span class="difficulty advanced">Advanced</span>
</div>

<div class="answer">
  <ul>
    <li><strong>Pull Model (Fan-out on Load):</strong> When user opens app, fetch all followings, get their latest posts, merge and sort. Good for small following lists.</li>
    <li><strong>Push Model (Fan-out on Write):</strong> When a user posts, push the ID to all followers' pre-computed feed lists. fast reads. Bad for celebrities (millions of followers).</li>
    <li><strong>Hybrid:</strong> Push for normal users, Pull for celebrities.</li>
  </ul>
</div>

<div id="q13-what-is-a-bloom-filter" class="question">
  13. What is a Bloom Filter?
  <span class="difficulty advanced">Advanced</span>
</div>

<div class="answer">
  <p>A space-efficient probabilistic data structure to test if an element is in a set.</p>
  <ul>
    <li><strong>False Positives:</strong> Possible ("It might be there").</li>
    <li><strong>False Negatives:</strong> Impossible ("It is definitely not there").</li>
    <li><strong>Usage:</strong> Checking if a username is taken, checking if a URL is malicious (Chrome), reducing disk lookups (Cassandra/HBase check bloom filter before checking disk).</li>
  </ul>
</div>

<div id="q14-explain-microservices-vs-monolith" class="question">
  14. Explain Microservices vs Monolith?
  <span class="difficulty beginner">Beginner</span>
</div>

<div class="answer">
  <ul>
    <li><strong>Monolith:</strong> Single codebase, single deployment unit.
      <ul>
        <li>Pros: Simple to develop/test initially, easy transactions.</li>
        <li>Cons: Hard to scale specific parts, tight coupling, single point of failure.</li>
      </ul>
    </li>
    <li><strong>Microservices:</strong> Loosely coupled services, independent deployment.
      <ul>
        <li>Pros: Independent scaling, technology agnostic, fault isolation.</li>
        <li>Cons: Distributed complexity (network latency, distributed tracing, consistency).</li>
      </ul>
    </li>
  </ul>
</div>

<div id="q15-design-a-web-crawler" class="question">
  15. Design a Web Crawler?
  <span class="difficulty advanced">Advanced</span>
</div>

<div class="answer">
  <ul>
    <li><strong>Seed URLs:</strong> Starting point.</li>
    <li><strong>URL Frontier (Queue):</strong> Prioritizes which URLs to crawl next (BFS/DFS). Needs politeness (don't DDoS servers).</li>
    <li><strong>Fetcher:</strong> Downloads HTML.</li>
    <li><strong>DNS Resolver:</strong> Caches IP addresses.</li>
    <li><strong>Content Deduplication:</strong> Compute fingerprint (checksum) of content to avoid storing duplicates.</li>
    <li><strong>Robots.txt:</strong> Must respect exclusion protocols.</li>
  </ul>
</div>

<div id="q16-how-to-handle-the-thundering-herd-problem" class="question">
  16. How to handle the "Thundering Herd" problem?
  <span class="difficulty advanced">Advanced</span>
</div>

<div class="answer">
  <p>Occurs when a popular cache item expires, and thousands of requests hit the database simultaneously to regenerate it.</p>
  <ul>
    <li><strong>Solution 1:</strong> Probabilistic Early Expiration (re-cache before it actually expires).</li>
    <li><strong>Solution 2:</strong> Mutex/Locking (only one process regenerates, others wait).</li>
    <li><strong>Solution 3:</strong> Exponential Backoff on retries.</li>
  </ul>
</div>

<div id="q17-design-google-drive-file-uploadsync" class="question">
  17. Design Google Drive (File Upload/Sync)?
  <span class="difficulty advanced">Advanced</span>
</div>

<div class="answer">
  <ul>
    <li><strong>Block Level Storage:</strong> Split large files into chunks (e.g., 4MB). Only upload modified chunks (differential sync).</li>
    <li><strong>Metadata DB:</strong> Stores file hierarchy, permissions, and block mappings (SQL/NoSQL).</li>
    <li><strong>Object Storage (S3):</strong> Stores the actual blocks.</li>
    <li><strong>Client:</strong> Watches local FS changes, queues uploads. Uses hashing to detect changes.</li>
  </ul>
</div>

<div id="q18-what-is-backpressure" class="question">
  18. What is Backpressure?
  <span class="difficulty advanced">Advanced</span>
</div>

<div class="answer">
  <p>A mechanism in data stream handling where a consumer signals the producer to slow down because it cannot keep up with the rate of data.</p>
  <ul>
    <li>Prevents the consumer from being overwhelmed (OOM crashes).</li>
    <li><strong>Strategies:</strong>
      <ul>
        <li><strong>Buffering:</strong> Store excess in a queue (limited capacity).</li>
        <li><strong>Dropping:</strong> Drop new messages (lossy).</li>
        <li><strong>Control:</strong> Pause the producer (TCP window sizing).</li>
      </ul>
    </li>
  </ul>
</div>

<div id="q19-design-typeahead-suggestion-autocomplete" class="question">
  19. Design Typeahead Suggestion (Autocomplete)?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <ul>
    <li><strong>Data Structure:</strong> Trie (Prefix Tree). Each node stores top N popular searches.</li>
    <li><strong>Optimization:</strong> Store data in memory or use a specialized search engine like Elasticsearch.</li>
    <li><strong>Update:</strong> Offline aggregation of logs (MapReduce) to update frequencies daily/hourly.</li>
    <li><strong>Sampling:</strong> Only log a percentage of queries to reduce volume.</li>
  </ul>
</div>

<div id="q20-explain-acid-transactions" class="question">
  20. Explain ACID transactions?
  <span class="difficulty beginner">Beginner</span>
</div>

<div class="answer">
  <ul>
    <li><strong>Atomicity:</strong> All or nothing.</li>
    <li><strong>Consistency:</strong> Database goes from one valid state to another (constraints satisfied).</li>
    <li><strong>Isolation:</strong> Concurrent transactions do not interfere (Serializability).</li>
    <li><strong>Durability:</strong> Once committed, data stays saved even after power loss.</li>
  </ul>
</div>
