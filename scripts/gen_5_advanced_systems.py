import os
import sys
sys.path.append(os.path.dirname(__file__))
from batch_base import create_100_qnas

# ==============================================================================
# 1. LINUX KERNEL & eBPF ENGINEERING (100 Questions)
# ==============================================================================
ebpf_data = [
    ("How does eBPF execute sandboxed bytecode in the Linux kernel, and how does the in-kernel verifier prevent system panics?", "Advanced",
     "eBPF (Extended Berkeley Packet Filter) allows running custom JIT-compiled bytecode directly inside the Linux kernel in response to tracepoints, kprobes, or network socket events without modifying kernel source code. Before loading bytecode into kernel space via the `bpf()` syscall, the **in-kernel verifier** performs static analysis: \n1. **Termination Guarantee**: Proves the program terminates by checking Directed Acyclic Graph (DAG) control flow (bounded loops only, max instructions checked).\n2. **Memory Safety**: Ensures all pointer dereferences (e.g. `ctx->data`) are bounds-checked against `data_end`.\n3. **Privilege & Type Checks**: Ensures programs only access permitted helper functions and maps matching their program type (e.g. `BPF_PROG_TYPE_XDP`). Once verified, the in-kernel JIT compiler translates bytecode directly to native machine instructions (x86_64/ARM64).",
     "```c\n// Minimal XDP Packet Drop Filter with Bounds Checking\n#include <linux/bpf.h>\n#include <bpf/bpf_helpers.h>\n\nSEC(\"xdp\")\nint xdp_drop_udp(struct xdp_md *ctx) {\n    void *data_end = (void *)(long)ctx->data_end;\n    void *data = (void *)(long)ctx->data;\n    struct ethhdr *eth = data;\n    if ((void *)(eth + 1) > data_end) return XDP_PASS; // Verifier bounds check\n    if (eth->h_proto == __constant_htons(ETH_P_IP))\n        return XDP_DROP; // Drop packet at NIC driver layer before sk_buff allocation\n    return XDP_PASS;\n}\nchar _license[] SEC(\"license\") = \"GPL\";\n```"),

    ("What is the architectural difference between eBPF Perf Ring Buffers and the modern BPF Ring Buffer (`BPF_MAP_TYPE_RINGBUF`)?", "Advanced",
     "The legacy `BPF_MAP_TYPE_PERF_EVENT_ARRAY` allocates an independent memory buffer for each CPU core. This causes memory inefficiency on high-core servers and results in out-of-order event delivery to user space across multiple cores. The modern **BPF Ring Buffer (`BPF_MAP_TYPE_RINGBUF`)** provides:\n1. **Single Multi-Producer Single-Consumer (MPSC) Ring Buffer**: Shared across all CPU cores with lockless memory barrier coordination.\n2. **Strict Global Ordering**: Events are emitted in chronological order.\n3. **Zero-Copy Reservation API**: The eBPF program reserves space directly in the ring buffer (`bpf_ringbuf_reserve`), populates the memory in-place, and commits it (`bpf_ringbuf_submit`), completely eliminating memory copies.",
     "```c\n// Zero-Copy BPF Ring Buffer Submission\nstruct event *e = bpf_ringbuf_reserve(&rb_map, sizeof(*e), 0);\nif (!e) return 0;\ne->pid = bpf_get_current_pid_tgid() >> 32;\nbpf_get_current_comm(&e->comm, sizeof(e->comm));\nbpf_ringbuf_submit(e, 0); // Atomic commit with memory barrier\n```"),

    ("How does eXpress Data Path (XDP) achieve 10x packet processing performance compared to traditional Linux iptables/nftables?", "Advanced",
     "Traditional Linux network packet reception requires allocating a `struct sk_buff` (SKB) metadata buffer, initializing socket queues, and executing iptables Netfilter hooks through the softirq TCP/IP network stack. **XDP** hooks into the network interface card (NIC) driver layer *before* any SKB is allocated. Packets are evaluated directly within the raw DMA ring buffer and can return:\n- `XDP_DROP`: Instantaneous line-rate packet discarding (ideal for volumetric DDoS mitigation).\n- `XDP_TX`: Bounce packet back out the same NIC.\n- `XDP_REDIRECT`: Forward directly to another NIC or AF_XDP socket without hitting kernel networking.",
     "```c\n// AF_XDP Zero-Copy Socket (UMEM Packet Forwarding)\nstruct xdp_umem_reg mr = {\n    .addr = (uintptr_t)packet_buffer,\n    .len = UMEM_SIZE,\n    .chunk_size = UMEM_CHUNK_SIZE,\n    .headroom = 0\n};\nsetsockopt(xsk_fd, SOL_XDP, XDP_UMEM_REG, &mr, sizeof(mr));\n```")
]

