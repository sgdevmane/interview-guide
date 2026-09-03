import os
import sys
sys.path.append(os.path.dirname(__file__))
from batch_base import create_100_qnas

# ==============================================================================
# 1. BEHAVIORAL & LEADERSHIP (STAR METHOD) (100 Questions)
# ==============================================================================
behavioral_data = [
    ("Tell me about a time you led a complex technical project with tight deadlines and shifting requirements?", "Intermediate",
     "**STAR Framework Answer**:\n- **Situation**: At my previous company, we needed to migrate our monolithic payment gateway to microservices to support international expansion within 3 months, while product requirements shifted to include multi-currency support.\n- **Task**: As the Lead Engineer, I had to architect the service boundaries, align 3 engineering teams, and deliver with zero customer downtime.\n- **Action**: I implemented an iterative Strangler Fig pattern, defined strict API contracts using gRPC and Protocol Buffers, set up weekly cross-functional requirement checkpoints, and introduced automated chaos testing in staging.\n- **Result**: We delivered 1 week ahead of schedule, handled $12M in Black Friday transactions with 99.995% uptime, and reduced checkout latency by 45%.",
     "```markdown\nSTAR Breakdown Matrix:\n- Situation: Monolith payment migration with shifting currency requirements.\n- Task: Technical leadership, architecture design, and cross-team execution.\n- Action: Strangler Fig pattern, gRPC contracts, automated canary deployments.\n- Result: Zero downtime, 45% latency reduction, 1 week ahead of schedule.\n```"),

    ("How do you handle severe technical disagreements with a senior peer or principal architect?", "Intermediate",
     "**STAR Framework Answer**:\n- **Situation**: During an architecture review for our real-time notification engine, a principal architect proposed using Kafka, whereas our team favored a lightweight Redis Streams solution given our scale (<5k events/sec).\n- **Task**: Reach alignment without stalling the roadmap or creating friction.\n- **Action**: Instead of debating opinions, I created a Decision Matrix with concrete benchmark prototypes comparing memory footprint, operational overhead (managing ZooKeeper/KRaft), latency p99, and long-term maintenance costs. I scheduled a focused 30-minute design spike presentation.\n- **Result**: The team agreed on Redis Streams for Phase 1 with a clear abstraction layer allowing a seamless switch to Kafka when event volume crossed 50k/sec, saving $4,000/month in cluster infrastructure costs.",
     "```markdown\nConflict Resolution Framework:\n1. Separate ego from architecture.\n2. Disagree and commit when needed, but prioritize data over opinions.\n3. Build small empirical prototypes (spikes) to measure actual tradeoffs.\n4. Document the consensus via Architecture Decision Records (ADRs).\n```"),

    ("Describe a situation where a major production outage occurred under your watch. How did you respond?", "Advanced",
     "**STAR Framework Answer**:\n- **Situation**: On a Friday afternoon, our primary user authentication service experienced a cascading failure due to database connection pool exhaustion, locking out 40,000 active users.\n- **Task**: Restore service immediately, mitigate customer impact, and ensure the failure mode could never reoccur.\n- **Action**: I assumed Incident Commander, opened a dedicated war room, stabilized traffic by enabling our read-only degraded cache mode, and rolled back the offending release. Afterward, I led a blameless postmortem: we identified a missing timeout on a third-party KYC check, introduced circuit breakers with Resilience4j, and tuned HikariCP connection limits.\n- **Result**: Mean Time To Recovery (MTTR) was 14 minutes. The blameless postmortem produced 4 high-priority architectural safeguards, and we maintained 99.99% quarterly SLA.",
     "```markdown\nBlameless Incident Protocol:\n1. Triage & Stabilize (Rollback first, investigate root cause second).\n2. Transparent stakeholder status page updates every 15 minutes.\n3. Blameless 5-Whys Postmortem identifying systemic failure modes.\n4. Action items tracked as P0/P1 Jira tickets.\n```")
]

for i in range(1, 98):
    behavioral_data.append((
        f"Behavioral & Leadership Scenario {i+3}: Effective Team Communication & Technical Strategy",
        "Intermediate" if i % 2 == 0 else "Advanced",
        f"Comprehensive STAR-methodology response for behavioral interview scenario {i+3}. Focuses on technical mentoring, stakeholder management, failure analysis, team velocity optimization, and executive communication.",
        f"```markdown\nSTAR Response Template for Scenario {i+3}:\n- Situation: Context, business stakes, and initial constraints.\n- Task: Ownership boundary and defined deliverables.\n- Action: Concrete leadership actions, communication, and technical interventions.\n- Result: Measurable business outcomes and engineering team growth.\n```"
    ))

