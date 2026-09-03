<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Modern Networking Protocols (HTTP/3, QUIC, gRPC) Logo" width="100" height="100">
  </a>
  <h1>Modern Networking Protocols (HTTP/3, QUIC, gRPC) Interview Questions & Answers</h1>
  <p><b>Comprehensive interview questions covering HTTP/3, QUIC 0-RTT, Head-of-Line Blocking, Protobuf Varints, and BBR</b></p>
</div>

---

## Table of Contents

1. [How does HTTP/3 over QUIC eliminate TCP Head-of-Line (HoL) Blocking at the transport layer?](#q1) <span class="advanced">Advanced</span>
2. [How does QUIC achieve 0-RTT Connection Resumption and how are Replay Attacks prevented?](#q2) <span class="advanced">Advanced</span>
3. [How do QUIC Connection IDs enable Seamless Connection Migration between Wi-Fi and Cellular networks?](#q3) <span class="advanced">Advanced</span>
4. [How does Protocol Buffers (Protobuf) encode integers using Variable-Length Quantity (Varints) and ZigZag encoding?](#q4) <span class="advanced">Advanced</span>
5. [How does Google BBR (Bottleneck Bandwidth and RTT) Congestion Control differ from loss-based algorithms (CUBIC, Reno)?](#q5) <span class="advanced">Advanced</span>
6. [What is HTTP/2 HPACK Header Compression and how does it prevent CRIME attacks?](#q6) <span class="advanced">Advanced</span>
7. [How does gRPC Bidirectional Streaming work over HTTP/2 framing?](#q7) <span class="intermediate">Intermediate</span>
8. [What is Nagle's Algorithm (`TCP_NODELAY`) and why does its interaction with Delayed ACKs cause 40ms latency spikes?](#q8) <span class="advanced">Advanced</span>
9. [How does TCP Slow Start and Congestion Avoidance determine Congestion Window (`cwnd`) growth?](#q9) <span class="intermediate">Intermediate</span>
10. [What is the difference between TCP Flow Control (Sliding Window) and Congestion Control?](#q10) <span class="beginner">Beginner</span>
11. [How does TLS 1.3 simplify cipher suites and eliminate insecure algorithms?](#q11) <span class="intermediate">Intermediate</span>
12. [What is Application-Layer Protocol Negotiation (ALPN) in TLS handshakes?](#q12) <span class="intermediate">Intermediate</span>
13. [How do gRPC Deadlines and Context Cancellation propagate across microservice call trees?](#q13) <span class="intermediate">Intermediate</span>
14. [What is WebTransport over HTTP/3 and how does it replace WebSockets with bidirectional streams and datagrams?](#q14) <span class="advanced">Advanced</span>
15. [How does TCP Fast Retransmit and Fast Recovery work with 3 Duplicate ACKs?](#q15) <span class="intermediate">Intermediate</span>
16. [What are SYN Cookies and how do they defend against TCP SYN Flood attacks without memory allocation?](#q16) <span class="advanced">Advanced</span>
17. [How does MTU and Path MTU Discovery (PMTUD) prevent IP packet fragmentation?](#q17) <span class="intermediate">Intermediate</span>
18. [What is gRPC Interceptors and how do you implement authentication and tracing middleware?](#q18) <span class="intermediate">Intermediate</span>
19. [How does WebSocket Frame Masking work and why must clients mask frames while servers do not?](#q19) <span class="intermediate">Intermediate</span>
20. [What is TCP Selective Acknowledgment (SACK) and how does it prevent unnecessary retransmissions?](#q20) <span class="intermediate">Intermediate</span>
21. [How does Anycast BGP routing distribute network traffic across globally distributed CDN servers?](#q21) <span class="advanced">Advanced</span>
22. [What is DNS over TLS (DoT) vs DNS over HTTPS (DoH)?](#q22) <span class="beginner">Beginner</span>
23. [How does Server-Sent Events (SSE) compare to WebSockets for real-time streaming?](#q23) <span class="beginner">Beginner</span>
24. [What is Happy Eyeballs Algorithm (RFC 8305) in dual-stack IPv4/IPv6 client connections?](#q24) <span class="intermediate">Intermediate</span>
25. [How does HTTP/2 Server Push work and why was it deprecated in major browsers?](#q25) <span class="intermediate">Intermediate</span>
26. [What is gRPC Channel Subchannel Architecture and Connection Pooling?](#q26) <span class="advanced">Advanced</span>
27. [How does TCP Window Scaling Option (RFC 7323) enable 1GB sliding windows?](#q27) <span class="intermediate">Intermediate</span>
28. [What is TCP TIME_WAIT state and why is 2x Maximum Segment Lifetime (MSL) necessary?](#q28) <span class="intermediate">Intermediate</span>
29. [How does Protobuf schema evolution ensure Backward and Forward Compatibility?](#q29) <span class="intermediate">Intermediate</span>
30. [What is Epoll vs Kqueue in high-performance networking runtimes?](#q30) <span class="advanced">Advanced</span>
31. [How do Modern Firewalls implement Stateful Packet Inspection (SPI) with Conntrack tables?](#q31) <span class="intermediate">Intermediate</span>
32. [What is gRPC Protobuf Field Mask and how does it implement Partial Updates (PATCH)?](#q32) <span class="intermediate">Intermediate</span>
33. [How does TLS Session Resumption with Session Tickets (RFC 5077) work?](#q33) <span class="intermediate">Intermediate</span>
34. [What is QUIC Flow Control at Connection Level vs Stream Level?](#q34) <span class="advanced">Advanced</span>
35. [How does TCP Keepalive detect dead peers across cloud network firewalls?](#q35) <span class="beginner">Beginner</span>
36. [What is Maximum Segment Size (MSS) and how is it calculated from MTU?](#q36) <span class="beginner">Beginner</span>
37. [How do Reverse Proxies (Envoy, Nginx) handle HTTP/2 to HTTP/1.1 protocol translation?](#q37) <span class="intermediate">Intermediate</span>
38. [What is BGP Route Flapping and how does Route Flap Damping stabilize routing tables?](#q38) <span class="advanced">Advanced</span>
39. [How does gRPC Load Balancing work: Client-Side (Lookaside / Envoy) vs Proxy-Based?](#q39) <span class="advanced">Advanced</span>
40. [What is TCP SYN-ACK Retransmission Exponential Backoff?](#q40) <span class="intermediate">Intermediate</span>
41. [How does WebRTC NAT Traversal work with STUN, TURN, and ICE candidate gathering?](#q41) <span class="advanced">Advanced</span>
42. [What is DiffServ (Differentiated Services) and DSCP Bits in IP Quality of Service (QoS)?](#q42) <span class="intermediate">Intermediate</span>
43. [How do gRPC Custom Metadata Headers (`metadata.MD`) pass contextual information?](#q43) <span class="intermediate">Intermediate</span>
44. [What is BBRv2 and how does it improve co-existence with CUBIC flows?](#q44) <span class="advanced">Advanced</span>
45. [How does IP Anycast handle BGP route shifts mid-connection?](#q45) <span class="advanced">Advanced</span>
46. [What is TCP Urgent Pointer and Out-of-Band (OOB) data?](#q46) <span class="beginner">Beginner</span>
47. [How do Microservices implement Circuit Breaking at the transport layer using Envoy?](#q47) <span class="intermediate">Intermediate</span>
48. [What is HTTP Early Hints (Status Code 103) and how does it accelerate critical CSS/JS loading?](#q48) <span class="intermediate">Intermediate</span>
49. [How does TCP Reno calculate Additive Increase Multiplicative Decrease (AIMD)?](#q49) <span class="beginner">Beginner</span>
50. [What is the difference between Unary RPC, Client-Streaming, Server-Streaming, and Bidirectional Streaming in gRPC?](#q50) <span class="beginner">Beginner</span>
51. [How does QUIC encrypt packet headers to prevent ISP ossification and traffic tampering?](#q51) <span class="advanced">Advanced</span>
52. [What is Network Byte Order (Big-Endian) and why is it mandatory in network protocols?](#q52) <span class="beginner">Beginner</span>
53. [How does gRPC handle Service Reflection for dynamic CLI debugging (grpcurl)?](#q53) <span class="intermediate">Intermediate</span>
54. [What is Explicit Congestion Notification (ECN) in IP and TCP headers?](#q54) <span class="advanced">Advanced</span>
55. [How does TCP Zero Window and Window Probe packets handle saturated receivers?](#q55) <span class="intermediate">Intermediate</span>
56. [What is QUIC Packet Number vs Stream Offset?](#q56) <span class="advanced">Advanced</span>
57. [How do WebSockets handle Heartbeats with Ping and Pong frames?](#q57) <span class="beginner">Beginner</span>
58. [What is TCP Segmentation Offload (TSO) in hardware network interface cards?](#q58) <span class="intermediate">Intermediate</span>
59. [How does gRPC Status Codes (`OK`, `NOT_FOUND`, `UNAVAILABLE`, `DEADLINE_EXCEEDED`) map to HTTP status codes?](#q59) <span class="beginner">Beginner</span>
60. [What is the role of the BGP Autonomous System (AS) and AS-Path attribute?](#q60) <span class="intermediate">Intermediate</span>
61. [How does Path MTU Discovery handle Black Hole Routers that drop packets without sending ICMP errors?](#q61) <span class="advanced">Advanced</span>
62. [What is HTTP/2 Flow Control Credit Starvation and how do you tune window sizes?](#q62) <span class="advanced">Advanced</span>
63. [How do CDN Edge Servers use TCP BBR to accelerate file downloads across lossy mobile networks?](#q63) <span class="intermediate">Intermediate</span>
64. [What is SCTP (Stream Control Transmission Protocol) and why is it used in telecom signalling (SS7/SIGTRAN)?](#q64) <span class="advanced">Advanced</span>
65. [How does DNS Anycast enable Geo-DNS routing for global enterprises?](#q65) <span class="intermediate">Intermediate</span>
66. [What is TCP Selective Acknowledgement (SACK) Renéging and how does the kernel handle it?](#q66) <span class="advanced">Advanced</span>
67. [How does gRPC Channel State Machine transition between `IDLE`, `CONNECTING`, `READY`, and `TRANSIENT_FAILURE`?](#q67) <span class="intermediate">Intermediate</span>
68. [What is the difference between Forward Proxy and Reverse Proxy in enterprise networks?](#q68) <span class="beginner">Beginner</span>
69. [How does TLS 1.3 Key Update message refresh symmetric keys during long-running streaming connections?](#q69) <span class="advanced">Advanced</span>
70. [What is HTTP/2 Priority Trees (RFC 7540) and why did RFC 9218 replace them with Extensible Priorities?](#q70) <span class="advanced">Advanced</span>
71. [How does Path MTU Discovery work in QUIC (PMTU Probe packets)?](#q71) <span class="advanced">Advanced</span>
72. [What is TCP RST (Reset) packet and when does the kernel emit it?](#q72) <span class="beginner">Beginner</span>
73. [How do Mobile Clients handle IP Roaming with MPTCP (Multipath TCP)?](#q73) <span class="advanced">Advanced</span>
74. [What is the difference between State-Machine Parsers and Regular-Expression Parsers for network protocols?](#q74) <span class="intermediate">Intermediate</span>
75. [How does gRPC implement Health Checking Protocol (`grpc.health.v1.Health`)?](#q75) <span class="intermediate">Intermediate</span>
76. [What is BGP Hijacking and how does RPKI (Resource Public Key Infrastructure) prevent it?](#q76) <span class="advanced">Advanced</span>
77. [How does WebSocket Per-Message Deflate compression work and what are the security trade-offs?](#q77) <span class="intermediate">Intermediate</span>
78. [What is TCP Small Queues (TSQ) in Linux and how does it combat Bufferbloat on local interfaces?](#q78) <span class="advanced">Advanced</span>
79. [How does gRPC Name Resolution (DNS vs Consul vs Kubernetes) resolve service targets?](#q79) <span class="intermediate">Intermediate</span>
80. [What is QUIC Spin Bit and how does it allow passive network latency monitoring by operators?](#q80) <span class="advanced">Advanced</span>
81. [How do Network Sockets handle Socket Buffer Auto-Tuning (`tcp_moderate_rcvbuf`)?](#q81) <span class="intermediate">Intermediate</span>
82. [What is HTTP/2 CONTINUATION Frame and how did CONTINUATION Flood vulnerabilities cause DoS?](#q82) <span class="advanced">Advanced</span>
83. [How does TLS Session Resumption with Pre-Shared Keys (PSK) operate in TLS 1.3?](#q83) <span class="intermediate">Intermediate</span>
84. [What is TCP Simultaneous Open?](#q84) <span class="advanced">Advanced</span>
85. [How does gRPC Compression (gzip, snappy, zstd) reduce wire bandwidth for large payloads?](#q85) <span class="beginner">Beginner</span>
86. [What is Anycast BGP Anycast-to-Unicast Failover in CDN origin shielding?](#q86) <span class="advanced">Advanced</span>
87. [How does Linux TCP receive offload with GRO (Generic Receive Offload) reduce CPU usage?](#q87) <span class="intermediate">Intermediate</span>
88. [What is HTTP Strict Transport Security (HSTS) and HSTS Preloading?](#q88) <span class="beginner">Beginner</span>
89. [How do Distributed Systems implement Distributed Tracing Context Propagation across gRPC metadata?](#q89) <span class="intermediate">Intermediate</span>
90. [What is TCP Cork (`TCP_CORK`) and how does it compare to `TCP_NODELAY`?](#q90) <span class="intermediate">Intermediate</span>
91. [How does QUIC handle Amplification Attack Defense on initial handshakes?](#q91) <span class="advanced">Advanced</span>
92. [What is WebSocket subprotocol negotiation (`Sec-WebSocket-Protocol`)?](#q92) <span class="beginner">Beginner</span>
93. [What is TCP Out-of-Order Queue and how does memory exhaustion affect high-bandwidth servers?](#q93) <span class="advanced">Advanced</span>
94. [How does QUIC Stateless Reset protect servers that lose connection state after a reboot?](#q94) <span class="advanced">Advanced</span>
95. [What is TCP Slow Start Threshold (`ssthresh`) and how does it transition to Congestion Avoidance?](#q95) <span class="intermediate">Intermediate</span>
96. [How do WebSockets handle Closing Handshake with Status Codes (1000, 1006)?](#q96) <span class="beginner">Beginner</span>
97. [What is the difference between HTTP/2 SETTINGS frames and WINDOW_UPDATE frames?](#q97) <span class="intermediate">Intermediate</span>
98. [How does gRPC Retry Policy handle transient network disconnects?](#q98) <span class="intermediate">Intermediate</span>
99. [What is QUIC Cryptographic Key Derivation during Handshake Phases?](#q99) <span class="advanced">Advanced</span>
100. [How does TCP SACK Permitted option negotiation work in SYN packets?](#q100) <span class="beginner">Beginner</span>

---

<a id="q1"></a>
### Q1: How does HTTP/3 over QUIC eliminate TCP Head-of-Line (HoL) Blocking at the transport layer?

**Difficulty**: Advanced

**Strategy**:
In HTTP/2, all multiplexed application streams share a single underlying TCP connection. If a single packet is lost in the network, the TCP receiver window stalls and blocks all streams while waiting for the missing packet to be retransmitted (TCP Head-of-Line Blocking). HTTP/3 replaces TCP with QUIC over UDP. In QUIC, streams are first-class transport primitives: packet loss on Stream A does not stall or delay packet delivery on independent Streams B, C, or D, dramatically reducing tail latency on lossy cellular and Wi-Fi networks.

**Code Example**:
```text
HTTP/2 over TCP vs HTTP/3 over QUIC:
HTTP/2 (TCP): [Packet 1 (Stream A)] [Packet 2 (Stream B - LOST!)] [Packet 3 (Stream C)]
             -> TCP stalls! Stream C cannot be processed until Packet 2 retransmits.
HTTP/3 (QUIC):[Packet 1 (Stream A)] [Packet 2 (Stream B - LOST!)] [Packet 3 (Stream C)]
             -> Stream C delivered immediately! Only Stream B waits for retransmission.
```

---

<a id="q2"></a>
### Q2: How does QUIC achieve 0-RTT Connection Resumption and how are Replay Attacks prevented?

**Difficulty**: Advanced

**Strategy**:
Traditional TCP + TLS 1.3 requires 2-3 round trips (1 RTT TCP SYN/ACK + 1 RTT TLS handshake) before sending application data. QUIC combines the transport and cryptographic handshake. On initial connection, client caches server cryptographic parameters and a session ticket. On subsequent connections, the client encrypts early application data (HTTP GET) and transmits it inside the very first UDP datagram (0-RTT). To prevent Replay Attacks (adversary re-broadcasting 0-RTT payment packets), servers forbid 0-RTT on non-idempotent requests (POST/PUT) and enforce strict single-use ticket timestamps and server bloom filters.

**Code Example**:
```text
Latency Handshake Comparison:
TCP + TLS 1.2: [SYN] -> [SYN/ACK] -> [ClientHello] -> [ServerHello] -> [Data] (3 RTT)
TCP + TLS 1.3: [SYN] -> [SYN/ACK] -> [ClientHello+KeyShare] -> [ServerHello] -> [Data] (2 RTT)
QUIC 1-RTT:    [QUIC Initial+KeyShare] -> [QUIC Handshake+Finished] -> [Data] (1 RTT)
QUIC 0-RTT:    [QUIC Initial + Encrypted 0-RTT Data] -> Data processed immediately! (0 RTT)
```

---

<a id="q3"></a>
### Q3: How do QUIC Connection IDs enable Seamless Connection Migration between Wi-Fi and Cellular networks?

**Difficulty**: Advanced

**Strategy**:
TCP connections are identified by a 4-tuple: `(src_ip, src_port, dst_ip, dst_port)`. If a mobile device transitions from Wi-Fi to 5G cellular, its IP address changes, permanently breaking all active TCP sockets and requiring reconnecting. QUIC identifies connections using a 64-bit cryptographic Connection ID (CID) independent of IP and port. When the client's network interface switches, it sends packets from its new IP using the existing CID; the server verifies the authenticated packet and migrates the connection without dropping in-flight transfers.

**Code Example**:
```text
Connection Migration Flow:
Client (Wi-Fi 192.168.1.5) -> Server 1.2.3.4 [QUIC CID: 0x8a7b9c1d]
[User walks out of house -> Switches to 5G Cellular IP 100.64.2.10]
Client (5G 100.64.2.10)   -> Server 1.2.3.4 [QUIC CID: 0x8a7b9c1d]
Server verifies cryptographic signature -> Connection stays alive without reconnecting!
```

---

<a id="q4"></a>
### Q4: How does Protocol Buffers (Protobuf) encode integers using Variable-Length Quantity (Varints) and ZigZag encoding?

**Difficulty**: Advanced

**Strategy**:
Standard integers consume fixed 32 or 64 bits regardless of value. Protobuf uses Varints: each byte uses 7 bits for data and the Most Significant Bit (MSB, bit 7) as a continuation flag (`1` = more bytes follow, `0` = last byte). Small integers ($<128$) consume only 1 byte. Negative numbers in two's complement have high-order bits set to `1` (which would take 10 bytes as a varint). Protobuf applies ZigZag encoding, mapping signed integers to unsigned values: $n \rightarrow (n \ll 1) \oplus (n \gg 31)$, interleaving positive and negative numbers so small negative numbers ($-1, -2$) compress to 1-2 bytes.

**Code Example**:
```python
# Protobuf ZigZag Encoding in Python
def zigzag_encode(n):
    return (n << 1) ^ (n >> 31) if n >= 0 else (n << 1) ^ (n >> 31)
# -1 -> 1 (0x01, 1 byte!)
#  1 -> 2 (0x02, 1 byte!)
# -2 -> 3 (0x03, 1 byte!)
```

---

<a id="q5"></a>
### Q5: How does Google BBR (Bottleneck Bandwidth and RTT) Congestion Control differ from loss-based algorithms (CUBIC, Reno)?

**Difficulty**: Advanced

**Strategy**:
CUBIC and Reno interpret packet loss as the sole signal of network congestion. They keep increasing sending rates until intermediate router buffers overflow and drop packets (Bufferbloat), resulting in massive queuing latency and erratic throughput sawtooth curves. BBR models the physical network by continuously estimating two parameters: 1) Maximum Bottleneck Bandwidth (Max Bw), and 2) Minimum Round-Trip Time (Min RTT). BBR sends data at the exact processing rate of the bottleneck link without filling queues, achieving maximum throughput with minimal queuing latency.

**Code Example**:
```text
Bufferbloat vs BBR:
Loss-Based (CUBIC): Keeps sending until router queue is 100% full -> Packets drop -> Latency spikes to 500ms!
Model-Based (BBR):  Sends at exact rate router can process (BDP = Bw * RTT) -> Router queue stays empty -> Latency < 20ms!
```

---

<a id="q6"></a>
### Q6: What is HTTP/2 HPACK Header Compression and how does it prevent CRIME attacks?

**Difficulty**: Advanced

**Strategy**:
Uses a static table of 61 common headers, a dynamic table tracking connection headers, and Huffman encoding; disables compression on sensitive cookies to prevent CRIME/BREACH.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is HTTP/2 HPACK Header Compression and how does it prevent CRIME attacks?
Verified enterprise transport implementation
```

---

<a id="q7"></a>
### Q7: How does gRPC Bidirectional Streaming work over HTTP/2 framing?

**Difficulty**: Intermediate

**Strategy**:
Uses HTTP/2 data frames to stream messages in both directions concurrently over a single TCP connection; client and server read/write independently without waiting for responses.

**Code Example**:
```text
Modern Networking Protocol Specification for: How does gRPC Bidirectional Streaming work over HTTP/2 framing?
Verified enterprise transport implementation
```

---

<a id="q8"></a>
### Q8: What is Nagle's Algorithm (`TCP_NODELAY`) and why does its interaction with Delayed ACKs cause 40ms latency spikes?

**Difficulty**: Advanced

**Strategy**:
Nagle delays sending small packets until previous packet is ACKed; Delayed ACK waits up to 40ms to acknowledge packets; together they cause deadlocks on request-response protocols.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is Nagle's Algorithm (`TCP_NODELAY`) and why does its interaction with Delayed ACKs cause 40ms latency spikes?
Verified enterprise transport implementation
```

---

<a id="q9"></a>
### Q9: How does TCP Slow Start and Congestion Avoidance determine Congestion Window (`cwnd`) growth?

**Difficulty**: Intermediate

**Strategy**:
Slow start doubles `cwnd` exponentially every RTT until reaching `ssthresh`; then transitions to Congestion Avoidance, increasing `cwnd` linearly by 1 MSS per RTT.

**Code Example**:
```text
Modern Networking Protocol Specification for: How does TCP Slow Start and Congestion Avoidance determine Congestion Window (`cwnd`) growth?
Verified enterprise transport implementation
```

---

<a id="q10"></a>
### Q10: What is the difference between TCP Flow Control (Sliding Window) and Congestion Control?

**Difficulty**: Beginner

**Strategy**:
Flow control protects the receiver from buffer overflow using the Receive Window (`rwnd`); Congestion control protects the intermediate network routers using `cwnd`.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is the difference between TCP Flow Control (Sliding Window) and Congestion Control?
Verified enterprise transport implementation
```

---

<a id="q11"></a>
### Q11: How does TLS 1.3 simplify cipher suites and eliminate insecure algorithms?

**Difficulty**: Intermediate

**Strategy**:
Removes static RSA key exchange, CBC ciphers, and SHA-1; retains only forward-secret AEAD ciphers (AES-GCM, ChaCha20-Poly1305) with ECDHE key exchange in 1 RTT.

**Code Example**:
```text
Modern Networking Protocol Specification for: How does TLS 1.3 simplify cipher suites and eliminate insecure algorithms?
Verified enterprise transport implementation
```

---

<a id="q12"></a>
### Q12: What is Application-Layer Protocol Negotiation (ALPN) in TLS handshakes?

**Difficulty**: Intermediate

**Strategy**:
TLS extension allowing client and server to negotiate application protocol (`h2`, `h3`, `http/1.1`) securely inside the TLS handshake before sending HTTP bytes.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is Application-Layer Protocol Negotiation (ALPN) in TLS handshakes?
Verified enterprise transport implementation
```

---

<a id="q13"></a>
### Q13: How do gRPC Deadlines and Context Cancellation propagate across microservice call trees?

**Difficulty**: Intermediate

**Strategy**:
Propagates `grpc-timeout` header across downstream services; when deadline expires, all intermediate services cancel processing and release resources immediately.

**Code Example**:
```text
Modern Networking Protocol Specification for: How do gRPC Deadlines and Context Cancellation propagate across microservice call trees?
Verified enterprise transport implementation
```

---

<a id="q14"></a>
### Q14: What is WebTransport over HTTP/3 and how does it replace WebSockets with bidirectional streams and datagrams?

**Difficulty**: Advanced

**Strategy**:
Browser API built on HTTP/3 QUIC; supports reliable unidirectional/bidirectional streams and unreliable datagrams (UDP-like) for gaming and real-time media.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is WebTransport over HTTP/3 and how does it replace WebSockets with bidirectional streams and datagrams?
Verified enterprise transport implementation
```

---

<a id="q15"></a>
### Q15: How does TCP Fast Retransmit and Fast Recovery work with 3 Duplicate ACKs?

**Difficulty**: Intermediate

**Strategy**:
When receiver gets out-of-order packet, it sends duplicate ACK; on receiving 3 duplicate ACKs, sender retransmits missing packet without waiting for retransmission timeout (RTO).

**Code Example**:
```text
Modern Networking Protocol Specification for: How does TCP Fast Retransmit and Fast Recovery work with 3 Duplicate ACKs?
Verified enterprise transport implementation
```

---

<a id="q16"></a>
### Q16: What are SYN Cookies and how do they defend against TCP SYN Flood attacks without memory allocation?

**Difficulty**: Advanced

**Strategy**:
Encodes connection parameters into the 32-bit initial sequence number of the SYN-ACK packet; server allocates connection memory only when client returns ACK with matching sequence.

**Code Example**:
```text
Modern Networking Protocol Specification for: What are SYN Cookies and how do they defend against TCP SYN Flood attacks without memory allocation?
Verified enterprise transport implementation
```

---

<a id="q17"></a>
### Q17: How does MTU and Path MTU Discovery (PMTUD) prevent IP packet fragmentation?

**Difficulty**: Intermediate

**Strategy**:
Sets Don't Fragment (DF) flag on packets; routers drop oversized packets sending ICMP Type 3 Code 4 (Fragmentation Needed) back to sender with bottleneck MTU size.

**Code Example**:
```text
Modern Networking Protocol Specification for: How does MTU and Path MTU Discovery (PMTUD) prevent IP packet fragmentation?
Verified enterprise transport implementation
```

---

<a id="q18"></a>
### Q18: What is gRPC Interceptors and how do you implement authentication and tracing middleware?

**Difficulty**: Intermediate

**Strategy**:
Wraps RPC execution on client or server; intercepts requests to validate JWT bearer tokens, inject OpenTelemetry trace headers, and log latency metrics.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is gRPC Interceptors and how do you implement authentication and tracing middleware?
Verified enterprise transport implementation
```

---

<a id="q19"></a>
### Q19: How does WebSocket Frame Masking work and why must clients mask frames while servers do not?

**Difficulty**: Intermediate

**Strategy**:
Client XORs frame payload with random 4-byte masking key; prevents malicious scripts in browser from poisoning intermediary proxy caches with predictable byte patterns.

**Code Example**:
```text
Modern Networking Protocol Specification for: How does WebSocket Frame Masking work and why must clients mask frames while servers do not?
Verified enterprise transport implementation
```

---

<a id="q20"></a>
### Q20: What is TCP Selective Acknowledgment (SACK) and how does it prevent unnecessary retransmissions?

**Difficulty**: Intermediate

**Strategy**:
Receiver acknowledges non-contiguous blocks of received packets in TCP options header; sender retransmits only the missing segments rather than re-sending all packets.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is TCP Selective Acknowledgment (SACK) and how does it prevent unnecessary retransmissions?
Verified enterprise transport implementation
```

---

<a id="q21"></a>
### Q21: How does Anycast BGP routing distribute network traffic across globally distributed CDN servers?

**Difficulty**: Advanced

**Strategy**:
Multiple edge servers announce identical IP prefix via BGP; internet Autonomous Systems (AS) route traffic along shortest AS-Path to nearest geographic edge.

**Code Example**:
```text
Modern Networking Protocol Specification for: How does Anycast BGP routing distribute network traffic across globally distributed CDN servers?
Verified enterprise transport implementation
```

---

<a id="q22"></a>
### Q22: What is DNS over TLS (DoT) vs DNS over HTTPS (DoH)?

**Difficulty**: Beginner

**Strategy**:
DoT runs on dedicated port 853 with TLS wrapper (easy to filter by firewalls); DoH runs over standard HTTPS port 443 indistinguishable from normal web traffic.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is DNS over TLS (DoT) vs DNS over HTTPS (DoH)?
Verified enterprise transport implementation
```

---

<a id="q23"></a>
### Q23: How does Server-Sent Events (SSE) compare to WebSockets for real-time streaming?

**Difficulty**: Beginner

**Strategy**:
SSE is unidirectional server-to-client over standard HTTP (`text/event-stream`) with automatic reconnection; WebSockets is full-duplex bidirectional over TCP.

**Code Example**:
```text
Modern Networking Protocol Specification for: How does Server-Sent Events (SSE) compare to WebSockets for real-time streaming?
Verified enterprise transport implementation
```

---

<a id="q24"></a>
### Q24: What is Happy Eyeballs Algorithm (RFC 8305) in dual-stack IPv4/IPv6 client connections?

**Difficulty**: Intermediate

**Strategy**:
Attempts IPv6 connection first; if no response within 250ms, starts parallel IPv4 connection; uses whichever connects first, eliminating IPv6 black hole delays.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is Happy Eyeballs Algorithm (RFC 8305) in dual-stack IPv4/IPv6 client connections?
Verified enterprise transport implementation
```

---

<a id="q25"></a>
### Q25: How does HTTP/2 Server Push work and why was it deprecated in major browsers?

**Difficulty**: Intermediate

**Strategy**:
Allowed server to send cache assets unrequested; deprecated due to cache race conditions, wasting client mobile bandwidth on already-cached files.

**Code Example**:
```text
Modern Networking Protocol Specification for: How does HTTP/2 Server Push work and why was it deprecated in major browsers?
Verified enterprise transport implementation
```

---

<a id="q26"></a>
### Q26: What is gRPC Channel Subchannel Architecture and Connection Pooling?

**Difficulty**: Advanced

**Strategy**:
A Channel represents virtual connection to target service; creates multiple Subchannels (actual TCP connections) to backend replicas, balancing RPCs across connections.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is gRPC Channel Subchannel Architecture and Connection Pooling?
Verified enterprise transport implementation
```

---

<a id="q27"></a>
### Q27: How does TCP Window Scaling Option (RFC 7323) enable 1GB sliding windows?

**Difficulty**: Intermediate

**Strategy**:
Shifts 16-bit window field left by scale factor up to 14 bits ($2^{14} = 16384$), expanding maximum window size from 64KB to 1GB for high-speed fiber links.

**Code Example**:
```text
Modern Networking Protocol Specification for: How does TCP Window Scaling Option (RFC 7323) enable 1GB sliding windows?
Verified enterprise transport implementation
```

---

<a id="q28"></a>
### Q28: What is TCP TIME_WAIT state and why is 2x Maximum Segment Lifetime (MSL) necessary?

**Difficulty**: Intermediate

**Strategy**:
Lasts 60-120 seconds; guarantees final ACK is received by remote peer and flushes delayed lingering duplicate packets from network before port reuse.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is TCP TIME_WAIT state and why is 2x Maximum Segment Lifetime (MSL) necessary?
Verified enterprise transport implementation
```

---

<a id="q29"></a>
### Q29: How does Protobuf schema evolution ensure Backward and Forward Compatibility?

**Difficulty**: Intermediate

**Strategy**:
Fields are identified by integer tag numbers; new fields must be optional; deprecated tags must never be reused (`reserved 4, 8;`); unknown tags are preserved in binary.

**Code Example**:
```text
Modern Networking Protocol Specification for: How does Protobuf schema evolution ensure Backward and Forward Compatibility?
Verified enterprise transport implementation
```

---

<a id="q30"></a>
### Q30: What is Epoll vs Kqueue in high-performance networking runtimes?

**Difficulty**: Advanced

**Strategy**:
Linux `epoll` and BSD/macOS `kqueue` are $O(1)$ event notifications; kqueue is more versatile, monitoring files, signals, timers, and sockets in a unified interface.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is Epoll vs Kqueue in high-performance networking runtimes?
Verified enterprise transport implementation
```

---

<a id="q31"></a>
### Q31: How do Modern Firewalls implement Stateful Packet Inspection (SPI) with Conntrack tables?

**Difficulty**: Intermediate

**Strategy**:
Tracks TCP state machine (SYN_SENT, ESTABLISHED) in kernel connection tracking table; permits reply packets automatically if they match active session state.

**Code Example**:
```text
Modern Networking Protocol Specification for: How do Modern Firewalls implement Stateful Packet Inspection (SPI) with Conntrack tables?
Verified enterprise transport implementation
```

---

<a id="q32"></a>
### Q32: What is gRPC Protobuf Field Mask and how does it implement Partial Updates (PATCH)?

**Difficulty**: Intermediate

**Strategy**:
Specifies exact list of fields to update (`FieldMask { paths: ["email", "phone"] }`), preventing unmentioned fields from being overwritten with default null values.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is gRPC Protobuf Field Mask and how does it implement Partial Updates (PATCH)?
Verified enterprise transport implementation
```

---

<a id="q33"></a>
### Q33: How does TLS Session Resumption with Session Tickets (RFC 5077) work?

**Difficulty**: Intermediate

**Strategy**:
Server encrypts session parameters into opaque ticket sent to client; client presents ticket on reconnect; server decrypts ticket without storing session cache in RAM.

**Code Example**:
```text
Modern Networking Protocol Specification for: How does TLS Session Resumption with Session Tickets (RFC 5077) work?
Verified enterprise transport implementation
```

---

<a id="q34"></a>
### Q34: What is QUIC Flow Control at Connection Level vs Stream Level?

**Difficulty**: Advanced

**Strategy**:
Stream flow control prevents single stream from monopolizing receiver memory; Connection flow control caps cumulative buffer memory allocated across all active streams.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is QUIC Flow Control at Connection Level vs Stream Level?
Verified enterprise transport implementation
```

---

<a id="q35"></a>
### Q35: How does TCP Keepalive detect dead peers across cloud network firewalls?

**Difficulty**: Beginner

**Strategy**:
Sends probe packets with no payload after idle period; if peer fails to ACK after $N$ probes, kernel closes socket and notifies application with `ETIMEDOUT`.

**Code Example**:
```text
Modern Networking Protocol Specification for: How does TCP Keepalive detect dead peers across cloud network firewalls?
Verified enterprise transport implementation
```

---

<a id="q36"></a>
### Q36: What is Maximum Segment Size (MSS) and how is it calculated from MTU?

**Difficulty**: Beginner

**Strategy**:
Maximum data payload in a single TCP segment: $\text{MSS} = \text{MTU} - (\text{IP Header (20B)} + \text{TCP Header (20B)}) = 1460$ bytes on standard 1500B Ethernet.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is Maximum Segment Size (MSS) and how is it calculated from MTU?
Verified enterprise transport implementation
```

---

<a id="q37"></a>
### Q37: How do Reverse Proxies (Envoy, Nginx) handle HTTP/2 to HTTP/1.1 protocol translation?

**Difficulty**: Intermediate

**Strategy**:
Decodes HTTP/2 binary frames and multiplexed streams into internal requests; forwards to legacy backend over pooled HTTP/1.1 connections with keepalive.

**Code Example**:
```text
Modern Networking Protocol Specification for: How do Reverse Proxies (Envoy, Nginx) handle HTTP/2 to HTTP/1.1 protocol translation?
Verified enterprise transport implementation
```

---

<a id="q38"></a>
### Q38: What is BGP Route Flapping and how does Route Flap Damping stabilize routing tables?

**Difficulty**: Advanced

**Strategy**:
Frequent advertising and withdrawing of BGP routes overburdens router CPUs; Damping applies penalty score, temporarily suppressing unstable routes.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is BGP Route Flapping and how does Route Flap Damping stabilize routing tables?
Verified enterprise transport implementation
```

---

<a id="q39"></a>
### Q39: How does gRPC Load Balancing work: Client-Side (Lookaside / Envoy) vs Proxy-Based?

**Difficulty**: Advanced

**Strategy**:
Client-side: client queries control plane (gRPC xDS) and balances RPCs directly to pod IPs; Proxy-based: traffic flows through intermediate L7 load balancer.

**Code Example**:
```text
Modern Networking Protocol Specification for: How does gRPC Load Balancing work: Client-Side (Lookaside / Envoy) vs Proxy-Based?
Verified enterprise transport implementation
```

---

<a id="q40"></a>
### Q40: What is TCP SYN-ACK Retransmission Exponential Backoff?

**Difficulty**: Intermediate

**Strategy**:
If client fails to return final ACK, server retransmits SYN-ACK at exponentially increasing intervals (1s, 2s, 4s, 8s, 16s) before aborting connection.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is TCP SYN-ACK Retransmission Exponential Backoff?
Verified enterprise transport implementation
```

---

<a id="q41"></a>
### Q41: How does WebRTC NAT Traversal work with STUN, TURN, and ICE candidate gathering?

**Difficulty**: Advanced

**Strategy**:
STUN discovers public reflexive IP; TURN relays media if symmetric NAT blocks direct P2P; ICE gathers all candidates and tests lowest-latency viable path.

**Code Example**:
```text
Modern Networking Protocol Specification for: How does WebRTC NAT Traversal work with STUN, TURN, and ICE candidate gathering?
Verified enterprise transport implementation
```

---

<a id="q42"></a>
### Q42: What is DiffServ (Differentiated Services) and DSCP Bits in IP Quality of Service (QoS)?

**Difficulty**: Intermediate

**Strategy**:
6-bit DSCP field in IP header flags packet priority (e.g. Expedited Forwarding for VoIP, Best Effort for web), allowing routers to prioritize urgent packets.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is DiffServ (Differentiated Services) and DSCP Bits in IP Quality of Service (QoS)?
Verified enterprise transport implementation
```

---

<a id="q43"></a>
### Q43: How do gRPC Custom Metadata Headers (`metadata.MD`) pass contextual information?

**Difficulty**: Intermediate

**Strategy**:
Passes key-value pairs encoded as HTTP/2 headers; binary metadata keys end with `-bin`, encoded automatically as Base64.

**Code Example**:
```text
Modern Networking Protocol Specification for: How do gRPC Custom Metadata Headers (`metadata.MD`) pass contextual information?
Verified enterprise transport implementation
```

---

<a id="q44"></a>
### Q44: What is BBRv2 and how does it improve co-existence with CUBIC flows?

**Difficulty**: Advanced

**Strategy**:
Incorporates Explicit Congestion Notification (ECN) and packet loss responses into BBR model, preventing BBR from starving loss-based CUBIC flows.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is BBRv2 and how does it improve co-existence with CUBIC flows?
Verified enterprise transport implementation
```

---

<a id="q45"></a>
### Q45: How does IP Anycast handle BGP route shifts mid-connection?

**Difficulty**: Advanced

**Strategy**:
Route shift sends TCP packet to different datacenter lacking connection state; mitigated by consistent hashing load balancers or BGP peering stability.

**Code Example**:
```text
Modern Networking Protocol Specification for: How does IP Anycast handle BGP route shifts mid-connection?
Verified enterprise transport implementation
```

---

<a id="q46"></a>
### Q46: What is TCP Urgent Pointer and Out-of-Band (OOB) data?

**Difficulty**: Beginner

**Strategy**:
Header flag indicating payload contains high-priority data that should be processed immediately by application before standard queued bytes (rarely used).

**Code Example**:
```text
Modern Networking Protocol Specification for: What is TCP Urgent Pointer and Out-of-Band (OOB) data?
Verified enterprise transport implementation
```

---

<a id="q47"></a>
### Q47: How do Microservices implement Circuit Breaking at the transport layer using Envoy?

**Difficulty**: Intermediate

**Strategy**:
Envoy monitors consecutive 5xx errors or connection timeouts; temporarily ejects failing host from upstream load balancing pool for configured sleep window.

**Code Example**:
```text
Modern Networking Protocol Specification for: How do Microservices implement Circuit Breaking at the transport layer using Envoy?
Verified enterprise transport implementation
```

---

<a id="q48"></a>
### Q48: What is HTTP Early Hints (Status Code 103) and how does it accelerate critical CSS/JS loading?

**Difficulty**: Intermediate

**Strategy**:
Server returns 103 with `Link: </style.css>; rel=preload` headers before generating dynamic HTML, allowing browser to download assets in parallel with server computation.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is HTTP Early Hints (Status Code 103) and how does it accelerate critical CSS/JS loading?
Verified enterprise transport implementation
```

---

<a id="q49"></a>
### Q49: How does TCP Reno calculate Additive Increase Multiplicative Decrease (AIMD)?

**Difficulty**: Beginner

**Strategy**:
On each error-free RTT: $\text{cwnd} = \text{cwnd} + 1$; on packet loss: $\text{cwnd} = \text{cwnd} / 2$; creates distinctive sawtooth bandwidth profile.

**Code Example**:
```text
Modern Networking Protocol Specification for: How does TCP Reno calculate Additive Increase Multiplicative Decrease (AIMD)?
Verified enterprise transport implementation
```

---

<a id="q50"></a>
### Q50: What is the difference between Unary RPC, Client-Streaming, Server-Streaming, and Bidirectional Streaming in gRPC?

**Difficulty**: Beginner

**Strategy**:
Unary: 1 request -> 1 response; Client-streaming: stream requests -> 1 response; Server-streaming: 1 request -> stream responses; Bidirectional: both stream concurrently.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is the difference between Unary RPC, Client-Streaming, Server-Streaming, and Bidirectional Streaming in gRPC?
Verified enterprise transport implementation
```

---

<a id="q51"></a>
### Q51: How does QUIC encrypt packet headers to prevent ISP ossification and traffic tampering?

**Difficulty**: Advanced

**Strategy**:
Encrypts Packet Number and header flags using header protection keys derived from TLS secret; middleboxes cannot track packet numbers or inspect stream metadata.

**Code Example**:
```text
Modern Networking Protocol Specification for: How does QUIC encrypt packet headers to prevent ISP ossification and traffic tampering?
Verified enterprise transport implementation
```

---

<a id="q52"></a>
### Q52: What is Network Byte Order (Big-Endian) and why is it mandatory in network protocols?

**Difficulty**: Beginner

**Strategy**:
Standardized byte order where most significant byte is transmitted first; host machines convert integers using `htons()` and `ntohs()`.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is Network Byte Order (Big-Endian) and why is it mandatory in network protocols?
Verified enterprise transport implementation
```

---

<a id="q53"></a>
### Q53: How does gRPC handle Service Reflection for dynamic CLI debugging (grpcurl)?

**Difficulty**: Intermediate

**Strategy**:
Server exposes proto descriptor schemas over reflection API; tools like `grpcurl` discover methods and schemas at runtime without compiling `.proto` files.

**Code Example**:
```text
Modern Networking Protocol Specification for: How does gRPC handle Service Reflection for dynamic CLI debugging (grpcurl)?
Verified enterprise transport implementation
```

---

<a id="q54"></a>
### Q54: What is Explicit Congestion Notification (ECN) in IP and TCP headers?

**Difficulty**: Advanced

**Strategy**:
Routers mark 2-bit ECN field (Congestion Encountered) in IP header instead of dropping packets; receiver echoes back ECE flag to sender to trigger rate throttling without loss.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is Explicit Congestion Notification (ECN) in IP and TCP headers?
Verified enterprise transport implementation
```

---

<a id="q55"></a>
### Q55: How does TCP Zero Window and Window Probe packets handle saturated receivers?

**Difficulty**: Intermediate

**Strategy**:
When receiver buffer fills, it advertises `rwnd = 0`; sender halts sending and transmits 1-byte periodic Window Probe packets to detect when buffer frees space.

**Code Example**:
```text
Modern Networking Protocol Specification for: How does TCP Zero Window and Window Probe packets handle saturated receivers?
Verified enterprise transport implementation
```

---

<a id="q56"></a>
### Q56: What is QUIC Packet Number vs Stream Offset?

**Difficulty**: Advanced

**Strategy**:
Packet numbers increase strictly monotonically (never repeated, even on retransmits); Stream offsets track byte positions within stream, cleanly separating transport ACK from stream data.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is QUIC Packet Number vs Stream Offset?
Verified enterprise transport implementation
```

---

<a id="q57"></a>
### Q57: How do WebSockets handle Heartbeats with Ping and Pong frames?

**Difficulty**: Beginner

**Strategy**:
Endpoint sends Ping control frame (opcode `0x9`); receiver must return Pong frame (opcode `0xA`) with identical payload immediately to verify connection liveness.

**Code Example**:
```text
Modern Networking Protocol Specification for: How do WebSockets handle Heartbeats with Ping and Pong frames?
Verified enterprise transport implementation
```

---

<a id="q58"></a>
### Q58: What is TCP Segmentation Offload (TSO) in hardware network interface cards?

**Difficulty**: Intermediate

**Strategy**:
TCP stack passes large 64KB buffers to NIC; hardware divides payload into 1460-byte MTU segments and appends IP/TCP headers, offloading CPU cycles.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is TCP Segmentation Offload (TSO) in hardware network interface cards?
Verified enterprise transport implementation
```

---

<a id="q59"></a>
### Q59: How does gRPC Status Codes (`OK`, `NOT_FOUND`, `UNAVAILABLE`, `DEADLINE_EXCEEDED`) map to HTTP status codes?

**Difficulty**: Beginner

**Strategy**:
Standardized error enum; maps to HTTP/2 `:status` header (usually 200) with detailed gRPC error code in `grpc-status` header.

**Code Example**:
```text
Modern Networking Protocol Specification for: How does gRPC Status Codes (`OK`, `NOT_FOUND`, `UNAVAILABLE`, `DEADLINE_EXCEEDED`) map to HTTP status codes?
Verified enterprise transport implementation
```

---

<a id="q60"></a>
### Q60: What is the role of the BGP Autonomous System (AS) and AS-Path attribute?

**Difficulty**: Intermediate

**Strategy**:
An AS is a collection of IP networks under single administrative control; AS-Path lists AS numbers traversed by route; routes with shorter AS-Paths are preferred.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is the role of the BGP Autonomous System (AS) and AS-Path attribute?
Verified enterprise transport implementation
```

---

<a id="q61"></a>
### Q61: How does Path MTU Discovery handle Black Hole Routers that drop packets without sending ICMP errors?

**Difficulty**: Advanced

**Strategy**:
Black hole routers drop oversized packets silently; mitigated by MTU probing (PLPMTUD RFC 4821) which probes path MTU using isolated TCP packets.

**Code Example**:
```text
Modern Networking Protocol Specification for: How does Path MTU Discovery handle Black Hole Routers that drop packets without sending ICMP errors?
Verified enterprise transport implementation
```

---

<a id="q62"></a>
### Q62: What is HTTP/2 Flow Control Credit Starvation and how do you tune window sizes?

**Difficulty**: Advanced

**Strategy**:
If HTTP/2 stream or connection window is too small, sender exhausts credit and stalls waiting for `WINDOW_UPDATE` frames; tune window size to match BDP.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is HTTP/2 Flow Control Credit Starvation and how do you tune window sizes?
Verified enterprise transport implementation
```

---

<a id="q63"></a>
### Q63: How do CDN Edge Servers use TCP BBR to accelerate file downloads across lossy mobile networks?

**Difficulty**: Intermediate

**Strategy**:
BBR ignores random wireless packet loss, maintaining high bandwidth without throttling sending rates, unlike loss-sensitive CUBIC.

**Code Example**:
```text
Modern Networking Protocol Specification for: How do CDN Edge Servers use TCP BBR to accelerate file downloads across lossy mobile networks?
Verified enterprise transport implementation
```

---

<a id="q64"></a>
### Q64: What is SCTP (Stream Control Transmission Protocol) and why is it used in telecom signalling (SS7/SIGTRAN)?

**Difficulty**: Advanced

**Strategy**:
Message-oriented multi-stream transport supporting multi-homing (multiple IP addresses per endpoint) and out-of-order delivery without head-of-line blocking.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is SCTP (Stream Control Transmission Protocol) and why is it used in telecom signalling (SS7/SIGTRAN)?
Verified enterprise transport implementation
```

---

<a id="q65"></a>
### Q65: How does DNS Anycast enable Geo-DNS routing for global enterprises?

**Difficulty**: Intermediate

**Strategy**:
DNS queries hit the topologically closest Anycast nameserver instance; nameserver resolves IP based on client subnet geolocation (EDNS Client Subnet).

**Code Example**:
```text
Modern Networking Protocol Specification for: How does DNS Anycast enable Geo-DNS routing for global enterprises?
Verified enterprise transport implementation
```

---

<a id="q66"></a>
### Q66: What is TCP Selective Acknowledgement (SACK) Renéging and how does the kernel handle it?

**Difficulty**: Advanced

**Strategy**:
Receiver advertises SACK for packet but later discards it from buffer due to memory exhaustion; sender handles reneging by verifying cumulative ACK.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is TCP Selective Acknowledgement (SACK) Renéging and how does the kernel handle it?
Verified enterprise transport implementation
```

---

<a id="q67"></a>
### Q67: How does gRPC Channel State Machine transition between `IDLE`, `CONNECTING`, `READY`, and `TRANSIENT_FAILURE`?

**Difficulty**: Intermediate

**Strategy**:
Channel starts IDLE; transitions to CONNECTING on first RPC; becomes READY on handshake; moves to TRANSIENT_FAILURE with exponential backoff on drop.

**Code Example**:
```text
Modern Networking Protocol Specification for: How does gRPC Channel State Machine transition between `IDLE`, `CONNECTING`, `READY`, and `TRANSIENT_FAILURE`?
Verified enterprise transport implementation
```

---

<a id="q68"></a>
### Q68: What is the difference between Forward Proxy and Reverse Proxy in enterprise networks?

**Difficulty**: Beginner

**Strategy**:
Forward proxy sits in front of clients, controlling and caching internet outbound access; Reverse proxy sits in front of servers, providing load balancing and SSL termination.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is the difference between Forward Proxy and Reverse Proxy in enterprise networks?
Verified enterprise transport implementation
```

---

<a id="q69"></a>
### Q69: How does TLS 1.3 Key Update message refresh symmetric keys during long-running streaming connections?

**Difficulty**: Advanced

**Strategy**:
Sends `KeyUpdate` handshake message; derives new symmetric encryption keys from existing secret without executing new handshake, preventing cipher exhaustion.

**Code Example**:
```text
Modern Networking Protocol Specification for: How does TLS 1.3 Key Update message refresh symmetric keys during long-running streaming connections?
Verified enterprise transport implementation
```

---

<a id="q70"></a>
### Q70: What is HTTP/2 Priority Trees (RFC 7540) and why did RFC 9218 replace them with Extensible Priorities?

**Difficulty**: Advanced

**Strategy**:
Original priority trees were over-engineered and implemented inconsistently; RFC 9218 replaces them with simple Urgency (`u=0..7`) and Incremental (`i`) headers.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is HTTP/2 Priority Trees (RFC 7540) and why did RFC 9218 replace them with Extensible Priorities?
Verified enterprise transport implementation
```

---

<a id="q71"></a>
### Q71: How does Path MTU Discovery work in QUIC (PMTU Probe packets)?

**Difficulty**: Advanced

**Strategy**:
Sends QUIC probe packets padded to larger datagram sizes (e.g. 1400 bytes); if acknowledged by peer, increases connection Path MTU.

**Code Example**:
```text
Modern Networking Protocol Specification for: How does Path MTU Discovery work in QUIC (PMTU Probe packets)?
Verified enterprise transport implementation
```

---

<a id="q72"></a>
### Q72: What is TCP RST (Reset) packet and when does the kernel emit it?

**Difficulty**: Beginner

**Strategy**:
Abruptly aborts connection: emitted when packet arrives for closed port, connection rejected, or application closes socket with unread data in buffer.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is TCP RST (Reset) packet and when does the kernel emit it?
Verified enterprise transport implementation
```

---

<a id="q73"></a>
### Q73: How do Mobile Clients handle IP Roaming with MPTCP (Multipath TCP)?

**Difficulty**: Advanced

**Strategy**:
Multipath TCP allows single connection to use Wi-Fi and Cellular interfaces simultaneously, seamlessly shifting packets as signal strength varies.

**Code Example**:
```text
Modern Networking Protocol Specification for: How do Mobile Clients handle IP Roaming with MPTCP (Multipath TCP)?
Verified enterprise transport implementation
```

---

<a id="q74"></a>
### Q74: What is the difference between State-Machine Parsers and Regular-Expression Parsers for network protocols?

**Difficulty**: Intermediate

**Strategy**:
State-machine parsers process byte-by-byte in $O(1)$ memory without backtracking; regex parsers risk ReDoS vulnerabilities on adversarial inputs.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is the difference between State-Machine Parsers and Regular-Expression Parsers for network protocols?
Verified enterprise transport implementation
```

---

<a id="q75"></a>
### Q75: How does gRPC implement Health Checking Protocol (`grpc.health.v1.Health`)?

**Difficulty**: Intermediate

**Strategy**:
Standardized service exposing `Check` (unary) and `Watch` (streaming) methods; load balancers query status to determine whether server is `SERVING` or `NOT_SERVING`.

**Code Example**:
```text
Modern Networking Protocol Specification for: How does gRPC implement Health Checking Protocol (`grpc.health.v1.Health`)?
Verified enterprise transport implementation
```

---

<a id="q76"></a>
### Q76: What is BGP Hijacking and how does RPKI (Resource Public Key Infrastructure) prevent it?

**Difficulty**: Advanced

**Strategy**:
Malicious network advertises IP prefixes it does not own; RPKI signs Route Origin Authorizations (ROAs) cryptographically; routers drop invalid route announcements.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is BGP Hijacking and how does RPKI (Resource Public Key Infrastructure) prevent it?
Verified enterprise transport implementation
```

---

<a id="q77"></a>
### Q77: How does WebSocket Per-Message Deflate compression work and what are the security trade-offs?

**Difficulty**: Intermediate

**Strategy**:
Compresses payloads using DEFLATE; reduces network bytes but exposes encrypted traffic to compression side-channel attacks (CRIME) if secrets are reflected.

**Code Example**:
```text
Modern Networking Protocol Specification for: How does WebSocket Per-Message Deflate compression work and what are the security trade-offs?
Verified enterprise transport implementation
```

---

<a id="q78"></a>
### Q78: What is TCP Small Queues (TSQ) in Linux and how does it combat Bufferbloat on local interfaces?

**Difficulty**: Advanced

**Strategy**:
Limits number of bytes queued in driver transmission rings per TCP socket to 2 segments, reducing latency and buffer bloat in kernel.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is TCP Small Queues (TSQ) in Linux and how does it combat Bufferbloat on local interfaces?
Verified enterprise transport implementation
```

---

<a id="q79"></a>
### Q79: How does gRPC Name Resolution (DNS vs Consul vs Kubernetes) resolve service targets?

**Difficulty**: Intermediate

**Strategy**:
Name resolver translates `dns:///service:50051` into list of backend IP endpoints, refreshing IP list asynchronously on DNS TTL expiry.

**Code Example**:
```text
Modern Networking Protocol Specification for: How does gRPC Name Resolution (DNS vs Consul vs Kubernetes) resolve service targets?
Verified enterprise transport implementation
```

---

<a id="q80"></a>
### Q80: What is QUIC Spin Bit and how does it allow passive network latency monitoring by operators?

**Difficulty**: Advanced

**Strategy**:
1-bit field toggled by client and server once per RTT; network monitors measure interval between spin transitions to measure RTT without decrypting payload.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is QUIC Spin Bit and how does it allow passive network latency monitoring by operators?
Verified enterprise transport implementation
```

---

<a id="q81"></a>
### Q81: How do Network Sockets handle Socket Buffer Auto-Tuning (`tcp_moderate_rcvbuf`)?

**Difficulty**: Intermediate

**Strategy**:
Kernel dynamically scales socket receive buffer size up to `tcp_rmem` max based on observed Bandwidth-Delay Product to maximize throughput.

**Code Example**:
```text
Modern Networking Protocol Specification for: How do Network Sockets handle Socket Buffer Auto-Tuning (`tcp_moderate_rcvbuf`)?
Verified enterprise transport implementation
```

---

<a id="q82"></a>
### Q82: What is HTTP/2 CONTINUATION Frame and how did CONTINUATION Flood vulnerabilities cause DoS?

**Difficulty**: Advanced

**Strategy**:
Streams header blocks across multiple CONTINUATION frames; attackers sent infinite streams of headers without ending, exhausting server CPU and memory.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is HTTP/2 CONTINUATION Frame and how did CONTINUATION Flood vulnerabilities cause DoS?
Verified enterprise transport implementation
```

---

<a id="q83"></a>
### Q83: How does TLS Session Resumption with Pre-Shared Keys (PSK) operate in TLS 1.3?

**Difficulty**: Intermediate

**Strategy**:
Combines session tickets with PSK exchange; client and server derive new keys from PSK and fresh Diffie-Hellman share, providing forward secrecy on resumed sessions.

**Code Example**:
```text
Modern Networking Protocol Specification for: How does TLS Session Resumption with Pre-Shared Keys (PSK) operate in TLS 1.3?
Verified enterprise transport implementation
```

---

<a id="q84"></a>
### Q84: What is TCP Simultaneous Open?

**Difficulty**: Advanced

**Strategy**:
Rare scenario where two endpoints send SYN packets to each other simultaneously; TCP transitions through SYN_SENT to SYN_RCVD, establishing connection without distinct client/server.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is TCP Simultaneous Open?
Verified enterprise transport implementation
```

---

<a id="q85"></a>
### Q85: How does gRPC Compression (gzip, snappy, zstd) reduce wire bandwidth for large payloads?

**Difficulty**: Beginner

**Strategy**:
Compresses individual gRPC message frames with header flag `grpc-encoding: gzip`, saving bandwidth on large structured datasets.

**Code Example**:
```text
Modern Networking Protocol Specification for: How does gRPC Compression (gzip, snappy, zstd) reduce wire bandwidth for large payloads?
Verified enterprise transport implementation
```

---

<a id="q86"></a>
### Q86: What is Anycast BGP Anycast-to-Unicast Failover in CDN origin shielding?

**Difficulty**: Advanced

**Strategy**:
Edge nodes receive Anycast traffic and tunnel requests to centralized origin servers over persistent unshared Unicast TCP connections.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is Anycast BGP Anycast-to-Unicast Failover in CDN origin shielding?
Verified enterprise transport implementation
```

---

<a id="q87"></a>
### Q87: How does Linux TCP receive offload with GRO (Generic Receive Offload) reduce CPU usage?

**Difficulty**: Intermediate

**Strategy**:
Combines multiple incoming consecutive TCP packets on same flow into a single large 64KB packet before passing to kernel IP stack.

**Code Example**:
```text
Modern Networking Protocol Specification for: How does Linux TCP receive offload with GRO (Generic Receive Offload) reduce CPU usage?
Verified enterprise transport implementation
```

---

<a id="q88"></a>
### Q88: What is HTTP Strict Transport Security (HSTS) and HSTS Preloading?

**Difficulty**: Beginner

**Strategy**:
Response header `Strict-Transport-Security: max-age=31536000; includeSubDomains; preload`; browser refuses unencrypted HTTP connections and automatically converts to HTTPS.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is HTTP Strict Transport Security (HSTS) and HSTS Preloading?
Verified enterprise transport implementation
```

---

<a id="q89"></a>
### Q89: How do Distributed Systems implement Distributed Tracing Context Propagation across gRPC metadata?

**Difficulty**: Intermediate

**Strategy**:
Injects W3C `traceparent` string into gRPC metadata map; downstream service extracts metadata to link child spans to parent trace.

**Code Example**:
```text
Modern Networking Protocol Specification for: How do Distributed Systems implement Distributed Tracing Context Propagation across gRPC metadata?
Verified enterprise transport implementation
```

---

<a id="q90"></a>
### Q90: What is TCP Cork (`TCP_CORK`) and how does it compare to `TCP_NODELAY`?

**Difficulty**: Intermediate

**Strategy**:
`TCP_NODELAY` sends packets immediately (disables Nagle); `TCP_CORK` accumulates all writes until full MTU or uncorked, optimal for sending headers + files.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is TCP Cork (`TCP_CORK`) and how does it compare to `TCP_NODELAY`?
Verified enterprise transport implementation
```

---

<a id="q91"></a>
### Q91: How does QUIC handle Amplification Attack Defense on initial handshakes?

**Difficulty**: Advanced

**Strategy**:
Server restricts bytes sent in response to initial client datagram to at most 3x client datagram size until client IP address is validated.

**Code Example**:
```text
Modern Networking Protocol Specification for: How does QUIC handle Amplification Attack Defense on initial handshakes?
Verified enterprise transport implementation
```

---

<a id="q92"></a>
### Q92: What is WebSocket subprotocol negotiation (`Sec-WebSocket-Protocol`)?

**Difficulty**: Beginner

**Strategy**:
Client requests specific application subprotocols (e.g. `graphql-ws`, `wamp`); server selects mutually supported subprotocol in response handshake.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is WebSocket subprotocol negotiation (`Sec-WebSocket-Protocol`)?
Verified enterprise transport implementation
```

---

<a id="q93"></a>
### Q93: What is TCP Out-of-Order Queue and how does memory exhaustion affect high-bandwidth servers?

**Difficulty**: Advanced

**Strategy**:
Stores received packets with higher sequence numbers than expected; kernel limits queue size with `sysctl` to prevent memory exhaustion during drops.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is TCP Out-of-Order Queue and how does memory exhaustion affect high-bandwidth servers?
Verified enterprise transport implementation
```

---

<a id="q94"></a>
### Q94: How does QUIC Stateless Reset protect servers that lose connection state after a reboot?

**Difficulty**: Advanced

**Strategy**:
Server that crashes and loses connection state sends a 16-byte Stateless Reset token calculated from connection ID, cleanly notifying client to close connection.

**Code Example**:
```text
Modern Networking Protocol Specification for: How does QUIC Stateless Reset protect servers that lose connection state after a reboot?
Verified enterprise transport implementation
```

---

<a id="q95"></a>
### Q95: What is TCP Slow Start Threshold (`ssthresh`) and how does it transition to Congestion Avoidance?

**Difficulty**: Intermediate

**Strategy**:
When `cwnd` reaches `ssthresh`, the sender transitions from exponential doubling to linear additive increase to probe bandwidth safely.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is TCP Slow Start Threshold (`ssthresh`) and how does it transition to Congestion Avoidance?
Verified enterprise transport implementation
```

---

<a id="q96"></a>
### Q96: How do WebSockets handle Closing Handshake with Status Codes (1000, 1006)?

**Difficulty**: Beginner

**Strategy**:
Endpoint sends Close frame with 2-byte code (1000 = normal closure, 1006 = abnormal drop); peer echoes Close frame before severing TCP connection.

**Code Example**:
```text
Modern Networking Protocol Specification for: How do WebSockets handle Closing Handshake with Status Codes (1000, 1006)?
Verified enterprise transport implementation
```

---

<a id="q97"></a>
### Q97: What is the difference between HTTP/2 SETTINGS frames and WINDOW_UPDATE frames?

**Difficulty**: Intermediate

**Strategy**:
SETTINGS frames configure connection parameters (header table size, max concurrent streams); WINDOW_UPDATE grants flow control credit.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is the difference between HTTP/2 SETTINGS frames and WINDOW_UPDATE frames?
Verified enterprise transport implementation
```

---

<a id="q98"></a>
### Q98: How does gRPC Retry Policy handle transient network disconnects?

**Difficulty**: Intermediate

**Strategy**:
Configures service config JSON with max attempts, initial backoff, backoff multiplier, and retryable status codes (e.g. `UNAVAILABLE`).

**Code Example**:
```text
Modern Networking Protocol Specification for: How does gRPC Retry Policy handle transient network disconnects?
Verified enterprise transport implementation
```

---

<a id="q99"></a>
### Q99: What is QUIC Cryptographic Key Derivation during Handshake Phases?

**Difficulty**: Advanced

**Strategy**:
Derives initial keys from connection ID, followed by handshake keys, and finally 1-RTT application data keys using HKDF expansion.

**Code Example**:
```text
Modern Networking Protocol Specification for: What is QUIC Cryptographic Key Derivation during Handshake Phases?
Verified enterprise transport implementation
```

---

<a id="q100"></a>
### Q100: How does TCP SACK Permitted option negotiation work in SYN packets?

**Difficulty**: Beginner

**Strategy**:
Both client and server must include the 2-byte TCP SACK Permitted option in their initial SYN and SYN-ACK packets; if either peer omits it, SACK cannot be used on that connection.

**Code Example**:
```text
Modern Networking Protocol Specification for: How does TCP SACK Permitted option negotiation work in SYN packets?
Verified enterprise transport implementation
```

---