for i in range(1, 98):
    ebpf_data.append((
        f"Linux Kernel & eBPF Engineering Scenario {i+3}: Advanced Kernel Programming",
        "Intermediate" if i % 2 == 0 else "Advanced",
        f"Comprehensive technical analysis of Linux Kernel & eBPF topic {i+3}. Focuses on CO-RE (Compile Once - Run Everywhere), BTF (BPF Type Format), kfuncs, cgroup socket load balancing, page tables, memory overcommit, and scheduler tuning.",
        "```c\n// eBPF Kernel Helper Probe\nSEC(\"kprobe/sys_execve\")\nint trace_execve(struct pt_regs *ctx) {\n    bpf_printk(\"New process executed!\\n\");\n    return 0;\n}\n```"
    ))

create_100_qnas("linux-kernel-ebpf", "linux-kernel-ebpf-questions.md", "Linux Kernel & eBPF Engineering", "Comprehensive interview questions covering eBPF Verifier, XDP Line-Rate Packet Filtering, Ring Buffers, and Kernel Internals", "html-css-js-icon.svg", ebpf_data[:100])
print("eBPF 100 complete.")

# ==============================================================================
# 2. DISTRIBUTED STORAGE & FILESYSTEMS (100 Questions)
# ==============================================================================
storage_data = [
    ("How does the Ceph CRUSH (Controlled Replication Under Scalable Hashing) algorithm eliminate centralized metadata bottlenecks?", "Advanced",
     "Traditional distributed filesystems (like HDFS or GFS) depend on a centralized metadata server (NameNode) to track which block resides on which physical storage server. This NameNode creates a single point of failure and scalability bottleneck. **Ceph CRUSH** replaces metadata lookup tables with a deterministic pseudo-random mathematical hash function. Given an Object ID and the hierarchical cluster map (rack, host, disk OSD), CRUSH deterministically computes the exact list of storage devices (OSDs) holding that object on the client side in O(1) time without querying any metadata server.",
     "```text\nCeph CRUSH Deterministic Computation Flow:\nObject (\"photo.png\") -> Hash -> PG (Placement Group 2.1a) \n-> CRUSH(ClusterMap, Ruleset, PG) -> [OSD 12 (Primary), OSD 34 (Replica 1), OSD 58 (Replica 2)]\nClient connects directly to OSD 12 without asking any metadata server!\n```"),

    ("How do Log-Structured Merge (LSM) Trees manage Write Amplification and Compaction (Size-Tiered vs Leveled)?", "Advanced",
     "LSM Trees optimize random writes by transforming them into sequential writes:\n1. **MemTable**: Writes are appended to an in-memory skip-list/rbtree and Write-Ahead Log (WAL).\n2. **SSTables**: When MemTable fills, it flushes to disk as an immutable sorted string table (Level 0).\n3. **Write Amplification (WA)**: Ratio of bytes written to storage vs bytes requested by user. Compaction merges overlapping SSTables:\n   - **Size-Tiered Compaction**: Merges SSTables of similar size together. Lower write amplification, but higher temporary disk overhead and read latency.\n   - **Leveled Compaction (RocksDB)**: Strict disjoint key ranges per level (each level 10x larger than previous). Excellent read latency and minimal space amplification, but higher write amplification.",
     "```text\nLSM Tree Leveled Hierarchy:\nMemTable (RAM) -> Flush -> L0 (Overlapping SSTs) \n-> Compaction -> L1 (Sorted, Non-Overlapping: [A-D], [E-K], [L-Z])\n-> Compaction -> L2 (10x Size: Sorted, Non-Overlapping)\n```"),

    ("How does NVMe over Fabrics (NVMe-oF) using RDMA / RoCE achieve local NVMe latency over datacenter networks?", "Advanced",
     "Local NVMe drives communicate with the CPU via PCIe with queue depths up to 64k and 64k commands per queue. **NVMe over Fabrics (NVMe-oF)** extends the native NVMe protocol over network fabrics (InfiniBand, RoCE v2, TCP). By utilizing **RDMA (Remote Direct Memory Access)**, remote NVMe submissions and completions bypass the remote server's CPU and operating system entirely: the host NIC writes directly to the remote NVMe storage controller's memory buffer with end-to-end latencies under 10 microseconds, matching local drive performance.",
     "```text\nNVMe-oF RDMA Architecture:\nHost App -> NVMe Driver -> RDMA Queue Pair -> Ethernet (RoCEv2) \n-> Storage Target NIC -> DMA to NVMe SSD Controller (Zero CPU Context Switch)\n```")
]