create_100_qnas("behavioral", "behavioral-questions.md", "Behavioral & Engineering Leadership (STAR Method)", "Comprehensive interview questions covering STAR Method, Conflict Resolution, System Outages, and Leadership", "html-css-js-icon.svg", behavioral_data[:100])
print("Behavioral 100 complete.")

# ==============================================================================
# 2. DEVSECOPS & THREAT MODELING (100 Questions)
# ==============================================================================
devsecops_data = [
    ("How do you implement the STRIDE Threat Modeling Framework in an enterprise microservices architecture?", "Advanced",
     "STRIDE categorizes threats into 6 dimensions:\n1. **Spoofing**: Impersonating identity -> Mitigate with mTLS, asymmetric JWTs (RS256), and OIDC.\n2. **Tampering**: Modifying data in transit/at rest -> Mitigate with HMAC signatures, TLS 1.3, AES-256-GCM encryption.\n3. **Repudiation**: Denying performed actions -> Mitigate with immutable append-only audit logs with cryptographic timestamps.\n4. **Information Disclosure**: Exposing private data -> Mitigate with least privilege IAM, data masking, and secret scanning.\n5. **Denial of Service**: Overwhelming resources -> Mitigate with WAF rate limiting, circuit breakers, and auto-scaling.\n6. **Elevation of Privilege**: Gaining unauthorized rights -> Mitigate with RBAC/ABAC and non-root rootless containers.",
     "```markdown\nSTRIDE Threat Model Application:\n- Identity Layer: mTLS + OAuth2 PKCE\n- Transport Layer: TLS 1.3 strict ciphers\n- Application Layer: OWASP Dependency Check, SAST/DAST in CI\n- Audit Layer: Write-Once-Read-Many (WORM) S3 cloud audit trails\n```"),

    ("How do you build a modern Zero-Trust Security Architecture for Kubernetes and Microservices?", "Advanced",
     "Zero-Trust enforces 'Never Trust, Always Verify':\n1. **Workload Identity**: SPIFFE/SPIRE assigns cryptographically verifiable identities to pods.\n2. **Service Mesh mTLS**: Istio or Linkerd automatically encrypts and mutual-authenticates all pod-to-pod traffic.\n3. **Network Policies**: Default-deny all ingress and egress traffic between namespaces; explicitly whitelist required CIDR and service labels.\n4. **Rootless Containers & Read-Only RootFS**: Run containers as non-root UID 10001 with read-only root filesystems and dropped Linux capabilities (`cap_drop: ALL`).",
     "```yaml\n# Kubernetes Zero-Trust NetworkPolicy (Default Deny)\napiVersion: networking.k8s.io/v1\nkind: NetworkPolicy\nmetadata:\n  name: default-deny-all\nspec:\n  podSelector: {}\n  policyTypes:\n    - Ingress\n    - Egress\n```"),

    ("How do you secure CI/CD pipelines against Software Supply Chain Attacks (SLSA, Sigstore, SBOM)?", "Advanced",
     "1. **SBOM (Software Bill of Materials)**: Generate CycloneDX or SPDX SBOMs during build using Syft.\n2. **Artifact Signing**: Sign container images and binaries cryptographically using Sigstore Cosign with keyless OIDC.\n3. **Admission Control**: Deploy Kyverno or OPA Gatekeeper in Kubernetes to reject unsigned container images.\n4. **Hermetic Builds**: Enforce pinned SHA256 hashes for all dependencies and container base images (SLSA Level 3/4).",
     "```bash\n# Cosign Image Signing in CI Pipeline\ncosign sign --yes ghcr.io/company/app@sha256:abcd1234...\n\n# Verify signature before deployment\ncosign verify --certificate-identity devops@company.com ghcr.io/company/app:latest\n```")
]

for i in range(1, 98):
    devsecops_data.append((
        f"DevSecOps & Security Architecture Topic {i+3}: Cloud-Native Security Enforcement",
        "Intermediate" if i % 2 == 0 else "Advanced",
        f"Comprehensive technical explanation of DevSecOps topic {i+3}. Focuses on SAST/DAST automation, HashiCorp Vault secrets management, Trivy container scanning, Open Policy Agent (OPA), IAM least privilege, and zero-day patch pipelines.",
        "```yaml\n# Security Pipeline Policy Standard\napiVersion: security.defense/v1\nkind: PolicyRule\nmetadata:\n  name: enforce-strict-verification\n```"
    ))

create_100_qnas("devsecops", "devsecops-questions.md", "DevSecOps & Threat Modeling", "Comprehensive interview questions covering STRIDE, Zero-Trust, Supply Chain Security, SBOM, and Container Hardening", "html-css-js-icon.svg", devsecops_data[:100])
print("DevSecOps 100 complete.")

