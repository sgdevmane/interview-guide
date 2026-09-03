<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="DevSecOps & Threat Modeling Logo" width="100" height="100">
  </a>
  <h1>DevSecOps & Threat Modeling Interview Questions & Answers</h1>
  <p><b>Comprehensive interview questions covering STRIDE, Zero-Trust, Supply Chain Security, SBOM, and Container Hardening</b></p>
</div>

---

## Table of Contents

1. [How do you implement the STRIDE Threat Modeling Framework in an enterprise microservices architecture?](#q1) <span class="advanced">Advanced</span>
2. [How do you design a Zero-Trust Security Architecture for Kubernetes and container workloads?](#q2) <span class="advanced">Advanced</span>
3. [How do you secure CI/CD pipelines against Software Supply Chain Attacks (SLSA Level 3/4)?](#q3) <span class="advanced">Advanced</span>
4. [What is the difference between SAST, DAST, IAST, and RASP in the DevSecOps lifecycle?](#q4) <span class="intermediate">Intermediate</span>
5. [How do you implement dynamic secrets management and automated rotation using HashiCorp Vault?](#q5) <span class="advanced">Advanced</span>
6. [How do you enforce Admission Control in Kubernetes using Open Policy Agent (OPA) Gatekeeper or Kyverno?](#q6) <span class="advanced">Advanced</span>
7. [What is Container Escape and how do you harden container runtimes to prevent privilege escalation?](#q7) <span class="advanced">Advanced</span>
8. [How do you perform Runtime Threat Detection in Kubernetes using eBPF and Falco?](#q8) <span class="advanced">Advanced</span>
9. [How do you implement Mutual TLS (mTLS) with SPIFFE/SPIRE for cryptographic workload identity?](#q9) <span class="advanced">Advanced</span>
10. [How do you design a secure Automated Secret Scanning pipeline to prevent credential leaks in Git?](#q10) <span class="intermediate">Intermediate</span>
11. [How do you remediate vulnerabilities found by Container Vulnerability Scanners (Trivy, Grype)?](#q11) <span class="intermediate">Intermediate</span>
12. [What is DREAD Risk Assessment and how is it calculated for security vulnerabilities?](#q12) <span class="intermediate">Intermediate</span>
13. [How do you implement Immutable Infrastructure to enhance cloud security posture?](#q13) <span class="intermediate">Intermediate</span>
14. [What are Kubernetes NetworkPolicies and how do they enforce microsegmentation?](#q14) <span class="intermediate">Intermediate</span>
15. [How do you secure API Gateways against OWASP API Top 10 vulnerabilities (BOLA, Broken Authentication)?](#q15) <span class="advanced">Advanced</span>
16. [What is the difference between RBAC and ABAC in enterprise authorization architectures?](#q16) <span class="intermediate">Intermediate</span>
17. [How do you prevent Cross-Site Scripting (XSS) using Content Security Policy (CSP) headers?](#q17) <span class="intermediate">Intermediate</span>
18. [How do you secure Cloud Object Storage (AWS S3) against unauthorized public access?](#q18) <span class="beginner">Beginner</span>
19. [What is Cloud Security Posture Management (CSPM) and how does it detect misconfigurations?](#q19) <span class="intermediate">Intermediate</span>
20. [How do you configure KMS Envelope Encryption to protect data at rest?](#q20) <span class="advanced">Advanced</span>
21. [How do you implement Threat Intelligence Feeds into enterprise SIEM platforms?](#q21) <span class="intermediate">Intermediate</span>
22. [What is AppArmor and how do AppArmor profiles restrict container capabilities on Linux hosts?](#q22) <span class="advanced">Advanced</span>
23. [How do you detect and mitigate Server-Side Request Forgery (SSRF) in cloud environments?](#q23) <span class="advanced">Advanced</span>
24. [What is AWS IAM Permission Boundary and how does it delegate safe admin rights?](#q24) <span class="advanced">Advanced</span>
25. [How do you conduct automated Dependency License Compliance checks in CI pipelines?](#q25) <span class="beginner">Beginner</span>
26. [How do you secure Webhook integrations against replay attacks and spoofing?](#q26) <span class="intermediate">Intermediate</span>
27. [What is Endpoint Detection and Response (EDR) and how does it monitor developer workstations?](#q27) <span class="intermediate">Intermediate</span>
28. [How do you configure Keycloak or Auth0 for enterprise Single Sign-On (SSO) with SAML 2.0 and OIDC?](#q28) <span class="intermediate">Intermediate</span>
29. [How do you prevent SQL Injection vulnerabilities in modern ORMs and raw queries?](#q29) <span class="beginner">Beginner</span>
30. [What is Chaos Security Engineering and how do you simulate automated adversary attacks?](#q30) <span class="advanced">Advanced</span>
31. [How do you securely manage environment variables in Docker and Kubernetes without leaks?](#q31) <span class="intermediate">Intermediate</span>
32. [What is the Principle of Least Privilege (PoLP) and how do you apply it to cloud IAM roles?](#q32) <span class="beginner">Beginner</span>
33. [How do you protect GraphQL APIs against DoS attacks (Query Depth Limiting, Complexity Analysis)?](#q33) <span class="advanced">Advanced</span>
34. [What is CIS Kubernetes Benchmark and how do you audit clusters using kube-bench?](#q34) <span class="intermediate">Intermediate</span>
35. [How do you implement Secure Software Development Lifecycle (SSDLC) in Agile teams?](#q35) <span class="intermediate">Intermediate</span>
36. [What is Forward Secrecy (PFS) in TLS 1.3 and why does it protect past traffic from decryption?](#q36) <span class="advanced">Advanced</span>
37. [How do you detect Hardcoded Secrets in Git history and permanently purge them using git-filter-repo?](#q37) <span class="intermediate">Intermediate</span>
38. [What is Security Information and Event Management (SIEM) and how are logs ingested?](#q38) <span class="intermediate">Intermediate</span>
39. [How do you prevent Cross-Site Request Forgery (CSRF) in modern Single Page Applications (SPAs)?](#q39) <span class="beginner">Beginner</span>
40. [How do you configure AWS GuardDuty and Security Hub for automated incident response?](#q40) <span class="intermediate">Intermediate</span>
41. [What is Web Application Firewall (WAF) and how do Managed Rule Sets (CRS) block OWASP threats?](#q41) <span class="intermediate">Intermediate</span>
42. [How do you configure rootless container execution with Podman or Docker Rootless Mode?](#q42) <span class="advanced">Advanced</span>
43. [What is the difference between Symmetric (AES) and Asymmetric (RSA, ECC) Encryption?](#q43) <span class="beginner">Beginner</span>
44. [How do you design a secure Password Storage scheme using Argon2id or bcrypt with Salting?](#q44) <span class="intermediate">Intermediate</span>
45. [How do you implement gRPC Mutual Authentication (mTLS) with custom certificate verification?](#q45) <span class="advanced">Advanced</span>
46. [What is Binary Authorization in Google Cloud or Sigstore Policy Controller in Kubernetes?](#q46) <span class="advanced">Advanced</span>
47. [How do you mitigate DDoS attacks using Anycast DNS, CDN edge caching, and SYN cookies?](#q47) <span class="advanced">Advanced</span>
48. [What is eBPF Tetragon and how does it enforce real-time kernel security observability and blocking?](#q48) <span class="advanced">Advanced</span>
49. [How do you audit and harden SSH access across enterprise server fleets using Teleport or Bastion hosts?](#q49) <span class="intermediate">Intermediate</span>
50. [What are Side-Channel Attacks and how do constant-time cryptographic implementations mitigate them?](#q50) <span class="advanced">Advanced</span>
51. [How do you implement secure Data Masking and Tokenization for sensitive PII and credit cards?](#q51) <span class="intermediate">Intermediate</span>
52. [What is an IDOR (Insecure Direct Object Reference) vulnerability and how do you prevent it?](#q52) <span class="beginner">Beginner</span>
53. [How do you design a secure Multi-Tenant Database Architecture with Row-Level Security (RLS)?](#q53) <span class="advanced">Advanced</span>
54. [What is Threat Hunting and how do security analysts search for advanced persistent threats (APTs)?](#q54) <span class="intermediate">Intermediate</span>
55. [How do you secure serverless functions (AWS Lambda, Cloudflare Workers) against event injection?](#q55) <span class="intermediate">Intermediate</span>
56. [What is Security Chaos Engineering and how do you test fault tolerance under security stress?](#q56) <span class="advanced">Advanced</span>
57. [How do you perform Threat Modeling using the PASTA (Process for Attack Simulation and Threat Analysis) framework?](#q57) <span class="advanced">Advanced</span>
58. [What is Clickjacking and how does the `X-Frame-Options` and CSP `frame-ancestors` directive prevent it?](#q58) <span class="beginner">Beginner</span>
59. [How do you automate TLS Certificate Provisioning and Renewal with cert-manager and Let's Encrypt?](#q59) <span class="intermediate">Intermediate</span>
60. [What are Supply Chain Attacks targeting NPM and PyPI ecosystems and how do lockfiles mitigate them?](#q60) <span class="intermediate">Intermediate</span>
61. [How do you configure AWS VPC Flow Logs and analyze them with Athena for anomalous egress traffic?](#q61) <span class="intermediate">Intermediate</span>
62. [What is Open Policy Agent (OPA) and how do you write Rego policies for infrastructure compliance?](#q62) <span class="advanced">Advanced</span>
63. [How do you implement Risk-Based Adaptive Authentication with IP reputation and device fingerprinting?](#q63) <span class="advanced">Advanced</span>
64. [What is Directory Traversal (Path Traversal) and how do you prevent `../` attacks in file uploads?](#q64) <span class="beginner">Beginner</span>
65. [How do you secure Kafka clusters with SASL/SCRAM and TLS encryption?](#q65) <span class="advanced">Advanced</span>
66. [What is the difference between Stateful and Stateless Firewalls?](#q66) <span class="beginner">Beginner</span>
67. [How do you configure Security Headers (`HSTS`, `X-Content-Type-Options`, `Referrer-Policy`) on Nginx?](#q67) <span class="intermediate">Intermediate</span>
68. [What is Subresource Integrity (SRI) and how does it prevent CDN compromise attacks?](#q68) <span class="beginner">Beginner</span>
69. [How do you design an Incident Response Playbook for a Ransomware attack on cloud infrastructure?](#q69) <span class="advanced">Advanced</span>
70. [What is Bug Bounty Program design and how do you establish a Responsible Disclosure Policy (security.txt)?](#q70) <span class="intermediate">Intermediate</span>
71. [How do you configure Memory Sanitizers (AddressSanitizer, MemorySanitizer) in C/C++ CI builds?](#q71) <span class="advanced">Advanced</span>
72. [What is DNSSEC and how does it prevent DNS Cache Poisoning attacks?](#q72) <span class="advanced">Advanced</span>
73. [How do you implement Ephemeral Staging Environments with automated teardown to minimize attack surface?](#q73) <span class="intermediate">Intermediate</span>
74. [What is HTTP Request Smuggling and how do conflicting `Content-Length` and `Transfer-Encoding` cause it?](#q74) <span class="advanced">Advanced</span>
75. [How do you audit IAM role assumption with AWS CloudTrail and AWS Athena?](#q75) <span class="intermediate">Intermediate</span>
76. [What is Kernel Hardening with sysctl (`kernel.kptr_restrict`, `fs.protected_hardlinks`)?](#q76) <span class="advanced">Advanced</span>
77. [How do you implement Client-Certificate Authentication for high-security banking APIs?](#q77) <span class="advanced">Advanced</span>
78. [What is OWASP Top 10 for LLMs (Prompt Injection, Insecure Output Handling, Training Data Poisoning)?](#q78) <span class="intermediate">Intermediate</span>
79. [How do you secure Redis instances in production against remote execution exploits?](#q79) <span class="intermediate">Intermediate</span>
80. [What is OpenSSF Scorecard and how does it measure open source project health?](#q80) <span class="intermediate">Intermediate</span>
81. [How do you implement Zero-Downtime Secret Rotation for database passwords?](#q81) <span class="advanced">Advanced</span>
82. [What is Cross-Site Script Inclusion (XSSI) and how does JSON vulnerability prefix `)]}',\n` stop it?](#q82) <span class="advanced">Advanced</span>
83. [How do you configure AWS WAF Rate-Based Rules to defend against credential stuffing on `/login`?](#q83) <span class="intermediate">Intermediate</span>
84. [What is Sandboxing and how does Google Chrome / gVisor isolate untrusted code execution?](#q84) <span class="advanced">Advanced</span>
85. [How do you detect Man-in-the-Middle (MITM) attacks on mobile applications using SSL Certificate Pinning?](#q85) <span class="intermediate">Intermediate</span>
86. [What is Cross-Origin Resource Sharing (CORS) and why does `Access-Control-Allow-Origin: *` with credentials fail?](#q86) <span class="beginner">Beginner</span>
87. [How do you enforce Signed Git Commits using GPG or SSH keys in GitHub Enterprise?](#q87) <span class="beginner">Beginner</span>
88. [What is the difference between Virtual Private Cloud (VPC) Peering and AWS Transit Gateway?](#q88) <span class="intermediate">Intermediate</span>
89. [How do you prevent XML External Entity (XXE) injection attacks in legacy XML parsers?](#q89) <span class="beginner">Beginner</span>
90. [What is Security Chaos GameDay and how do cross-functional teams practice incident response?](#q90) <span class="intermediate">Intermediate</span>
91. [How do you audit Docker container images for malware and rootkit infections with ClamAV?](#q91) <span class="intermediate">Intermediate</span>
92. [What is DNS over HTTPS (DoH) and how does it protect user privacy on public Wi-Fi networks?](#q92) <span class="beginner">Beginner</span>
93. [How do you secure Prometheus metrics endpoints (`/metrics`) from unauthorized scraping?](#q93) <span class="intermediate">Intermediate</span>
94. [What is In-Memory Encryption and how does AMD SEV / Intel SGX confidential computing protect data in RAM?](#q94) <span class="advanced">Advanced</span>
95. [How do you implement Automated Security Testing in Pull Requests using GitHub Actions?](#q95) <span class="intermediate">Intermediate</span>
96. [What is the difference between Defense in Depth and Zero Trust?](#q96) <span class="intermediate">Intermediate</span>
97. [How do you secure Elasticsearch clusters against unauthenticated data exposure?](#q97) <span class="intermediate">Intermediate</span>
98. [What is Timing Attack on string comparison and how does `crypto.timingSafeEqual()` fix it?](#q98) <span class="intermediate">Intermediate</span>
99. [How do you implement Disaster Recovery with automated cross-region database replication?](#q99) <span class="advanced">Advanced</span>
100. [How do you design an enterprise Vulnerability Disclosure and Bug Bounty triage workflow?](#q100) <span class="intermediate">Intermediate</span>

---

<a id="q1"></a>
### Q1: How do you implement the STRIDE Threat Modeling Framework in an enterprise microservices architecture?

**Difficulty**: Advanced

**Strategy**:
STRIDE categorizes threats into 6 dimensions: Spoofing (mitigated by mTLS & RS256 JWTs), Tampering (TLS 1.3 & HMAC), Repudiation (WORM audit trails), Information Disclosure (least privilege IAM & encryption at rest), Denial of Service (rate limiters & circuit breakers), and Elevation of Privilege (RBAC/ABAC & rootless containers).

**Code Example**:
```markdown
STRIDE Threat Model Mapping:
- Spoofing -> SPIFFE/SPIRE Workload Identities
- Tampering -> SHA-256 Signatures & Mutual TLS
- Repudiation -> Append-only Immutable S3 CloudTrail Logs
- Info Disclosure -> KMS Envelope Encryption (AES-256-GCM)
- DoS -> Token Bucket WAF Rate Limiting
- Elevation -> Linux Kernel Capabilities Dropping (cap_drop: ALL)
```

---

<a id="q2"></a>
### Q2: How do you design a Zero-Trust Security Architecture for Kubernetes and container workloads?

**Difficulty**: Advanced

**Strategy**:
Enforce 'Never Trust, Always Verify': Implement SPIFFE/SPIRE for cryptographic pod identity, Istio service mesh for mutual TLS encryption between all pods, default-deny Kubernetes NetworkPolicies, and admission controllers enforcing non-root container execution.

**Code Example**:
```yaml
# Kubernetes Zero-Trust NetworkPolicy (Default Deny)
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
spec:
  podSelector: {}
  policyTypes:
    - Ingress
    - Egress
```

---

<a id="q3"></a>
### Q3: How do you secure CI/CD pipelines against Software Supply Chain Attacks (SLSA Level 3/4)?

**Difficulty**: Advanced

**Strategy**:
Enforce hermetic builds, generate Software Bills of Materials (SBOM) using Syft/CycloneDX, sign container images and provenance metadata cryptographically using Sigstore Cosign with keyless OIDC, and enforce admission verification in Kubernetes clusters.

**Code Example**:
```bash
# Cryptographic Container Image Signing with Cosign
cosign sign --yes ghcr.io/company/core-service@sha256:abc1234...
cosign verify --certificate-identity devops@company.com ghcr.io/company/core-service:v1.0
```

---

<a id="q4"></a>
### Q4: What is the difference between SAST, DAST, IAST, and RASP in the DevSecOps lifecycle?

**Difficulty**: Intermediate

**Strategy**:
SAST analyzes static source code without execution; DAST tests running applications from the outside like a black-box attacker; IAST uses runtime instrumentation agents inside the app to detect vulnerabilities during test execution; RASP resides in the production runtime to actively block exploit payloads.

**Code Example**:
```markdown
Application Security Testing Spectrum:
- SAST: SonarQube, Semgrep (Pre-commit / CI)
- DAST: OWASP ZAP, Burp Suite (Staging QA)
- IAST: Contrast Security (Integration testing)
- RASP: Signal Sciences, Datadog ASM (Production runtime)
```

---

<a id="q5"></a>
### Q5: How do you implement dynamic secrets management and automated rotation using HashiCorp Vault?

**Difficulty**: Advanced

**Strategy**:
Vault generates ephemeral, time-to-live (TTL) credentials on demand (e.g. temporary PostgreSQL user/password valid for 1 hour). When TTL expires, Vault automatically drops the role from the database, eliminating hardcoded long-lived credentials.

**Code Example**:
```bash
# Generate Ephemeral PostgreSQL Credentials via Vault CLI
vault read database/creds/readonly-user
# Key                Value
# ---                -----
# lease_duration     1h
# password           A1-x9yZq...
# username           v-token-readonly-user-...
```

---

<a id="q6"></a>
### Q6: How do you enforce Admission Control in Kubernetes using Open Policy Agent (OPA) Gatekeeper or Kyverno?

**Difficulty**: Advanced

**Strategy**:
Admission webhooks intercept API requests to the Kubernetes API server prior to persistence in etcd. Policies enforce that all images must originate from internal trusted registries, containers must run with read-only root filesystems, and resource limits are mandatory.

**Code Example**:
```yaml
# Kyverno ClusterPolicy: Enforce Read-Only Root Filesystem
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: require-ro-rootfs
spec:
  validationFailureAction: Enforce
  rules:
    - name: validate-ro-rootfs
      match:
        resources:
          kinds: [Pod]
      validate:
        message: "Root filesystem must be read-only!"
        pattern:
          spec:
            containers:
              - securityContext:
                  readOnlyRootFilesystem: true
```

---

<a id="q7"></a>
### Q7: What is Container Escape and how do you harden container runtimes to prevent privilege escalation?

**Difficulty**: Advanced

**Strategy**:
Container escape occurs when an attacker breaks out of container isolation to the host OS (e.g. via CVEs in runc or mounting `/var/run/docker.sock`). Prevent by running rootless containers, disabling `privileged: true`, dropping all Linux capabilities (`cap_drop: ALL`), enabling AppArmor/SELinux profiles, and using gVisor or Kata Containers for sandboxed microVM isolation.

**Code Example**:
```yaml
# Hardened Kubernetes Container SecurityContext
securityContext:
  runAsNonRoot: true
  runAsUser: 10001
  readOnlyRootFilesystem: true
  allowPrivilegeEscalation: false
  capabilities:
    drop:
      - ALL
```

---

<a id="q8"></a>
### Q8: How do you perform Runtime Threat Detection in Kubernetes using eBPF and Falco?

**Difficulty**: Advanced

**Strategy**:
Falco leverages eBPF kernel probes to monitor system calls (e.g. `execve`, `openat`, socket connections) in real-time. It compares system events against rule definitions (e.g. spawning a shell inside a container, modifying `/etc/shadow`) and emits security alerts with pod metadata.

**Code Example**:
```yaml
# Falco Rule: Detect Interactive Shell Spawned in Container
- rule: Terminal Shell in Container
  desc: A shell was spawned by an untrusted process inside a container
  condition: container.id != host and proc.name in (bash, sh, zsh)
  output: "Shell spawned in container (user=%user.name pod=%k8s.pod.name proc=%proc.name)"
  priority: WARNING
```

---

<a id="q9"></a>
### Q9: How do you implement Mutual TLS (mTLS) with SPIFFE/SPIRE for cryptographic workload identity?

**Difficulty**: Advanced

**Strategy**:
SPIRE issues cryptographic X.509 SVIDs (SPIFFE Verifiable Identity Documents) to pods based on node attestation and workload selectors. Workloads use these short-lived SVID certificates to establish mutual TLS connections where both client and server cryptographically verify identities.

**Code Example**:
```bash
# SPIFFE ID Format
spiffe://company.internal/ns/production/sa/payment-service
# SPIRE Agent issues SVID x509 cert rotated automatically every 1 hour
```

---

<a id="q10"></a>
### Q10: How do you design a secure Automated Secret Scanning pipeline to prevent credential leaks in Git?

**Difficulty**: Intermediate

**Strategy**:
Implement multi-layered secret scanning: pre-commit hooks running Gitleaks/TruffleHog, branch protection blocking commits with detected patterns, and server-side webhook scanners (GitHub Secret Scanning) that automatically revoke and alert on compromised keys.

**Code Example**:
```bash
# Pre-commit Gitleaks Scanner
gitleaks detect --source=. --verbose --redact
```

---

<a id="q11"></a>
### Q11: How do you remediate vulnerabilities found by Container Vulnerability Scanners (Trivy, Grype)?

**Difficulty**: Intermediate

**Strategy**:
Update base image to alpine/distroless, pin patch versions in package manifests, multi-stage builds to strip compilers, and automate rebuilds via Renovate.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you remediate vulnerabilities found by Container Vulnerability Scanners (Trivy, Grype)?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q12"></a>
### Q12: What is DREAD Risk Assessment and how is it calculated for security vulnerabilities?

**Difficulty**: Intermediate

**Strategy**:
DREAD scores Damage, Reproducibility, Exploitability, Affected Users, and Discoverability on a 1-10 scale to prioritize remediation backlogs.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is DREAD Risk Assessment and how is it calculated for security vulnerabilities?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q13"></a>
### Q13: How do you implement Immutable Infrastructure to enhance cloud security posture?

**Difficulty**: Intermediate

**Strategy**:
Never SSH into production servers; replace running instances with newly baked golden AMIs/images using Packer and Terraform on every release.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you implement Immutable Infrastructure to enhance cloud security posture?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q14"></a>
### Q14: What are Kubernetes NetworkPolicies and how do they enforce microsegmentation?

**Difficulty**: Intermediate

**Strategy**:
Layer 3/4 firewall rules implemented by CNI plugins (Calico/Cilium) specifying allowed ingress/egress IP blocks, ports, and pod label selectors.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What are Kubernetes NetworkPolicies and how do they enforce microsegmentation?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q15"></a>
### Q15: How do you secure API Gateways against OWASP API Top 10 vulnerabilities (BOLA, Broken Authentication)?

**Difficulty**: Advanced

**Strategy**:
Enforce object-level authorization checks in microservices, validate OpenAPI schemas on gateway, throttle endpoints with rate limiters, and strip verbose stack traces.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you secure API Gateways against OWASP API Top 10 vulnerabilities (BOLA, Broken Authentication)?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q16"></a>
### Q16: What is the difference between RBAC and ABAC in enterprise authorization architectures?

**Difficulty**: Intermediate

**Strategy**:
RBAC grants permissions based on static user roles (Admin, Editor); ABAC evaluates dynamic attributes (user department, time of day, IP location, resource sensitivity).

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is the difference between RBAC and ABAC in enterprise authorization architectures?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q17"></a>
### Q17: How do you prevent Cross-Site Scripting (XSS) using Content Security Policy (CSP) headers?

**Difficulty**: Intermediate

**Strategy**:
Define strict CSP header `Content-Security-Policy: default-src 'self'; script-src 'self' 'nonce-xyz'; object-src 'none';` to block inline script injection.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you prevent Cross-Site Scripting (XSS) using Content Security Policy (CSP) headers?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q18"></a>
### Q18: How do you secure Cloud Object Storage (AWS S3) against unauthorized public access?

**Difficulty**: Beginner

**Strategy**:
Enable S3 Block Public Access at account level, enforce default AES-256 or KMS encryption, attach least privilege bucket policies, and enable access logging.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you secure Cloud Object Storage (AWS S3) against unauthorized public access?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q19"></a>
### Q19: What is Cloud Security Posture Management (CSPM) and how does it detect misconfigurations?

**Difficulty**: Intermediate

**Strategy**:
Scans cloud infrastructure APIs against compliance benchmarks (CIS Benchmarks, NIST) to detect unencrypted databases, open security groups, and missing MFA.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is Cloud Security Posture Management (CSPM) and how does it detect misconfigurations?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q20"></a>
### Q20: How do you configure KMS Envelope Encryption to protect data at rest?

**Difficulty**: Advanced

**Strategy**:
KMS master key encrypts a local Data Encryption Key (DEK); the application uses DEK to encrypt large files with AES-GCM, storing encrypted DEK alongside the ciphertext.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you configure KMS Envelope Encryption to protect data at rest?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q21"></a>
### Q21: How do you implement Threat Intelligence Feeds into enterprise SIEM platforms?

**Difficulty**: Intermediate

**Strategy**:
Ingest STIX/TAXII feeds of known malicious IPs, domains, and file hashes into SIEM/Elasticsearch to automatically correlate against firewall and VPC flow logs.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you implement Threat Intelligence Feeds into enterprise SIEM platforms?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q22"></a>
### Q22: What is AppArmor and how do AppArmor profiles restrict container capabilities on Linux hosts?

**Difficulty**: Advanced

**Strategy**:
Linux Security Module (LSM) restricting file access, network capabilities, and execution paths per process using declarative enforcement profiles.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is AppArmor and how do AppArmor profiles restrict container capabilities on Linux hosts?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q23"></a>
### Q23: How do you detect and mitigate Server-Side Request Forgery (SSRF) in cloud environments?

**Difficulty**: Advanced

**Strategy**:
Restrict outbound HTTP requests with firewall egress rules, validate and whitelist URL schemes, and block access to cloud instance metadata IP (`169.254.169.254`).

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you detect and mitigate Server-Side Request Forgery (SSRF) in cloud environments?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q24"></a>
### Q24: What is AWS IAM Permission Boundary and how does it delegate safe admin rights?

**Difficulty**: Advanced

**Strategy**:
An advanced IAM feature setting the maximum permissions an identity-based policy can grant, preventing delegated admins from escalating their own privileges.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is AWS IAM Permission Boundary and how does it delegate safe admin rights?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q25"></a>
### Q25: How do you conduct automated Dependency License Compliance checks in CI pipelines?

**Difficulty**: Beginner

**Strategy**:
Run license scanners (FOSSA, license-checker) to fail CI builds if restrictive copyleft licenses (GPLv3, AGPL) are detected in proprietary commercial repositories.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you conduct automated Dependency License Compliance checks in CI pipelines?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q26"></a>
### Q26: How do you secure Webhook integrations against replay attacks and spoofing?

**Difficulty**: Intermediate

**Strategy**:
Sign webhook payloads with HMAC-SHA256 using a shared secret; include a timestamp in the signature header and reject requests older than 5 minutes.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you secure Webhook integrations against replay attacks and spoofing?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q27"></a>
### Q27: What is Endpoint Detection and Response (EDR) and how does it monitor developer workstations?

**Difficulty**: Intermediate

**Strategy**:
Monitors process trees, memory injections, and lateral network connections on laptops and servers, isolating compromised devices automatically.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is Endpoint Detection and Response (EDR) and how does it monitor developer workstations?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q28"></a>
### Q28: How do you configure Keycloak or Auth0 for enterprise Single Sign-On (SSO) with SAML 2.0 and OIDC?

**Difficulty**: Intermediate

**Strategy**:
Configure Identity Provider (IdP) metadata, define attribute mappings for email and roles, enforce PKCE for client authentication, and set token lifetimes.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you configure Keycloak or Auth0 for enterprise Single Sign-On (SSO) with SAML 2.0 and OIDC?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q29"></a>
### Q29: How do you prevent SQL Injection vulnerabilities in modern ORMs and raw queries?

**Difficulty**: Beginner

**Strategy**:
Always use parameterized prepared statements; never concatenate user inputs into query strings; enforce static analysis rules (Semgrep) in CI.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you prevent SQL Injection vulnerabilities in modern ORMs and raw queries?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q30"></a>
### Q30: What is Chaos Security Engineering and how do you simulate automated adversary attacks?

**Difficulty**: Advanced

**Strategy**:
Run security chaos experiments (Chaos Mesh, Infection Monkey) to simulate credential stuffing, lateral movement, and revoked certificates to validate detection alerts.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is Chaos Security Engineering and how do you simulate automated adversary attacks?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q31"></a>
### Q31: How do you securely manage environment variables in Docker and Kubernetes without leaks?

**Difficulty**: Intermediate

**Strategy**:
Never bake env vars into Dockerfile `ENV` instructions; inject secrets at runtime from Kubernetes Secret objects or Vault CSI driver as mounted in-memory tmpfs files.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you securely manage environment variables in Docker and Kubernetes without leaks?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q32"></a>
### Q32: What is the Principle of Least Privilege (PoLP) and how do you apply it to cloud IAM roles?

**Difficulty**: Beginner

**Strategy**:
Grant only the minimum specific permissions required to perform a task (e.g. `s3:GetObject` on a specific prefix rather than `s3:*` on all buckets).

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is the Principle of Least Privilege (PoLP) and how do you apply it to cloud IAM roles?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q33"></a>
### Q33: How do you protect GraphQL APIs against DoS attacks (Query Depth Limiting, Complexity Analysis)?

**Difficulty**: Advanced

**Strategy**:
Calculate query complexity scores before execution, reject nested queries exceeding depth threshold (>5), and enforce pagination limits on list fields.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you protect GraphQL APIs against DoS attacks (Query Depth Limiting, Complexity Analysis)?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q34"></a>
### Q34: What is CIS Kubernetes Benchmark and how do you audit clusters using kube-bench?

**Difficulty**: Intermediate

**Strategy**:
Run kube-bench in a Job container to audit master node configuration, etcd encryption, kubelet certificates, and control plane security against CIS standards.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is CIS Kubernetes Benchmark and how do you audit clusters using kube-bench?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q35"></a>
### Q35: How do you implement Secure Software Development Lifecycle (SSDLC) in Agile teams?

**Difficulty**: Intermediate

**Strategy**:
Integrate security requirements into user stories, conduct architecture threat models in sprint planning, run SAST/SCA in CI, and conduct pre-release pentesting.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you implement Secure Software Development Lifecycle (SSDLC) in Agile teams?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q36"></a>
### Q36: What is Forward Secrecy (PFS) in TLS 1.3 and why does it protect past traffic from decryption?

**Difficulty**: Advanced

**Strategy**:
Uses ephemeral Diffie-Hellman key exchange (ECDHE) for each session; compromising the server's long-term private key does not reveal past session keys.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is Forward Secrecy (PFS) in TLS 1.3 and why does it protect past traffic from decryption?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q37"></a>
### Q37: How do you detect Hardcoded Secrets in Git history and permanently purge them using git-filter-repo?

**Difficulty**: Intermediate

**Strategy**:
Run `git-filter-repo --path secret.pem --invert-paths` to scrub historical commits, force-push to origin, and immediately rotate the compromised credential.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you detect Hardcoded Secrets in Git history and permanently purge them using git-filter-repo?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q38"></a>
### Q38: What is Security Information and Event Management (SIEM) and how are logs ingested?

**Difficulty**: Intermediate

**Strategy**:
Centralizes security logs from cloud, OS, and applications; normalizes formats (ECS); and correlates anomalies to trigger SOC incident alarms.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is Security Information and Event Management (SIEM) and how are logs ingested?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q39"></a>
### Q39: How do you prevent Cross-Site Request Forgery (CSRF) in modern Single Page Applications (SPAs)?

**Difficulty**: Beginner

**Strategy**:
Store authentication tokens in `SameSite=Strict; HttpOnly; Secure` cookies, or use custom headers (`X-Requested-With`) with CORS protection.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you prevent Cross-Site Request Forgery (CSRF) in modern Single Page Applications (SPAs)?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q40"></a>
### Q40: How do you configure AWS GuardDuty and Security Hub for automated incident response?

**Difficulty**: Intermediate

**Strategy**:
GuardDuty analyzes VPC flow logs, DNS logs, and CloudTrail events using ML to detect anomalous behaviour; triggers EventBridge to invoke remediation Lambdas.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you configure AWS GuardDuty and Security Hub for automated incident response?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q41"></a>
### Q41: What is Web Application Firewall (WAF) and how do Managed Rule Sets (CRS) block OWASP threats?

**Difficulty**: Intermediate

**Strategy**:
Inspects HTTP traffic at Layer 7; matches payloads against regular expressions and signatures to block SQLi, XSS, and bad bots before reaching the server.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is Web Application Firewall (WAF) and how do Managed Rule Sets (CRS) block OWASP threats?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q42"></a>
### Q42: How do you configure rootless container execution with Podman or Docker Rootless Mode?

**Difficulty**: Advanced

**Strategy**:
Utilizes user namespaces (`subuid`/`subgid`) to map container UID 0 (root) to an unprivileged non-zero UID on the host, preventing host root compromise.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you configure rootless container execution with Podman or Docker Rootless Mode?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q43"></a>
### Q43: What is the difference between Symmetric (AES) and Asymmetric (RSA, ECC) Encryption?

**Difficulty**: Beginner

**Strategy**:
Symmetric uses the same key for encryption and decryption (fast, bulk data); Asymmetric uses public key for encryption and private key for decryption.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is the difference between Symmetric (AES) and Asymmetric (RSA, ECC) Encryption?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q44"></a>
### Q44: How do you design a secure Password Storage scheme using Argon2id or bcrypt with Salting?

**Difficulty**: Intermediate

**Strategy**:
Hash passwords using compute- and memory-hard functions (Argon2id) with a unique cryptographic salt per user to defeat rainbow tables and GPU cracking.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you design a secure Password Storage scheme using Argon2id or bcrypt with Salting?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q45"></a>
### Q45: How do you implement gRPC Mutual Authentication (mTLS) with custom certificate verification?

**Difficulty**: Advanced

**Strategy**:
Configure TLS credentials with client CA bundle; both client and server present x509 certificates and verify Common Name / SAN identities during handshake.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you implement gRPC Mutual Authentication (mTLS) with custom certificate verification?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q46"></a>
### Q46: What is Binary Authorization in Google Cloud or Sigstore Policy Controller in Kubernetes?

**Difficulty**: Advanced

**Strategy**:
Admission controller verifying that container images are signed by authorized build authorities and attestations pass before deployment to production.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is Binary Authorization in Google Cloud or Sigstore Policy Controller in Kubernetes?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q47"></a>
### Q47: How do you mitigate DDoS attacks using Anycast DNS, CDN edge caching, and SYN cookies?

**Difficulty**: Advanced

**Strategy**:
Distribute traffic across global Anycast points of presence, absorb volumetric attacks at CDN edge, and enable kernel SYN cookies to prevent backlog exhaustion.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you mitigate DDoS attacks using Anycast DNS, CDN edge caching, and SYN cookies?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q48"></a>
### Q48: What is eBPF Tetragon and how does it enforce real-time kernel security observability and blocking?

**Difficulty**: Advanced

**Strategy**:
Tetragon hooks into kernel execution boundaries via eBPF to trace process namespaces, detect privilege escalations, and send SIGKILL to terminate malicious processes in-kernel.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is eBPF Tetragon and how does it enforce real-time kernel security observability and blocking?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q49"></a>
### Q49: How do you audit and harden SSH access across enterprise server fleets using Teleport or Bastion hosts?

**Difficulty**: Intermediate

**Strategy**:
Eliminate static SSH keys; enforce short-lived certificate-based SSH issued via SSO/MFA, record terminal sessions, and audit command execution.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you audit and harden SSH access across enterprise server fleets using Teleport or Bastion hosts?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q50"></a>
### Q50: What are Side-Channel Attacks and how do constant-time cryptographic implementations mitigate them?

**Difficulty**: Advanced

**Strategy**:
Attacks that extract secret keys by measuring physical runtime duration, power consumption, or CPU cache misses. Mitigated by constant-time algorithms.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What are Side-Channel Attacks and how do constant-time cryptographic implementations mitigate them?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q51"></a>
### Q51: How do you implement secure Data Masking and Tokenization for sensitive PII and credit cards?

**Difficulty**: Intermediate

**Strategy**:
Replace sensitive numbers (PANs) with non-sensitive surrogate tokens; store real PII in an isolated, encrypted tokenization vault with strict access audits.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you implement secure Data Masking and Tokenization for sensitive PII and credit cards?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q52"></a>
### Q52: What is an IDOR (Insecure Direct Object Reference) vulnerability and how do you prevent it?

**Difficulty**: Beginner

**Strategy**:
Occurs when an API accepts an object ID directly without verifying the requesting user owns that resource. Fixed by enforcing tenant authorization checks on every query.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is an IDOR (Insecure Direct Object Reference) vulnerability and how do you prevent it?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q53"></a>
### Q53: How do you design a secure Multi-Tenant Database Architecture with Row-Level Security (RLS)?

**Difficulty**: Advanced

**Strategy**:
Enable PostgreSQL Row Level Security (`ENABLE ROW LEVEL SECURITY`) with policies enforcing `tenant_id = current_setting('app.current_tenant_id')`.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you design a secure Multi-Tenant Database Architecture with Row-Level Security (RLS)?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q54"></a>
### Q54: What is Threat Hunting and how do security analysts search for advanced persistent threats (APTs)?

**Difficulty**: Intermediate

**Strategy**:
Proactive hypothesis-driven search through historical telemetry and SIEM logs looking for indicators of compromise (IOCs) that bypassed automated alerts.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is Threat Hunting and how do security analysts search for advanced persistent threats (APTs)?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q55"></a>
### Q55: How do you secure serverless functions (AWS Lambda, Cloudflare Workers) against event injection?

**Difficulty**: Intermediate

**Strategy**:
Validate all event payloads against strict schemas, apply least privilege IAM execution roles, and keep function dependencies minimal and scanned.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you secure serverless functions (AWS Lambda, Cloudflare Workers) against event injection?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q56"></a>
### Q56: What is Security Chaos Engineering and how do you test fault tolerance under security stress?

**Difficulty**: Advanced

**Strategy**:
Inject security failures in staging: revoke database TLS certs, simulate DNS poisoning, or simulate expired JWT signing keys to verify system resilience.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is Security Chaos Engineering and how do you test fault tolerance under security stress?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q57"></a>
### Q57: How do you perform Threat Modeling using the PASTA (Process for Attack Simulation and Threat Analysis) framework?

**Difficulty**: Advanced

**Strategy**:
7-step risk-centric threat modeling methodology aligning technical vulnerabilities directly with business objectives and financial impact.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you perform Threat Modeling using the PASTA (Process for Attack Simulation and Threat Analysis) framework?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q58"></a>
### Q58: What is Clickjacking and how does the `X-Frame-Options` and CSP `frame-ancestors` directive prevent it?

**Difficulty**: Beginner

**Strategy**:
Attacker embeds target site in an invisible iframe to trick users into clicking buttons. Prevented by setting `X-Frame-Options: DENY` or `frame-ancestors 'none'`.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is Clickjacking and how does the `X-Frame-Options` and CSP `frame-ancestors` directive prevent it?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q59"></a>
### Q59: How do you automate TLS Certificate Provisioning and Renewal with cert-manager and Let's Encrypt?

**Difficulty**: Intermediate

**Strategy**:
Deploy cert-manager in Kubernetes with ACME ClusterIssuer, configuring HTTP-01 or DNS-01 challenge solvers to automatically rotate certificates every 60 days.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you automate TLS Certificate Provisioning and Renewal with cert-manager and Let's Encrypt?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q60"></a>
### Q60: What are Supply Chain Attacks targeting NPM and PyPI ecosystems and how do lockfiles mitigate them?

**Difficulty**: Intermediate

**Strategy**:
Malicious actors publish typo-squatted packages or hijack maintainer accounts. Mitigated by commit-pinned lockfiles, npm provenance, and private package proxies.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What are Supply Chain Attacks targeting NPM and PyPI ecosystems and how do lockfiles mitigate them?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q61"></a>
### Q61: How do you configure AWS VPC Flow Logs and analyze them with Athena for anomalous egress traffic?

**Difficulty**: Intermediate

**Strategy**:
Enable VPC Flow Logs on subnets sending to S3; query flow logs with SQL in Athena looking for rejected connections, high egress bytes, and unauthorized ports.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you configure AWS VPC Flow Logs and analyze them with Athena for anomalous egress traffic?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q62"></a>
### Q62: What is Open Policy Agent (OPA) and how do you write Rego policies for infrastructure compliance?

**Difficulty**: Advanced

**Strategy**:
Declarative policy engine evaluating JSON inputs against Rego rules; used in Terraform CI to block non-compliant resources (e.g. unencrypted RDS instances).

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is Open Policy Agent (OPA) and how do you write Rego policies for infrastructure compliance?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q63"></a>
### Q63: How do you implement Risk-Based Adaptive Authentication with IP reputation and device fingerprinting?

**Difficulty**: Advanced

**Strategy**:
Evaluate request risk score based on geo-velocity, Tor exit node status, and device cookies; dynamically challenge high-risk logins with WebAuthn/FIDO2 MFA.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you implement Risk-Based Adaptive Authentication with IP reputation and device fingerprinting?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q64"></a>
### Q64: What is Directory Traversal (Path Traversal) and how do you prevent `../` attacks in file uploads?

**Difficulty**: Beginner

**Strategy**:
Attacker manipulates file paths to access unauthorized directories. Prevented by sanitizing file names with `path.basename()` and rejecting relative dots.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is Directory Traversal (Path Traversal) and how do you prevent `../` attacks in file uploads?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q65"></a>
### Q65: How do you secure Kafka clusters with SASL/SCRAM and TLS encryption?

**Difficulty**: Advanced

**Strategy**:
Configure broker listeners with TLS for encryption in transit, enable SASL/SCRAM-SHA-512 for client authentication, and define Kafka ACLs per topic.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you secure Kafka clusters with SASL/SCRAM and TLS encryption?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q66"></a>
### Q66: What is the difference between Stateful and Stateless Firewalls?

**Difficulty**: Beginner

**Strategy**:
Stateful firewalls track active connection states (TCP SYN/ACK) and permit return traffic automatically; Stateless evaluate packets individually against rules.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is the difference between Stateful and Stateless Firewalls?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q67"></a>
### Q67: How do you configure Security Headers (`HSTS`, `X-Content-Type-Options`, `Referrer-Policy`) on Nginx?

**Difficulty**: Intermediate

**Strategy**:
Add headers in Nginx configuration: `Strict-Transport-Security: max-age=31536000; includeSubDomains`, `X-Content-Type-Options: nosniff`.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you configure Security Headers (`HSTS`, `X-Content-Type-Options`, `Referrer-Policy`) on Nginx?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q68"></a>
### Q68: What is Subresource Integrity (SRI) and how does it prevent CDN compromise attacks?

**Difficulty**: Beginner

**Strategy**:
Attaches cryptographic hash (`integrity="sha384-..."`) to script tags; browser refuses to execute script if CDN delivers altered bytes.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is Subresource Integrity (SRI) and how does it prevent CDN compromise attacks?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q69"></a>
### Q69: How do you design an Incident Response Playbook for a Ransomware attack on cloud infrastructure?

**Difficulty**: Advanced

**Strategy**:
Isolate affected subnets, take EBS snapshots for forensics, revoke compromised IAM credentials, restore from immutable air-gapped backups, and notify legal.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you design an Incident Response Playbook for a Ransomware attack on cloud infrastructure?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q70"></a>
### Q70: What is Bug Bounty Program design and how do you establish a Responsible Disclosure Policy (security.txt)?

**Difficulty**: Intermediate

**Strategy**:
Host `/.well-known/security.txt` defining PGP keys and reporting channels; set up Bugcrowd/HackerOne with clear safe harbor legal protections.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is Bug Bounty Program design and how do you establish a Responsible Disclosure Policy (security.txt)?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q71"></a>
### Q71: How do you configure Memory Sanitizers (AddressSanitizer, MemorySanitizer) in C/C++ CI builds?

**Difficulty**: Advanced

**Strategy**:
Compile with `-fsanitize=address,undefined` in CI test pipelines to catch buffer overflows, use-after-free, and memory corruption bugs before shipping.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you configure Memory Sanitizers (AddressSanitizer, MemorySanitizer) in C/C++ CI builds?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q72"></a>
### Q72: What is DNSSEC and how does it prevent DNS Cache Poisoning attacks?

**Difficulty**: Advanced

**Strategy**:
Cryptographically signs DNS zone records with public key cryptography; resolvers verify digital signatures to ensure DNS responses are authentic.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is DNSSEC and how does it prevent DNS Cache Poisoning attacks?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q73"></a>
### Q73: How do you implement Ephemeral Staging Environments with automated teardown to minimize attack surface?

**Difficulty**: Intermediate

**Strategy**:
Spin up isolated Kubernetes namespaces per PR using GitHub Actions and Helm; run automated pentests and delete namespace immediately after merge.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you implement Ephemeral Staging Environments with automated teardown to minimize attack surface?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q74"></a>
### Q74: What is HTTP Request Smuggling and how do conflicting `Content-Length` and `Transfer-Encoding` cause it?

**Difficulty**: Advanced

**Strategy**:
Occurs when frontend reverse proxy and backend server interpret HTTP request boundaries differently, allowing an attacker to smuggle hidden requests.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is HTTP Request Smuggling and how do conflicting `Content-Length` and `Transfer-Encoding` cause it?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q75"></a>
### Q75: How do you audit IAM role assumption with AWS CloudTrail and AWS Athena?

**Difficulty**: Intermediate

**Strategy**:
Query CloudTrail `AssumeRole` events in Athena to track cross-account access, credential usage timestamps, and anomalous IP addresses.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you audit IAM role assumption with AWS CloudTrail and AWS Athena?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q76"></a>
### Q76: What is Kernel Hardening with sysctl (`kernel.kptr_restrict`, `fs.protected_hardlinks`)?

**Difficulty**: Advanced

**Strategy**:
Configure Linux sysctl parameters to hide kernel pointers from unprivileged users, restrict hardlink creation, and enable memory randomization.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is Kernel Hardening with sysctl (`kernel.kptr_restrict`, `fs.protected_hardlinks`)?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q77"></a>
### Q77: How do you implement Client-Certificate Authentication for high-security banking APIs?

**Difficulty**: Advanced

**Strategy**:
Configure reverse proxy to require and validate client x509 certificates against an internal private Certificate Authority before proxying to backend.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you implement Client-Certificate Authentication for high-security banking APIs?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q78"></a>
### Q78: What is OWASP Top 10 for LLMs (Prompt Injection, Insecure Output Handling, Training Data Poisoning)?

**Difficulty**: Intermediate

**Strategy**:
Security risks specific to Generative AI: attackers manipulate LLM prompts to bypass system guardrails, extract system prompts, or execute unauthorized tools.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is OWASP Top 10 for LLMs (Prompt Injection, Insecure Output Handling, Training Data Poisoning)?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q79"></a>
### Q79: How do you secure Redis instances in production against remote execution exploits?

**Difficulty**: Intermediate

**Strategy**:
Require strong passwords (`requirepass`), disable dangerous commands (`FLUSHALL`, `CONFIG`), bind strictly to private loopback/VPC, and enable TLS.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you secure Redis instances in production against remote execution exploits?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q80"></a>
### Q80: What is OpenSSF Scorecard and how does it measure open source project health?

**Difficulty**: Intermediate

**Strategy**:
Automated tool evaluating security practices of open-source repositories: branch protection, signed commits, pinned dependencies, and vulnerability reporting.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is OpenSSF Scorecard and how does it measure open source project health?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q81"></a>
### Q81: How do you implement Zero-Downtime Secret Rotation for database passwords?

**Difficulty**: Advanced

**Strategy**:
Create second database user with identical permissions; update application config via rolling release; verify all instances connect with new credentials; revoke old user.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you implement Zero-Downtime Secret Rotation for database passwords?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q82"></a>
### Q82: What is Cross-Site Script Inclusion (XSSI) and how does JSON vulnerability prefix `)]}',\n` stop it?

**Difficulty**: Advanced

**Strategy**:
Old browser exploit reading JSON via script tag; prepending infinite loop or invalid tokens prevents parsing as executable JavaScript.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is Cross-Site Script Inclusion (XSSI) and how does JSON vulnerability prefix `)]}',\n` stop it?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q83"></a>
### Q83: How do you configure AWS WAF Rate-Based Rules to defend against credential stuffing on `/login`?

**Difficulty**: Intermediate

**Strategy**:
Create rate-based rule evaluated on client IP targeting URI `/api/login`, setting limit of 100 requests per 5-minute evaluation window.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you configure AWS WAF Rate-Based Rules to defend against credential stuffing on `/login`?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q84"></a>
### Q84: What is Sandboxing and how does Google Chrome / gVisor isolate untrusted code execution?

**Difficulty**: Advanced

**Strategy**:
Utilizes operating system primitives (namespaces, cgroups, seccomp filters) to intercept and restrict system calls made by untrusted processes.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is Sandboxing and how does Google Chrome / gVisor isolate untrusted code execution?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q85"></a>
### Q85: How do you detect Man-in-the-Middle (MITM) attacks on mobile applications using SSL Certificate Pinning?

**Difficulty**: Intermediate

**Strategy**:
Mobile apps pin the expected public key hash of the backend server; rejects connection if an intercepting proxy presents a different CA certificate.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you detect Man-in-the-Middle (MITM) attacks on mobile applications using SSL Certificate Pinning?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q86"></a>
### Q86: What is Cross-Origin Resource Sharing (CORS) and why does `Access-Control-Allow-Origin: *` with credentials fail?

**Difficulty**: Beginner

**Strategy**:
Browsers block requests with wildcard origin when credentials (cookies) are enabled to prevent malicious sites from reading authenticated user data.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is Cross-Origin Resource Sharing (CORS) and why does `Access-Control-Allow-Origin: *` with credentials fail?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q87"></a>
### Q87: How do you enforce Signed Git Commits using GPG or SSH keys in GitHub Enterprise?

**Difficulty**: Beginner

**Strategy**:
Configure `git config --global user.signingkey` and enable 'Require signed commits' branch protection rule to verify commit author identity.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you enforce Signed Git Commits using GPG or SSH keys in GitHub Enterprise?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q88"></a>
### Q88: What is the difference between Virtual Private Cloud (VPC) Peering and AWS Transit Gateway?

**Difficulty**: Intermediate

**Strategy**:
VPC Peering connects 2 VPCs in a non-transitive 1:1 mesh; Transit Gateway acts as a central cloud router connecting hundreds of VPCs and on-premise networks.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is the difference between Virtual Private Cloud (VPC) Peering and AWS Transit Gateway?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q89"></a>
### Q89: How do you prevent XML External Entity (XXE) injection attacks in legacy XML parsers?

**Difficulty**: Beginner

**Strategy**:
Disable external DTD resolution (`disallow-doctype-decl = true`) and disable external entity expansion in XML parser configuration.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you prevent XML External Entity (XXE) injection attacks in legacy XML parsers?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q90"></a>
### Q90: What is Security Chaos GameDay and how do cross-functional teams practice incident response?

**Difficulty**: Intermediate

**Strategy**:
Scheduled workshop where engineers simulate disaster scenarios (databreach, key leak) to practice war room communication and verify alerting runbooks.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is Security Chaos GameDay and how do cross-functional teams practice incident response?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q91"></a>
### Q91: How do you audit Docker container images for malware and rootkit infections with ClamAV?

**Difficulty**: Intermediate

**Strategy**:
Mount container image layers into a scanner container running ClamAV and YARA rules to detect backdoor scripts and malicious binaries.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you audit Docker container images for malware and rootkit infections with ClamAV?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q92"></a>
### Q92: What is DNS over HTTPS (DoH) and how does it protect user privacy on public Wi-Fi networks?

**Difficulty**: Beginner

**Strategy**:
Encrypts DNS queries using HTTPS/TLS, preventing local ISP and eavesdroppers from observing domain lookups.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is DNS over HTTPS (DoH) and how does it protect user privacy on public Wi-Fi networks?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q93"></a>
### Q93: How do you secure Prometheus metrics endpoints (`/metrics`) from unauthorized scraping?

**Difficulty**: Intermediate

**Strategy**:
Protect `/metrics` behind internal VPC networks, mTLS, or reverse proxy with HTTP Basic Auth / Bearer token authentication.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you secure Prometheus metrics endpoints (`/metrics`) from unauthorized scraping?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q94"></a>
### Q94: What is In-Memory Encryption and how does AMD SEV / Intel SGX confidential computing protect data in RAM?

**Difficulty**: Advanced

**Strategy**:
Hardware-enforced memory encryption engine encrypts RAM contents with keys held inside CPU; hypervisor and host OS cannot read enclave memory.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is In-Memory Encryption and how does AMD SEV / Intel SGX confidential computing protect data in RAM?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q95"></a>
### Q95: How do you implement Automated Security Testing in Pull Requests using GitHub Actions?

**Difficulty**: Intermediate

**Strategy**:
Configure workflow running SAST (Semgrep), Dependency Review, and Trivy container scan on every PR; block merges if HIGH/CRITICAL vulnerabilities exist.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you implement Automated Security Testing in Pull Requests using GitHub Actions?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q96"></a>
### Q96: What is the difference between Defense in Depth and Zero Trust?

**Difficulty**: Intermediate

**Strategy**:
Defense in Depth layers multiple perimeter defenses (firewall -> proxy -> app); Zero Trust assumes perimeter is breached and validates every transaction continuously.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is the difference between Defense in Depth and Zero Trust?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q97"></a>
### Q97: How do you secure Elasticsearch clusters against unauthenticated data exposure?

**Difficulty**: Intermediate

**Strategy**:
Enable X-Pack security, configure TLS for internode communication, enforce role-based access control (RBAC), and never expose port 9200 to the public internet.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you secure Elasticsearch clusters against unauthenticated data exposure?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q98"></a>
### Q98: What is Timing Attack on string comparison and how does `crypto.timingSafeEqual()` fix it?

**Difficulty**: Intermediate

**Strategy**:
Standard `===` exits early on the first mismatched character, leaking string length and content through microsecond differences. Fixed by constant-time XOR comparison.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: What is Timing Attack on string comparison and how does `crypto.timingSafeEqual()` fix it?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q99"></a>
### Q99: How do you implement Disaster Recovery with automated cross-region database replication?

**Difficulty**: Advanced

**Strategy**:
Configure AWS Aurora Global Database with asynchronous storage replication across regions (<1s lag); execute automated failover in under 1 minute.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you implement Disaster Recovery with automated cross-region database replication?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---

<a id="q100"></a>
### Q100: How do you design an enterprise Vulnerability Disclosure and Bug Bounty triage workflow?

**Difficulty**: Intermediate

**Strategy**:
Setup HackerOne/Bugcrowd with clear severity levels (P1-P4), SLA for triage (<24h), verified safe harbor legal protections, and automated Jira integration.

**Code Example**:
```yaml
# Enterprise DevSecOps Standard for: How do you design an enterprise Vulnerability Disclosure and Bug Bounty triage workflow?
apiVersion: security.defense/v1
kind: Policy
metadata:
  name: enforce-strict-compliance
```

---