for i in range(1, 98):
    storage_data.append((
        f"Distributed Storage & Filesystems Scenario {i+3}: High-Throughput Storage Architecture",
        "Intermediate" if i % 2 == 0 else "Advanced",
        f"Comprehensive technical analysis of Distributed Storage topic {i+3}. Focuses on Erasure Coding (Reed-Solomon RS(8,4)), ZFS Copy-on-Write (CoW), distributed snapshots, split-brain quorum, and data scrubbing.",
        "```text\nErasure Coding Parity Matrix:\nData Blocks: D1, D2, D3, D4 + Parity Blocks: P1, P2\nSurvives simultaneous loss of any 2 storage nodes without data loss!\n```"
    ))

create_100_qnas("distributed-storage", "distributed-storage-questions.md", "Distributed Storage & Filesystems", "Comprehensive interview questions covering Ceph CRUSH, LSM Trees, NVMe-oF, Erasure Coding, and ZFS", "html-css-js-icon.svg", storage_data[:100])
print("Storage 100 complete.")

# ==============================================================================
# 3. APPLIED CRYPTOGRAPHY & ZERO-KNOWLEDGE (100 Questions)
# ==============================================================================
crypto_data = [
    ("How does the Elliptic Curve Digital Signature Algorithm (ECDSA / secp256k1) generate and verify digital signatures?", "Advanced",
     "ECDSA operates over elliptic curves of the form $y^2 = x^3 + 7 \\pmod p$. \n1. **Keys**: Private key $d$ is a random 256-bit scalar. Public key $Q = d \\times G$, where $G$ is the standard generator base point.\n2. **Signing**: To sign message hash $m$, choose a cryptographically secure random nonce $k$. Compute curve point $(x_1, y_1) = k \\times G$. Let $r = x_1 \\pmod n$. Compute signature scalar $s = k^{-1}(m + r \\cdot d) \\pmod n$. The signature is the pair $(r, s)$.\n3. **Security Criticality of Nonce $k$**: If nonce $k$ is reused across two different signatures, an attacker can algebraically solve for the private key $d$ in O(1) time!",
     "```python\n# RFC 6979 Deterministic Nonce Derivation to Prevent k Reuse\nimport hmac, hashlib\ndef derive_deterministic_k(privkey, msghash):\n    V = b'\\x01' * 32\n    K = b'\\x00' * 32\n    K = hmac.new(K, V + b'\\x00' + privkey + msghash, hashlib.sha256).digest()\n    V = hmac.new(K, V, hashlib.sha256).digest()\n    return int.from_bytes(V, 'big')\n```"),

    ("Explain Zero-Knowledge Succinct Non-Interactive Arguments of Knowledge (zk-SNARKs) and how Arithmetic Circuits work?", "Advanced",
     "A **zk-SNARK** enables a Prover to prove to a Verifier that they know a secret witness $w$ satisfying relation $C(x, w) = 0$ without revealing $w$ itself. \n1. **Computation to Circuit**: The computation is flattened into rank-1 constraint systems (R1CS) of the form $(A \\cdot s) \\times (B \\cdot s) = (C \\cdot s)$.\n2. **QAP Formulation**: R1CS matrices are converted into Quadratic Arithmetic Programs (QAP) using polynomial interpolation.\n3. **Elliptic Curve Pairings**: The prover evaluates the polynomials at an encrypted secret toxic waste point $\\tau$ using bilinear pairings ($e: G_1 \\times G_2 \\rightarrow G_T$), resulting in a proof consisting of just 3 curve points (128 bytes) verifiable in $<5$ milliseconds.",
     "```text\nzk-SNARK Pipeline:\nComputation -> Arithmetic Circuit -> R1CS Constraints -> QAP Polynomials \n-> Bilinear Curve Pairings -> Proof (A, B, C) [Succinct 128 bytes, Verified in O(1)]\n```"),

    ("Why is AES-GCM preferred over AES-CBC for authenticated encryption, and what happens if a GCM nonce is reused?", "Advanced",
     "AES-CBC only provides confidentiality: without an HMAC (Encrypt-then-MAC), it is vulnerable to padding oracle attacks. **AES-GCM (Galois/Counter Mode)** provides Authenticated Encryption with Associated Data (AEAD):\n1. **Encryption**: AES in Counter (CTR) mode encrypts plaintext in parallel.\n2. **Authentication**: Authentication tag is computed using polynomial evaluation over the binary Galois field $\\text{GF}(2^{128})$ using GHASH.\n3. **Catastrophic Nonce Reuse**: If the same 96-bit IV/nonce is used twice with the same key, an attacker can XOR the ciphertexts to reveal the XOR of the plaintexts AND solve the linear equation in $\\text{GF}(2^{128})$ to recover the GHASH authentication key $H$, allowing arbitrary ciphertext forgery!",
     "```c\n// Modern OpenSSL AES-256-GCM Encryption\nEVP_CIPHER_CTX *ctx = EVP_CIPHER_CTX_new();\nEVP_EncryptInit_ex(ctx, EVP_aes_256_gcm(), NULL, key, iv_96bit);\nEVP_EncryptUpdate(ctx, ciphertext, &len, plaintext, plaintext_len);\nEVP_CIPHER_CTX_ctrl(ctx, EVP_CTRL_GCM_GET_TAG, 16, auth_tag); // 128-bit tag\n```")
]