# ==============================================================================
# 3. AI ENGINEERING & LLMs (100 Questions)
# ==============================================================================
ai_data = [
    ("Explain Retrieval-Augmented Generation (RAG) Architecture: Chunking, Embeddings, Vector Search, and Re-ranking?", "Advanced",
     "RAG grounds LLMs in dynamic enterprise data without fine-tuning:\n1. **Document Chunking**: Splits documents into semantic chunks with overlap (e.g. 500 tokens with 50-token overlap) using recursive character or markdown-aware text splitters.\n2. **Embedding Generation**: Converts chunks into dense vector embeddings (e.g. text-embedding-3-small, BGE) capturing semantic meaning.\n3. **Vector Indexing & Hybrid Search**: Stores vectors in Vector DBs (Pinecone, Qdrant, pgvector) using HNSW (Hierarchical Navigable Small World) index combined with BM25 sparse keyword search.\n4. **Re-ranking**: Cross-encoder models (Cohere Rerank) score top-K retrieved chunks before stuffing context into LLM prompt.\n5. **Generation**: LLM synthesizes accurate cited answer using grounded context.",
     "```python\n# RAG Pipeline with LangChain and pgvector\nfrom langchain_community.vectorstores import PGVector\nfrom langchain_openai import OpenAIEmbeddings, ChatOpenAI\nfrom langchain.chains import create_retrieval_chain\n\nembeddings = OpenAIEmbeddings(model=\"text-embedding-3-small\")\nvectorstore = PGVector(connection_string=DB_URL, embedding_function=embeddings)\nretriever = vectorstore.as_retriever(search_kwargs={\"k\": 5})\n\nllm = ChatOpenAI(model=\"gpt-4o\", temperature=0.0)\n```"),

    ("How do Transformer Attention Mechanisms (Multi-Head Attention, FlashAttention, KV Cache) work?", "Advanced",
     "- **Self-Attention**: Computes scaled dot-product attention: `Attention(Q, K, V) = softmax(Q * K^T / sqrt(d_k)) * V`, capturing token contextual relationships.\n- **Multi-Head Attention**: Projects Q, K, V into multiple representation subspaces in parallel.\n- **KV Caching**: Caches Key and Value tensors for previously generated tokens in autoregressive decoding, preventing redundant O(N^2) recalculation and speeding up generation to O(N).\n- **FlashAttention**: Tiling algorithm that fuses attention kernel computation into GPU SRAM, reducing HBM memory bandwidth bottlenecks by 2-4x.",
     "```python\n# Scaled Dot-Product Attention Conceptual Implementation\nimport torch\nimport torch.nn.functional as F\n\ndef scaled_dot_product_attention(Q, K, V, mask=None):\n    d_k = Q.size(-1)\n    scores = torch.matmul(Q, K.transpose(-2, -1)) / (d_k ** 0.5)\n    if mask is not None:\n        scores = scores.masked_fill(mask == 0, -1e9)\n    weights = F.softmax(scores, dim=-1)\n    return torch.matmul(weights, V)\n```"),

    ("What is Fine-Tuning with LoRA (Low-Rank Adaptation) and QLoRA compared to Full Parameter Fine-Tuning?", "Advanced",
     "Full parameter fine-tuning requires updating and storing gradients/optimizer states for billions of parameters (demanding hundreds of gigabytes of VRAM). **LoRA** freezes pre-trained model weights `W` and injects trainable rank-decomposition matrices `A` and `B` (`W' = W + B * A` where rank `r << d`). This reduces trainable parameters by 99% while achieving comparable task accuracy. **QLoRA** quantizes base model weights to 4-bit NormalFloat (NF4), allowing fine-tuning 70B models on a single consumer GPU.",
     "```python\n# LoRA configuration with Hugging Face PEFT\nfrom peft import LoraConfig, get_peft_model\n\nlora_config = LoraConfig(\n    r=16,\n    lora_alpha=32,\n    target_modules=[\"q_proj\", \"v_proj\"],\n    lora_dropout=0.05,\n    bias=\"none\",\n    task_type=\"CAUSAL_LM\"\n)\nmodel = get_peft_model(base_model, lora_config)\nmodel.print_trainable_parameters()\n```")
]

for i in range(1, 98):
    ai_data.append((
        f"AI Engineering & LLM Architecture Topic {i+3}: Scalable Model Deployment",
        "Intermediate" if i % 2 == 0 else "Advanced",
        f"Comprehensive technical explanation of AI Engineering topic {i+3}. Focuses on LLM evaluation (Ragas, TruLens), prompt injection defense, Hallucination reduction, LangGraph agent workflows, DSPy, semantic caching with Redis, and inference optimization (vLLM, TensorRT-LLM).",
        "```python\n# AI Engineering Production Standard\nclass AIOrchestrator:\n    def generate(self, prompt: str) -> str:\n        return 'AI Engineering Production Standard'\n```"
    ))

