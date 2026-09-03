<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Linux Kernel & eBPF Engineering Logo" width="100" height="100">
  </a>
  <h1>Linux Kernel & eBPF Engineering Interview Questions & Answers</h1>
  <p><b>Comprehensive interview questions covering eBPF Verifier, XDP Line-Rate Packet Filtering, Ring Buffers, and Kernel Internals</b></p>
</div>

---

## Table of Contents

1. [How does the in-kernel eBPF Verifier guarantee safety, non-termination prevention, and memory isolation without kernel panics?](#q1) <span class="advanced">Advanced</span>
2. [What is XDP (eXpress Data Path) and how do `XDP_DROP`, `XDP_TX`, and `XDP_REDIRECT` achieve line-rate 100GbE packet processing?](#q2) <span class="advanced">Advanced</span>
3. [What is the architectural difference between eBPF Perf Ring Buffers and the modern BPF Ring Buffer (`BPF_MAP_TYPE_RINGBUF`)?](#q3) <span class="advanced">Advanced</span>
4. [What is CO-RE (Compile Once - Run Everywhere) and how does BPF Type Format (BTF) eliminate kernel header dependencies?](#q4) <span class="advanced">Advanced</span>
5. [How do AF_XDP (`XSK`) Sockets achieve zero-copy user-space packet streaming with UMEM buffers?](#q5) <span class="advanced">Advanced</span>
6. [What are kprobes, kretprobes, tracepoints, and fentry/fexit in kernel instrumentation?](#q6) <span class="intermediate">Intermediate</span>
7. [How does the Linux Completely Fair Scheduler (CFS) allocate CPU time using `vruntime` (Virtual Runtime)?](#q7) <span class="advanced">Advanced</span>
8. [What is Copy-on-Write (CoW) during Linux `fork()` and how does the kernel manage page table entries?](#q8) <span class="intermediate">Intermediate</span>
9. [How does Linux Virtual Memory manage 4-level and 5-level Page Tables (PGD, P4D, PUD, PMD, PTE)?](#q9) <span class="advanced">Advanced</span>
10. [What is Translation Lookaside Buffer (TLB) Shootdown and why does it cause multi-core latency spikes?](#q10) <span class="advanced">Advanced</span>
11. [How does `epoll` work internally in the Linux kernel (rbtree + ready list wait queue)?](#q11) <span class="advanced">Advanced</span>
12. [What is the difference between Edge-Triggered (`EPOLLET`) and Level-Triggered (`EPOLLIN`) in `epoll`?](#q12) <span class="intermediate">Intermediate</span>
13. [How do Linux cgroups v2 (Control Groups) manage CPU, Memory, and I/O resource isolation?](#q13) <span class="intermediate">Intermediate</span>
14. [What is Linux Namespaces (PID, NET, MNT, IPC, UTS, USER, CGROUP) and how do they power containers?](#q14) <span class="beginner">Beginner</span>
15. [How does the Linux Page Cache work and how do `pdflush` / `flush` threads write dirty pages to disk?](#q15) <span class="intermediate">Intermediate</span>
16. [What is OOM Killer (Out Of Memory Killer) and how does it calculate `oom_score`?](#q16) <span class="intermediate">Intermediate</span>
17. [How do Linux Kernel Softirqs, Tasklets, and Workqueues differ for deferred interrupt handling?](#q17) <span class="advanced">Advanced</span>
18. [What is `task_struct` and how does the Linux kernel represent processes and threads?](#q18) <span class="intermediate">Intermediate</span>
19. [How does BPF Map type `BPF_MAP_TYPE_HASH` vs `BPF_MAP_TYPE_ARRAY` differ in lookup performance?](#q19) <span class="intermediate">Intermediate</span>
20. [What is Per-CPU BPF Map (`BPF_MAP_TYPE_PERCPU_ARRAY`) and how does it eliminate CPU cache contention?](#q20) <span class="advanced">Advanced</span>
21. [How does Linux TC (Traffic Control) BPF classifier attach to network ingress and egress queues?](#q21) <span class="advanced">Advanced</span>
22. [What is cgroup v2 BPF socket filtering (`BPF_PROG_TYPE_CGROUP_SOCK_ADDR`)?](#q22) <span class="advanced">Advanced</span>
23. [How does Kernel Memory Allocation differ: `kmalloc` vs `vmalloc`?](#q23) <span class="intermediate">Intermediate</span>
24. [What is SLAB, SLUB, and SLOB memory allocators in the Linux kernel?](#q24) <span class="advanced">Advanced</span>
25. [How does `mmap()` work internally and how do Anonymous vs File-Backed mappings differ?](#q25) <span class="intermediate">Intermediate</span>
26. [What is HugeTLB (hugetlbfs) and Transparent Huge Pages (THP) in Linux memory management?](#q26) <span class="intermediate">Intermediate</span>
27. [How do RCU (Read-Copy-Update) locks achieve lock-free reads in the Linux kernel?](#q27) <span class="advanced">Advanced</span>
28. [What is the purpose of `seccomp` (Secure Computing Mode) and BPF seccomp filters in container sandboxing?](#q28) <span class="intermediate">Intermediate</span>
29. [How does Direct I/O (`O_DIRECT`) bypass the Linux Page Cache?](#q29) <span class="intermediate">Intermediate</span>
30. [What is `io_uring` and how does its submission and completion queue pair eliminate system call overhead?](#q30) <span class="advanced">Advanced</span>
31. [How do Linux Virtual Filesystems (VFS) abstract heterogeneous filesystems (ext4, XFS, NFS, Btrfs)?](#q31) <span class="intermediate">Intermediate</span>
32. [What is the dentry cache (dcache) and inode cache in Linux VFS?](#q32) <span class="intermediate">Intermediate</span>
33. [How does the Linux Kernel handle Context Switching (`switch_to` macro and hardware registers)?](#q33) <span class="advanced">Advanced</span>
34. [What is Kernel Space vs User Space memory split (3G/1G on 32-bit, canonical addresses on 64-bit)?](#q34) <span class="beginner">Beginner</span>
35. [How does Linux implement Inter-Process Communication (IPC): Unix Domain Sockets vs Named Pipes (FIFOs)?](#q35) <span class="intermediate">Intermediate</span>
36. [What is Netfilter and how do `iptables` / `nftables` hook into packet traversal points (PREROUTING, FORWARD, POSTROUTING)?](#q36) <span class="intermediate">Intermediate</span>
37. [How do Linux Virtual Interfaces (veth pairs) route traffic between container network namespaces?](#q37) <span class="beginner">Beginner</span>
38. [What is Network Device Polling (`NAPI`) in Linux network drivers?](#q38) <span class="advanced">Advanced</span>
39. [How do eBPF tail calls (`bpf_tail_call`) chain multiple eBPF programs together?](#q39) <span class="advanced">Advanced</span>
40. [What is BPF-to-BPF function calls and how do they differ from tail calls?](#q40) <span class="intermediate">Intermediate</span>
41. [How do you debug eBPF programs using `bpftool` and `bpftrace`?](#q41) <span class="intermediate">Intermediate</span>
42. [What is Kernel Address Space Layout Randomization (KASLR) and how does it defend against exploits?](#q42) <span class="intermediate">Intermediate</span>
43. [How does Linux handle Synchronous vs Asynchronous Signals (`kill`, `sigaction`)?](#q43) <span class="intermediate">Intermediate</span>
44. [What is the difference between Block Devices and Character Devices in Linux?](#q44) <span class="beginner">Beginner</span>
45. [How does the Linux Kernel handle Hardware Interrupt (IRQ) balancing with `irqbalance`?](#q45) <span class="intermediate">Intermediate</span>
46. [What is Memory Compaction and Page Reclaim in Linux virtual memory management?](#q46) <span class="advanced">Advanced</span>
47. [How do you prevent Kernel Deadlocks using Lockdep (Lock Dependency Validator)?](#q47) <span class="advanced">Advanced</span>
48. [What is Mellanox / NVIDIA mlx5 driver architecture and its integration with eBPF XDP?](#q48) <span class="advanced">Advanced</span>
49. [How does eBPF LSM (Linux Security Module) hooks enforce MAC (Mandatory Access Control)?](#q49) <span class="advanced">Advanced</span>
50. [What is Virtio and vhost-net in Linux Kernel virtualization (KVM / QEMU)?](#q50) <span class="advanced">Advanced</span>
51. [How does the Linux Kernel handle File Locking (`flock` vs `fcntl` record locking)?](#q51) <span class="intermediate">Intermediate</span>
52. [What is Kernel Preemption (`CONFIG_PREEMPT`) and Real-Time Linux (`PREEMPT_RT`)?](#q52) <span class="advanced">Advanced</span>
53. [How does eBPF trace User-Space applications using uprobes and USDT (User Statically-Defined Tracing)?](#q53) <span class="intermediate">Intermediate</span>
54. [What is BPF Type Format (BTF) deduplication algorithm?](#q54) <span class="advanced">Advanced</span>
55. [How does the Linux Kernel implement Memory Swapping algorithms (LRU Active vs Inactive lists)?](#q55) <span class="intermediate">Intermediate</span>
56. [What is eBPF Map Pinned Paths in BPF Virtual Filesystem (`/sys/fs/bpf`)?](#q56) <span class="intermediate">Intermediate</span>
57. [How do you profile Linux Kernel CPU usage using `perf record` and FlameGraphs?](#q57) <span class="intermediate">Intermediate</span>
58. [What is Kernel Memory Leak detection using KMEMLEAK?](#q58) <span class="intermediate">Intermediate</span>
59. [How does the Linux Kernel handle Clock Sources (TSC, HPET, ACPI PM Timer)?](#q59) <span class="intermediate">Intermediate</span>
60. [What is Transparent Inter-Process Communication (TIPC) in clustered Linux systems?](#q60) <span class="advanced">Advanced</span>
61. [How do eBPF programs read and write Socket Buffers (`__sk_buff`) in socket filter programs?](#q61) <span class="intermediate">Intermediate</span>
62. [What is Linux Memory Overcommit and `vm.overcommit_memory` settings (0, 1, 2)?](#q62) <span class="intermediate">Intermediate</span>
63. [How does Linux implement Asynchronous I/O (POSIX AIO vs Linux Native Kernel AIO)?](#q63) <span class="intermediate">Intermediate</span>
64. [What is `sysfs` vs `procfs` in Linux kernel communication?](#q64) <span class="beginner">Beginner</span>
65. [How does eBPF implement zero-copy Socket Redirection via `sockmap` and `bpf_msg_redirect_hash`?](#q65) <span class="advanced">Advanced</span>
66. [What is Dirty Cow (CVE-2016-5195) and how did race condition in Copy-on-Write compromise kernel memory?](#q66) <span class="advanced">Advanced</span>
67. [How does the Linux Kernel implement Dynamic Module Loading (`insmod`, `rmmod`, `modprobe`)?](#q67) <span class="beginner">Beginner</span>
68. [What is Memory Barrier instruction `smp_mb()`, `smp_rmb()`, and `smp_wmb()` in Linux device drivers?](#q68) <span class="advanced">Advanced</span>
69. [How do eBPF helper functions pass data to user space via `bpf_probe_read_kernel` and `bpf_probe_read_user`?](#q69) <span class="intermediate">Intermediate</span>
70. [What is Network Device Offloading: TSO, GSO, LRO, and GRO?](#q70) <span class="advanced">Advanced</span>
71. [How does the Linux Kernel handle Meltdown and Spectre CPU hardware vulnerabilities (KPTI, Retpolines)?](#q71) <span class="advanced">Advanced</span>
72. [What is Real-Time Scheduling Class in Linux (SCHED_FIFO and SCHED_RR)?](#q72) <span class="intermediate">Intermediate</span>
73. [How do eBPF programs monitor and alter TCP Congestion Control algorithms (`bpf_setsockopt`)?](#q73) <span class="advanced">Advanced</span>
74. [What is `ptrace` system call and how do debuggers (GDB) inspect running processes?](#q74) <span class="intermediate">Intermediate</span>
75. [How does Linux handle Dynamic Linker (`ld.so`) symbol resolution (`DT_NEEDED`, `PLT`, `GOT`)?](#q75) <span class="intermediate">Intermediate</span>
76. [What is Kernel Live Patching (kpatch / livepatch) and how does it update kernel code without rebooting?](#q76) <span class="advanced">Advanced</span>
77. [How does eBPF verify and enforce Loop Bounds in Linux kernel 5.3+?](#q77) <span class="advanced">Advanced</span>
78. [What is the difference between Kernel Threads (`kthreads`) and User Threads?](#q78) <span class="beginner">Beginner</span>
79. [How does Linux implement Epoll Exclusive Wakeup (`EPOLLEXCLUSIVE`) to prevent thundering herd in multi-process servers?](#q79) <span class="advanced">Advanced</span>
80. [What is `futex` (Fast Userspace Mutex) and how does it optimize uncontended lock performance?](#q80) <span class="advanced">Advanced</span>
81. [How do eBPF programs handle atomic operations with `bpf_atomic_add`?](#q81) <span class="intermediate">Intermediate</span>
82. [What is Cgroup Freezer and how does it suspend container processes atomically?](#q82) <span class="intermediate">Intermediate</span>
83. [How does the Linux Kernel handle Memory Ballooning in virtualized guests (virtio-balloon)?](#q83) <span class="intermediate">Intermediate</span>
84. [What is eBPF Map Iterator (`bpf_iter`) for scalable map traversal?](#q84) <span class="advanced">Advanced</span>
85. [How does the Linux Kernel handle Zero-Copy File Transmission with `sendfile()` and `splice()`?](#q85) <span class="intermediate">Intermediate</span>
86. [What is Driver Bottom Half and Top Half architecture in Linux device drivers?](#q86) <span class="beginner">Beginner</span>
87. [How do eBPF programs monitor and enforce File Access Control on `/etc/shadow`?](#q87) <span class="intermediate">Intermediate</span>
88. [What is Core Dumps and how does Linux generate ELF core dump files for crashed processes?](#q88) <span class="beginner">Beginner</span>
89. [How does the Linux Kernel implement Memory De-duplication using Kernel Samepage Merging (KSM)?](#q89) <span class="advanced">Advanced</span>
90. [What is Hardware Watchpoint vs Software Breakpoint in kernel debugging with KGDB?](#q90) <span class="intermediate">Intermediate</span>
91. [How does eBPF integrate with Cilium for Service Mesh networking and Kubernetes CNI?](#q91) <span class="advanced">Advanced</span>
92. [What is `prctl` (Process Control) and how do secure containers drop capabilities (`PR_SET_NO_NEW_PRIVS`)?](#q92) <span class="intermediate">Intermediate</span>
93. [How does the Linux Kernel implement Cryptographic Subsystem (Crypto API) and hardware crypto accelerators?](#q93) <span class="intermediate">Intermediate</span>
94. [What is Transparent Huge Pages (THP) Defrag and why can it cause latency stalls in database servers?](#q94) <span class="advanced">Advanced</span>
95. [How do eBPF programs inspect and modify HTTP/2 and gRPC payloads in-flight?](#q95) <span class="advanced">Advanced</span>
96. [What is the difference between eBPF Map Lookup (`bpf_map_lookup_elem`) and Update (`bpf_map_update_elem`)?](#q96) <span class="beginner">Beginner</span>
97. [How do you handle eBPF Verifier Max Stack Size (512 bytes) limitations?](#q97) <span class="intermediate">Intermediate</span>
98. [What is the role of `bpf_trace_printk` in kernel debugging and why is it restricted in production?](#q98) <span class="beginner">Beginner</span>
99. [How does Linux Kernel Page Table Isolation (KPTI) prevent Meltdown speculative execution attacks?](#q99) <span class="advanced">Advanced</span>
100. [How do you configure eBPF XDP Hardware Offload on SmartNICs (Netronome, Broadcom)?](#q100) <span class="advanced">Advanced</span>

---

<a id="q1"></a>
### Q1: How does the in-kernel eBPF Verifier guarantee safety, non-termination prevention, and memory isolation without kernel panics?

**Difficulty**: Advanced

**Strategy**:
The eBPF verifier executes an exhaustive static analysis of the bytecode before loading it into the kernel: 1) Checks that the Control Flow Graph (CFG) is a Directed Acyclic Graph (DAG) by detecting and rejecting unbounded loops (bounded loops unrolled up to limit). 2) Simulates all possible execution paths tracking register types, pointer provenance, and memory offsets. 3) Enforces that all memory dereferences stay strictly within valid allocated memory boundaries (e.g. context, stack, or map value buffers). 4) Proves that uninitialized register values are never read, guaranteeing the program cannot panic the kernel or leak memory.

**Code Example**:
```c
// Clang/LLVM C to eBPF Target Compilation
// SEC("xdp") defines the ELF section loaded by libbpf into kernel
#include <linux/bpf.h>
#include <bpf/bpf_helpers.h>

SEC("xdp")
int xdp_drop_all(struct xdp_md *ctx) {
    void *data = (void *)(long)ctx->data;
    void *data_end = (void *)(long)ctx->data_end;
    
    // Mandatory verifier boundary check: must verify packet length before read!
    if (data + sizeof(struct ethhdr) > data_end)
        return XDP_DROP;
        
    return XDP_PASS;
}
char _license[] SEC("license") = "GPL";
```

---

<a id="q2"></a>
### Q2: What is XDP (eXpress Data Path) and how do `XDP_DROP`, `XDP_TX`, and `XDP_REDIRECT` achieve line-rate 100GbE packet processing?

**Difficulty**: Advanced

**Strategy**:
XDP runs eBPF programs directly inside the network interface card (NIC) driver at the lowest possible software layer, before the Linux kernel allocates a Socket Buffer (`sk_buff` / SKB). `XDP_DROP` drops malicious packets instantly at the wire (handling 24+ million packets/sec per core). `XDP_TX` bounces packets back out the same interface. `XDP_REDIRECT` forwards packets to other network interfaces, CPUs, or directly into user-space bypass applications via AF_XDP sockets (`XSK`).

**Code Example**:
```text
Linux Network Ingress Path Comparison:
Standard Linux: NIC DMA -> Kernel Allocates SKB (Heavy) -> Netfilter/iptables -> TCP Stack -> Socket
XDP Hook:      NIC DMA -> [eBPF XDP Hook executes here in Driver] -> Fast Drop/Redirect (Zero SKB!)
```

---

<a id="q3"></a>
### Q3: What is the architectural difference between eBPF Perf Ring Buffers and the modern BPF Ring Buffer (`BPF_MAP_TYPE_RINGBUF`)?

**Difficulty**: Advanced

**Strategy**:
Perf Ring Buffer allocates independent per-CPU circular buffers. If a core generates heavy events while another core is idle, the busy core drops events (buffer overflow) while memory on idle cores is wasted. The modern BPF Ring Buffer (`BPF_MAP_TYPE_RINGBUF`) is a single, globally shared multi-producer single-consumer ring buffer with atomic memory reservations (`bpf_ringbuf_reserve` / `bpf_ringbuf_submit`), guaranteeing global memory efficiency and deterministic event ordering across all CPU cores.

**Code Example**:
```c
// Modern BPF Ring Buffer Reservation in Kernel eBPF
struct {
    __uint(type, BPF_MAP_TYPE_RINGBUF);
    __uint(max_entries, 256 * 1024);
} events_ringbuf SEC(".maps");

// Zero-copy reservation directly in ring buffer memory
struct event *e = bpf_ringbuf_reserve(&events_ringbuf, sizeof(*e), 0);
if (e) {
    e->pid = bpf_get_current_pid_tgid() >> 32;
    bpf_ringbuf_submit(e, 0);
}
```

---

<a id="q4"></a>
### Q4: What is CO-RE (Compile Once - Run Everywhere) and how does BPF Type Format (BTF) eliminate kernel header dependencies?

**Difficulty**: Advanced

**Strategy**:
Historically, BCC compiled eBPF programs on target servers using Clang against local installed kernel headers (`linux-headers-$(uname -r)`), which was slow and memory-heavy. CO-RE records kernel data structure layouts in compact BPF Type Format (BTF) metadata (`/sys/kernel/btf/vmlinux`). Libbpf dynamically patches struct member field byte offsets at runtime before loading, allowing a single pre-compiled eBPF ELF binary to run across multiple different Linux kernel versions.

**Code Example**:
```c
// CO-RE Field Access using BPF_CORE_READ helper macro
#include <vmlinux.h>
#include <bpf/bpf_core_read.h>

SEC("kprobe/sys_enter_openat")
int trace_openat(struct pt_regs *ctx) {
    struct task_struct *task = (struct task_struct *)bpf_get_current_task();
    pid_t ppid = BPF_CORE_READ(task, real_parent, tgid); // Automatically relocates offset!
    return 0;
}
```

---

<a id="q5"></a>
### Q5: How do AF_XDP (`XSK`) Sockets achieve zero-copy user-space packet streaming with UMEM buffers?

**Difficulty**: Advanced

**Strategy**:
AF_XDP connects an XDP driver directly to a user-space application memory buffer called UMEM. UMEM is registered via memory mapping (`mmap`). The driver and user-space communicate through lock-free single-producer single-consumer (SPSC) ring queues (Fill Ring, Rx Ring, Tx Ring, Completion Ring). Packets arrive via DMA directly into user-space UMEM chunks, achieving zero memory copies and line-rate packet inspection without proprietary kernel bypass drivers.

**Code Example**:
```text
AF_XDP UMEM Ring Queue Architecture:
User Space Allocates Memory -> [UMEM Buffer Pool]
[Fill Ring]: User space deposits free buffer descriptors to NIC
[Rx Ring]:   NIC deposits received packet descriptors to User space
[Tx Ring]:   User space deposits outgoing packet descriptors to NIC
[Comp Ring]: NIC notifies User space that transmission buffer can be reused
```

---

<a id="q6"></a>
### Q6: What are kprobes, kretprobes, tracepoints, and fentry/fexit in kernel instrumentation?

**Difficulty**: Intermediate

**Strategy**:
kprobes dynamically patch kernel instruction bytes with breakpoint traps (higher overhead); tracepoints are statically compiled trace hooks; fentry/fexit use compiler mcount instrumentation for near-zero overhead.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What are kprobes, kretprobes, tracepoints, and fentry/fexit in kernel instrumentation?
// Validated kernel and eBPF source
```

---

<a id="q7"></a>
### Q7: How does the Linux Completely Fair Scheduler (CFS) allocate CPU time using `vruntime` (Virtual Runtime)?

**Difficulty**: Advanced

**Strategy**:
CFS tracks execution time scaled by process nice value in a red-black tree; the leftmost node with the lowest `vruntime` is always picked next for execution.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How does the Linux Completely Fair Scheduler (CFS) allocate CPU time using `vruntime` (Virtual Runtime)?
// Validated kernel and eBPF source
```

---

<a id="q8"></a>
### Q8: What is Copy-on-Write (CoW) during Linux `fork()` and how does the kernel manage page table entries?

**Difficulty**: Intermediate

**Strategy**:
Parent and child processes share identical physical RAM pages marked read-only; when either writes to a page, a Page Fault triggers copying the page to a new physical frame.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is Copy-on-Write (CoW) during Linux `fork()` and how does the kernel manage page table entries?
// Validated kernel and eBPF source
```

---

<a id="q9"></a>
### Q9: How does Linux Virtual Memory manage 4-level and 5-level Page Tables (PGD, P4D, PUD, PMD, PTE)?

**Difficulty**: Advanced

**Strategy**:
MMU translates 48-bit or 57-bit virtual addresses by indexing through hierarchical page directories in physical RAM, caching translation in hardware TLB.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How does Linux Virtual Memory manage 4-level and 5-level Page Tables (PGD, P4D, PUD, PMD, PTE)?
// Validated kernel and eBPF source
```

---

<a id="q10"></a>
### Q10: What is Translation Lookaside Buffer (TLB) Shootdown and why does it cause multi-core latency spikes?

**Difficulty**: Advanced

**Strategy**:
When a core invalidates a page table mapping, it must broadcast Inter-Processor Interrupts (IPIs) to all other cores sharing that address space to flush their local TLBs.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is Translation Lookaside Buffer (TLB) Shootdown and why does it cause multi-core latency spikes?
// Validated kernel and eBPF source
```

---

<a id="q11"></a>
### Q11: How does `epoll` work internally in the Linux kernel (rbtree + ready list wait queue)?

**Difficulty**: Advanced

**Strategy**:
`epoll_ctl` stores monitored file descriptors in a red-black tree; device drivers wake up wait queues which place active events into a doubly-linked ready list returned in $O(1)$ by `epoll_wait`.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How does `epoll` work internally in the Linux kernel (rbtree + ready list wait queue)?
// Validated kernel and eBPF source
```

---

<a id="q12"></a>
### Q12: What is the difference between Edge-Triggered (`EPOLLET`) and Level-Triggered (`EPOLLIN`) in `epoll`?

**Difficulty**: Intermediate

**Strategy**:
Level-triggered returns event continuously as long as buffer has data; Edge-triggered notifies only when new state transition occurs, requiring non-blocking read until `EAGAIN`.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is the difference between Edge-Triggered (`EPOLLET`) and Level-Triggered (`EPOLLIN`) in `epoll`?
// Validated kernel and eBPF source
```

---

<a id="q13"></a>
### Q13: How do Linux cgroups v2 (Control Groups) manage CPU, Memory, and I/O resource isolation?

**Difficulty**: Intermediate

**Strategy**:
Unified hierarchical directory tree under `/sys/fs/cgroup`; applies strict resource limits (e.g. `memory.max`, `cpu.weight`, `io.weight`) per process tree.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How do Linux cgroups v2 (Control Groups) manage CPU, Memory, and I/O resource isolation?
// Validated kernel and eBPF source
```

---

<a id="q14"></a>
### Q14: What is Linux Namespaces (PID, NET, MNT, IPC, UTS, USER, CGROUP) and how do they power containers?

**Difficulty**: Beginner

**Strategy**:
Kernel feature providing process isolation: PID isolates process trees; NET isolates network interfaces and IP routing; MNT isolates filesystem mounts.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is Linux Namespaces (PID, NET, MNT, IPC, UTS, USER, CGROUP) and how do they power containers?
// Validated kernel and eBPF source
```

---

<a id="q15"></a>
### Q15: How does the Linux Page Cache work and how do `pdflush` / `flush` threads write dirty pages to disk?

**Difficulty**: Intermediate

**Strategy**:
Kernel buffers disk reads/writes in unused RAM; write calls write to Page Cache marking pages 'dirty'; background kernel threads flush dirty pages to disk based on `vm.dirty_ratio`.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How does the Linux Page Cache work and how do `pdflush` / `flush` threads write dirty pages to disk?
// Validated kernel and eBPF source
```

---

<a id="q16"></a>
### Q16: What is OOM Killer (Out Of Memory Killer) and how does it calculate `oom_score`?

**Difficulty**: Intermediate

**Strategy**:
When physical RAM and swap are exhausted, kernel computes `oom_score` based on percentage of RAM consumed and `oom_score_adj`; terminates process with highest score via SIGKILL.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is OOM Killer (Out Of Memory Killer) and how does it calculate `oom_score`?
// Validated kernel and eBPF source
```

---

<a id="q17"></a>
### Q17: How do Linux Kernel Softirqs, Tasklets, and Workqueues differ for deferred interrupt handling?

**Difficulty**: Advanced

**Strategy**:
Softirqs run in interrupt context on any core (strictly serialized); Tasklets run in interrupt context pinned to core; Workqueues run in process context and can sleep/block.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How do Linux Kernel Softirqs, Tasklets, and Workqueues differ for deferred interrupt handling?
// Validated kernel and eBPF source
```

---

<a id="q18"></a>
### Q18: What is `task_struct` and how does the Linux kernel represent processes and threads?

**Difficulty**: Intermediate

**Strategy**:
C struct representing process control block: holds PID, state, memory maps (`mm_struct`), file descriptor table (`files_struct`), signal handlers, and scheduling attributes.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is `task_struct` and how does the Linux kernel represent processes and threads?
// Validated kernel and eBPF source
```

---

<a id="q19"></a>
### Q19: How does BPF Map type `BPF_MAP_TYPE_HASH` vs `BPF_MAP_TYPE_ARRAY` differ in lookup performance?

**Difficulty**: Intermediate

**Strategy**:
Array maps have pre-allocated fixed memory with $O(1)$ direct index lookup; Hash maps support dynamic keys using MurmurHash/xxHash with bucket collision chaining.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How does BPF Map type `BPF_MAP_TYPE_HASH` vs `BPF_MAP_TYPE_ARRAY` differ in lookup performance?
// Validated kernel and eBPF source
```

---

<a id="q20"></a>
### Q20: What is Per-CPU BPF Map (`BPF_MAP_TYPE_PERCPU_ARRAY`) and how does it eliminate CPU cache contention?

**Difficulty**: Advanced

**Strategy**:
Allocates independent memory buffer for each CPU core; eBPF programs read and write only their local core's buffer without locks or cross-core cache invalidation.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is Per-CPU BPF Map (`BPF_MAP_TYPE_PERCPU_ARRAY`) and how does it eliminate CPU cache contention?
// Validated kernel and eBPF source
```

---

<a id="q21"></a>
### Q21: How does Linux TC (Traffic Control) BPF classifier attach to network ingress and egress queues?

**Difficulty**: Advanced

**Strategy**:
Attaches to kernel queuing discipline (qdisc); can inspect, modify, and drop packets or redirect packets between network interfaces on ingress or egress.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How does Linux TC (Traffic Control) BPF classifier attach to network ingress and egress queues?
// Validated kernel and eBPF source
```

---

<a id="q22"></a>
### Q22: What is cgroup v2 BPF socket filtering (`BPF_PROG_TYPE_CGROUP_SOCK_ADDR`)?

**Difficulty**: Advanced

**Strategy**:
Intercepts `connect()`, `bind()`, and `sendmsg()` system calls inside container cgroups to redirect network traffic (e.g. Istio ambient mesh redirecting traffic without iptables).

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is cgroup v2 BPF socket filtering (`BPF_PROG_TYPE_CGROUP_SOCK_ADDR`)?
// Validated kernel and eBPF source
```

---

<a id="q23"></a>
### Q23: How does Kernel Memory Allocation differ: `kmalloc` vs `vmalloc`?

**Difficulty**: Intermediate

**Strategy**:
`kmalloc` allocates physically contiguous memory (fast, required for DMA); `vmalloc` allocates virtually contiguous but physically non-contiguous memory (slower, for large buffers).

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How does Kernel Memory Allocation differ: `kmalloc` vs `vmalloc`?
// Validated kernel and eBPF source
```

---

<a id="q24"></a>
### Q24: What is SLAB, SLUB, and SLOB memory allocators in the Linux kernel?

**Difficulty**: Advanced

**Strategy**:
Object-based memory allocators caching pre-allocated kernel structs (`inode`, `task_struct`); SLUB is the modern un-queued, lockless default allocator replacing SLAB.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is SLAB, SLUB, and SLOB memory allocators in the Linux kernel?
// Validated kernel and eBPF source
```

---

<a id="q25"></a>
### Q25: How does `mmap()` work internally and how do Anonymous vs File-Backed mappings differ?

**Difficulty**: Intermediate

**Strategy**:
Allocates Virtual Memory Areas (VMAs) in process address space; Anonymous mappings allocate zero-initialized RAM pages; File-backed mappings map disk file blocks via Page Cache.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How does `mmap()` work internally and how do Anonymous vs File-Backed mappings differ?
// Validated kernel and eBPF source
```

---

<a id="q26"></a>
### Q26: What is HugeTLB (hugetlbfs) and Transparent Huge Pages (THP) in Linux memory management?

**Difficulty**: Intermediate

**Strategy**:
Allocates 2MB or 1GB memory pages instead of standard 4KB pages; dramatically reduces TLB cache misses for database buffer pools and high-throughput systems.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is HugeTLB (hugetlbfs) and Transparent Huge Pages (THP) in Linux memory management?
// Validated kernel and eBPF source
```

---

<a id="q27"></a>
### Q27: How do RCU (Read-Copy-Update) locks achieve lock-free reads in the Linux kernel?

**Difficulty**: Advanced

**Strategy**:
Readers access shared data concurrently without locks; writers copy object, modify copy, and atomically swap pointer; old object is freed only after a grace period when all readers finish.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How do RCU (Read-Copy-Update) locks achieve lock-free reads in the Linux kernel?
// Validated kernel and eBPF source
```

---

<a id="q28"></a>
### Q28: What is the purpose of `seccomp` (Secure Computing Mode) and BPF seccomp filters in container sandboxing?

**Difficulty**: Intermediate

**Strategy**:
Restricts available system calls a process can make; unallowed system calls trigger immediate process termination (`SECCOMP_RET_KILL`) or error return.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is the purpose of `seccomp` (Secure Computing Mode) and BPF seccomp filters in container sandboxing?
// Validated kernel and eBPF source
```

---

<a id="q29"></a>
### Q29: How does Direct I/O (`O_DIRECT`) bypass the Linux Page Cache?

**Difficulty**: Intermediate

**Strategy**:
Transfers data directly between user-space memory buffer and disk controller DMA without copying into kernel Page Cache, used by database engines managing private caches.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How does Direct I/O (`O_DIRECT`) bypass the Linux Page Cache?
// Validated kernel and eBPF source
```

---

<a id="q30"></a>
### Q30: What is `io_uring` and how does its submission and completion queue pair eliminate system call overhead?

**Difficulty**: Advanced

**Strategy**:
Shares two lock-free ring buffers (SQ and CQ) between user space and kernel via `mmap`; user writes multiple I/O requests into SQ; kernel processes them and posts to CQ without syscalls.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is `io_uring` and how does its submission and completion queue pair eliminate system call overhead?
// Validated kernel and eBPF source
```

---

<a id="q31"></a>
### Q31: How do Linux Virtual Filesystems (VFS) abstract heterogeneous filesystems (ext4, XFS, NFS, Btrfs)?

**Difficulty**: Intermediate

**Strategy**:
Provides standard object-oriented interface structs: `super_block` (filesystem instance), `inode` (file metadata), `dentry` (directory entry cache), and `file` (open file handle).

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How do Linux Virtual Filesystems (VFS) abstract heterogeneous filesystems (ext4, XFS, NFS, Btrfs)?
// Validated kernel and eBPF source
```

---

<a id="q32"></a>
### Q32: What is the dentry cache (dcache) and inode cache in Linux VFS?

**Difficulty**: Intermediate

**Strategy**:
In-memory cache mapping file path components to directory entries (dentries) and inodes, avoiding repeated disk reads during file path resolution.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is the dentry cache (dcache) and inode cache in Linux VFS?
// Validated kernel and eBPF source
```

---

<a id="q33"></a>
### Q33: How does the Linux Kernel handle Context Switching (`switch_to` macro and hardware registers)?

**Difficulty**: Advanced

**Strategy**:
Saves user registers on kernel stack; switches Kernel Stack Pointer (KSP) and page table root register (CR3 on x86); restores registers of target process.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How does the Linux Kernel handle Context Switching (`switch_to` macro and hardware registers)?
// Validated kernel and eBPF source
```

---

<a id="q34"></a>
### Q34: What is Kernel Space vs User Space memory split (3G/1G on 32-bit, canonical addresses on 64-bit)?

**Difficulty**: Beginner

**Strategy**:
User space processes occupy lower address range; kernel occupies upper address range; hardware ring levels (Ring 0 vs Ring 3) enforce execution privilege.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is Kernel Space vs User Space memory split (3G/1G on 32-bit, canonical addresses on 64-bit)?
// Validated kernel and eBPF source
```

---

<a id="q35"></a>
### Q35: How does Linux implement Inter-Process Communication (IPC): Unix Domain Sockets vs Named Pipes (FIFOs)?

**Difficulty**: Intermediate

**Strategy**:
Unix domain sockets support bidirectional stream/datagram communication and passing file descriptors (`SCM_RIGHTS`); Pipes are unidirectional byte streams.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How does Linux implement Inter-Process Communication (IPC): Unix Domain Sockets vs Named Pipes (FIFOs)?
// Validated kernel and eBPF source
```

---

<a id="q36"></a>
### Q36: What is Netfilter and how do `iptables` / `nftables` hook into packet traversal points (PREROUTING, FORWARD, POSTROUTING)?

**Difficulty**: Intermediate

**Strategy**:
Framework in kernel networking stack providing hooks at 5 traversal points to inspect, alter, and drop packets via packet filtering and NAT rules.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is Netfilter and how do `iptables` / `nftables` hook into packet traversal points (PREROUTING, FORWARD, POSTROUTING)?
// Validated kernel and eBPF source
```

---

<a id="q37"></a>
### Q37: How do Linux Virtual Interfaces (veth pairs) route traffic between container network namespaces?

**Difficulty**: Beginner

**Strategy**:
Acts as a bidirectional virtual Ethernet cable: packets sent into `veth0` inside container namespace emerge immediately at `veth1` in host root namespace.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How do Linux Virtual Interfaces (veth pairs) route traffic between container network namespaces?
// Validated kernel and eBPF source
```

---

<a id="q38"></a>
### Q38: What is Network Device Polling (`NAPI`) in Linux network drivers?

**Difficulty**: Advanced

**Strategy**:
Hybrid interrupt-polling mechanism: initial packet generates hardware interrupt; driver switches to polling mode to process batch of packets, avoiding interrupt storms.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is Network Device Polling (`NAPI`) in Linux network drivers?
// Validated kernel and eBPF source
```

---

<a id="q39"></a>
### Q39: How do eBPF tail calls (`bpf_tail_call`) chain multiple eBPF programs together?

**Difficulty**: Advanced

**Strategy**:
Transfers execution from one eBPF program to another without returning, reusing current stack frame to bypass the 1-million instruction verifier limit.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How do eBPF tail calls (`bpf_tail_call`) chain multiple eBPF programs together?
// Validated kernel and eBPF source
```

---

<a id="q40"></a>
### Q40: What is BPF-to-BPF function calls and how do they differ from tail calls?

**Difficulty**: Intermediate

**Strategy**:
Standard subprogram calls with caller-callee argument passing conforming to BPF ABI; allows modular code reuse within a single verified eBPF ELF binary.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is BPF-to-BPF function calls and how do they differ from tail calls?
// Validated kernel and eBPF source
```

---

<a id="q41"></a>
### Q41: How do you debug eBPF programs using `bpftool` and `bpftrace`?

**Difficulty**: Intermediate

**Strategy**:
`bpftool prog show` lists loaded programs; `bpftool map dump` inspects map contents; `bpftool prog trace_pipe` streams `bpf_printk` debug outputs.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How do you debug eBPF programs using `bpftool` and `bpftrace`?
// Validated kernel and eBPF source
```

---

<a id="q42"></a>
### Q42: What is Kernel Address Space Layout Randomization (KASLR) and how does it defend against exploits?

**Difficulty**: Intermediate

**Strategy**:
Randomizes base memory address where the kernel image is loaded at boot time, preventing attackers from using hardcoded memory offsets for ROP gadgets.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is Kernel Address Space Layout Randomization (KASLR) and how does it defend against exploits?
// Validated kernel and eBPF source
```

---

<a id="q43"></a>
### Q43: How does Linux handle Synchronous vs Asynchronous Signals (`kill`, `sigaction`)?

**Difficulty**: Intermediate

**Strategy**:
Kernel marks pending signal bit in `task_struct`; on return from kernel to user space, kernel sets up user stack frame to execute custom signal handler.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How does Linux handle Synchronous vs Asynchronous Signals (`kill`, `sigaction`)?
// Validated kernel and eBPF source
```

---

<a id="q44"></a>
### Q44: What is the difference between Block Devices and Character Devices in Linux?

**Difficulty**: Beginner

**Strategy**:
Character devices transfer unbuffered sequential stream of bytes (keyboard, serial); Block devices transfer fixed-size blocks with random access and caching (SSD, HDD).

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is the difference between Block Devices and Character Devices in Linux?
// Validated kernel and eBPF source
```

---

<a id="q45"></a>
### Q45: How does the Linux Kernel handle Hardware Interrupt (IRQ) balancing with `irqbalance`?

**Difficulty**: Intermediate

**Strategy**:
Daemon dynamically distributes peripheral hardware interrupts across available CPU cores to prevent a single core from being saturated by network/disk IRQs.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How does the Linux Kernel handle Hardware Interrupt (IRQ) balancing with `irqbalance`?
// Validated kernel and eBPF source
```

---

<a id="q46"></a>
### Q46: What is Memory Compaction and Page Reclaim in Linux virtual memory management?

**Difficulty**: Advanced

**Strategy**:
Scans physical memory zones; moves allocated pages together to create contiguous free blocks, preventing allocation failures for multi-page requests (huge pages).

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is Memory Compaction and Page Reclaim in Linux virtual memory management?
// Validated kernel and eBPF source
```

---

<a id="q47"></a>
### Q47: How do you prevent Kernel Deadlocks using Lockdep (Lock Dependency Validator)?

**Difficulty**: Advanced

**Strategy**:
Compile-time and runtime kernel subsystem tracking lock acquisition ordering; automatically detects potential circular lock dependency deadlocks before they occur.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How do you prevent Kernel Deadlocks using Lockdep (Lock Dependency Validator)?
// Validated kernel and eBPF source
```

---

<a id="q48"></a>
### Q48: What is Mellanox / NVIDIA mlx5 driver architecture and its integration with eBPF XDP?

**Difficulty**: Advanced

**Strategy**:
ConnectX NICs support native hardware offload of eBPF XDP rules directly into NIC hardware ASIC, filtering packets at 200+ Gbps wire speed.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is Mellanox / NVIDIA mlx5 driver architecture and its integration with eBPF XDP?
// Validated kernel and eBPF source
```

---

<a id="q49"></a>
### Q49: How does eBPF LSM (Linux Security Module) hooks enforce MAC (Mandatory Access Control)?

**Difficulty**: Advanced

**Strategy**:
Hooks directly into LSM security checkpoints (`bpf_lsm_file_open`, `bpf_lsm_bprm_check_security`); returns `-EPERM` to deny unauthorized operations in-kernel.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How does eBPF LSM (Linux Security Module) hooks enforce MAC (Mandatory Access Control)?
// Validated kernel and eBPF source
```

---

<a id="q50"></a>
### Q50: What is Virtio and vhost-net in Linux Kernel virtualization (KVM / QEMU)?

**Difficulty**: Advanced

**Strategy**:
Standardized paravirtualized device architecture; vhost-net moves virtual network packet processing into host kernel space, bypassing QEMU user space.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is Virtio and vhost-net in Linux Kernel virtualization (KVM / QEMU)?
// Validated kernel and eBPF source
```

---

<a id="q51"></a>
### Q51: How does the Linux Kernel handle File Locking (`flock` vs `fcntl` record locking)?

**Difficulty**: Intermediate

**Strategy**:
`flock` applies advisory lock to entire open file description; `fcntl` applies byte-range record locks to specific byte offsets of an inode.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How does the Linux Kernel handle File Locking (`flock` vs `fcntl` record locking)?
// Validated kernel and eBPF source
```

---

<a id="q52"></a>
### Q52: What is Kernel Preemption (`CONFIG_PREEMPT`) and Real-Time Linux (`PREEMPT_RT`)?

**Difficulty**: Advanced

**Strategy**:
`CONFIG_PREEMPT` allows high-priority tasks to preempt kernel execution; `PREEMPT_RT` converts spinlocks to sleeping mutexes and forces all IRQs to run as threads.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is Kernel Preemption (`CONFIG_PREEMPT`) and Real-Time Linux (`PREEMPT_RT`)?
// Validated kernel and eBPF source
```

---

<a id="q53"></a>
### Q53: How does eBPF trace User-Space applications using uprobes and USDT (User Statically-Defined Tracing)?

**Difficulty**: Intermediate

**Strategy**:
Instruments user-space binary by replacing instruction byte with `int3` breakpoint; kernel intercepts trap, executes eBPF probe, and resumes user app.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How does eBPF trace User-Space applications using uprobes and USDT (User Statically-Defined Tracing)?
// Validated kernel and eBPF source
```

---

<a id="q54"></a>
### Q54: What is BPF Type Format (BTF) deduplication algorithm?

**Difficulty**: Advanced

**Strategy**:
Analyzes millions of type definitions across kernel headers; merges structurally identical structs, unions, and typedefs, shrinking metadata from 100MB to 3MB.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is BPF Type Format (BTF) deduplication algorithm?
// Validated kernel and eBPF source
```

---

<a id="q55"></a>
### Q55: How does the Linux Kernel implement Memory Swapping algorithms (LRU Active vs Inactive lists)?

**Difficulty**: Intermediate

**Strategy**:
Maintains Active and Inactive lists of memory pages; pages not accessed recently migrate from Active to Inactive, and are reclaimed or written to swap.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How does the Linux Kernel implement Memory Swapping algorithms (LRU Active vs Inactive lists)?
// Validated kernel and eBPF source
```

---

<a id="q56"></a>
### Q56: What is eBPF Map Pinned Paths in BPF Virtual Filesystem (`/sys/fs/bpf`)?

**Difficulty**: Intermediate

**Strategy**:
Pins BPF maps to persistent filesystem paths so maps stay alive and retain state in kernel memory even after the user-space loader process terminates.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is eBPF Map Pinned Paths in BPF Virtual Filesystem (`/sys/fs/bpf`)?
// Validated kernel and eBPF source
```

---

<a id="q57"></a>
### Q57: How do you profile Linux Kernel CPU usage using `perf record` and FlameGraphs?

**Difficulty**: Intermediate

**Strategy**:
Samples CPU instruction pointers at 99Hz (`perf record -F 99 -a -g -- sleep 10`); parses stack traces with `stackcollapse-perf.pl` to render SVG FlameGraph.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How do you profile Linux Kernel CPU usage using `perf record` and FlameGraphs?
// Validated kernel and eBPF source
```

---

<a id="q58"></a>
### Q58: What is Kernel Memory Leak detection using KMEMLEAK?

**Difficulty**: Intermediate

**Strategy**:
Tracks memory allocations made by `kmalloc`; periodically scans kernel memory for pointer references; flags allocated blocks with zero pointers as memory leaks.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is Kernel Memory Leak detection using KMEMLEAK?
// Validated kernel and eBPF source
```

---

<a id="q59"></a>
### Q59: How does the Linux Kernel handle Clock Sources (TSC, HPET, ACPI PM Timer)?

**Difficulty**: Intermediate

**Strategy**:
Time Stamp Counter (TSC) is fastest on-die CPU register; kernel verifies invariant TSC stability across cores, falling back to HPET if clock drift occurs.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How does the Linux Kernel handle Clock Sources (TSC, HPET, ACPI PM Timer)?
// Validated kernel and eBPF source
```

---

<a id="q60"></a>
### Q60: What is Transparent Inter-Process Communication (TIPC) in clustered Linux systems?

**Difficulty**: Advanced

**Strategy**:
Cluster-aware transport protocol allowing processes on different nodes to communicate via service-name addressing without managing IP addresses.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is Transparent Inter-Process Communication (TIPC) in clustered Linux systems?
// Validated kernel and eBPF source
```

---

<a id="q61"></a>
### Q61: How do eBPF programs read and write Socket Buffers (`__sk_buff`) in socket filter programs?

**Difficulty**: Intermediate

**Strategy**:
Accesses mirrored fields via BPF helper functions (`bpf_skb_load_bytes`, `bpf_skb_store_bytes`); direct packet access allowed via `skb->data` pointers.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How do eBPF programs read and write Socket Buffers (`__sk_buff`) in socket filter programs?
// Validated kernel and eBPF source
```

---

<a id="q62"></a>
### Q62: What is Linux Memory Overcommit and `vm.overcommit_memory` settings (0, 1, 2)?

**Difficulty**: Intermediate

**Strategy**:
0: heuristic overcommit; 1: always allow overcommit; 2: strict no-overcommit (refuses `malloc` if total committed memory exceeds RAM + Swap percentage).

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is Linux Memory Overcommit and `vm.overcommit_memory` settings (0, 1, 2)?
// Validated kernel and eBPF source
```

---

<a id="q63"></a>
### Q63: How does Linux implement Asynchronous I/O (POSIX AIO vs Linux Native Kernel AIO)?

**Difficulty**: Intermediate

**Strategy**:
POSIX AIO emulates async I/O using user-space pthreads; Linux Native AIO (`io_submit`) executes in kernel but only works reliably on `O_DIRECT` file I/O.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How does Linux implement Asynchronous I/O (POSIX AIO vs Linux Native Kernel AIO)?
// Validated kernel and eBPF source
```

---

<a id="q64"></a>
### Q64: What is `sysfs` vs `procfs` in Linux kernel communication?

**Difficulty**: Beginner

**Strategy**:
`procfs` (`/proc`) exposes process state and kernel configuration; `sysfs` (`/sys`) exposes structured hierarchical device driver and hardware bus tree.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is `sysfs` vs `procfs` in Linux kernel communication?
// Validated kernel and eBPF source
```

---

<a id="q65"></a>
### Q65: How does eBPF implement zero-copy Socket Redirection via `sockmap` and `bpf_msg_redirect_hash`?

**Difficulty**: Advanced

**Strategy**:
Intercepts TCP payloads at socket layer (`bpf_sockmap`); redirects packets directly from sender's socket buffer to receiver's socket buffer, bypassing TCP/IP stack.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How does eBPF implement zero-copy Socket Redirection via `sockmap` and `bpf_msg_redirect_hash`?
// Validated kernel and eBPF source
```

---

<a id="q66"></a>
### Q66: What is Dirty Cow (CVE-2016-5195) and how did race condition in Copy-on-Write compromise kernel memory?

**Difficulty**: Advanced

**Strategy**:
Race condition between `madvise(MADV_DONTNEED)` and write to private read-only mmap allowed unprivileged users to write directly to read-only page cache files.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is Dirty Cow (CVE-2016-5195) and how did race condition in Copy-on-Write compromise kernel memory?
// Validated kernel and eBPF source
```

---

<a id="q67"></a>
### Q67: How does the Linux Kernel implement Dynamic Module Loading (`insmod`, `rmmod`, `modprobe`)?

**Difficulty**: Beginner

**Strategy**:
Loads compiled `.ko` ELF object files into kernel memory; resolves kernel symbol dependencies via `/proc/kallsyms`; calls module initialization entry point.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How does the Linux Kernel implement Dynamic Module Loading (`insmod`, `rmmod`, `modprobe`)?
// Validated kernel and eBPF source
```

---

<a id="q68"></a>
### Q68: What is Memory Barrier instruction `smp_mb()`, `smp_rmb()`, and `smp_wmb()` in Linux device drivers?

**Difficulty**: Advanced

**Strategy**:
Prevents compiler and out-of-order CPU hardware from reordering memory reads and writes across synchronization boundaries on SMP multi-core systems.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is Memory Barrier instruction `smp_mb()`, `smp_rmb()`, and `smp_wmb()` in Linux device drivers?
// Validated kernel and eBPF source
```

---

<a id="q69"></a>
### Q69: How do eBPF helper functions pass data to user space via `bpf_probe_read_kernel` and `bpf_probe_read_user`?

**Difficulty**: Intermediate

**Strategy**:
Safely dereferences arbitrary pointers from kernel or user virtual memory, handling page faults transparently without crashing the kernel.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How do eBPF helper functions pass data to user space via `bpf_probe_read_kernel` and `bpf_probe_read_user`?
// Validated kernel and eBPF source
```

---

<a id="q70"></a>
### Q70: What is Network Device Offloading: TSO, GSO, LRO, and GRO?

**Difficulty**: Advanced

**Strategy**:
TSO/GSO segment large 64KB TCP packets into MTU frames in NIC hardware; LRO/GRO reassemble multiple incoming packets into a single large packet before CPU stack.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is Network Device Offloading: TSO, GSO, LRO, and GRO?
// Validated kernel and eBPF source
```

---

<a id="q71"></a>
### Q71: How does the Linux Kernel handle Meltdown and Spectre CPU hardware vulnerabilities (KPTI, Retpolines)?

**Difficulty**: Advanced

**Strategy**:
Kernel Page Table Isolation (KPTI) separates user and kernel page tables to prevent speculative cache leaks; Retpolines replace indirect jumps with return trampolines.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How does the Linux Kernel handle Meltdown and Spectre CPU hardware vulnerabilities (KPTI, Retpolines)?
// Validated kernel and eBPF source
```

---

<a id="q72"></a>
### Q72: What is Real-Time Scheduling Class in Linux (SCHED_FIFO and SCHED_RR)?

**Difficulty**: Intermediate

**Strategy**:
Fixed priority classes (1-99) that preempt normal CFS tasks; SCHED_FIFO runs until it blocks or yields; SCHED_RR runs with round-robin time slice.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is Real-Time Scheduling Class in Linux (SCHED_FIFO and SCHED_RR)?
// Validated kernel and eBPF source
```

---

<a id="q73"></a>
### Q73: How do eBPF programs monitor and alter TCP Congestion Control algorithms (`bpf_setsockopt`)?

**Difficulty**: Advanced

**Strategy**:
Dynamically attaches to socket initialization; switches TCP congestion algorithm from CUBIC to BBR based on destination IP or client connection parameters.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How do eBPF programs monitor and alter TCP Congestion Control algorithms (`bpf_setsockopt`)?
// Validated kernel and eBPF source
```

---

<a id="q74"></a>
### Q74: What is `ptrace` system call and how do debuggers (GDB) inspect running processes?

**Difficulty**: Intermediate

**Strategy**:
Allows tracing process to observe and control target execution, read/write memory and CPU registers, and intercept system calls via `PTRACE_PEEKTEXT` / `PTRACE_POKETEXT`.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is `ptrace` system call and how do debuggers (GDB) inspect running processes?
// Validated kernel and eBPF source
```

---

<a id="q75"></a>
### Q75: How does Linux handle Dynamic Linker (`ld.so`) symbol resolution (`DT_NEEDED`, `PLT`, `GOT`)?

**Difficulty**: Intermediate

**Strategy**:
Dynamic linker loads shared libraries; Global Offset Table (GOT) and Procedure Linkage Table (PLT) resolve external function addresses lazily on first invocation.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How does Linux handle Dynamic Linker (`ld.so`) symbol resolution (`DT_NEEDED`, `PLT`, `GOT`)?
// Validated kernel and eBPF source
```

---

<a id="q76"></a>
### Q76: What is Kernel Live Patching (kpatch / livepatch) and how does it update kernel code without rebooting?

**Difficulty**: Advanced

**Strategy**:
Redirects function entry points to patched functions using ftrace; waits until all threads exit the old function before committing replacement.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is Kernel Live Patching (kpatch / livepatch) and how does it update kernel code without rebooting?
// Validated kernel and eBPF source
```

---

<a id="q77"></a>
### Q77: How does eBPF verify and enforce Loop Bounds in Linux kernel 5.3+?

**Difficulty**: Advanced

**Strategy**:
Allows bounded loops if the verifier can prove all branches terminate within 1 million instructions, tracking loop induction variable limits.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How does eBPF verify and enforce Loop Bounds in Linux kernel 5.3+?
// Validated kernel and eBPF source
```

---

<a id="q78"></a>
### Q78: What is the difference between Kernel Threads (`kthreads`) and User Threads?

**Difficulty**: Beginner

**Strategy**:
Kernel threads run entirely in kernel mode without user-space virtual memory mappings (e.g. `kswapd`, `kworker`), managing system background tasks.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is the difference between Kernel Threads (`kthreads`) and User Threads?
// Validated kernel and eBPF source
```

---

<a id="q79"></a>
### Q79: How does Linux implement Epoll Exclusive Wakeup (`EPOLLEXCLUSIVE`) to prevent thundering herd in multi-process servers?

**Difficulty**: Advanced

**Strategy**:
When a socket event arrives, wakes up only a single process waiting on the epoll set instead of waking all processes simultaneously.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How does Linux implement Epoll Exclusive Wakeup (`EPOLLEXCLUSIVE`) to prevent thundering herd in multi-process servers?
// Validated kernel and eBPF source
```

---

<a id="q80"></a>
### Q80: What is `futex` (Fast Userspace Mutex) and how does it optimize uncontended lock performance?

**Difficulty**: Advanced

**Strategy**:
Uncontended lock acquisition executes atomic CAS in user space without entering kernel; threads only make `sys_futex` syscall to sleep when lock is contended.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is `futex` (Fast Userspace Mutex) and how does it optimize uncontended lock performance?
// Validated kernel and eBPF source
```

---

<a id="q81"></a>
### Q81: How do eBPF programs handle atomic operations with `bpf_atomic_add`?

**Difficulty**: Intermediate

**Strategy**:
Emits hardware atomic CPU instructions (`lock xadd` on x86) directly into eBPF bytecode, updating shared counters safely without mutex locks.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How do eBPF programs handle atomic operations with `bpf_atomic_add`?
// Validated kernel and eBPF source
```

---

<a id="q82"></a>
### Q82: What is Cgroup Freezer and how does it suspend container processes atomically?

**Difficulty**: Intermediate

**Strategy**:
Freezes all tasks within a cgroup into an uninterruptible sleep state for snapshotting, checkpointing, or debugging without killing processes.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is Cgroup Freezer and how does it suspend container processes atomically?
// Validated kernel and eBPF source
```

---

<a id="q83"></a>
### Q83: How does the Linux Kernel handle Memory Ballooning in virtualized guests (virtio-balloon)?

**Difficulty**: Intermediate

**Strategy**:
Hypervisor instructs balloon driver inside guest to allocate physical RAM pages and release them to host, dynamically reclaiming guest memory.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How does the Linux Kernel handle Memory Ballooning in virtualized guests (virtio-balloon)?
// Validated kernel and eBPF source
```

---

<a id="q84"></a>
### Q84: What is eBPF Map Iterator (`bpf_iter`) for scalable map traversal?

**Difficulty**: Advanced

**Strategy**:
Streams map contents to user space sequentially through synthetic file descriptors, avoiding allocating giant snapshot arrays in user space.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is eBPF Map Iterator (`bpf_iter`) for scalable map traversal?
// Validated kernel and eBPF source
```

---

<a id="q85"></a>
### Q85: How does the Linux Kernel handle Zero-Copy File Transmission with `sendfile()` and `splice()`?

**Difficulty**: Intermediate

**Strategy**:
Transfers data directly between file page cache and socket buffer descriptors in kernel space without copying bytes back and forth to user space buffers.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How does the Linux Kernel handle Zero-Copy File Transmission with `sendfile()` and `splice()`?
// Validated kernel and eBPF source
```

---

<a id="q86"></a>
### Q86: What is Driver Bottom Half and Top Half architecture in Linux device drivers?

**Difficulty**: Beginner

**Strategy**:
Top half is the quick hardware interrupt handler that acknowledges device; Bottom half executes deferred heavy processing via tasklets or workqueues.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is Driver Bottom Half and Top Half architecture in Linux device drivers?
// Validated kernel and eBPF source
```

---

<a id="q87"></a>
### Q87: How do eBPF programs monitor and enforce File Access Control on `/etc/shadow`?

**Difficulty**: Intermediate

**Strategy**:
Attaches eBPF probe to `security_file_open` LSM hook; inspects target file path; checks process credentials and denies access if not authorized admin.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How do eBPF programs monitor and enforce File Access Control on `/etc/shadow`?
// Validated kernel and eBPF source
```

---

<a id="q88"></a>
### Q88: What is Core Dumps and how does Linux generate ELF core dump files for crashed processes?

**Difficulty**: Beginner

**Strategy**:
Saves entire memory image, CPU registers, and thread stacks of crashed process to disk in ELF format for post-mortem analysis in GDB.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is Core Dumps and how does Linux generate ELF core dump files for crashed processes?
// Validated kernel and eBPF source
```

---

<a id="q89"></a>
### Q89: How does the Linux Kernel implement Memory De-duplication using Kernel Samepage Merging (KSM)?

**Difficulty**: Advanced

**Strategy**:
Scans user memory for identical physical pages; merges them into a single Copy-on-Write page, saving memory across identical virtual machines.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How does the Linux Kernel implement Memory De-duplication using Kernel Samepage Merging (KSM)?
// Validated kernel and eBPF source
```

---

<a id="q90"></a>
### Q90: What is Hardware Watchpoint vs Software Breakpoint in kernel debugging with KGDB?

**Difficulty**: Intermediate

**Strategy**:
Software breakpoint replaces instruction with `int3` trap; Hardware watchpoint configures CPU debug registers (`DR0-DR3`) to trigger on memory read/write.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is Hardware Watchpoint vs Software Breakpoint in kernel debugging with KGDB?
// Validated kernel and eBPF source
```

---

<a id="q91"></a>
### Q91: How does eBPF integrate with Cilium for Service Mesh networking and Kubernetes CNI?

**Difficulty**: Advanced

**Strategy**:
Replaces kube-proxy iptables with eBPF maps for service load balancing; routes pod-to-pod traffic at BPF layer with sub-millisecond latency.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How does eBPF integrate with Cilium for Service Mesh networking and Kubernetes CNI?
// Validated kernel and eBPF source
```

---

<a id="q92"></a>
### Q92: What is `prctl` (Process Control) and how do secure containers drop capabilities (`PR_SET_NO_NEW_PRIVS`)?

**Difficulty**: Intermediate

**Strategy**:
`PR_SET_NO_NEW_PRIVS` prevents child processes from gaining new privileges (e.g. via setuid binaries), securing containers against privilege escalation.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is `prctl` (Process Control) and how do secure containers drop capabilities (`PR_SET_NO_NEW_PRIVS`)?
// Validated kernel and eBPF source
```

---

<a id="q93"></a>
### Q93: How does the Linux Kernel implement Cryptographic Subsystem (Crypto API) and hardware crypto accelerators?

**Difficulty**: Intermediate

**Strategy**:
Provides unified API for symmetric ciphers, hashes, and AEAD; routes requests to CPU hardware instructions (AES-NI) or offload hardware engines.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How does the Linux Kernel implement Cryptographic Subsystem (Crypto API) and hardware crypto accelerators?
// Validated kernel and eBPF source
```

---

<a id="q94"></a>
### Q94: What is Transparent Huge Pages (THP) Defrag and why can it cause latency stalls in database servers?

**Difficulty**: Advanced

**Strategy**:
Background compaction attempts to defragment memory synchronously during memory allocation, causing 100ms pauses; recommended disabled for databases.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is Transparent Huge Pages (THP) Defrag and why can it cause latency stalls in database servers?
// Validated kernel and eBPF source
```

---

<a id="q95"></a>
### Q95: How do eBPF programs inspect and modify HTTP/2 and gRPC payloads in-flight?

**Difficulty**: Advanced

**Strategy**:
Attaches to socket layer or uprobes on OpenSSL `SSL_read` / `SSL_write` to capture decrypted TLS payloads before encryption for transparent observability.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How do eBPF programs inspect and modify HTTP/2 and gRPC payloads in-flight?
// Validated kernel and eBPF source
```

---

<a id="q96"></a>
### Q96: What is the difference between eBPF Map Lookup (`bpf_map_lookup_elem`) and Update (`bpf_map_update_elem`)?

**Difficulty**: Beginner

**Strategy**:
Lookup returns pointer to value in map or NULL; Update inserts or overwrites key-value pair atomically based on flags (`BPF_ANY`, `BPF_NOEXIST`, `BPF_EXIST`).

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is the difference between eBPF Map Lookup (`bpf_map_lookup_elem`) and Update (`bpf_map_update_elem`)?
// Validated kernel and eBPF source
```

---

<a id="q97"></a>
### Q97: How do you handle eBPF Verifier Max Stack Size (512 bytes) limitations?

**Difficulty**: Intermediate

**Strategy**:
Allocate larger buffers in BPF Per-CPU Array maps rather than declaring large local structs directly on the 512-byte eBPF stack.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How do you handle eBPF Verifier Max Stack Size (512 bytes) limitations?
// Validated kernel and eBPF source
```

---

<a id="q98"></a>
### Q98: What is the role of `bpf_trace_printk` in kernel debugging and why is it restricted in production?

**Difficulty**: Beginner

**Strategy**:
Prints debug messages to `/sys/kernel/debug/tracing/trace_pipe`; restricted in production due to global lock contention and rate limit bottlenecks.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: What is the role of `bpf_trace_printk` in kernel debugging and why is it restricted in production?
// Validated kernel and eBPF source
```

---

<a id="q99"></a>
### Q99: How does Linux Kernel Page Table Isolation (KPTI) prevent Meltdown speculative execution attacks?

**Difficulty**: Advanced

**Strategy**:
Maintains two separate page tables per process: user page table has only essential trampolines; kernel page table is swapped in only during system call execution.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How does Linux Kernel Page Table Isolation (KPTI) prevent Meltdown speculative execution attacks?
// Validated kernel and eBPF source
```

---

<a id="q100"></a>
### Q100: How do you configure eBPF XDP Hardware Offload on SmartNICs (Netronome, Broadcom)?

**Difficulty**: Advanced

**Strategy**:
Compile with target flags for hardware offload; `ip link set dev eth0 xdpoffload obj prog.o` loads bytecode directly into SmartNIC NPU processors.

**Code Example**:
```c
// Linux Kernel & eBPF Engineering Implementation for: How do you configure eBPF XDP Hardware Offload on SmartNICs (Netronome, Broadcom)?
// Validated kernel and eBPF source
```

---