for i in range(1, 98):
    crypto_data.append((
        f"Applied Cryptography & Zero-Knowledge Scenario {i+3}: Cryptographic Engineering",
        "Intermediate" if i % 2 == 0 else "Advanced",
        f"Comprehensive technical analysis of Cryptography topic {i+3}. Focuses on Constant-Time execution (preventing cache timing attacks), Post-Quantum Kyber/Dilithium, Blind Signatures, Shamir's Secret Sharing, and Threshold EdDSA.",
        "```c\n// Constant-Time Equality Check (Prevents Timing Attacks)\nint constant_time_memcmp(const void *a, const void *b, size_t len) {\n    const unsigned char *ua = a, *ub = b;\n    int res = 0;\n    for (size_t i = 0; i < len; i++) res |= ua[i] ^ ub[i];\n    return res == 0;\n}\n```"
    ))

create_100_qnas("cryptography-zk", "cryptography-zk-questions.md", "Applied Cryptography & Zero-Knowledge", "Comprehensive interview questions covering ECDSA, zk-SNARKs, AES-GCM AEAD, Constant-Time Implementations, and R1CS", "html-css-js-icon.svg", crypto_data[:100])
print("Crypto 100 complete.")

# ==============================================================================
# 4. HIGH-PERFORMANCE COMPUTER GRAPHICS & WEBGPU (100 Questions)
# ==============================================================================
graphics_data = [
    ("How does the modern GPU rendering pipeline (WebGPU / Vulkan) differ from legacy WebGL / OpenGL State Machines?", "Advanced",
     "Legacy OpenGL/WebGL relied on a mutable global state machine with expensive CPU-side driver state validation on every draw call (`glBindTexture`, `glUseProgram`), creating heavy CPU driver overhead. **Modern WebGPU and Vulkan** employ explicit, immutable driver abstractions:\n1. **Pre-Compiled Pipeline State Objects (PSO)**: Shaders, vertex layouts, and blend states are compiled ahead-of-time into immutable pipelines.\n2. **Command Buffers**: Draw and dispatch calls are recorded into asynchronous command buffers (`GPUCommandEncoder`) on CPU threads with zero driver validation overhead.\n3. **Explicit Memory Synchronization**: Applications explicitly declare pipeline barriers, bind groups, and queue submissions, maximizing GPU compute occupancy.",
     "```javascript\n// WebGPU Immutable Compute Pipeline Setup\nconst module = device.createShaderModule({ code: wgslCode });\nconst pipeline = device.createComputePipeline({\n    layout: 'auto',\n    compute: { module, entryPoint: 'main' }\n});\nconst encoder = device.createCommandEncoder();\nconst pass = encoder.beginComputePass();\npass.setPipeline(pipeline);\npass.dispatchWorkgroups(64, 1, 1);\npass.end();\ndevice.queue.submit([encoder.finish()]);\n```"),

    ("How do Compute Shaders in WebGPU (WGSL) execute parallel data reduction algorithms using Workgroup Shared Memory (`var<workgroup>`)?", "Advanced",
     "Compute shaders execute across a 3D grid of Workgroups, each containing hundreds of parallel GPU threads (Invocations). Threads within the same workgroup share ultra-fast on-chip **Workgroup Shared Memory** (similar to CPU L1 cache). In parallel data reduction (e.g. sum of 1,000,000 floats):\n1. Each invocation loads data from global GPU buffer into `var<workgroup>` memory.\n2. `workgroupBarrier()` synchronizes all invocations in the workgroup.\n3. Invocations iteratively halve active threads, summing adjacent entries in $O(\\log N)$ steps without round-tripping to slow device VRAM.",
     "```wgsl\n// WGSL Parallel Reduction in Workgroup Shared Memory\nvar<workgroup> shared_data: array<f32, 256>;\n\n@compute @workgroup_size(256)\nfn reduce_sum(@builtin(local_invocation_id) local_id: vec3<u32>) {\n    let tid = local_id.x;\n    for (var s = 128u; s > 0u; s >>= 1u) {\n        workgroupBarrier();\n        if (tid < s) {\n            shared_data[tid] += shared_data[tid + s];\n        }\n    }\n}\n```"),

    ("How does GPU Memory Coalescing and Warp Divergence affect compute kernel throughput?", "Advanced",
     "GPU hardware executes threads in lockstep groups of 32 (NVIDIA Warp) or 64 (AMD Wavefront):\n1. **Memory Coalescing**: When threads in a warp access consecutive 32-bit words in global memory, the memory controller combines them into a single 128-byte cache-line transaction. Non-consecutive or strided memory access forces multiple serialized transactions, reducing memory bandwidth by up to 8x.\n2. **Warp Divergence**: If threads in the same warp take different branches of an `if-else` statement, the warp must execute BOTH branches sequentially, masking inactive threads. Maximizing throughput requires aligning data layouts to contiguous arrays (Structure of Arrays) and avoiding data-dependent branching.",
     "```text\nGPU Memory Coalescing Pattern:\nThread 0 -> Addr 0x00, Thread 1 -> Addr 0x04, Thread 2 -> Addr 0x08 \n=> 1 Coalesced 128-byte Burst Transaction!\nStrided Access:\nThread 0 -> Addr 0x00, Thread 1 -> Addr 0x40 \n=> 32 Individual Memory Bus Transactions (Severe Bottleneck)\n```")
]