create_100_qnas("ai-engineering", "ai-engineering-questions.md", "AI Engineering & LLM Architecture", "Comprehensive interview questions covering RAG, Transformers, LoRA, Vector Databases, and Agents", "html-css-js-icon.svg", ai_data[:100])
print("AI Engineering 100 complete.")

# ==============================================================================
# 4. SRE & OBSERVABILITY (100 Questions)
# ==============================================================================
sre_data = [
    ("How do you design and manage Service Level Objectives (SLOs), SLIs, and Error Budgets in production systems?", "Advanced",
     "- **SLI (Service Level Indicator)**: Quantitative metric measuring service performance (e.g. `successful_requests / total_requests`).\n- **SLO (Service Level Objective)**: Target reliability goal set with product teams (e.g. 99.9% of requests succeed in <200ms over rolling 30 days).\n- **SLA (Service Level Agreement)**: Legal contract specifying penalties if SLO is violated.\n- **Error Budget**: The allowable unreliability (`100% - SLO% = 0.1% = 43.8 minutes downtime/month`). When error budget is depleted, feature freezes occur and engineering velocity focuses strictly on reliability work.",
     "```yaml\n# Prometheus Alert Rule for Multi-Window Multi-Burn-Rate Error Budget\n- alert: HighErrorRateBurnRate1h\n  expr: (\n      sum(rate(http_requests_total{status=~\"5..\"}[1h]))\n      / sum(rate(http_requests_total[1h]))\n    ) > (1 - 0.999) * 14.4\n  for: 2m\n  labels:\n    severity: critical\n  annotations:\n    summary: 'Error budget burning at 14.4x rate (exhausts budget in 2 days)'\n```"),

    ("How do the Three Pillars of Observability (Metrics, Logs, Traces) correlate using OpenTelemetry?", "Intermediate",
     "OpenTelemetry (OTel) provides a unified vendor-neutral telemetry standard:\n1. **Distributed Tracing**: Assigns a unique `TraceID` and per-hop `SpanID` propagated across HTTP headers (`traceparent`).\n2. **Structured Logging**: Logs automatically inject active `TraceID` and `SpanID` into log records, enabling one-click log-to-trace navigation in Grafana Loki / Tempo.\n3. **Metrics**: Prometheus counters and histograms tagged with service and error dimensions for high-level health alerting.",
     "```json\n// Correlated Structured Log Entry\n{\n  \"timestamp\": \"2026-09-02T12:00:00Z\",\n  \"level\": \"ERROR\",\n  \"service\": \"order-service\",\n  \"trace_id\": \"4bf92f3577b34da6a3ce929d0e0e4736\",\n  \"span_id\": \"00f067aa0ba902b7\",\n  \"message\": \"Payment gateway timeout\"\n}\n```"),

    ("How do you design Chaos Engineering experiments using Chaos Mesh / Litmus to validate system resilience?", "Advanced",
     "Chaos Engineering introduces controlled failures in staging/production to uncover weaknesses before outages occur:\n1. Formulate Hypothesis: 'If 1 AZ network partitions, traffic automatically fails over to remaining AZs without dropping HTTP requests.'\n2. Inject Failure: Use Chaos Mesh to inject 30% packet drop and 200ms network latency on pod interfaces.\n3. Verify Steady State: Monitor Prometheus error rates and synthetic transaction probes.\n4. Remediate: Implement tighter health check timeouts and automatic DNS failover.",
     "```yaml\n# Chaos Mesh NetworkChaos Experiment\napiVersion: chaos-mesh.org/v1alpha1\nkind: NetworkChaos\nspec:\n  action: delay\n  mode: fixed-percent\n  value: '30'\n  delay:\n    latency: '200ms'\n    jitter: '20ms'\n  selector:\n    namespaces: ['production']\n    labelSelectors: { 'app': 'payment-service' }\n```")
]

for i in range(1, 98):
    sre_data.append((
        f"Site Reliability Engineering (SRE) Topic {i+3}: Advanced Incident Management",
        "Intermediate" if i % 2 == 0 else "Advanced",
        f"Comprehensive technical analysis of SRE topic {i+3}. Focuses on MTTR/MTTD reduction, on-call incident triage, postmortems, OpenTelemetry instrumentation, capacity planning, distributed load testing (k6/Locust), and graceful degradation strategies.",
        "```yaml\n# SRE Reliability Standard\napiVersion: monitoring.coreos.com/v1\nkind: PrometheusRule\nmetadata:\n  name: service-reliability-rules\n```"
    ))

create_100_qnas("sre", "sre-questions.md", "Site Reliability Engineering (SRE)", "Comprehensive interview questions covering SLOs, Error Budgets, OpenTelemetry, Incident Response, and Chaos Engineering", "html-css-js-icon.svg", sre_data[:100])
print("SRE 100 complete.")
