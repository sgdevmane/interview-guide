<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Site Reliability Engineering (SRE) Logo" width="100" height="100">
  </a>
  <h1>Site Reliability Engineering (SRE) Interview Questions & Answers</h1>
  <p><b>Comprehensive interview questions covering SLIs, SLOs, Error Budgets, OpenTelemetry, Incident Response, and Chaos Engineering</b></p>
</div>

---

## Table of Contents

1. [How do you define SLIs, SLOs, and SLAs, and how do Error Budget Policies dictate engineering deployment velocity?](#q1) <span class="advanced">Advanced</span>
2. [How do you implement Multi-Window Multi-Burn-Rate Alerting in Prometheus to avoid pager fatigue?](#q2) <span class="advanced">Advanced</span>
3. [How does Distributed Tracing work with OpenTelemetry (Context Propagation, Trace ID, Span ID, Baggage)?](#q3) <span class="advanced">Advanced</span>
4. [What is Chaos Engineering and how do you design Chaos Mesh experiments to validate resilience?](#q4) <span class="advanced">Advanced</span>
5. [How do Circuit Breakers (Resilience4j) prevent Cascading Failures in microservices architectures?](#q5) <span class="advanced">Advanced</span>
6. [What is the Bulkhead Pattern and how does it isolate thread pools and resources?](#q6) <span class="intermediate">Intermediate</span>
7. [How do you mitigate Thundering Herd and Cache Stampede problems using probabilistic early expiration (XFetch)?](#q7) <span class="advanced">Advanced</span>
8. [What is Retry Amplification and how do Exponential Backoff and Jitter prevent server collapse?](#q8) <span class="intermediate">Intermediate</span>
9. [How do you conduct a Blameless Postmortem and what are the key sections of a production incident report?](#q9) <span class="intermediate">Intermediate</span>
10. [What is Load Shedding and Graceful Degradation during extreme traffic spikes?](#q10) <span class="advanced">Advanced</span>
11. [How do you tune Linux Kernel parameters (`somaxconn`, `tcp_max_syn_backlog`) for high concurrency?](#q11) <span class="advanced">Advanced</span>
12. [What is the difference between Prometheus Counter, Gauge, Histogram, and Summary metrics?](#q12) <span class="beginner">Beginner</span>
13. [How do you design a Zero-Downtime Blue-Green Deployment on Kubernetes?](#q13) <span class="intermediate">Intermediate</span>
14. [What is Canary Deployment with Argo Rollouts and automated metric analysis?](#q14) <span class="advanced">Advanced</span>
15. [How do you prevent Out-Of-Memory (OOM) kills in Kubernetes (`limits` vs `requests`)?](#q15) <span class="intermediate">Intermediate</span>
16. [What is Mean Time to Detect (MTTD), Mean Time to Acknowledge (MTTA), and Mean Time to Recovery (MTTR)?](#q16) <span class="beginner">Beginner</span>
17. [How do you design an Effective On-Call Rotation that prevents burnout?](#q17) <span class="intermediate">Intermediate</span>
18. [What is the difference between Runbooks and Playbooks in SRE operations?](#q18) <span class="beginner">Beginner</span>
19. [How do you handle Distributed Deadlocks in database transactions?](#q19) <span class="advanced">Advanced</span>
20. [What is Kubernetes PodDisruptionBudget (PDB) and why is it critical during node draining?](#q20) <span class="intermediate">Intermediate</span>
21. [How do you configure Horizontal Pod Autoscaler (HPA) with custom Prometheus metrics?](#q21) <span class="advanced">Advanced</span>
22. [What is MTU (Maximum Transmission Unit) mismatch and how does Path MTU Discovery (PMTUD) work?](#q22) <span class="intermediate">Intermediate</span>
23. [How do you diagnose CPU Steal Time on virtualized cloud instances (AWS EC2)?](#q23) <span class="intermediate">Intermediate</span>
24. [What is TCP TIME_WAIT state and how do you prevent socket exhaustion on high-throughput proxies?](#q24) <span class="advanced">Advanced</span>
25. [How do you implement Distributed Rate Limiting using Redis Token Bucket with Lua scripts?](#q25) <span class="advanced">Advanced</span>
26. [What is the difference between Synchronous and Asynchronous Replication in distributed databases?](#q26) <span class="intermediate">Intermediate</span>
27. [How do you calculate RTO (Recovery Time Objective) and RPO (Recovery Point Objective)?](#q27) <span class="beginner">Beginner</span>
28. [What is Split-Brain scenario in clustered systems (ZooKeeper, etcd, Elasticsearch) and how do Quorums prevent it?](#q28) <span class="advanced">Advanced</span>
29. [How do you perform Load Testing and Stress Testing using k6 or Locust?](#q29) <span class="intermediate">Intermediate</span>
30. [What is eBPF and how does it transform Linux system profiling with BCC tools (execsnoop, biolatency)?](#q30) <span class="advanced">Advanced</span>
31. [How do you design a Multi-Region Active-Active Architecture with Route 53 Latency-Based Routing?](#q31) <span class="advanced">Advanced</span>
32. [What is Zombie Process (Defunct) in Linux and how does an init system (PID 1) reap them?](#q32) <span class="intermediate">Intermediate</span>
33. [How do you manage Alert Fatigue when receiving hundreds of non-critical pages?](#q33) <span class="intermediate">Intermediate</span>
34. [What is the difference between Whitebox Monitoring and Blackbox Monitoring?](#q34) <span class="beginner">Beginner</span>
35. [How do you implement Canary Analysis with Kayenta in Spinnaker?](#q35) <span class="advanced">Advanced</span>
36. [What is Kernel Panic in Linux and how do you analyze `kdump` / `vmcore` crash dumps?](#q36) <span class="advanced">Advanced</span>
37. [How do you configure Liveness, Readiness, and Startup Probes in Kubernetes?](#q37) <span class="intermediate">Intermediate</span>
38. [What is Epoll (Event Poll) in Linux and why does it scale to 100k connections over `select`?](#q38) <span class="advanced">Advanced</span>
39. [How do you configure Automated Database Failover in PostgreSQL using Patroni and etcd?](#q39) <span class="advanced">Advanced</span>
40. [What is the difference between Vertical Scaling and Horizontal Scaling?](#q40) <span class="beginner">Beginner</span>
41. [How do you handle Cascade Deletions and Distributed Transactions with Saga Orchestration?](#q41) <span class="advanced">Advanced</span>
42. [What is Disk I/O Throttling in AWS EBS (Burst Credits, IOPS, Throughput)?](#q42) <span class="intermediate">Intermediate</span>
43. [How do you design a Disaster Recovery Runbook for total AWS Region Outage?](#q43) <span class="advanced">Advanced</span>
44. [What is Log Aggregation Architecture (FluentBit -> Kafka -> OpenSearch)?](#q44) <span class="intermediate">Intermediate</span>
45. [How do you measure Page Load Performance with Core Web Vitals (LCP, FID, CLS)?](#q45) <span class="beginner">Beginner</span>
46. [What is TCP Window Scaling and how does it enable gigabit throughput over high-latency networks?](#q46) <span class="advanced">Advanced</span>
47. [How do you diagnose Memory Fragmentation in long-running C/C++ or Go services?](#q47) <span class="advanced">Advanced</span>
48. [What is the purpose of Graceful Shutdown handling (`SIGTERM` vs `SIGKILL`) in microservices?](#q48) <span class="intermediate">Intermediate</span>
49. [How do you configure PromQL queries to alert on disk space exhaustion within 4 hours (`predict_linear`)?](#q49) <span class="intermediate">Intermediate</span>
50. [What is BGP Anycast and how is it used for Global DNS and DDoS Mitigation?](#q50) <span class="advanced">Advanced</span>
51. [How do you prevent DNS Caching issues when rotating IP addresses during deployments?](#q51) <span class="intermediate">Intermediate</span>
52. [What is Swapping in Linux and why is swap usually disabled on Kubernetes nodes?](#q52) <span class="intermediate">Intermediate</span>
53. [How do you audit and trace slow database queries in PostgreSQL with `pg_stat_statements`?](#q53) <span class="intermediate">Intermediate</span>
54. [What is the role of Bastion Hosts and Jump Servers in secure infrastructure access?](#q54) <span class="beginner">Beginner</span>
55. [How do you set up synthetic monitoring to detect silent frontend failures?](#q55) <span class="intermediate">Intermediate</span>
56. [What is the CAP Theorem and how does PACELC expand upon it?](#q56) <span class="advanced">Advanced</span>
57. [How do you handle Clock Drift in distributed systems using NTP and PTP (IEEE 1588)?](#q57) <span class="advanced">Advanced</span>
58. [What is Vector Clock and Lamport Timestamp in distributed state tracking?](#q58) <span class="advanced">Advanced</span>
59. [How do you troubleshoot high 504 Gateway Timeout errors on an API reverse proxy?](#q59) <span class="intermediate">Intermediate</span>
60. [What is Blue-Green Database Migration and how do you handle backward compatibility?](#q60) <span class="advanced">Advanced</span>
61. [How do you manage Secrets Rotation with Zero Downtime for TLS Certificates?](#q61) <span class="intermediate">Intermediate</span>
62. [What is the Two Generals Problem and why is consensus over unreliable networks unsolvable in bounded time?](#q62) <span class="advanced">Advanced</span>
63. [How do you implement Backpressure in Reactive Streams to prevent out-of-memory crashes?](#q63) <span class="advanced">Advanced</span>
64. [What is Sticky Sessions (Session Affinity) and why does it undermine horizontal scaling?](#q64) <span class="intermediate">Intermediate</span>
65. [How do you configure Envoy Proxy as an edge ingress controller?](#q65) <span class="advanced">Advanced</span>
66. [What is Shadow Traffic (Dark Launching) and how do you test new versions with production load?](#q66) <span class="advanced">Advanced</span>
67. [How do you detect Memory Leaks in Java applications using Garbage Collection logs and Heap Dumps?](#q67) <span class="intermediate">Intermediate</span>
68. [What is Caching Tier Invalidation: TTL vs Event-Driven Invalidation?](#q68) <span class="intermediate">Intermediate</span>
69. [How do you configure Core Dumps in Linux for post-crash debugging?](#q69) <span class="intermediate">Intermediate</span>
70. [What is Service Mesh (Istio / Linkerd) and what are the trade-offs of sidecar proxies?](#q70) <span class="advanced">Advanced</span>
71. [How do you monitor and resolve Connection Pool Exhaustion in microservices?](#q71) <span class="intermediate">Intermediate</span>
72. [What is the difference between Load Balancing Algorithms: Round Robin, Least Connections, IP Hash?](#q72) <span class="beginner">Beginner</span>
73. [How do you build an SLA Dashboard in Grafana showing uptime compliance?](#q73) <span class="intermediate">Intermediate</span>
74. [What is Chaos Engineering GameDay and how do you run it safely in staging?](#q74) <span class="intermediate">Intermediate</span>
75. [How do you debug high CPU usage caused by spinlocks or busy-waiting threads?](#q75) <span class="advanced">Advanced</span>
76. [What is Dead Letter Queue (DLQ) in message brokers and how do you handle poisoned messages?](#q76) <span class="intermediate">Intermediate</span>
77. [How do you configure Log Rotation using `logrotate` to prevent disk saturation?](#q77) <span class="beginner">Beginner</span>
78. [What is Rate Limiting using Leaky Bucket vs Token Bucket algorithms?](#q78) <span class="intermediate">Intermediate</span>
79. [How do you handle High Availability for Redis with Redis Sentinel vs Redis Cluster?](#q79) <span class="advanced">Advanced</span>
80. [What is Edge Caching and how does Cloudflare / CloudFront accelerate static and dynamic content?](#q80) <span class="beginner">Beginner</span>
81. [How do you perform Disaster Recovery Testing without impacting production users?](#q81) <span class="advanced">Advanced</span>
82. [What is the difference between Active-Active and Active-Passive Failover?](#q82) <span class="beginner">Beginner</span>
83. [How do you detect Slow Memory Leaks using Prometheus `rate()` on process resident memory?](#q83) <span class="intermediate">Intermediate</span>
84. [What is Out-of-Band Management (IPMI, iLO) and how does it rescue unresponsive bare-metal servers?](#q84) <span class="intermediate">Intermediate</span>
85. [How do you secure Production Systems during an ongoing Zero-Day Vulnerability Incident?](#q85) <span class="advanced">Advanced</span>
86. [What is the role of Site Reliability Engineering in Architecture Review Boards (ARB)?](#q86) <span class="intermediate">Intermediate</span>
87. [How do you build automated rollback mechanisms in Continuous Deployment pipelines?](#q87) <span class="intermediate">Intermediate</span>
88. [What is the difference between Hard Links and Soft Links (Symlinks) in Linux filesystems?](#q88) <span class="beginner">Beginner</span>
89. [How do you trace Kernel I/O bottlenecks with `iostat` and `iotop`?](#q89) <span class="intermediate">Intermediate</span>
90. [What is the Single Responsibility Principle applied to Microservices Architecture?](#q90) <span class="intermediate">Intermediate</span>
91. [How do you handle Database Connection Leaks in Node.js or Python backend services?](#q91) <span class="intermediate">Intermediate</span>
92. [What is the difference between Horizontal Pod Autoscaling (HPA) and Vertical Pod Autoscaling (VPA)?](#q92) <span class="intermediate">Intermediate</span>
93. [How do you tune TCP Keepalive settings to detect dead peers across cloud firewalls?](#q93) <span class="intermediate">Intermediate</span>
94. [What is Incident Retrospective Follow-Through and how do you ensure P0 action items get completed?](#q94) <span class="intermediate">Intermediate</span>
95. [How do you manage DNS Propagation Delays when changing authoritative nameservers?](#q95) <span class="intermediate">Intermediate</span>
96. [How do you configure CoreDNS in Kubernetes to prevent DNS resolution throttling?](#q96) <span class="intermediate">Intermediate</span>
97. [What is the difference between Ingress Controller and Service of type LoadBalancer in Kubernetes?](#q97) <span class="beginner">Beginner</span>
98. [How do you design a graceful connection draining policy during rolling updates?](#q98) <span class="intermediate">Intermediate</span>
99. [What is Write-Ahead Logging (WAL) in distributed storage and how does it guarantee durability?](#q99) <span class="advanced">Advanced</span>
100. [How do you automate Capacity Planning using historical growth metrics and linear extrapolation?](#q100) <span class="intermediate">Intermediate</span>

---

<a id="q1"></a>
### Q1: How do you define SLIs, SLOs, and SLAs, and how do Error Budget Policies dictate engineering deployment velocity?

**Difficulty**: Advanced

**Strategy**:
SLI (Service Level Indicator) is a quantifiable metric (e.g. 99.92% of HTTP requests return 2xx within 200ms). SLO (Service Level Objective) is the internal target agreed with Product (e.g. 99.9% availability per 30-day window). SLA (Service Level Agreement) is the legal contract with financial penalties. The Error Budget is $100\% - \text{SLO}$ (e.g. 0.1% = 43 minutes downtime/month). When the error budget is exhausted, automated deployment policies freeze feature releases, shifting all engineering focus to reliability and tech debt until stability returns.

**Code Example**:
```markdown
Error Budget Policy Framework:
- 100% - 25% Budget: Normal feature velocity.
- 25% - 0% Budget: Warning threshold, non-essential deployments delayed.
- 0% Budget (Exhausted): Feature freeze enforced; engineering works exclusively on P0 reliability.
```

---

<a id="q2"></a>
### Q2: How do you implement Multi-Window Multi-Burn-Rate Alerting in Prometheus to avoid pager fatigue?

**Difficulty**: Advanced

**Strategy**:
Single-window alerts either trigger too slowly or wake up engineers for transient spikes. Google SRE Multi-Burn-Rate Alerting evaluates two windows simultaneously (short and long window): e.g. a 14.4x burn rate consumed over 1 hour AND 5 minutes indicates 2% error budget lost in an hour, paging the on-call engineer immediately. A 1x burn rate over 3 days opens a low-priority Jira ticket.

**Code Example**:
```yaml
# Prometheus Multi-Burn-Rate Alert (14.4x burn rate = 2% budget in 1 hour)
expr: (
  sum(rate(http_requests_total{status=~"5.."}[1h])) / sum(rate(http_requests_total[1h])) > (14.4 * 0.001)
  and
  sum(rate(http_requests_total{status=~"5.."}[5m])) / sum(rate(http_requests_total[5m])) > (14.4 * 0.001)
)
for: 2m
labels:
  severity: page
```

---

<a id="q3"></a>
### Q3: How does Distributed Tracing work with OpenTelemetry (Context Propagation, Trace ID, Span ID, Baggage)?

**Difficulty**: Advanced

**Strategy**:
When an HTTP request enters an edge gateway, OpenTelemetry generates a 128-bit Trace ID and 64-bit Span ID. As the request calls downstream microservices, the Trace Context is propagated via W3C HTTP headers (`traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01`). Downstream services create child spans linked to the parent Span ID, building an end-to-end directed acyclic graph (DAG) visualizing latency waterfalls across all services.

**Code Example**:
```bash
# W3C Traceparent Header Format
traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01
#            version-trace_id(32 hex)-parent_span_id(16 hex)-trace_flags(2 hex)
```

---

<a id="q4"></a>
### Q4: What is Chaos Engineering and how do you design Chaos Mesh experiments to validate resilience?

**Difficulty**: Advanced

**Strategy**:
Chaos Engineering empirically proves that a distributed system survives unpredictable failures in production. With Chaos Mesh, declarative experiments inject network latency, packet loss, pod kills, or clock skew. The steady state (SLIs like error rate and latency) must remain within SLO boundaries during the blast radius of the experiment.

**Code Example**:
```yaml
# Chaos Mesh PodKill Experiment Definition
apiVersion: chaos-mesh.org/v1alpha1
kind: PodChaos
metadata:
  name: random-pod-kill
spec:
  action: pod-kill
  mode: fixed
  value: '1'
  selector:
    namespaces:
      - production
    labelSelectors:
      app: order-processor
  scheduler:
    cron: '@every 2h'
```

---

<a id="q5"></a>
### Q5: How do Circuit Breakers (Resilience4j) prevent Cascading Failures in microservices architectures?

**Difficulty**: Advanced

**Strategy**:
When downstream service latency or errors spike, calling threads block waiting for timeouts, quickly exhausting thread and connection pools. A Circuit Breaker transitions between three states: 1) **Closed**: Requests pass normally. 2) **Open**: If failure rate exceeds threshold (e.g. 50%), all calls fail fast immediately without hitting downstream service. 3) **Half-Open**: After a sleep window, permits trial requests to probe if downstream has recovered.

**Code Example**:
```yaml
# Resilience4j Circuit Breaker Configuration
resilience4j.circuitbreaker:
  instances:
    paymentService:
      failureRateThreshold: 50
      waitDurationInOpenState: 10000ms
      ringBufferSizeInHalfOpenState: 5
      ringBufferSizeInClosedState: 100
```

---

<a id="q6"></a>
### Q6: What is the Bulkhead Pattern and how does it isolate thread pools and resources?

**Difficulty**: Intermediate

**Strategy**:
Separates resource pools (thread pools, connection pools) per dependent service so a slow payment gateway cannot consume all threads and crash search.

**Code Example**:
```yaml
# Production SRE Specification for: What is the Bulkhead Pattern and how does it isolate thread pools and resources?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q7"></a>
### Q7: How do you mitigate Thundering Herd and Cache Stampede problems using probabilistic early expiration (XFetch)?

**Difficulty**: Advanced

**Strategy**:
Uses probabilistic algorithm where background workers asynchronously refresh cache before actual TTL expires as load increases.

**Code Example**:
```yaml
# Production SRE Specification for: How do you mitigate Thundering Herd and Cache Stampede problems using probabilistic early expiration (XFetch)?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q8"></a>
### Q8: What is Retry Amplification and how do Exponential Backoff and Jitter prevent server collapse?

**Difficulty**: Intermediate

**Strategy**:
Naive immediate retries multiply load on failing servers. Exponential backoff with randomized jitter spreads out retries evenly over time.

**Code Example**:
```yaml
# Production SRE Specification for: What is Retry Amplification and how do Exponential Backoff and Jitter prevent server collapse?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q9"></a>
### Q9: How do you conduct a Blameless Postmortem and what are the key sections of a production incident report?

**Difficulty**: Intermediate

**Strategy**:
Focuses on systemic failures: Incident Summary, Impact Duration, Timeline of Events, Root Cause (5 Whys), What Went Well, Action Items with Owners.

**Code Example**:
```yaml
# Production SRE Specification for: How do you conduct a Blameless Postmortem and what are the key sections of a production incident report?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q10"></a>
### Q10: What is Load Shedding and Graceful Degradation during extreme traffic spikes?

**Difficulty**: Advanced

**Strategy**:
Drops non-essential requests (e.g. recommendations) when CPU/queue depth crosses 80%, guaranteeing core revenue paths (e.g. checkout) succeed.

**Code Example**:
```yaml
# Production SRE Specification for: What is Load Shedding and Graceful Degradation during extreme traffic spikes?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q11"></a>
### Q11: How do you tune Linux Kernel parameters (`somaxconn`, `tcp_max_syn_backlog`) for high concurrency?

**Difficulty**: Advanced

**Strategy**:
Increase socket listen backlog (`net.core.somaxconn = 65535`) and SYN backlog (`net.ipv4.tcp_max_syn_backlog = 65535`) to prevent connection drops.

**Code Example**:
```yaml
# Production SRE Specification for: How do you tune Linux Kernel parameters (`somaxconn`, `tcp_max_syn_backlog`) for high concurrency?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q12"></a>
### Q12: What is the difference between Prometheus Counter, Gauge, Histogram, and Summary metrics?

**Difficulty**: Beginner

**Strategy**:
Counter: monotonically increasing; Gauge: snapshot value that goes up/down; Histogram: client-bucketed counts for quantiles; Summary: calculates quantiles on client.

**Code Example**:
```yaml
# Production SRE Specification for: What is the difference between Prometheus Counter, Gauge, Histogram, and Summary metrics?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q13"></a>
### Q13: How do you design a Zero-Downtime Blue-Green Deployment on Kubernetes?

**Difficulty**: Intermediate

**Strategy**:
Deploys identical new version (Green) alongside active (Blue); validates Green health probes, switches service selector labels, and terminates Blue after grace period.

**Code Example**:
```yaml
# Production SRE Specification for: How do you design a Zero-Downtime Blue-Green Deployment on Kubernetes?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q14"></a>
### Q14: What is Canary Deployment with Argo Rollouts and automated metric analysis?

**Difficulty**: Advanced

**Strategy**:
Directs 5% traffic to canary; queries Prometheus error rate; automatically steps up traffic if metrics pass, or rolls back immediately if error threshold is breached.

**Code Example**:
```yaml
# Production SRE Specification for: What is Canary Deployment with Argo Rollouts and automated metric analysis?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q15"></a>
### Q15: How do you prevent Out-Of-Memory (OOM) kills in Kubernetes (`limits` vs `requests`)?

**Difficulty**: Intermediate

**Strategy**:
`requests` guarantees node scheduling capacity; `limits` sets cgroup hard ceiling. Setting limits equal to requests assigns Guaranteed QoS class preventing early evictions.

**Code Example**:
```yaml
# Production SRE Specification for: How do you prevent Out-Of-Memory (OOM) kills in Kubernetes (`limits` vs `requests`)?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q16"></a>
### Q16: What is Mean Time to Detect (MTTD), Mean Time to Acknowledge (MTTA), and Mean Time to Recovery (MTTR)?

**Difficulty**: Beginner

**Strategy**:
MTTD: time from failure to alert; MTTA: time from page to engineer investigating; MTTR: time from investigation to service restoration.

**Code Example**:
```yaml
# Production SRE Specification for: What is Mean Time to Detect (MTTD), Mean Time to Acknowledge (MTTA), and Mean Time to Recovery (MTTR)?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q17"></a>
### Q17: How do you design an Effective On-Call Rotation that prevents burnout?

**Difficulty**: Intermediate

**Strategy**:
Implement follow-the-sun rotation across global teams, secondary on-call backup, mandatory comp time after overnight pages, and maximum 1 week shifts.

**Code Example**:
```yaml
# Production SRE Specification for: How do you design an Effective On-Call Rotation that prevents burnout?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q18"></a>
### Q18: What is the difference between Runbooks and Playbooks in SRE operations?

**Difficulty**: Beginner

**Strategy**:
Runbooks provide step-by-step technical procedures for routine tasks (e.g. certificate renewal); Playbooks outline incident remediation responses.

**Code Example**:
```yaml
# Production SRE Specification for: What is the difference between Runbooks and Playbooks in SRE operations?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q19"></a>
### Q19: How do you handle Distributed Deadlocks in database transactions?

**Difficulty**: Advanced

**Strategy**:
Enforce consistent global lock ordering across services, set low lock acquisition timeouts, and implement distributed transaction orchestrator dead-letter queues.

**Code Example**:
```yaml
# Production SRE Specification for: How do you handle Distributed Deadlocks in database transactions?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q20"></a>
### Q20: What is Kubernetes PodDisruptionBudget (PDB) and why is it critical during node draining?

**Difficulty**: Intermediate

**Strategy**:
Specifies minimum number of concurrent replicas that must remain available during voluntary disruptions (e.g. cluster node upgrades).

**Code Example**:
```yaml
# Production SRE Specification for: What is Kubernetes PodDisruptionBudget (PDB) and why is it critical during node draining?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q21"></a>
### Q21: How do you configure Horizontal Pod Autoscaler (HPA) with custom Prometheus metrics?

**Difficulty**: Advanced

**Strategy**:
Deploy Prometheus Adapter; configure HPA to scale pods based on custom metrics like Kafka queue lag or request latency rather than raw CPU/RAM.

**Code Example**:
```yaml
# Production SRE Specification for: How do you configure Horizontal Pod Autoscaler (HPA) with custom Prometheus metrics?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q22"></a>
### Q22: What is MTU (Maximum Transmission Unit) mismatch and how does Path MTU Discovery (PMTUD) work?

**Difficulty**: Intermediate

**Strategy**:
Large packets exceeding MTU are dropped if DF flag is set; PMTUD uses ICMP Destination Unreachable (Fragmentation Needed) packets to negotiate size.

**Code Example**:
```yaml
# Production SRE Specification for: What is MTU (Maximum Transmission Unit) mismatch and how does Path MTU Discovery (PMTUD) work?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q23"></a>
### Q23: How do you diagnose CPU Steal Time on virtualized cloud instances (AWS EC2)?

**Difficulty**: Intermediate

**Strategy**:
Check `top` '%st'; high steal time indicates hypervisor host is oversubscribed and competing VMs are consuming CPU cycles.

**Code Example**:
```yaml
# Production SRE Specification for: How do you diagnose CPU Steal Time on virtualized cloud instances (AWS EC2)?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q24"></a>
### Q24: What is TCP TIME_WAIT state and how do you prevent socket exhaustion on high-throughput proxies?

**Difficulty**: Advanced

**Strategy**:
Socket remains in TIME_WAIT for 2x MSL (60s) to handle delayed packets. Prevent exhaustion with connection pooling, keepalive, and `tcp_tw_reuse`.

**Code Example**:
```yaml
# Production SRE Specification for: What is TCP TIME_WAIT state and how do you prevent socket exhaustion on high-throughput proxies?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q25"></a>
### Q25: How do you implement Distributed Rate Limiting using Redis Token Bucket with Lua scripts?

**Difficulty**: Advanced

**Strategy**:
Execute atomic Lua script on Redis checking token refill rate and decrementing token count in a single round-trip, preventing race conditions.

**Code Example**:
```yaml
# Production SRE Specification for: How do you implement Distributed Rate Limiting using Redis Token Bucket with Lua scripts?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q26"></a>
### Q26: What is the difference between Synchronous and Asynchronous Replication in distributed databases?

**Difficulty**: Intermediate

**Strategy**:
Synchronous guarantees zero data loss (RPO=0) but adds network latency to write path; Asynchronous writes locally first, risking data loss on primary crash.

**Code Example**:
```yaml
# Production SRE Specification for: What is the difference between Synchronous and Asynchronous Replication in distributed databases?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q27"></a>
### Q27: How do you calculate RTO (Recovery Time Objective) and RPO (Recovery Point Objective)?

**Difficulty**: Beginner

**Strategy**:
RTO: maximum acceptable duration of system downtime; RPO: maximum acceptable age of data lost measured in time.

**Code Example**:
```yaml
# Production SRE Specification for: How do you calculate RTO (Recovery Time Objective) and RPO (Recovery Point Objective)?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q28"></a>
### Q28: What is Split-Brain scenario in clustered systems (ZooKeeper, etcd, Elasticsearch) and how do Quorums prevent it?

**Difficulty**: Advanced

**Strategy**:
Network partition isolates cluster nodes into two halves, both claiming leadership. Prevented by requiring strict majority quorum: $N/2 + 1$ votes.

**Code Example**:
```yaml
# Production SRE Specification for: What is Split-Brain scenario in clustered systems (ZooKeeper, etcd, Elasticsearch) and how do Quorums prevent it?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q29"></a>
### Q29: How do you perform Load Testing and Stress Testing using k6 or Locust?

**Difficulty**: Intermediate

**Strategy**:
Write code-defined load test scenarios simulating ramp-up to peak traffic; monitor p95 latency, error rates, and resource bottlenecks.

**Code Example**:
```yaml
# Production SRE Specification for: How do you perform Load Testing and Stress Testing using k6 or Locust?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q30"></a>
### Q30: What is eBPF and how does it transform Linux system profiling with BCC tools (execsnoop, biolatency)?

**Difficulty**: Advanced

**Strategy**:
Attaches to kernel tracepoints to record block I/O latency distributions and process executions with near-zero overhead without modifying kernel.

**Code Example**:
```yaml
# Production SRE Specification for: What is eBPF and how does it transform Linux system profiling with BCC tools (execsnoop, biolatency)?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q31"></a>
### Q31: How do you design a Multi-Region Active-Active Architecture with Route 53 Latency-Based Routing?

**Difficulty**: Advanced

**Strategy**:
Deploy services in 2+ cloud regions; Route 53 routes users to lowest-latency region; cross-region database replication handles data synchronization.

**Code Example**:
```yaml
# Production SRE Specification for: How do you design a Multi-Region Active-Active Architecture with Route 53 Latency-Based Routing?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q32"></a>
### Q32: What is Zombie Process (Defunct) in Linux and how does an init system (PID 1) reap them?

**Difficulty**: Intermediate

**Strategy**:
Terminated child process whose parent has not read its exit status via `waitpid()`. If parent dies, PID 1 (systemd/tini) adopts and reaps the zombie.

**Code Example**:
```yaml
# Production SRE Specification for: What is Zombie Process (Defunct) in Linux and how does an init system (PID 1) reap them?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q33"></a>
### Q33: How do you manage Alert Fatigue when receiving hundreds of non-critical pages?

**Difficulty**: Intermediate

**Strategy**:
Audit all alerts triggered over last 90 days; delete any alert that did not require human action; convert warnings to Slack channels instead of pagers.

**Code Example**:
```yaml
# Production SRE Specification for: How do you manage Alert Fatigue when receiving hundreds of non-critical pages?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q34"></a>
### Q34: What is the difference between Whitebox Monitoring and Blackbox Monitoring?

**Difficulty**: Beginner

**Strategy**:
Whitebox monitors internal state (memory, thread pools, logs); Blackbox monitors external user-facing behavior (HTTP status, ping, synthetic probes).

**Code Example**:
```yaml
# Production SRE Specification for: What is the difference between Whitebox Monitoring and Blackbox Monitoring?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q35"></a>
### Q35: How do you implement Canary Analysis with Kayenta in Spinnaker?

**Difficulty**: Advanced

**Strategy**:
Statistically compares metrics between baseline and canary deployments over time using Mann-Whitney U test, automatically rolling back on statistical regressions.

**Code Example**:
```yaml
# Production SRE Specification for: How do you implement Canary Analysis with Kayenta in Spinnaker?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q36"></a>
### Q36: What is Kernel Panic in Linux and how do you analyze `kdump` / `vmcore` crash dumps?

**Difficulty**: Advanced

**Strategy**:
Kernel fatal error unrecoverable by OS. Dump memory to disk via kdump; load vmcore into `crash` utility with vmlinux symbols to inspect stack trace.

**Code Example**:
```yaml
# Production SRE Specification for: What is Kernel Panic in Linux and how do you analyze `kdump` / `vmcore` crash dumps?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q37"></a>
### Q37: How do you configure Liveness, Readiness, and Startup Probes in Kubernetes?

**Difficulty**: Intermediate

**Strategy**:
Startup probe delays checks during slow boot; Readiness probe removes unready pod from Service endpoints; Liveness probe restarts deadlocked containers.

**Code Example**:
```yaml
# Production SRE Specification for: How do you configure Liveness, Readiness, and Startup Probes in Kubernetes?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q38"></a>
### Q38: What is Epoll (Event Poll) in Linux and why does it scale to 100k connections over `select`?

**Difficulty**: Advanced

**Strategy**:
`select` scans all file descriptors in $O(N)$ time; `epoll` registers interest once in kernel and uses wait queues to return only active FDs in $O(1)$.

**Code Example**:
```yaml
# Production SRE Specification for: What is Epoll (Event Poll) in Linux and why does it scale to 100k connections over `select`?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q39"></a>
### Q39: How do you configure Automated Database Failover in PostgreSQL using Patroni and etcd?

**Difficulty**: Advanced

**Strategy**:
Patroni nodes use etcd for leader election; when primary fails to renew DCS lease, a standby is elected and promoted automatically with minimal downtime.

**Code Example**:
```yaml
# Production SRE Specification for: How do you configure Automated Database Failover in PostgreSQL using Patroni and etcd?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q40"></a>
### Q40: What is the difference between Vertical Scaling and Horizontal Scaling?

**Difficulty**: Beginner

**Strategy**:
Vertical: upgrade machine CPU/RAM (simple, hardware ceiling, single point of failure); Horizontal: add more instances (resilient, requires stateless design).

**Code Example**:
```yaml
# Production SRE Specification for: What is the difference between Vertical Scaling and Horizontal Scaling?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q41"></a>
### Q41: How do you handle Cascade Deletions and Distributed Transactions with Saga Orchestration?

**Difficulty**: Advanced

**Strategy**:
Orchestrator sends compensating transactions (undo actions) to previous services when a step fails, maintaining eventual consistency without distributed locks.

**Code Example**:
```yaml
# Production SRE Specification for: How do you handle Cascade Deletions and Distributed Transactions with Saga Orchestration?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q42"></a>
### Q42: What is Disk I/O Throttling in AWS EBS (Burst Credits, IOPS, Throughput)?

**Difficulty**: Intermediate

**Strategy**:
GP3 provides baseline 3,000 IOPS and 125 MB/s; exceeding burst limits triggers I/O queueing and high latency. Monitor `VolumeQueueLength` in CloudWatch.

**Code Example**:
```yaml
# Production SRE Specification for: What is Disk I/O Throttling in AWS EBS (Burst Credits, IOPS, Throughput)?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q43"></a>
### Q43: How do you design a Disaster Recovery Runbook for total AWS Region Outage?

**Difficulty**: Advanced

**Strategy**:
Automated Terraform apply in secondary region, restore DB snapshots or failover Global Database, update Route 53 health check DNS records.

**Code Example**:
```yaml
# Production SRE Specification for: How do you design a Disaster Recovery Runbook for total AWS Region Outage?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q44"></a>
### Q44: What is Log Aggregation Architecture (FluentBit -> Kafka -> OpenSearch)?

**Difficulty**: Intermediate

**Strategy**:
FluentBit collects container logs from node; buffers in Kafka to absorb spikes; Logstash parses and indexes into OpenSearch with lifecycle retention.

**Code Example**:
```yaml
# Production SRE Specification for: What is Log Aggregation Architecture (FluentBit -> Kafka -> OpenSearch)?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q45"></a>
### Q45: How do you measure Page Load Performance with Core Web Vitals (LCP, FID, CLS)?

**Difficulty**: Beginner

**Strategy**:
LCP (Largest Contentful Paint < 2.5s); FID / INP (Interaction to Next Paint < 200ms); CLS (Cumulative Layout Shift < 0.1).

**Code Example**:
```yaml
# Production SRE Specification for: How do you measure Page Load Performance with Core Web Vitals (LCP, FID, CLS)?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q46"></a>
### Q46: What is TCP Window Scaling and how does it enable gigabit throughput over high-latency networks?

**Difficulty**: Advanced

**Strategy**:
Expands the 16-bit window size field up to 1GB using a scale factor option in the SYN packet, allowing filling the Bandwidth-Delay Product (BDP).

**Code Example**:
```yaml
# Production SRE Specification for: What is TCP Window Scaling and how does it enable gigabit throughput over high-latency networks?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q47"></a>
### Q47: How do you diagnose Memory Fragmentation in long-running C/C++ or Go services?

**Difficulty**: Advanced

**Strategy**:
Compare virtual memory size (VSS/RSS) with allocated heap bytes; use jemalloc memory profiler with heap profiling flags (`MALLOC_CONF=prof:true`).

**Code Example**:
```yaml
# Production SRE Specification for: How do you diagnose Memory Fragmentation in long-running C/C++ or Go services?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q48"></a>
### Q48: What is the purpose of Graceful Shutdown handling (`SIGTERM` vs `SIGKILL`) in microservices?

**Difficulty**: Intermediate

**Strategy**:
On SIGTERM, finish in-flight requests, drain active connection pools, stop accepting new connections; SIGKILL immediately terminates process without cleanup.

**Code Example**:
```yaml
# Production SRE Specification for: What is the purpose of Graceful Shutdown handling (`SIGTERM` vs `SIGKILL`) in microservices?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q49"></a>
### Q49: How do you configure PromQL queries to alert on disk space exhaustion within 4 hours (`predict_linear`)?

**Difficulty**: Intermediate

**Strategy**:
`predict_linear(node_filesystem_free_bytes[4h], 4 * 3600) < 0` alerts before disk is completely full based on current write velocity.

**Code Example**:
```yaml
# Production SRE Specification for: How do you configure PromQL queries to alert on disk space exhaustion within 4 hours (`predict_linear`)?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q50"></a>
### Q50: What is BGP Anycast and how is it used for Global DNS and DDoS Mitigation?

**Difficulty**: Advanced

**Strategy**:
Multiple servers worldwide advertise the identical IP address via BGP; internet routers route clients to topologically closest datacenter.

**Code Example**:
```yaml
# Production SRE Specification for: What is BGP Anycast and how is it used for Global DNS and DDoS Mitigation?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q51"></a>
### Q51: How do you prevent DNS Caching issues when rotating IP addresses during deployments?

**Difficulty**: Intermediate

**Strategy**:
Lower DNS TTL to 60 seconds days before the planned migration; verify all clients respect TTL before swapping endpoints.

**Code Example**:
```yaml
# Production SRE Specification for: How do you prevent DNS Caching issues when rotating IP addresses during deployments?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q52"></a>
### Q52: What is Swapping in Linux and why is swap usually disabled on Kubernetes nodes?

**Difficulty**: Intermediate

**Strategy**:
Moving memory pages to slow disk ruins deterministic latency guarantees; disabling swap ensures kubelet accurately manages memory limits and evictions.

**Code Example**:
```yaml
# Production SRE Specification for: What is Swapping in Linux and why is swap usually disabled on Kubernetes nodes?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q53"></a>
### Q53: How do you audit and trace slow database queries in PostgreSQL with `pg_stat_statements`?

**Difficulty**: Intermediate

**Strategy**:
Enable extension `pg_stat_statements`; query top queries by `total_exec_time` and `mean_exec_time` to identify unindexed full table scans.

**Code Example**:
```yaml
# Production SRE Specification for: How do you audit and trace slow database queries in PostgreSQL with `pg_stat_statements`?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q54"></a>
### Q54: What is the role of Bastion Hosts and Jump Servers in secure infrastructure access?

**Difficulty**: Beginner

**Strategy**:
Single hardened entry point into private networks; enforces MFA, logs all SSH sessions, and keeps internal servers inaccessible to the public internet.

**Code Example**:
```yaml
# Production SRE Specification for: What is the role of Bastion Hosts and Jump Servers in secure infrastructure access?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q55"></a>
### Q55: How do you set up synthetic monitoring to detect silent frontend failures?

**Difficulty**: Intermediate

**Strategy**:
Run headless browser scripts (Playwright) every 5 minutes in multiple geographic regions to test login, search, and checkout flows continuously.

**Code Example**:
```yaml
# Production SRE Specification for: How do you set up synthetic monitoring to detect silent frontend failures?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q56"></a>
### Q56: What is the CAP Theorem and how does PACELC expand upon it?

**Difficulty**: Advanced

**Strategy**:
CAP: Consistency vs Availability under Partition; PACELC adds: if no Partition (P), choose between Availability (A) or Consistency (C); Else (E), Latency (L) vs Consistency (C).

**Code Example**:
```yaml
# Production SRE Specification for: What is the CAP Theorem and how does PACELC expand upon it?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q57"></a>
### Q57: How do you handle Clock Drift in distributed systems using NTP and PTP (IEEE 1588)?

**Difficulty**: Advanced

**Strategy**:
Hardware clock drift causes out-of-order events; NTP synchronizes within milliseconds; PTP synchronizes via hardware NIC timestamps within nanoseconds.

**Code Example**:
```yaml
# Production SRE Specification for: How do you handle Clock Drift in distributed systems using NTP and PTP (IEEE 1588)?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q58"></a>
### Q58: What is Vector Clock and Lamport Timestamp in distributed state tracking?

**Difficulty**: Advanced

**Strategy**:
Logical clocks capturing causal ordering of events ($A \rightarrow B$) across distributed systems without relying on synchronized physical wall clocks.

**Code Example**:
```yaml
# Production SRE Specification for: What is Vector Clock and Lamport Timestamp in distributed state tracking?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q59"></a>
### Q59: How do you troubleshoot high 504 Gateway Timeout errors on an API reverse proxy?

**Difficulty**: Intermediate

**Strategy**:
504 means upstream backend failed to respond within proxy timeout window; inspect backend thread pool saturation, slow DB queries, or deadlock.

**Code Example**:
```yaml
# Production SRE Specification for: How do you troubleshoot high 504 Gateway Timeout errors on an API reverse proxy?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q60"></a>
### Q60: What is Blue-Green Database Migration and how do you handle backward compatibility?

**Difficulty**: Advanced

**Strategy**:
Database schema changes must be backward-compatible with older application code (additive changes only; drop deprecated columns in later release).

**Code Example**:
```yaml
# Production SRE Specification for: What is Blue-Green Database Migration and how do you handle backward compatibility?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q61"></a>
### Q61: How do you manage Secrets Rotation with Zero Downtime for TLS Certificates?

**Difficulty**: Intermediate

**Strategy**:
Cert-manager loads new certificate into secret; web servers reload TLS context dynamically or execute seamless zero-downtime worker reload without dropping connections.

**Code Example**:
```yaml
# Production SRE Specification for: How do you manage Secrets Rotation with Zero Downtime for TLS Certificates?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q62"></a>
### Q62: What is the Two Generals Problem and why is consensus over unreliable networks unsolvable in bounded time?

**Difficulty**: Advanced

**Strategy**:
Fundamental theorem proving two nodes cannot reach absolute certainty over an unreliable communication link, motivating randomized consensus algorithms (Raft).

**Code Example**:
```yaml
# Production SRE Specification for: What is the Two Generals Problem and why is consensus over unreliable networks unsolvable in bounded time?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q63"></a>
### Q63: How do you implement Backpressure in Reactive Streams to prevent out-of-memory crashes?

**Difficulty**: Advanced

**Strategy**:
Subscribers signal demand to publishers via `request(n)`, ensuring publishers never send more events than consumer buffers can process.

**Code Example**:
```yaml
# Production SRE Specification for: How do you implement Backpressure in Reactive Streams to prevent out-of-memory crashes?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q64"></a>
### Q64: What is Sticky Sessions (Session Affinity) and why does it undermine horizontal scaling?

**Difficulty**: Intermediate

**Strategy**:
Pins client to single server; prevents even load distribution and causes session loss if that server crashes. Best replaced by distributed Redis session stores.

**Code Example**:
```yaml
# Production SRE Specification for: What is Sticky Sessions (Session Affinity) and why does it undermine horizontal scaling?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q65"></a>
### Q65: How do you configure Envoy Proxy as an edge ingress controller?

**Difficulty**: Advanced

**Strategy**:
Configure Envoy listener, route table matching prefixes, clusters with round-robin load balancing, and active HTTP health checks.

**Code Example**:
```yaml
# Production SRE Specification for: How do you configure Envoy Proxy as an edge ingress controller?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q66"></a>
### Q66: What is Shadow Traffic (Dark Launching) and how do you test new versions with production load?

**Difficulty**: Advanced

**Strategy**:
Proxy duplicates live customer requests asynchronously to a new shadow service; compares response outputs without returning shadow results to user.

**Code Example**:
```yaml
# Production SRE Specification for: What is Shadow Traffic (Dark Launching) and how do you test new versions with production load?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q67"></a>
### Q67: How do you detect Memory Leaks in Java applications using Garbage Collection logs and Heap Dumps?

**Difficulty**: Intermediate

**Strategy**:
Enable `-Xlog:gc*`, look for Old Gen memory that does not decrease after Full GC; analyze heap dump with Eclipse Memory Analyzer (MAT).

**Code Example**:
```yaml
# Production SRE Specification for: How do you detect Memory Leaks in Java applications using Garbage Collection logs and Heap Dumps?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q68"></a>
### Q68: What is Caching Tier Invalidation: TTL vs Event-Driven Invalidation?

**Difficulty**: Intermediate

**Strategy**:
TTL: eventual consistency based on time expiry; Event-driven: message broker publishes invalidation events immediately on data write (zero stale reads).

**Code Example**:
```yaml
# Production SRE Specification for: What is Caching Tier Invalidation: TTL vs Event-Driven Invalidation?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q69"></a>
### Q69: How do you configure Core Dumps in Linux for post-crash debugging?

**Difficulty**: Intermediate

**Strategy**:
Set `ulimit -c unlimited` and configure `/proc/sys/kernel/core_pattern` to save full memory core dumps for analysis with GDB.

**Code Example**:
```yaml
# Production SRE Specification for: How do you configure Core Dumps in Linux for post-crash debugging?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q70"></a>
### Q70: What is Service Mesh (Istio / Linkerd) and what are the trade-offs of sidecar proxies?

**Difficulty**: Advanced

**Strategy**:
Provides mTLS, traffic splitting, and telemetry transparently; trade-offs are added memory footprint per pod and ~2ms network latency overhead per hop.

**Code Example**:
```yaml
# Production SRE Specification for: What is Service Mesh (Istio / Linkerd) and what are the trade-offs of sidecar proxies?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q71"></a>
### Q71: How do you monitor and resolve Connection Pool Exhaustion in microservices?

**Difficulty**: Intermediate

**Strategy**:
Monitor active connections, pending acquisition threads, and wait times; increase pool size or optimize queries holding connections open too long.

**Code Example**:
```yaml
# Production SRE Specification for: How do you monitor and resolve Connection Pool Exhaustion in microservices?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q72"></a>
### Q72: What is the difference between Load Balancing Algorithms: Round Robin, Least Connections, IP Hash?

**Difficulty**: Beginner

**Strategy**:
Round Robin: sequential; Least Connections: sends to server with fewest active requests; IP Hash: maps client IP to server for affinity.

**Code Example**:
```yaml
# Production SRE Specification for: What is the difference between Load Balancing Algorithms: Round Robin, Least Connections, IP Hash?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q73"></a>
### Q73: How do you build an SLA Dashboard in Grafana showing uptime compliance?

**Difficulty**: Intermediate

**Strategy**:
Write PromQL calculating percentage of successful requests meeting response threshold over rolling 30-day window; display with Gauge and Table panels.

**Code Example**:
```yaml
# Production SRE Specification for: How do you build an SLA Dashboard in Grafana showing uptime compliance?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q74"></a>
### Q74: What is Chaos Engineering GameDay and how do you run it safely in staging?

**Difficulty**: Intermediate

**Strategy**:
Schedule team session, inject controlled failures, verify automated alerting fires, validate runbooks, and document remediation action items.

**Code Example**:
```yaml
# Production SRE Specification for: What is Chaos Engineering GameDay and how do you run it safely in staging?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q75"></a>
### Q75: How do you debug high CPU usage caused by spinlocks or busy-waiting threads?

**Difficulty**: Advanced

**Strategy**:
Profile CPU samples with `perf top` or async-profiler; identify functions consuming 100% core cycles without yielding or sleeping.

**Code Example**:
```yaml
# Production SRE Specification for: How do you debug high CPU usage caused by spinlocks or busy-waiting threads?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q76"></a>
### Q76: What is Dead Letter Queue (DLQ) in message brokers and how do you handle poisoned messages?

**Difficulty**: Intermediate

**Strategy**:
Messages that fail processing after max retry attempts are moved to DLQ; alerts on-call engineer to inspect payload and prevent pipeline stalling.

**Code Example**:
```yaml
# Production SRE Specification for: What is Dead Letter Queue (DLQ) in message brokers and how do you handle poisoned messages?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q77"></a>
### Q77: How do you configure Log Rotation using `logrotate` to prevent disk saturation?

**Difficulty**: Beginner

**Strategy**:
Define configuration in `/etc/logrotate.d/` specifying daily rotation, compression (`compress`), and maximum retention count (`rotate 7`).

**Code Example**:
```yaml
# Production SRE Specification for: How do you configure Log Rotation using `logrotate` to prevent disk saturation?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q78"></a>
### Q78: What is Rate Limiting using Leaky Bucket vs Token Bucket algorithms?

**Difficulty**: Intermediate

**Strategy**:
Token bucket allows temporary bursts up to capacity; Leaky bucket enforces a strictly steady, constant outflow rate regardless of burstiness.

**Code Example**:
```yaml
# Production SRE Specification for: What is Rate Limiting using Leaky Bucket vs Token Bucket algorithms?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q79"></a>
### Q79: How do you handle High Availability for Redis with Redis Sentinel vs Redis Cluster?

**Difficulty**: Advanced

**Strategy**:
Sentinel provides automated master failover for single-shard setups; Cluster provides multi-master sharding across up to 1,000 nodes with data partitioning.

**Code Example**:
```yaml
# Production SRE Specification for: How do you handle High Availability for Redis with Redis Sentinel vs Redis Cluster?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q80"></a>
### Q80: What is Edge Caching and how does Cloudflare / CloudFront accelerate static and dynamic content?

**Difficulty**: Beginner

**Strategy**:
Caches assets at hundreds of Points of Presence (PoPs) worldwide close to users, reducing round-trip latency and origin server load.

**Code Example**:
```yaml
# Production SRE Specification for: What is Edge Caching and how does Cloudflare / CloudFront accelerate static and dynamic content?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q81"></a>
### Q81: How do you perform Disaster Recovery Testing without impacting production users?

**Difficulty**: Advanced

**Strategy**:
Clone production environment to isolated DR VPC, replay sanitized production traffic, simulate failover, and measure RTO/RPO metrics.

**Code Example**:
```yaml
# Production SRE Specification for: How do you perform Disaster Recovery Testing without impacting production users?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q82"></a>
### Q82: What is the difference between Active-Active and Active-Passive Failover?

**Difficulty**: Beginner

**Strategy**:
Active-Active: all nodes serve traffic simultaneously; Active-Passive: standby node stays idle and only takes over when primary fails.

**Code Example**:
```yaml
# Production SRE Specification for: What is the difference between Active-Active and Active-Passive Failover?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q83"></a>
### Q83: How do you detect Slow Memory Leaks using Prometheus `rate()` on process resident memory?

**Difficulty**: Intermediate

**Strategy**:
Alert if `deriv(process_resident_memory_bytes[24h]) > 0` consistently over 7 days without stabilizing after garbage collection cycles.

**Code Example**:
```yaml
# Production SRE Specification for: How do you detect Slow Memory Leaks using Prometheus `rate()` on process resident memory?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q84"></a>
### Q84: What is Out-of-Band Management (IPMI, iLO) and how does it rescue unresponsive bare-metal servers?

**Difficulty**: Intermediate

**Strategy**:
Dedicated hardware controller with separate network interface allowing power cycling and console access even if OS is frozen.

**Code Example**:
```yaml
# Production SRE Specification for: What is Out-of-Band Management (IPMI, iLO) and how does it rescue unresponsive bare-metal servers?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q85"></a>
### Q85: How do you secure Production Systems during an ongoing Zero-Day Vulnerability Incident?

**Difficulty**: Advanced

**Strategy**:
Isolate vulnerable components behind WAF virtual patches, disable affected feature flags, apply emergency vendor mitigations, and schedule off-hours deployment.

**Code Example**:
```yaml
# Production SRE Specification for: How do you secure Production Systems during an ongoing Zero-Day Vulnerability Incident?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q86"></a>
### Q86: What is the role of Site Reliability Engineering in Architecture Review Boards (ARB)?

**Difficulty**: Intermediate

**Strategy**:
Ensure proposed architectures define SLOs upfront, include graceful degradation modes, avoid single points of failure, and plan capacity scaling.

**Code Example**:
```yaml
# Production SRE Specification for: What is the role of Site Reliability Engineering in Architecture Review Boards (ARB)?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q87"></a>
### Q87: How do you build automated rollback mechanisms in Continuous Deployment pipelines?

**Difficulty**: Intermediate

**Strategy**:
Monitor canary error rates post-deploy; if metric exceeds threshold within 10 minutes, trigger automated rollback to previous revision.

**Code Example**:
```yaml
# Production SRE Specification for: How do you build automated rollback mechanisms in Continuous Deployment pipelines?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q88"></a>
### Q88: What is the difference between Hard Links and Soft Links (Symlinks) in Linux filesystems?

**Difficulty**: Beginner

**Strategy**:
Hard link points directly to the inode (shares data, same filesystem); Symlink points to the file path name (can span filesystems).

**Code Example**:
```yaml
# Production SRE Specification for: What is the difference between Hard Links and Soft Links (Symlinks) in Linux filesystems?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q89"></a>
### Q89: How do you trace Kernel I/O bottlenecks with `iostat` and `iotop`?

**Difficulty**: Intermediate

**Strategy**:
`iostat -xz 1` displays `%util`, `await`, and throughput per disk; `iotop -o` shows exact processes causing heavy disk reads/writes.

**Code Example**:
```yaml
# Production SRE Specification for: How do you trace Kernel I/O bottlenecks with `iostat` and `iotop`?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q90"></a>
### Q90: What is the Single Responsibility Principle applied to Microservices Architecture?

**Difficulty**: Intermediate

**Strategy**:
Each microservice owns a single distinct business domain and its private database; prevents coupling and enables independent deployment.

**Code Example**:
```yaml
# Production SRE Specification for: What is the Single Responsibility Principle applied to Microservices Architecture?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q91"></a>
### Q91: How do you handle Database Connection Leaks in Node.js or Python backend services?

**Difficulty**: Intermediate

**Strategy**:
Always release connection back to pool in `finally` blocks; configure pool leak detection timeouts that log stack traces of unclosed connections.

**Code Example**:
```yaml
# Production SRE Specification for: How do you handle Database Connection Leaks in Node.js or Python backend services?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q92"></a>
### Q92: What is the difference between Horizontal Pod Autoscaling (HPA) and Vertical Pod Autoscaling (VPA)?

**Difficulty**: Intermediate

**Strategy**:
HPA increases number of pod replicas; VPA increases CPU and memory limits/requests of existing pods (requires restart).

**Code Example**:
```yaml
# Production SRE Specification for: What is the difference between Horizontal Pod Autoscaling (HPA) and Vertical Pod Autoscaling (VPA)?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q93"></a>
### Q93: How do you tune TCP Keepalive settings to detect dead peers across cloud firewalls?

**Difficulty**: Intermediate

**Strategy**:
Set `tcp_keepalive_time = 300`, `tcp_keepalive_intvl = 15`, `tcp_keepalive_probes = 5` to terminate stale half-open connections in minutes.

**Code Example**:
```yaml
# Production SRE Specification for: How do you tune TCP Keepalive settings to detect dead peers across cloud firewalls?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q94"></a>
### Q94: What is Incident Retrospective Follow-Through and how do you ensure P0 action items get completed?

**Difficulty**: Intermediate

**Strategy**:
Track action items as high-priority Jira tickets with assigned owners; review progress in weekly engineering leadership standups.

**Code Example**:
```yaml
# Production SRE Specification for: What is Incident Retrospective Follow-Through and how do you ensure P0 action items get completed?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q95"></a>
### Q95: How do you manage DNS Propagation Delays when changing authoritative nameservers?

**Difficulty**: Intermediate

**Strategy**:
Lower TTLs on old nameserver weeks in advance; keep old nameserver active serving updated records until all public resolvers refresh.

**Code Example**:
```yaml
# Production SRE Specification for: How do you manage DNS Propagation Delays when changing authoritative nameservers?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q96"></a>
### Q96: How do you configure CoreDNS in Kubernetes to prevent DNS resolution throttling?

**Difficulty**: Intermediate

**Strategy**:
Increase CoreDNS replicas, enable node-local DNS cache (NodeLocal DNSCache) to avoid connection tracking conntrack table exhaustion.

**Code Example**:
```yaml
# Production SRE Specification for: How do you configure CoreDNS in Kubernetes to prevent DNS resolution throttling?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q97"></a>
### Q97: What is the difference between Ingress Controller and Service of type LoadBalancer in Kubernetes?

**Difficulty**: Beginner

**Strategy**:
LoadBalancer provisions an external cloud L4 load balancer per service; Ingress is a single L7 reverse proxy (Nginx/Envoy) routing traffic across multiple services via host/path rules.

**Code Example**:
```yaml
# Production SRE Specification for: What is the difference between Ingress Controller and Service of type LoadBalancer in Kubernetes?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q98"></a>
### Q98: How do you design a graceful connection draining policy during rolling updates?

**Difficulty**: Intermediate

**Strategy**:
Set `terminationGracePeriodSeconds: 60`, implement a preStop hook with `sleep 15` allowing endpoint controllers to remove pod from kube-proxy routing before sending SIGTERM.

**Code Example**:
```yaml
# Production SRE Specification for: How do you design a graceful connection draining policy during rolling updates?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q99"></a>
### Q99: What is Write-Ahead Logging (WAL) in distributed storage and how does it guarantee durability?

**Difficulty**: Advanced

**Strategy**:
All state changes are appended sequentially to non-volatile disk log before being applied in-memory; allows exact state replay after sudden crash.

**Code Example**:
```yaml
# Production SRE Specification for: What is Write-Ahead Logging (WAL) in distributed storage and how does it guarantee durability?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---

<a id="q100"></a>
### Q100: How do you automate Capacity Planning using historical growth metrics and linear extrapolation?

**Difficulty**: Intermediate

**Strategy**:
Analyze 90-day storage and CPU trends; calculate growth slope; alert 6 months before reaching 80% physical cluster capacity.

**Code Example**:
```yaml
# Production SRE Specification for: How do you automate Capacity Planning using historical growth metrics and linear extrapolation?
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sre-reliability-standard
```

---