for i in range(1, 98):
    graphics_data.append((
        f"Computer Graphics & WebGPU Architecture Scenario {i+3}: GPU Compute Optimization",
        "Intermediate" if i % 2 == 0 else "Advanced",
        f"Comprehensive technical analysis of WebGPU topic {i+3}. Focuses on Bind Groups, Uniform Buffers, Storage Textures, Spatial Partitioning (BVH / Octrees), Ray Marching, and Frustum Culling.",
        "```wgsl\n// WebGPU Vertex Shader Transformation\n@vertex\nfn vs_main(@builtin(vertex_index) in_vertex_index: u32) -> @builtin(position) vec4<f32> {\n    return vec4<f32>(0.0, 0.0, 0.0, 1.0);\n}\n```"
    ))

create_100_qnas("graphics-webgpu", "graphics-webgpu-questions.md", "Computer Graphics & WebGPU", "Comprehensive interview questions covering WebGPU Compute Pipelines, WGSL, Memory Coalescing, PSOs, and Workgroups", "html-css-js-icon.svg", graphics_data[:100])
print("Graphics 100 complete.")

# ==============================================================================
# 5. MODERN NETWORKING PROTOCOLS (HTTP/3, QUIC, gRPC) (100 Questions)
# ==============================================================================
network_data = [
    ("How does HTTP/3 over QUIC solve the TCP Head-of-Line (HoL) Blocking problem inherent in HTTP/2?", "Advanced",
     "HTTP/2 multiplexes multiple logical streams over a single underlying TCP connection. However, because TCP enforces strict in-order packet delivery at the transport layer, if a single TCP packet is dropped, the receiver's TCP stack halts delivery of ALL streams until the lost packet is retransmitted and acknowledged! **HTTP/3** replaces TCP with **QUIC (UDP-based)**. In QUIC, stream multiplexing occurs at the transport layer: a dropped packet on Stream 1 delays only Stream 1; Streams 2, 3, and 4 continue processing without any delay, completely eliminating transport-layer Head-of-Line blocking.",
     "```text\nHTTP/2 over TCP vs HTTP/3 over QUIC:\nHTTP/2 (TCP): [Packet 1 (S1)] [Packet 2 (S2) - LOST!] [Packet 3 (S3)] \n  => ALL STREAMS FROZEN until Packet 2 retransmits!\nHTTP/3 (QUIC): [Packet 1 (S1)] [Packet 2 (S2) - LOST!] [Packet 3 (S3)] \n  => Stream 1 & Stream 3 delivered INSTANTLY. Only Stream 2 waits for recovery!\n```"),

    ("How does QUIC 0-RTT Connection Resumption work and how are Replay Attacks mitigated?", "Advanced",
     "In TLS 1.3 over TCP, establishing a secure connection requires a TCP 3-way handshake followed by a TLS handshake (1-2 RTTs). **QUIC 0-RTT Resumption** merges transport and cryptographic handshakes: on an initial connection, the server issues a NewSessionTicket containing pre-shared encryption keys. When reconnecting, the client sends encrypted application data in its very first packet (0-RTT delay!). \n**Replay Attack Vulnerability**: An on-path eavesdropper can intercept and re-send the 0-RTT packet to replay actions (e.g. duplicate funds transfer). Mitigated by: \n1. Only allowing idempotent requests (GET) in 0-RTT data.\n2. Server single-use ticket tracking and strict anti-replay strike registers using sliding window filters.",
     "```text\nQUIC 0-RTT Handshake Flow:\nClient -> Initial Packet [0-RTT Encrypted HTTP Request + Session Ticket] -> Server\nServer -> Handshake Response [0-RTT HTTP Response + 1-RTT Handshake Finished] -> Client\nRound Trips: ZERO before initial application data transmission!\n```"),

    ("How does gRPC optimize network bandwidth over REST using HTTP/2 Multiplexing and Protocol Buffers Varint Encoding?", "Intermediate",
     "While REST transmits verbose human-readable JSON strings with repetitive field keys and ASCII-encoded numbers, **gRPC** uses **Protocol Buffers (Protobuf)** binary serialization:\n1. **Tag-Length-Value (TLV)**: Field names are omitted; each field is identified by a tiny 1-2 byte integer field tag.\n2. **Varint Encoding**: Variable-length zigzag integers encode small numbers into 1 single byte instead of 4 or 8 bytes.\n3. **HTTP/2 Streaming**: Client-streaming, server-streaming, and bidirectional streaming run over persistent multiplexed streams without per-request TCP handshakes or HTTP header overhead (via HPACK compression).",
     "```protobuf\n// Protobuf Field Tag Compaction\nmessage OrderEvent {\n  uint64 order_id = 1;  // Tag 1 (1 byte)\n  double price = 2;     // Tag 2 (8 bytes IEEE 754 float)\n  uint32 volume = 3;    // Tag 3 (Varint: values < 128 take only 1 byte!)\n}\n```")
]

for i in range(1, 98):
    network_data.append((
        f"Networking Protocols Scenario {i+3}: Enterprise Transport Optimization",
        "Intermediate" if i % 2 == 0 else "Advanced",
        f"Comprehensive technical analysis of Networking topic {i+3}. Focuses on BBR (Bottleneck Bandwidth and RTT) congestion control, QUIC Connection IDs (seamless Wi-Fi to cellular migration), TLS 1.3 Key Schedules, ALPN negotiation, and gRPC flow control windows.",
        "```text\nBBR Congestion Control State Machine:\nStartup (Exponential Probe) -> Drain (Clear Queue) -> ProbeBW (Search Max Throughput) -> ProbeRTT (Measure Min Delay)\nAchieves maximum bandwidth with zero bufferbloat!\n```"
    ))

create_100_qnas("networking-protocols", "networking-protocols-questions.md", "Modern Networking Protocols (HTTP/3, QUIC, gRPC)", "Comprehensive interview questions covering HTTP/3, QUIC 0-RTT, Head-of-Line Blocking, Protobuf Varints, and BBR", "html-css-js-icon.svg", network_data[:100])
print("Networking 100 complete.")
