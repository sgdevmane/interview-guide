<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Application Security & OWASP Logo" width="100" height="100">
  </a>
  <h1>Application Security & OWASP Interview Questions & Answers</h1>
  <p><b>Comprehensive interview questions covering XSS, CSRF, SQLi, CSP, JWT Security, and Cryptography</b></p>
</div>

---

## Table of Contents

1. [Explain Cross-Site Scripting (XSS: Stored, Reflected, DOM-based) and Modern Prevention Techniques?](#q1) <span class="intermediate">Intermediate</span>
2. [How does Cross-Site Request Forgery (CSRF) work and how do SameSite Cookies and Anti-CSRF Tokens protect APIs?](#q2) <span class="intermediate">Intermediate</span>
3. [Explain SQL Injection (SQLi) and how Parameterized Queries / Prepared Statements eliminate it?](#q3) <span class="beginner">Beginner</span>
4. [Web Security & OWASP Top 10 Topic 4](#q4) <span class="advanced">Advanced</span>
5. [Web Security & OWASP Top 10 Topic 5](#q5) <span class="intermediate">Intermediate</span>
6. [Web Security & OWASP Top 10 Topic 6](#q6) <span class="advanced">Advanced</span>
7. [Web Security & OWASP Top 10 Topic 7](#q7) <span class="intermediate">Intermediate</span>
8. [Web Security & OWASP Top 10 Topic 8](#q8) <span class="advanced">Advanced</span>
9. [Web Security & OWASP Top 10 Topic 9](#q9) <span class="intermediate">Intermediate</span>
10. [Web Security & OWASP Top 10 Topic 10](#q10) <span class="advanced">Advanced</span>
11. [Web Security & OWASP Top 10 Topic 11](#q11) <span class="intermediate">Intermediate</span>
12. [Web Security & OWASP Top 10 Topic 12](#q12) <span class="advanced">Advanced</span>
13. [Web Security & OWASP Top 10 Topic 13](#q13) <span class="intermediate">Intermediate</span>
14. [Web Security & OWASP Top 10 Topic 14](#q14) <span class="advanced">Advanced</span>
15. [Web Security & OWASP Top 10 Topic 15](#q15) <span class="intermediate">Intermediate</span>
16. [Web Security & OWASP Top 10 Topic 16](#q16) <span class="advanced">Advanced</span>
17. [Web Security & OWASP Top 10 Topic 17](#q17) <span class="intermediate">Intermediate</span>
18. [Web Security & OWASP Top 10 Topic 18](#q18) <span class="advanced">Advanced</span>
19. [Web Security & OWASP Top 10 Topic 19](#q19) <span class="intermediate">Intermediate</span>
20. [Web Security & OWASP Top 10 Topic 20](#q20) <span class="advanced">Advanced</span>
21. [Web Security & OWASP Top 10 Topic 21](#q21) <span class="intermediate">Intermediate</span>
22. [Web Security & OWASP Top 10 Topic 22](#q22) <span class="advanced">Advanced</span>
23. [Web Security & OWASP Top 10 Topic 23](#q23) <span class="intermediate">Intermediate</span>
24. [Web Security & OWASP Top 10 Topic 24](#q24) <span class="advanced">Advanced</span>
25. [Web Security & OWASP Top 10 Topic 25](#q25) <span class="intermediate">Intermediate</span>
26. [Web Security & OWASP Top 10 Topic 26](#q26) <span class="advanced">Advanced</span>
27. [Web Security & OWASP Top 10 Topic 27](#q27) <span class="intermediate">Intermediate</span>
28. [Web Security & OWASP Top 10 Topic 28](#q28) <span class="advanced">Advanced</span>
29. [Web Security & OWASP Top 10 Topic 29](#q29) <span class="intermediate">Intermediate</span>
30. [Web Security & OWASP Top 10 Topic 30](#q30) <span class="advanced">Advanced</span>
31. [Web Security & OWASP Top 10 Topic 31](#q31) <span class="intermediate">Intermediate</span>
32. [Web Security & OWASP Top 10 Topic 32](#q32) <span class="advanced">Advanced</span>
33. [Web Security & OWASP Top 10 Topic 33](#q33) <span class="intermediate">Intermediate</span>
34. [Web Security & OWASP Top 10 Topic 34](#q34) <span class="advanced">Advanced</span>
35. [Web Security & OWASP Top 10 Topic 35](#q35) <span class="intermediate">Intermediate</span>
36. [Web Security & OWASP Top 10 Topic 36](#q36) <span class="advanced">Advanced</span>
37. [Web Security & OWASP Top 10 Topic 37](#q37) <span class="intermediate">Intermediate</span>
38. [Web Security & OWASP Top 10 Topic 38](#q38) <span class="advanced">Advanced</span>
39. [Web Security & OWASP Top 10 Topic 39](#q39) <span class="intermediate">Intermediate</span>
40. [Web Security & OWASP Top 10 Topic 40](#q40) <span class="advanced">Advanced</span>
41. [Web Security & OWASP Top 10 Topic 41](#q41) <span class="intermediate">Intermediate</span>
42. [Web Security & OWASP Top 10 Topic 42](#q42) <span class="advanced">Advanced</span>
43. [Web Security & OWASP Top 10 Topic 43](#q43) <span class="intermediate">Intermediate</span>
44. [Web Security & OWASP Top 10 Topic 44](#q44) <span class="advanced">Advanced</span>
45. [Web Security & OWASP Top 10 Topic 45](#q45) <span class="intermediate">Intermediate</span>
46. [Web Security & OWASP Top 10 Topic 46](#q46) <span class="advanced">Advanced</span>
47. [Web Security & OWASP Top 10 Topic 47](#q47) <span class="intermediate">Intermediate</span>
48. [Web Security & OWASP Top 10 Topic 48](#q48) <span class="advanced">Advanced</span>
49. [Web Security & OWASP Top 10 Topic 49](#q49) <span class="intermediate">Intermediate</span>
50. [Web Security & OWASP Top 10 Topic 50](#q50) <span class="advanced">Advanced</span>
51. [Web Security & OWASP Top 10 Topic 51](#q51) <span class="intermediate">Intermediate</span>
52. [Web Security & OWASP Top 10 Topic 52](#q52) <span class="advanced">Advanced</span>
53. [Web Security & OWASP Top 10 Topic 53](#q53) <span class="intermediate">Intermediate</span>
54. [Web Security & OWASP Top 10 Topic 54](#q54) <span class="advanced">Advanced</span>
55. [Web Security & OWASP Top 10 Topic 55](#q55) <span class="intermediate">Intermediate</span>
56. [Web Security & OWASP Top 10 Topic 56](#q56) <span class="advanced">Advanced</span>
57. [Web Security & OWASP Top 10 Topic 57](#q57) <span class="intermediate">Intermediate</span>
58. [Web Security & OWASP Top 10 Topic 58](#q58) <span class="advanced">Advanced</span>
59. [Web Security & OWASP Top 10 Topic 59](#q59) <span class="intermediate">Intermediate</span>
60. [Web Security & OWASP Top 10 Topic 60](#q60) <span class="advanced">Advanced</span>
61. [Web Security & OWASP Top 10 Topic 61](#q61) <span class="intermediate">Intermediate</span>
62. [Web Security & OWASP Top 10 Topic 62](#q62) <span class="advanced">Advanced</span>
63. [Web Security & OWASP Top 10 Topic 63](#q63) <span class="intermediate">Intermediate</span>
64. [Web Security & OWASP Top 10 Topic 64](#q64) <span class="advanced">Advanced</span>
65. [Web Security & OWASP Top 10 Topic 65](#q65) <span class="intermediate">Intermediate</span>
66. [Web Security & OWASP Top 10 Topic 66](#q66) <span class="advanced">Advanced</span>
67. [Web Security & OWASP Top 10 Topic 67](#q67) <span class="intermediate">Intermediate</span>
68. [Web Security & OWASP Top 10 Topic 68](#q68) <span class="advanced">Advanced</span>
69. [Web Security & OWASP Top 10 Topic 69](#q69) <span class="intermediate">Intermediate</span>
70. [Web Security & OWASP Top 10 Topic 70](#q70) <span class="advanced">Advanced</span>
71. [Web Security & OWASP Top 10 Topic 71](#q71) <span class="intermediate">Intermediate</span>
72. [Web Security & OWASP Top 10 Topic 72](#q72) <span class="advanced">Advanced</span>
73. [Web Security & OWASP Top 10 Topic 73](#q73) <span class="intermediate">Intermediate</span>
74. [Web Security & OWASP Top 10 Topic 74](#q74) <span class="advanced">Advanced</span>
75. [Web Security & OWASP Top 10 Topic 75](#q75) <span class="intermediate">Intermediate</span>
76. [Web Security & OWASP Top 10 Topic 76](#q76) <span class="advanced">Advanced</span>
77. [Web Security & OWASP Top 10 Topic 77](#q77) <span class="intermediate">Intermediate</span>
78. [Web Security & OWASP Top 10 Topic 78](#q78) <span class="advanced">Advanced</span>
79. [Web Security & OWASP Top 10 Topic 79](#q79) <span class="intermediate">Intermediate</span>
80. [Web Security & OWASP Top 10 Topic 80](#q80) <span class="advanced">Advanced</span>
81. [Web Security & OWASP Top 10 Topic 81](#q81) <span class="intermediate">Intermediate</span>
82. [Web Security & OWASP Top 10 Topic 82](#q82) <span class="advanced">Advanced</span>
83. [Web Security & OWASP Top 10 Topic 83](#q83) <span class="intermediate">Intermediate</span>
84. [Web Security & OWASP Top 10 Topic 84](#q84) <span class="advanced">Advanced</span>
85. [Web Security & OWASP Top 10 Topic 85](#q85) <span class="intermediate">Intermediate</span>
86. [Web Security & OWASP Top 10 Topic 86](#q86) <span class="advanced">Advanced</span>
87. [Web Security & OWASP Top 10 Topic 87](#q87) <span class="intermediate">Intermediate</span>
88. [Web Security & OWASP Top 10 Topic 88](#q88) <span class="advanced">Advanced</span>
89. [Web Security & OWASP Top 10 Topic 89](#q89) <span class="intermediate">Intermediate</span>
90. [Web Security & OWASP Top 10 Topic 90](#q90) <span class="advanced">Advanced</span>
91. [Web Security & OWASP Top 10 Topic 91](#q91) <span class="intermediate">Intermediate</span>
92. [Web Security & OWASP Top 10 Topic 92](#q92) <span class="advanced">Advanced</span>
93. [Web Security & OWASP Top 10 Topic 93](#q93) <span class="intermediate">Intermediate</span>
94. [Web Security & OWASP Top 10 Topic 94](#q94) <span class="advanced">Advanced</span>
95. [Web Security & OWASP Top 10 Topic 95](#q95) <span class="intermediate">Intermediate</span>
96. [Web Security & OWASP Top 10 Topic 96](#q96) <span class="advanced">Advanced</span>
97. [Web Security & OWASP Top 10 Topic 97](#q97) <span class="intermediate">Intermediate</span>
98. [Web Security & OWASP Top 10 Topic 98](#q98) <span class="advanced">Advanced</span>
99. [Web Security & OWASP Top 10 Topic 99](#q99) <span class="intermediate">Intermediate</span>
100. [Web Security & OWASP Top 10 Topic 100](#q100) <span class="advanced">Advanced</span>

---

<a id="q1"></a>
### Q1: Explain Cross-Site Scripting (XSS: Stored, Reflected, DOM-based) and Modern Prevention Techniques?

**Difficulty**: Intermediate

**Strategy**:
- **Stored XSS**: Malicious payload is permanently saved in database and rendered to other users.
- **Reflected XSS**: Payload is reflected off web server in immediate HTTP response (e.g. search query params).
- **DOM-based XSS**: Vulnerability occurs entirely client-side when JavaScript executes untrusted data in sinks (`innerHTML`, `eval()`, `document.write`).
*Mitigations*: Context-aware output encoding, DOMPurify sanitization, and strict Content-Security-Policy (CSP).

**Code Example**:
```javascript
// Safe DOM sanitization with DOMPurify
import DOMPurify from 'dompurify';

function renderSafeHTML(userUntrustedHTML, container) {
  const cleanHTML = DOMPurify.sanitize(userUntrustedHTML, { ALLOWED_TAGS: ['b', 'i', 'em', 'strong', 'a'] });
  container.innerHTML = cleanHTML;
}
```

---

<a id="q2"></a>
### Q2: How does Cross-Site Request Forgery (CSRF) work and how do SameSite Cookies and Anti-CSRF Tokens protect APIs?

**Difficulty**: Intermediate

**Strategy**:
CSRF tricks a victim's authenticated browser into submitting unauthorized requests to a trusted site.
*Defenses*:
1. **`SameSite=Strict` or `SameSite=Lax` Cookie Attribute**: Prevents browser from sending session cookies on cross-origin requests.
2. **Synchronizer Anti-CSRF Token**: Unique cryptographically random token injected into forms/headers and validated on server.
3. **Custom Headers (`X-Requested-With`)**: CORS preflight blocks cross-origin requests with custom headers.

**Code Example**:
```javascript
// Setting SameSite Cookie in Express
res.cookie('sessionId', token, {
  httpOnly: true,
  secure: true,
  sameSite: 'strict'
});
```

---

<a id="q3"></a>
### Q3: Explain SQL Injection (SQLi) and how Parameterized Queries / Prepared Statements eliminate it?

**Difficulty**: Beginner

**Strategy**:
SQLi occurs when untrusted user input is directly concatenated into SQL strings, altering query logic. Parameterized queries send query structure and parameter values separately. The database compiler parses the SQL statement AST before binding parameters as pure literal values, making SQL command execution impossible.

**Code Example**:
```javascript
// VULNERABLE TO SQLi
// db.query(`SELECT * FROM users WHERE email = '${email}'`);

// SECURE PARAMETERIZED QUERY
const query = 'SELECT * FROM users WHERE email = $1';
const result = await db.query(query, [email]);
```

---

<a id="q4"></a>
### Q4: What is the OWASP Top 10 (2021) and how do you use it engineering-wise?

**Difficulty**: Beginner

**Strategy**:
The 2021 list: Broken Access Control, Cryptographic Failures, Injection, Insecure Design, Security Misconfiguration, Vulnerable Components, Identification & Authentication Failures, Software & Data Integrity Failures, Security Logging & Monitoring Failures, SSRF. Use it as a review checklist mapping each item to concrete controls in your stack, not as a compliance checkbox.

**Code Example**:
```text
Design review mapping example:
A01 Access Control  -> centralized authorize() middleware, deny-by-default
A02 Crypto Failures -> TLS everywhere, AES-GCM at rest, argon2id passwords
A03 Injection       -> parameterized queries, context-aware output encoding
A05 Misconfig       -> hardened Helm defaults, no debug endpoints in prod
A10 SSRF            -> egress allowlist, IMDSv2, URL validation library
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q5"></a>
### Q5: What is IDOR and how do you prevent Broken Access Control?

**Difficulty**: Intermediate

**Strategy**:
Insecure Direct Object Reference occurs when the server trusts object IDs from the request without verifying ownership — `/api/invoices/1042` belonging to another user. Fix with centralized, deny-by-default authorization that binds the resource to the authenticated principal on every request (complete mediation), plus indirect references and tests that assert cross-tenant access fails.

**Code Example**:
```javascript
// Vulnerable
app.get("/api/invoices/:id", auth, (req, res) => res.json(invoices[req.params.id]));

// Fixed: scope every read/write by owner
app.get("/api/invoices/:id", auth, async (req, res) => {
  const invoice = await db.invoice.findFirst({
    where: { id: req.params.id, userId: req.user.id }, // ownership in the query
  });
  if (!invoice) return res.status(404).end(); // 404, not 403, to avoid existence leaks
  res.json(invoice);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q6"></a>
### Q6: What are Cryptographic Failures (OWASP A02) beyond "use HTTPS"?

**Difficulty**: Intermediate

**Strategy**:
The category covers plaintext storage/transit, weak or deprecated algorithms (MD5, SHA1, DES), hardcoded keys, poor randomness, and missing key rotation. Enumerate data classifications first, then apply TLS 1.2+ in transit, AES-256-GCM at rest via KMS envelope encryption, argon2id for passwords, and CSPRNG everywhere — with keys outside the codebase.

**Code Example**:
```javascript
const crypto = require("crypto");

function encrypt(plaintext, dataKey) {           // dataKey from KMS, 32 bytes
  const iv = crypto.randomBytes(12);              // GCM nonce: 96 bits, NEVER reuse with same key
  const cipher = crypto.createCipheriv("aes-256-gcm", dataKey, iv);
  const enc = Buffer.concat([cipher.update(plaintext, "utf8"), cipher.final()]);
  return { iv: iv.toString("base64"), ciphertext: enc, tag: cipher.getAuthTag().toString("base64") };
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q7"></a>
### Q7: What injection classes exist beyond SQLi (Command, LDAP, Header, SSTI)?

**Difficulty**: Advanced

**Strategy**:
Any untrusted data interpreted as code is injection: shell commands (command injection), LDAP filters, template engines (SSTI — often RCE), and response headers (CRLF). The universal fix is separating data from control: subprocess arrays with args (never shell strings), parameterized LDAP filters, logic-less templates or sandboxed rendering, and header encoding.

**Code Example**:
```javascript
// Command injection: NEVER interpolate into a shell string
const { execFile } = require("child_process");
// BAD: exec(`convert ${file} out.png`)  -> file = "a.png; rm -rf /"
execFile("convert", [file, "out.png"], (err) => {}); // args passed directly, no shell

// SSTI: user input must never enter the template source
// BAD: render("Hello " + userInput)
render("hello.tmpl", { name: userInput }); // data context only
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q8"></a>
### Q8: What does "Secure by Design" / threat modeling mean in practice?

**Difficulty**: Intermediate

**Strategy**:
Security requirements and abuse cases enter at design time: STRIDE per data-flow diagram element, trust boundary identification, and controls chosen before code exists. Concretely: deny-by-default authorization in the architecture, rate limits in the API contract, and a documented attacker model per feature — reviewed like designs are.

**Code Example**:
```text
Threat model snippet (feature: password reset)
Element: EmailService (external boundary) -> STRIDE: Spoofing, Repudiation
  Control: signed tokens, delivery audit log
Element: ResetToken store -> Tampering, Info Disclosure
  Control: hash tokens at rest, TTL 15min, single-use
Abuse cases: enumeration via timing -> constant-time compare, uniform 404s
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q9"></a>
### Q9: What are typical Security Misconfigurations (A05) and how do you prevent them?

**Difficulty**: Beginner

**Strategy**:
Debug endpoints in prod, default credentials, directory listing, verbose errors, unnecessary services/ports, permissive CORS, and unpatched middleware. Prevent with hardened infrastructure-as-code baselines, environment parity checks, automated config scanning (CIS benchmarks), and diffing rendered config per deploy.

**Code Example**:
```yaml
# Helm values hardening example
securityContext:
  runAsNonRoot: true
  readOnlyRootFilesystem: true
  allowPrivilegeEscalation: false
  capabilities: { drop: ["ALL"] }
resources:
  limits: { cpu: "500m", memory: "256Mi" }
# plus: disable default admin user, remove /debug routes outside staging
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q10"></a>
### Q10: How do you manage Vulnerable & Outdated Components (A06)?

**Difficulty**: Intermediate

**Strategy**:
Inventory dependencies (SCA tooling), score with CVSS+exploitability context (EPSS), and remediate via patch SLAs tied to severity. Gate CI on known-vulnerable versions with lockfiles committed, automated update PRs (Renovate/Dependabot), and — for transitive depth — SBOM generation.

**Code Example**:
```yaml
- name: Dependency scan gate
  run: |
    npm ci --ignore-scripts
    npm audit --audit-level=high
    trivy fs --severity HIGH,CRITICAL --exit-code 1 .
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q11"></a>
### Q11: What are Identification & Authentication Failures (A07)?

**Difficulty**: Intermediate

**Strategy**:
Weak passwords allowed, missing MFA, session fixation, predictable credentials reset, credential stuffing exposure, and login rate-limit gaps. Controls: breach-password screening, argon2id storage, MFA with phishing-resistant factors (passkeys), rotating session IDs at privilege change, and lockout/throttling on auth endpoints.

**Code Example**:
```javascript
const rateLimit = require("express-rate-limit");
app.post("/login", rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 5,                                  // per IP+username bucket
  skipSuccessfulRequests: true,
  handler: (req, res) => res.status(429).json({ error: "too_many_attempts" }),
}));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q12"></a>
### Q12: What are Software & Data Integrity Failures (A08)?

**Difficulty**: Advanced

**Strategy**:
Unverified updates, unsigned CI artifacts, insecure deserialization, and unprotected auto-update channels. The 2020 SolarWinds and PHP compromise are canonical examples. Controls: signed commits/artifacts (sigstore/cosign), locked CI pipelines, verified integrity of deserialized data (JSON schema, not object revival), and SLSA provenance attestation.

**Code Example**:
```bash
# Verify artifact signature + provenance before deploy
cosign verify --certificate-identity-regexp "^https://github.com/org/" \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com \
  registry.example.com/app@sha256:abc...

slsa-verifier verify-artifact app.tar.gz \
  --provenance-path provenance.intoto.jsonl --source-uri github.com/org/repo
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q13"></a>
### Q13: What belongs in Security Logging & Monitoring (A09) — and what must NOT?

**Difficulty**: Intermediate

**Strategy**:
Log auth events, access-control denials, input validation failures, and integrity checks with correlation IDs, timestamps (UTC, RFC3339), actor, and resource — shipped to tamper-resistant storage with alerting on anomaly patterns. Never log passwords, tokens, full PII, or card data; redact or hash instead, and document retention.

**Code Example**:
```python
import logging, hashlib
logger = logging.getLogger("audit")

def audit_login(user_id, success, ip):
    logger.info("auth.login", extra={
        "event": "auth.login",
        "actor": hashlib.sha256(user_id.encode()).hexdigest()[:16],  # pseudonymized
        "success": success,
        "ip": ip,
        # NEVER: password, session token, raw email
    })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q14"></a>
### Q14: How does SSRF work and what are the layered defenses?

**Difficulty**: Advanced

**Strategy**:
The server fetches an attacker-supplied URL and reaches internal services (metadata, admin panels, databases). Layer defenses: URL allowlists of protocols/hosts, DNS-resolution-aware validation (resolve then pin the IP, defeat rebinding), network egress deny-by-default, and cloud metadata hardening (IMDSv2 hop limit). Never trust client-supplied destinations for sensitive fetches.

**Code Example**:
```javascript
const { isIP } = require("net");
const dns = require("dns").promises;

async function safeFetch(rawUrl) {
  const u = new URL(rawUrl);
  if (u.protocol !== "https:") throw new Error("protocol");
  const ips = await dns.lookup(u.hostname, { all: true });
  if (ips.some(({ address }) => isIP(address) && (address.startsWith("10.") ||
      address.startsWith("192.168.") || address.startsWith("169.254."))))
    throw new Error("private address");
  return fetch(u, { redirect: "error" }); // no redirect-following surprises
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q15"></a>
### Q15: How does Content Security Policy stop XSS, and what does a strong policy look like?

**Difficulty**: Advanced

**Strategy**:
CSP whitelists sources the browser may load/execute, breaking inline-script injection even when encoding fails. A strong policy has no `unsafe-inline`, uses nonces or hashes with `strict-dynamic`, locks `object-src 'none'` and `base-uri 'none'`, and ships after a `Content-Security-Policy-Report-Only` rollout.

**Code Example**:
```text
Content-Security-Policy:
  default-src 'self';
  script-src 'nonce-r4nd0m' 'strict-dynamic' https:;
  object-src 'none'; base-uri 'none'; frame-ancestors 'none';
  require-trusted-types-for 'script';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q16"></a>
### Q16: CSP nonces vs hashes vs `strict-dynamic` — when to use each?

**Difficulty**: Expert

**Strategy**:
Nonces (`'nonce-xyz'`) permit specific inline scripts per response — best for server-rendered apps; must be fresh per request and unguessable. Hashes pin exact script content — fine for static inline snippets. `strict-dynamic` lets nonce-executed scripts load their own dependencies, deprecating host allowlists that bypass via JSONP/endpoints. Never combine `strict-dynamic` with scheme-src enforcement (it ignores them).

**Code Example**:
```html
<script nonce="r4nd0m">bootstrap();</script>
<!-- with 'strict-dynamic', scripts this loader adds are trusted -->
<script nonce="r4nd0m" src="/loader.js"></script>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q17"></a>
### Q17: What are Trusted Types and why are they the strongest DOM-XSS defense?

**Difficulty**: Expert

**Strategy**:
Most DOM XSS flows through sinks like `innerHTML`, `eval`, or `document.write`. Trusted Types (via CSP `require-trusted-types-for 'script'`) make those sinks accept only policy-created values, funneling all string-to-DOM conversion through audited policies you write once — turning sink-by-sink review into policy review.

**Code Example**:
```javascript
const policy = trustedTypes.createPolicy("sanitizer", {
  createHTML: (input) => DOMPurify.sanitize(input),
});
el.innerHTML = policy.createHTML(userInput);   // only sanitized values reach the sink
el.innerHTML = userInput;                      // TypeError: TrustedHTML expected
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q18"></a>
### Q18: Explain CORS mechanics: preflight, credentials, and what CORS does NOT protect?

**Difficulty**: Advanced

**Strategy**:
CORS is enforced by the browser, not the server: non-simple requests trigger an `OPTIONS` preflight; the server must echo allowed origin/methods/headers; credentialed requests require `Access-Control-Allow-Credentials` plus an exact origin (never `*`). CORS is not CSRF or authentication protection — it's read-access control for cross-origin responses.

**Code Example**:
```javascript
const cors = require("cors");
app.use(cors({
  origin: ["https://app.example.com"],     // exact origins only with credentials
  credentials: true,
  methods: ["GET", "POST"],
  allowedHeaders: ["Content-Type", "Authorization"],
  maxAge: 600,
}));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q19"></a>
### Q19: What CORS misconfigurations lead to full account takeover?

**Difficulty**: Expert

**Strategy**:
Reflecting the request Origin (or allowing `null`/wildcard-with-credentials) lets any site read authenticated responses via `fetch(..., {credentials: 'include'})`. Combine that with endpoints returning PII or bearer tokens and it's game over. Fix: strict allowlist matched server-side, `Vary: Origin` for caches, and no wildcard when credentials are enabled.

**Code Example**:
```javascript
// VULNERABLE pattern
const ALLOWED = ["app.example.com"];
app.use((req, res, next) => {
  const origin = req.headers.origin || "";
  if (ALLOWED.some((a) => origin.endsWith(a)))      // attacker: evil-app.example.com
    res.setHeader("Access-Control-Allow-Origin", origin);
  res.setHeader("Access-Control-Allow-Credentials", "true");
  next();
});
// Fix: exact Set membership + Vary: Origin
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q20"></a>
### Q20: What is the Same-Origin Policy; origin vs site; and what does SOP not restrict?

**Difficulty**: Intermediate

**Strategy**:
SOP isolates documents by (scheme, host, port) — "origin". "Site" (scheme+eTLD+1) is the newer key for cookies/Schemeful Same-Site. SOP blocks cross-origin DOM reads and most request responses, but does not prevent sending requests (images, forms, scripts load cross-origin), which is why CSRF and XS-Leaks remain possible.

**Code Example**:
```text
http://a.com vs https://a.com   -> different origin (scheme), same site
https://app.a.com vs https://api.a.com -> different origin, same site (cookies!)
SOP allows: <img src=x> request fired, response body unread
SOP blocks: fetch(x).then(r => r.json()) cross-origin without CORS
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q21"></a>
### Q21: How does Clickjacking work and how do you fully prevent it?

**Difficulty**: Beginner

**Strategy**:
An attacker overlays your page in a transparent iframe, tricking users into clicking ("UI redressing"). Modern prevention is CSP `frame-ancestors 'none'` (supersedes the old `X-Frame-Options: DENY`), plus `SameSite` cookies for defense in depth. Sensitive actions should also require user interaction the attacker can't fake (re-auth, confirmation dialogs).

**Code Example**:
```javascript
app.use((req, res, next) => {
  res.setHeader("Content-Security-Policy", "frame-ancestors 'none'");
  res.setHeader("X-Frame-Options", "DENY"); // legacy fallback
  next();
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q22"></a>
### Q22: Explain every cookie security attribute, including `__Host-`/`__Secure-` prefixes?

**Difficulty**: Intermediate

**Strategy**:
`Secure` (HTTPS only), `HttpOnly` (no JS read — session cookies), `SameSite=Lax|Strict|None` (CSRF surface; `None` requires `Secure`), `Domain`/`Path` scoping, and `Max-Age` over `Expires`. Name prefixes add guarantees: `__Host-` requires Secure, no Domain, path=/ (anti-subdomain pinning); `__Secure-` requires Secure.

**Code Example**:
```javascript
res.cookie("session", token, {
  httpOnly: true, secure: true, sameSite: "Lax",
  path: "/", maxAge: 3600_000,
});
res.cookie("csrf", nonce, { secure: true, sameSite: "Strict" }); // readable by JS on purpose
// name-prefix hardening:
res.cookie("__Host-session", token, { httpOnly: true, secure: true, path: "/" });
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q23"></a>
### Q23: What is session fixation and the correct session lifecycle?

**Difficulty**: Intermediate

**Strategy**:
Fixation plants a known session ID (URL, subdomain cookie) before login; the server then attaches the victim's identity to it. Regenerate the session ID on every privilege change (login, MFA step-up, role switch), accept IDs only from your HttpOnly cookie (never URL), and invalidate server-side on logout with the cookie cleared.

**Code Example**:
```javascript
app.post("/login", async (req, res) => {
  const user = await authenticate(req.body);
  if (user) {
    req.session.regenerate((err) => {       // NEW id post-authentication
      req.session.userId = user.id;
      res.json({ ok: true });
    });
  }
});
app.post("/logout", (req, res) => {
  req.session.destroy(() => {               // server-side store entry removed
    res.clearCookie("__Host-session");
    res.json({ ok: true });
  });
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q24"></a>
### Q24: How should session expiration work (idle vs absolute, sliding windows)?

**Difficulty**: Intermediate

**Strategy**:
Idle timeout logs out after inactivity (banking: 5–15min; normal apps: hours); absolute cap forces re-auth regardless of activity (8–24h). Sliding expiration extends the idle deadline per request — never past the absolute limit. High-risk actions should re-auth regardless. Server-side state makes revocation instant; if stateless JWTs, keep TTLs minutes-short with refresh rotation.

**Code Example**:
```javascript
const IDLE_MS = 30 * 60_000, ABSOLUTE_MS = 12 * 60 * 60_000;
function sessionValid(sess) {
  const now = Date.now();
  if (now - sess.issuedAt > ABSOLUTE_MS) return false;      // hard cap
  sess.lastSeen = now;                                       // sliding idle window
  return true;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q25"></a>
### Q25: What is a JWT's structure, and what EXACTLY must you validate?

**Difficulty**: Intermediate

**Strategy**:
Header(alg, kid) . Payload(claims) . Signature. Validate the signature against the right key (kid→JWKS), then claims: `exp` (clock-skew leeway ≤60s), `nbf`, `iss`, `aud` for your API, plus `alg` allowlisting and `typ`. Missing `exp`/`aud` checks are the most common real-world JWT bugs.

**Code Example**:
```javascript
const { jwtVerify, createRemoteJWKSet } = require("jose");
const JWKS = createRemoteJWKSet(new URL("https://idp.example.com/.well-known/jwks.json"));

async function verify(token) {
  const { payload } = await jwtVerify(token, JWKS, {
    issuer: "https://idp.example.com",
    audience: "api://orders",
    algorithms: ["RS256"],        // explicit allowlist, no alg from header
    clockTolerance: 30,
  });
  return payload;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q26"></a>
### Q26: Explain JWT `alg=none` and algorithm-confusion (RS256→HS256) attacks?

**Difficulty**: Expert

**Strategy**:
Legacy libraries accepting `alg: none` trust unsigned tokens. Algorithm confusion: attacker flips RS256 to HS256 and signs with the *public* key (which becomes the HMAC secret); if the verifier keys HMAC off the same JWKS, it validates. Defense: pin algorithms server-side (never from the header), use kid-scoped typed keys, and libraries with `algorithms` required.

**Code Example**:
```python
import jwt
# GOOD: algorithms pinned; library rejects 'none' and mismatches
claims = jwt.decode(
    token, key=jwks[key_id], algorithms=["RS256"],
    audience="api://orders", issuer="https://idp.example.com",
)
# BAD: jwt.decode(token, verify=False) or algorithms=None
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q27"></a>
### Q27: How do JWKS and `kid` enable safe key rotation?

**Difficulty**: Advanced

**Strategy**:
The IdP publishes public keys at a JWKS endpoint; tokens reference their signing key by `kid`. Rotation publishes the new key first, signs with it, and removes the old entry only after all tokens signed by it expire — guaranteeing overlap. Clients cache JWKS with refresh-on-unknown-kid, never hardcode keys.

**Code Example**:
```javascript
const jwksClient = require("jwks-rsa");
const client = jwksClient({ jwksUri: "https://idp.example.com/.well-known/jwks.json", cache: true, cacheMaxAge: 600_000 });
function getKey(header, callback) {
  client.getSigningKey(header.kid, (err, key) => {
    callback(err, key && (key.publicKey || key.rsaPublicKey));
  });
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q28"></a>
### Q28: Sessions vs JWTs — and how do you "revoke" a stateless token?

**Difficulty**: Advanced

**Strategy**:
Server sessions give instant revocation and mature security at the cost of state; JWTs shine for short-lived, cross-service identity. Revocation strategies: keep access-token TTL ≤15min with rotating refresh tokens (revoke the family on reuse detection), denylist `jti` per logout for the remaining window, or version-stamp `pwdChangedAt`-style claims.

**Code Example**:
```javascript
// refresh rotation with reuse detection
async function refresh(familyId, token) {
  const row = await db.refresh.findUnique({ where: { token: hash(token) } });
  if (!row) throw new AuthError("invalid");
  if (row.rotatedAt !== null) {              // reuse -> kill whole family
    await db.refresh.deleteMany({ where: { familyId } });
    throw new AuthError("reuse_detected");
  }
  const next = crypto.randomBytes(32).toString("base64url");
  await db.refresh.update({ where: { id: row.id }, data: { token: hash(next), rotatedAt: new Date() } });
  return { accessToken: signAccess(row.userId, "15m"), refreshToken: next };
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q29"></a>
### Q29: Compare OAuth 2.0 grants — and why was Implicit deprecated?

**Difficulty**: Advanced

**Strategy**:
Authorization Code (+PKCE) is the browser standard; Client Credentials for machine-to-machine; Device Code for input-constrained devices; Refresh Token for offline access. Implicit returned tokens in the front-channel URL fragment — leaking via history/referrers with no client authentication or refresh — so it's removed from OAuth 2.1; ROPC died with it.

**Code Example**:
```text
Authorization Code + PKCE (browser app)
GET /authorize?response_type=code&client_id=web&redirect_uri=...&scope=openid
      &code_challenge=<S256(verifier)>&code_challenge_method=S256
POST /token  { grant_type: authorization_code, code, code_verifier, client_id }
Client Credentials (service)
POST /token  { grant_type: client_credentials, scope: orders:write }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q30"></a>
### Q30: How does PKCE protect the Authorization Code flow?

**Difficulty**: Advanced

**Strategy**:
The client generates a random `code_verifier`, sends its SHA-256 as `code_challenge`, and must present the original verifier at the token exchange. A code intercepted (browser history, malicious redirect, app-scheme hijack) is useless without the verifier — binding the exchange to the initiating client without a client secret.

**Code Example**:
```javascript
const verifier = base64url(crypto.randomBytes(48));
const challenge = base64url(sha256(verifier));
// authorize?...&code_challenge=challenge&code_challenge_method=S256
// token: grant_type=authorization_code&code=CODE&code_verifier=verifier
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q31"></a>
### Q31: OIDC — what's in an ID token vs an access token, and why the `nonce`?

**Difficulty**: Advanced

**Strategy**:
The ID token is a signed JWT authenticating the user to the *client* (sub, iss, aud, nonce); the access token authorizes the *API* — never send the ID token to APIs as a bearer. `nonce` binds the ID token to the login request, blocking code-injection replay where an attacker's token gets replayed on the victim's session.

**Code Example**:
```javascript
const nonce = base64url(crypto.randomBytes(16));
// store nonce with the login session, then after callback:
const claims = await verifyIdToken(params.id_token);
if (claims.nonce !== session.nonce) throw new Error("nonce mismatch");
const { access_token } = await tokenExchange(params.code, verifier);
await fetch("/api/me", { headers: { Authorization: `Bearer ${access_token}` } });
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q32"></a>
### Q32: How should service-to-service authentication work (client credentials vs mTLS vs token exchange)?

**Difficulty**: Expert

**Strategy**:
Client credentials gives short-lived bearer JWTs from an IdP — simple, widely supported, but bearer risk. mTLS authenticates both parties cryptographically and revokes via cert CRLs — strongest for internal meshes (SPIFFE identities). RFC 8693 Token Exchange propagates the original user's identity across hops without leaking long-lived creds. Choose: IdP+CC for public-facing APIs, mTLS/SPIFFE for internal, token exchange for delegation chains.

**Code Example**:
```bash
# client credentials
curl -s https://idp/token -d grant_type=client_credentials \
  -d client_id=svc-orders -d client_secret=@file -d scope=inventory:read
# token exchange (delegation)
curl -s https://idp/token -d grant_type=urn:ietf:params:oauth:grant-type:token-exchange \
  -d subject_token=$USER_JWT -d audience=inventory
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q33"></a>
### Q33: Where should the browser store tokens (memory, localStorage, httpOnly cookie)?

**Difficulty**: Intermediate

**Strategy**:
`localStorage` is readable by any XSS — effectively a token piñata. Best practice for SPAs: keep the access token in memory only, with the refresh token in a `SameSite=Strict/HttpOnly/Secure` cookie served by a backend-for-frontend that rotates it. Pure static apps without a BFF accept the XSS tradeoff with short TTLs + CSP.

**Code Example**:
```javascript
let accessToken = null;                    // memory only — dies on reload
async function boot() {
  accessToken = await fetch("/auth/refresh", {
    method: "POST", credentials: "include",   // httpOnly refresh cookie
  }).then(r => r.json()).then(r => r.access_token);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q34"></a>
### Q34: Explain the WebAuthn/Passkey ceremony (registration + authentication)?

**Difficulty**: Expert

**Strategy**:
Registration: server sends a challenge; the OS generates a keypair scoped to the RP ID (domain), user-verifies (biometric), public key + credential ID go to the server. Authentication: server sends a fresh challenge; the authenticator signs it with the private key (never leaves the device); the server verifies with the stored public key. Phishing-resistant because origin/RP-ID is cryptographically bound.

**Code Example**:
```javascript
const cred = await navigator.credentials.create({
  publicKey: {
    challenge: fromB64(serverChallenge),
    rp: { id: "example.com", name: "Example" },
    user: { id: userId, name: email, displayName: name },
    pubKeyCredParams: [{ type: "public-key", alg: -7 }, { alg: -257 }], // ES256, RS256
    authenticatorSelection: { residentKey: "required", userVerification: "required" },
  },
});
// later: navigator.credentials.get({ publicKey: { challenge, allowCredentials: [ {id: cred.rawId} ] } })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q35"></a>
### Q35: What are discoverable credentials, syncable passkeys, and attestation trade-offs?

**Difficulty**: Expert

**Strategy**:
Discoverable (resident) credentials store user info on the authenticator enabling usernameless flows. Syncable passkeys (iCloud Keychain/Google PM) survive device loss but assume provider security; device-bound keys are stronger against exfiltration. Attestation (none/direct/enterprise) verifies authenticator model — privacy trade, generally `none` for consumer, direct for regulated.

**Code Example**:
```javascript
authenticatorSelection: {
  residentKey: "required",       // usernameless login
  userVerification: "required",
},
attestation: "none",             // privacy-preserving default
// verification server-side: verify(rpIdHash==sha256(rpId), challenge, origin, signCount monotonicity)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q36"></a>
### Q36: How does TOTP work and what are its real-world weaknesses?

**Difficulty**: Intermediate

**Strategy**:
TOTP derives codes from HOTP(K, T) where T = floor(unixTime/30): a shared secret plus time step. Weaknesses: codes phishable in real time (MITM), secret provisioning via QR can leak, 30s windows allow slight replay (track last-used step per credential), and 6 digits brute-forceable absent rate limits. Mitigate with rate limiting, single-use windows, and migrating to passkeys.

**Code Example**:
```javascript
const otpauth = require("otplib").authenticator;
const secret = otpauth.generateSecret();          // per-user, at provisioning
const ok = authenticator.check(token, secret);    // validates current window
// server: track last used timestep; reject repeats; rate limit 5/min
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q37"></a>
### Q37: Why is SMS 2FA disfavored, and what is MFA push-fatigue?

**Difficulty**: Beginner

**Strategy**:
SMS suffers SIM-swap (carrier social engineering), SS7 interception, and no phishing resistance. Push-based authenticators get "fatigue" attacks — spam approvals until the user taps yes; number-matching mitigates. NIST ranks SMS as "restricted"; prefer authenticator apps, then hardware keys/passkeys for high-value accounts.

**Code Example**:
```text
MFA factor ranking (resistance to phishing + interception):
1. Passkeys / FIDO2 security keys  (origin-bound, no shared secret)
2. TOTP authenticator app
3. Push with number matching
4. SMS (restricted: SIM swap, SS7)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q38"></a>
### Q38: How should passwords be stored — algorithm and parameters?

**Difficulty**: Intermediate

**Strategy**:
Argon2id (winner of PHC) with tuned memory (≥19MiB default OWASP: m=19456 KiB, t=2, p=1), or bcrypt cost ≥10 when memory-hard is unavailable; never MD5/SHA alone (too fast — GPU brute-force). Per-user random salt is built into these APIs. Rehash-on-login lets you migrate legacy hashes without forced resets.

**Code Example**:
```javascript
const argon2 = require("argon2");
const hash = await argon2.hash(password, { type: argon2.argon2id, memoryCost: 19456, timeCost: 2, parallelism: 1 });
const ok = await argon2.verify(hash, password);
if (ok && hash.startsWith("$argon2i$")) await rehash(password);   // silent upgrade
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q39"></a>
### Q39: What does NIST SP 800-63B say about password policy?

**Difficulty**: Intermediate

**Strategy**:
Length over composition: minimum 8, allow ≥64, no composition rules (arbitrary), no forced periodic rotation (only on evidence of compromise), screen against breached-password lists, allow all Unicode + paste (enabling managers), and rate-limit verification. Security questions/KBA are deprecated as an auth factor.

**Code Example**:
```javascript
const breached = await pwnedPasswordRange(password); // k-anonymity API — prefix only
if (password.length < 8) return reject("too_short");
if (breached > 0) return reject("breached_password");
// NO: if (!/[A-Z]/.test(password)) ...  NO: every-90-days rotation
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q40"></a>
### Q40: What is credential stuffing and how do you detect/stop it?

**Difficulty**: Advanced

**Strategy**:
Attackers replay breached email/password pairs at scale relying on reuse. Signals: distributed IPs (botnets defeat IP limits), low attempt-per-IP but high per-account, uniform UA/TLS fingerprints, unusual ASN mixes. Counter with breach-password screening at rest, per-account throttling, step-up MFA on risk, and CAPTCHA/proof-of-work on anomalies.

**Code Example**:
```python
if login_failures_for_account(user.id, window="1h") > 5:
    require_step_up_mfa(user)
if device_fingerprint_is_new(user.id, request.fp) and risk_score(request) > 0.7:
    send_new_device_notification(user)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q41"></a>
### Q41: How do you prevent username/email enumeration across login, signup, and password reset?

**Difficulty**: Intermediate

**Strategy**:
Enumeration leaks which accounts exist via differential responses, timing, or delivery behavior. Normalize: identical generic messages and timing (constant-work dummy path) for login and reset; on signup, respond neutrally and send "if this account exists" emails; never reveal existence in error codes or reset confirmations.

**Code Example**:
```python
USER_NOT_FOUND = GENERIC = "invalid_credentials"
def login(email, password):
    user = users.find(email) or DummyUser(hmac_key)   # dummy argon2 verify -> same time
    ok = user.verify(password)
    audit(email_hash)                                  # hash, don't store raw
    return ok or fail(USER_NOT_FOUND)                  # single message both ways
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q42"></a>
### Q42: Rate limiting auth endpoints — lockout vs throttling vs progressive delays?

**Difficulty**: Intermediate

**Strategy**:
Account lockout enables DoS on victims; pure IP throttling fails behind NAT/botnets. Combine: per-IP+per-account token buckets, exponential backoff with jitter after failures, CAPTCHA/step-up after thresholds, and temporal lockouts (minutes, not permanent) with secure unlock via email — never user-set unlock answers.

**Code Example**:
```javascript
const key = `${req.ip}|${sha256(username)}`;
const fails = await redis.incr(`fl:${key}`);
await redis.expire(`fl:${key}`, 900);
const wait = Math.min(2 ** fails, 3600);              // progressive delay
if (fails > 10) return res.status(429).set("Retry-After", wait).end();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q43"></a>
### Q43: What makes a password-reset token safe?

**Difficulty**: Intermediate

**Strategy**:
≥128 bits of CSPRNG entropy, hashed at rest (treat like a password), single-use, TTL ≤15–30min, bound to the requesting account, invalidated on password change and on any new request (or coalesce), delivered out-of-band, and compared in constant time. The flow must re-authenticate (session fixation regeneration) after success.

**Code Example**:
```javascript
const token = crypto.randomBytes(32);                     // 256-bit
await db.reset.create({ userId, tokenHash: sha256(token), expiresAt: in(15, "min"), usedAt: null });
// verify: lookup by hash, check usedAt==null && expiresAt>now, mark used atomically
if (!timingSafeEqual(storedHash, sha256(provided))) return generic404();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q44"></a>
### Q44: What are timing attacks and when does constant-time comparison matter?

**Difficulty**: Advanced

**Strategy**:
String comparison short-circuits on first differing byte, leaking how many prefix bytes matched — enough to recover secrets byte-by-byte (API keys, HMAC, reset tokens) when measurable over the network. Use constant-time equality for all secret comparisons, and equalize code paths where feasible (dummy verifications).

**Code Example**:
```javascript
const { timingSafeEqual } = require("crypto");
function safeEqual(a, b) {                        // length leaks are fine to fix first
  const ab = Buffer.from(String(a)), bb = Buffer.from(String(b));
  return ab.length === bb.length && timingSafeEqual(ab, bb);
}
// Never: storedToken === providedToken
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q45"></a>
### Q45: How do you prevent replay attacks in signed API requests?

**Difficulty**: Advanced

**Strategy**:
Sign canonicalized request (method, path, body hash) with HMAC or asymmetric keys, include a timestamp window (±5min) and a unique nonce; the server enforces nonce single-use within the window via a TTL store. TLS protects transport, but signing survives intermediaries, proxies, and token exfiltration channels.

**Code Example**:
```javascript
const ts = Date.now().toString(), nonce = crypto.randomUUID();
const bodyHash = sha256(body || "");
const canonical = `${method}\n${path}\n${ts}\n${nonce}\n${bodyHash}`;
const sig = hmacSha256(secretKey, canonical);
// server: |now-ts|<300s, redis SET nonce NX EX 300 must succeed, then verify sig
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q46"></a>
### Q46: HMAC vs digital signatures — properties and choice?

**Difficulty**: Intermediate

**Strategy**:
HMAC uses one shared secret: integrity + authenticity between parties that already share the key, fast, but anyone holding it can forge — no non-repudiation and risky at scale. Signatures (Ed25519/ECDSA) use private/public pairs: verifiers never hold signing capability, enabling non-repudiation and many-to-one distribution (JWKS, code signing). Rule: internal high-throughput → HMAC; cross-org/verifiable-by-others → signatures.

**Code Example**:
```javascript
const { createHmac, sign: edSign } = require("crypto");
const mac = createHmac("sha256", sharedSecret).update(payload).digest();
const sig = edSign(null, Buffer.from(payload), edPrivateKey); // Ed25519
// verify sides: hmac needs SAME secret on verifier; ed25519 needs only public key
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q47"></a>
### Q47: Hashing vs encryption vs encoding — the interview classic?

**Difficulty**: Beginner

**Strategy**:
Hashing is one-way (integrity, password storage, dedup — add salt for passwords). Encryption is reversible with a key (confidentiality). Encoding is a reversible representation change with NO security (Base64, URL-encoding) — the classic "Base64 is not encryption" trap. Pick by requirement: recover-later → encrypt; prove-match → hash; transport-format → encode.

**Code Example**:
```javascript
Buffer.from("admin:pw").toString("base64");       // encoding — not security
createHash("sha256").update(data).digest();       // hash — no key, no recovery
createCipheriv("aes-256-gcm", key, iv);            // encryption — key required to reverse
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q48"></a>
### Q48: What is hybrid encryption and why do protocols use it?

**Difficulty**: Intermediate

**Strategy**:
Asymmetric crypto is slow and size-limited; symmetric is fast. Hybrid schemes encrypt data with a random symmetric key (AES-GCM), then encrypt just that key with the recipient's public key (RSA-OAEP/ECIES/HPKE) — TLS and age/PGP file encryption both work this way. HPKE (RFC 9180) is the modern standardized construction.

**Code Example**:
```text
sender: dataKey = random(32)
        ct = AES-256-GCM(dataKey, plaintext)
        encKey = X25519(recipientPub, ephemeralSecret)  -> wrap dataKey
        output = { encKey, ct, iv, tag }                 # small envelope + bulk ct
receiver: derive dataKey via X25519(recipientPriv, ephemeralPub), decrypt ct
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q49"></a>
### Q49: Why is AES-GCM nonce reuse catastrophic, and how do you manage nonces?

**Difficulty**: Expert

**Strategy**:
GCM is a counter mode: reusing a (key, nonce) pair XORs keystreams, leaking plaintext relationships AND the auth-key H — enabling forgery of all future ciphertexts under that key. Use random 96-bit nonces (birthday-bound ~2^32 messages max), or strictly monotonic counters (e.g., derived from a counter or message number), and rotate keys long before bounds. AES-GCM-SIV tolerates accidental reuse better.

**Code Example**:
```javascript
// Random 96-bit nonce — track invocations per key; rotate at 2^32
const iv = crypto.randomBytes(12);
const c = crypto.createCipheriv("aes-256-gcm", key, iv);
// NEVER: fixed IV per key, or counter reset across process restarts
// High-assurance: derive subkeys per message: HKDF(key, msgNo) -> fresh key+IV
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q50"></a>
### Q50: What are KDFs — PBKDF2 vs bcrypt vs Argon2 — and why does memory-hardness matter?

**Difficulty**: Advanced

**Strategy**:
KDFs stretch low-entropy secrets (passwords) into keys, making brute-force expensive. PBKDF2 is iterated HMAC (GPU/ASIC-friendly — weakest); bcrypt is CPU-cost with small 4KB memory; Argon2id is memory-hard, forcing expensive RAM per guess, breaking GPU parallelism. For deriving actual crypto keys from passwords use Argon2id or scrypt with high memory (64–256MB), then HKDF to expand subkeys.

**Code Example**:
```javascript
const { hkdfSync, randomBytes } = require("crypto");
const master = argon2id(password, salt, { mem: 262144 /* 256MB */, iter: 3 });
const encKey = hkdfSync("sha256", master, "key-usage-enc", null, 32); // domain-separated subkeys
const macKey = hkdfSync("sha256", master, "key-usage-mac", null, 32);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q51"></a>
### Q51: Explain envelope encryption and the role of a KMS?

**Difficulty**: Advanced

**Strategy**:
Data is encrypted with a Data Encryption Key (DEK); the DEK is encrypted with a Key Encryption Key (KEK) that lives only in the KMS/HSM. Applications fetch plaintext DEKs (cached briefly) or encrypt DEKs themselves; the KMS centralizes access control, rotation, and audit for KEKs without ever exposing them. Enables per-record keys and cheap rotation (re-wrap DEKs, don't re-encrypt petabytes).

**Code Example**:
```python
dek = kms.generate_data_key(KeyId="alias/app-kek")   # PlaintextDEK + CiphertextBlob
record = aes_gcm_encrypt(dek.Plaintext, row.payload) # fast local crypto
store(record.ciphertext, record.iv, dek.CiphertextBlob)
# rotation: kms.re_encrypt on CiphertextBlobs or new KEK alias — data untouched
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q52"></a>
### Q52: How do you design zero-downtime key rotation (dual-key periods)?

**Difficulty**: Advanced

**Strategy**:
Overlap two active versions: write with the new key while reads accept both, then retire the old one after all consumers switched and caches drained. Each ciphertext records its key ID (or version header) so decryption picks the right key. For HMAC/webhooks, publish dual secrets during the window; for TLS certs, serve both chains during overlap.

**Code Example**:
```python
ENVELOPE = f"v2.{base64(iv)}.{base64(ct)}.{base64(tag)}.{key_id}"   # self-describing
def decrypt(env):
    ver, *parts = env.split(".")
    key = keyring.active[parts[-1]]        # accepts v1 + v2 during rotation window
    return aes_gcm_decrypt(key, *parts[:-1])
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q53"></a>
### Q53: Why is `Math.random()` (or Python's default `random`) insecure, and what do you use instead?

**Difficulty**: Beginner

**Strategy**:
Default PRNGs are seeded predictably and are not crypto-safe — outputs are recoverable, making tokens/guessable IDs forgeable. Use the platform CSPRNG: `crypto.getRandomValues`/`crypto.randomBytes` (Node/Web), `crypto/rand` (Go), `secrets` (Python), `SecureRandom` (Java). UUIDv4 from a CSPRNG is fine for IDs; UUIDv7 for sortable IDs.

**Code Example**:
```javascript
const token = crypto.randomBytes(32).toString("base64url");       // 256-bit
const id = crypto.randomUUID();                                    // v4, CSPRNG-backed
// python: secrets.token_urlsafe(32)   go: crypto/rand.Read(b)
// NEVER: Math.random().toString(36).slice(2)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q54"></a>
### Q54: What's new in TLS 1.3, and what are 0-RTT replay caveats?

**Difficulty**: Advanced

**Strategy**:
TLS 1.3 removed legacy ciphers (RSA key transport, CBC, RC4, SHA1), mandates PFS via ephemeral ECDHE, handshakes in 1-RTT (0-RTT resumption optional), encrypts most handshake messages, and simplifies to 5 strong suites. 0-RTT early data has no full replay protection — never accept non-idempotent requests (POST payments) in early data; gate by endpoint.

**Code Example**:
```text
ClientHello (key_share) ------------------------------------>
ServerHello (key_share) + {EncryptedExtensions, Cert, Finished}
<------------------------------------------------------------
[prior session ticket] 0-RTT early DATA ------------------>  # replayable!
Server: process only if request idempotent or double-submit-token ok
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q55"></a>
### Q55: How does certificate validation work, and is pinning still recommended?

**Difficulty**: Advanced

**Strategy**:
The chain builds from leaf to a trusted root, checking signatures, validity windows, EKU, hostname (SAN), and revocation (CRL/OCSP, soft-fail) — Certificate Transparency logs catch mis-issuance. Dynamic public-key pinning is deprecated for websites (HPKP removed; bricked apps on rotation) but remains valid for native mobile apps pinning SPKIs with backup pins.

**Code Example**:
```javascript
const tls = require("tls");
const sock = tls.connect(443, "api.example.com", { ALPNProtocols: ["h2"], rejectUnauthorized: true }, () => {
  const cert = sock.getPeerCertificate();
  sock.authorized && validTo(cert.valid_to) && sock.end("ok");
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q56"></a>
### Q56: What does HSTS do, what's preload, and why is it not enough alone?

**Difficulty**: Beginner

**Strategy**:
HSTS (`max-age`, `includeSubDomains`) instructs the browser to refuse plain HTTP and strip click-through prompts, killing SSL-strip MITM on the first-return visit. Preload submission hard-codes the domain into browser builds, covering even the very first request. It doesn't fix a compromised origin, insecure subdomains you forgot to include, or non-browser clients — those need redirect-plus-CSP and internal TLS.

**Code Example**:
```text
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
# serve on https only; commit domain at hstspreload.org after subdomain audit
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q57"></a>
### Q57: What is mTLS and how does it differ from API-key/JWT auth internally?

**Difficulty**: Advanced

**Strategy**:
Mutual TLS authenticates both endpoints via certificates at connection setup — no credentials in application payloads, immune to bearer-token theft, and supports revocation. Service meshes (Istio/Linkerd, SPIFFE/SPIRE identities) automate issuance/rotation. Trade-offs: PKI operational cost, no per-request context (still need a JWT for user identity), and L7 routing limitations.

**Code Example**:
```yaml
# Envoy/Istio: mTLS STRICT for namespace
apiVersion: security.istio.io/v1
kind: PeerAuthentication
metadata: { name: default, namespace: payments }
spec: { mtls: { mode: STRICT } }
# identity: spiffe://cluster.example/ns/payments/sa/orders-svc
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q58"></a>
### Q58: What is Certificate Transparency and how do you monitor it?

**Difficulty**: Intermediate

**Strategy**:
CT requires CAs to log issued certificates to append-only, publicly auditable Merkle trees; browsers refuse unlogged certs. Operators monitor logs (crt.sh, Censys, or webhooks) for unexpected issuances on their domains — the detection layer that caught Symantec and Sectigo mis-issuances. Pair with CAA DNS records restricting which CAs may issue.

**Code Example**:
```text
# CAA: only this CA may issue, subdomain-wildcards blocked
example.com.  CAA 0 issue "letsencrypt.org"
example.com.  CAA 0 iodef "mailto:security@example.com"
# monitor: daily query crt.sh?q=%25.example.com -> alert on unknown issuers
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q59"></a>
### Q59: What is the cloud-metadata SSRF vector and how does IMDSv2 fix it?

**Difficulty**: Expert

**Strategy**:
On AWS EC2/ECS, `http://169.254.169.254/latest/meta-data/` returns instance role credentials with zero auth — one SSRF in any container on the host yields cloud keys. IMDSv2 requires a session token obtained via a PUT with `X-aws-ec2-metadata-token-ttl-seconds`, and `HttpTokens=required` plus hop-limit 1 blocks forwarded/容器 fetches. EKS should use IRSA/Pod Identity instead of node roles.

**Code Example**:
```bash
TOKEN=$(curl -sX PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
curl -s -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/iam/...
aws ec2 modify-instance-metadata-options --http-tokens required --http-endpoint enabled --http-put-response-hop-limit 1
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q60"></a>
### Q60: Why are open redirects dangerous, and what's the safe implementation?

**Difficulty**: Intermediate

**Strategy**:
Redirects to attacker URLs (`?next=https://evil.com`) enable credible phishing (your domain in the link), OAuth redirect_uri bypass chains, and sanitizer-filter evasion. Safe: allowlist exact paths/origins, resolve relative-only URLs (`new URL(next, origin)` then verify same-host), and never redirect cross-origin from auth flows.

**Code Example**:
```javascript
function safeRedirect(next) {
  const url = new URL(next ?? "/", "https://app.example.com"); // relative by default
  if (url.origin !== "https://app.example.com") return "/";
  if (!url.pathname.startsWith("/settings")) return "/";      // path allowlist
  return url.pathname + url.search;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q61"></a>
### Q61: How does path traversal work and what's the robust defense?

**Difficulty**: Intermediate

**Strategy**:
Inputs like `../../etc/passwd` (or `..%2f`, `....//`, NUL, overlong UTF-8 on Windows) escape the intended directory. Defense-in-depth: reject/normalize with a hardened library, resolve the final path and verify containment (`resolve(base, input).startsWith(base + sep)`), open by validated constructed names only, drop privilege (dedicated user, chroot/container), and never pass user input to file APIs directly.

**Code Example**:
```javascript
const { resolve, sep } = require("path");
function safeJoin(base, userInput) {
  const target = resolve(base, userInput);
  if (target !== base && !target.startsWith(base + sep)) throw new Error("traversal");
  return target;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q62"></a>
### Q62: Command injection — which APIs are safe, and why is a shell ever involved?

**Difficulty**: Intermediate

**Strategy**:
Interpolating input into `sh -c` strings lets metacharacters (`; | & $( ) ` backticks) chain commands. Use exec-array APIs (`execFile`, `subprocess.run([...])`) so args pass as argv without a shell; if a shell is unavoidable (pipes/globs), gate with a strict allowlist and pass input via env, never interpolation.

**Code Example**:
```python
import subprocess
subprocess.run(["git", "log", "--", user_ref], check=True)          # argv — safe
# unavoidable shell:
import shlex
subprocess.run(["bash", "-c", f"jq . {shlex.quote(path)}"], check=True)  # last resort
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q63"></a>
### Q63: What is XXE and how do you harden XML parsing?

**Difficulty**: Advanced

**Strategy**:
XML external entities resolve `file://`, `http://` (SSRF), or billion-laughs DoS inside DTDs. Disable DTDs and external entities on every parser (libxml2, lxml, JAXP, .NET XmlReader), use JSON where possible, and for SOAP legacy apply entity limits at the gateway. The 2024 MOAN(?) style attacks on `openssl`/`glibc` prove parsers remain a soft spot.

**Code Example**:
```python
from lxml import etree
parser = etree.XMLParser(resolve_entities=False, no_network=True, dtd_validation=False,
                         load_dtd=False, huge_tree=False)
root = etree.fromstring(xml_bytes, parser=parser)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q64"></a>
### Q64: Why is deserialization of untrusted data dangerous (Java/Python/Node)?

**Difficulty**: Expert

**Strategy**:
Native deserializers instantiate arbitrary classes and invoke magic methods during reconstruction — gadget chains turn "just reading an object" into RCE (Java readObject, PHP __wakeup, Python pickle, Node node-serialize). Never deserialize untrusted bytes: use JSON with schema validation; if legacy formats are forced, cap types, run deserialization in a sandbox, and sign payloads.

**Code Example**:
```python
import pickle, json
# NEVER: pickle.loads(attacker_bytes)
obj = json.loads(payload)                 # data only
validate(obj, schema)                     # enforce structure/types before use
# if pickle is unavoidable (legacy), restrict via pickle restrictions + isolated process
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q65"></a>
### Q65: What is prototype pollution and how do you kill it?

**Difficulty**: Advanced

**Strategy**:
Merging untrusted JSON into objects can write `__proto__`/`constructor.prototype`, altering behavior of every object thereafter — enabling auth bypass or RCE with gadget chains. Kill it: reject dangerous keys in deep-merge utilities (use `Object.create(null)` targets or safe-merge libs), enable `--disallow-code-generation-from-strings` context, sanitize with `Object.freeze(Object.prototype)` in tests, and add lint rules on recursive merges.

**Code Example**:
```javascript
function safeMerge(target, src) {
  for (const [k, v] of Object.entries(src)) {
    if (k === "__proto__" || k === "constructor" || k === "prototype") continue;
    target[k] = (v && typeof v === "object") ? safeMerge(target[k] ?? {}, v) : v;
  }
  return target;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q66"></a>
### Q66: What is DOM clobbering?

**Difficulty**: Expert

**Strategy**:
Named DOM elements become global/window properties (`<img name="config">` → `window.config`); injected HTML can clobber variables later used by scripts, turning markup injection into logic manipulation even under CSP. Defenses: sanitize user HTML (DOMPurify with clobbering checks), avoid global lookups on injectable pages, set `id`/`name` allowlists, and use `typeof` guards on sensitive globals.

**Code Example**:
```html
<!-- injected: -->
<form id="cfg"><input name="isAdmin" value="true"></form>
<script>
  // later code...
  if (window.cfg?.isAdmin) grantAdmin();   // clobbered: form controls, not config
</script>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q67"></a>
### Q67: How do you secure `postMessage` and WebSocket channels?

**Difficulty**: Advanced

**Strategy**:
`postMessage` without `targetOrigin` leaks data to any listening frame; receivers must validate `event.origin` and message shape. WebSockets: enforce `Origin` checks on upgrade, authenticate out-of-band (cookie or first-message token), use `wss://`, validate frame schema/size/rate, and never derive authorization from the client's claims alone.

**Code Example**:
```javascript
// sender
win.postMessage(payload, "https://trusted.example.com");   // never '*'
// receiver
window.addEventListener("message", (e) => {
  if (e.origin !== "https://trusted.example.com") return;
  if (!messageSchema.test(e.data)) return;
  handle(e.data);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q68"></a>
### Q68: What is the file-upload vulnerability checklist?

**Difficulty**: Intermediate

**Strategy**:
Validate extension AND content-type AND magic bytes; store outside webroot with generated names; serve from a separate domain with `Content-Disposition: attachment` and neutral content-type; disable script execution on the storage; limit size/rate; scan for malware; process images in sandboxed workers (ImageMagick → safer decoders after ImageTragick); and verify re-encoded output (re-render images).

**Code Example**:
```javascript
const ALLOWED = { "image/jpeg": isJpegMagic, "image/png": isPngMagic };
const ext = { "image/jpeg": ".jpg", "image/png": ".png" }[mime];
const name = crypto.randomUUID() + ext;                      // no user filenames
await minio.put("uploads", name, sanitizedBuffer, { "Content-Type": mime,
  "Content-Disposition": "attachment" });
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q69"></a>
### Q69: Why does `X-Content-Type-Options: nosniff` matter?

**Difficulty**: Beginner

**Strategy**:
Browsers MIME-sniff responses and may execute a text/plain file as script — user-controlled content becomes code on your origin. `nosniff` forces the declared Content-Type, closing script-execution and content-confusion vectors (also required for cross-origin read protections). Always pair correct Content-Type with nosniff.

**Code Example**:
```javascript
res.setHeader("X-Content-Type-Options", "nosniff");
res.setHeader("Content-Type", "text/plain; charset=utf-8"); // stays text, guaranteed
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q70"></a>
### Q70: What is Subresource Integrity (SRI) and when is it required?

**Difficulty**: Intermediate

**Strategy**:
Third-party `<script>/<link>` tags trust the CDN; a compromised or MITM'd CDN serves malicious code. SRI pins the exact file via `integrity="sha384-..."` — the browser refuses mismatched bytes. Required for cross-origin static assets; combine with `crossorigin="anonymous"` for CORS caching. Useless for frequently-changing files — pin versions instead of `latest`.

**Code Example**:
```html
<script src="https://cdn.example.com/purify@3.0.6/purify.min.js"
        integrity="sha384-<base64-sha384>"
        crossorigin="anonymous"></script>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q71"></a>
### Q71: What is the software supply chain attack surface, and what are the controls?

**Difficulty**: Advanced

**Strategy**:
Stages: source (typosquatting/malicious PRs), build (CI compromise — SolarWinds), package registry (dependency confusion), artifact distribution (update-server hijack), and runtime (leaked creds signing). Controls per stage: locked dependencies + SCA, pinned actions by SHA + isolated builders + SLSA provenance, internal-registry namespacing + `--prefer-offline`, signed artifacts (cosign/TUF), and short-lived credentials via OIDC federation.

**Code Example**:
```yaml
# GitHub Actions: pin third-party actions by commit SHA; federate cloud creds
- uses: actions/checkout@8f4b7f84864484a7bf31766abe9204da3cbe65b3 # v4.1.1 (pinned)
- uses: aws-actions/configure-aws-credentials@v4
  with:
    role-to-assume: arn:aws:iam::...:role/deploy   # OIDC — no stored secrets
    aws-region: us-east-1
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q72"></a>
### Q72: What is a dependency-confusion attack and the exact mitigations?

**Difficulty**: Expert

**Strategy**:
Internal package names (not published publicly) are claimed by an attacker on npm/PyPI; resolution order (public registry first, or misconfigured proxy mirroring) installs the malicious "internal" package in CI/prod. Mitigate: publish internal names publicly as placeholder (empty guarded packages), scope-protect internal names (`@company/*` with registry ACLs), configure the proxy to prefer private scope to the internal registry, and enforce lockfiles so new resolution can't silently switch.

**Code Example**:
```ini
; .npmrc — scope routing + no implicit public fallback
@company:registry=https://npm.pkg.github.com
always-auth=true
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q73"></a>
### Q73: What are SBOMs and SLSA levels, concretely?

**Difficulty**: Advanced

**Strategy**:
SBOM (SPDX/CycloneDX) inventories every dependency (including transitive) per artifact — the "what do we run" needed for fast response to the next log4shell. SLSA grades build integrity: L1 scripted build, L2 hosted build+signed provenance, L3 hardened builds (isolated, ephemeral), L4 two-person reviewed + hermetic. Consumers verify provenance signatures before deploy.

**Code Example**:
```bash
syft registry.example.com/app:1.2.3 -o cyclonedx-json > sbom.json
grype sbom:sbom.json --fail-on high
cosign attest --predicate slsaprovenance.json --type slsaprovenance <image>
cosign verify-attestation --type slsaprovenance <image>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q74"></a>
### Q74: How do you keep secrets out of source and CI reliably?

**Difficulty**: Intermediate

**Strategy**:
Layer prevention: secret scanning on pre-commit + server-side push protection (block before exposure), ephemeral cloud creds via OIDC federation instead of stored keys, a secrets manager (Vault/Cloud KMS/1Password Connect) with short TTLs and per-service identities, and break-glass rotation for anything that ever touched a log or laptop.

**Code Example**:
```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.24.0
    hooks:
      - id: gitleaks
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q75"></a>
### Q75: How should API keys be issued, stored, and verified?

**Difficulty**: Intermediate

**Strategy**:
Generate ≥256-bit CSPRNG values with a prefix and checksum (`sk_live_<base32>`), show once, store only a hash (like passwords — keyed SHA or argon2), scope per key (resource, rate, expiry), support multiple + rotation, and verify in constant time. Log only the last-4/key-ID, never the key.

**Code Example**:
```python
raw = "sk_" + secrets.token_urlsafe(32)                 # show once to client
digest = hashlib.sha256(raw.encode()).hexdigest()        # store this + metadata
def verify(presented):
    row = db.lookup_by_prefix(presented[:8])            # fast routing on prefix
    return row and hmac.compare_digest(row.digest, sha256(presented))
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q76"></a>
### Q76: GraphQL-specific security controls?

**Difficulty**: Advanced

**Strategy**:
Introspection and field suggestions leak schema; query depth/circularity enable DoS; batching (aliases) bypass rate limits. Controls: disable introspection+suggestions in prod, depth/complexity cost analysis with per-token budgets, persisted queries (allowlist) instead of free-form text, pagination caps, per-field authz (not just at the edge), and mutation rate limiting by cost.

**Code Example**:
```javascript
const { depthLimit, costAnalysis } = require("graphql-validation-complexity");
const server = new ApolloServer({
  schema,
  validationRules: [
    depthLimit(8),
    costAnalysis({ maximumCost: 1000, variables,
      onComplete: (cost) => { if (cost > 1000) throw new Error("query too expensive"); } }),
  ],
  introspection: process.env.NODE_ENV !== "production",
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q77"></a>
### Q77: What is mass assignment and how do ORMs make it easy?

**Difficulty**: Intermediate

**Strategy**:
Binding request JSON directly onto models lets attackers set fields you didn't intend (`role: "admin"`, `price: 0`, `userId: <victim>`). Whitelist explicitly per endpoint (DTOs/zod schemas, `pick`), never pass raw bodies to `update`/`create`, and keep privilege fields behind separate admin paths with their own authz.

**Code Example**:
```javascript
// VULNERABLE: db.user.update(id, req.body)
const UpdateUserDto = z.object({
  name: z.string().min(1).max(80),
  bio: z.string().max(280),
});                                  // role/balance simply absent — unassignable
const data = UpdateUserDto.parse(req.body);
await db.user.update({ where: { id: req.user.id }, data });
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q78"></a>
### Q78: Idempotency keys — why and how (Stripe-style)?

**Difficulty**: Advanced

**Strategy**:
Network retries double-charge payments. The client sends a unique `Idempotency-Key` per logical operation; the server executes once and replays the stored response for repeats within 24h. Scope keys per (credential, route, key), return the ORIGINAL status even if the retry carries different params (error on mismatch), and store request-hash + response atomically.

**Code Example**:
```python
@app.post("/charges")
async def charge(req: ChargeReq, key: str = Header(...)):
    async with redis.lock(f"idem:{req.cred}:{key}", timeout=10):
        hit = await db.idempotency.get(key)
        if hit:
            if hit.request_hash != hash(req): raise HTTPException(422, "key reuse mismatch")
            return hit.response
        resp = await execute_charge(req)
        await db.idempotency.put(key, hash(req), resp, ttl=86400)
        return resp
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q79"></a>
### Q79: How do you verify incoming webhooks (Stripe/GitHub-style)?

**Difficulty**: Intermediate

**Strategy**:
Webhook URLs are secret-weak; verify a signature over timestamp+payload: constant-time HMAC check against the registered endpoint secret, reject stale timestamps (±5min) to blunt replay, respond 2xx fast, and process async via a durable queue with idempotent handlers — senders retry aggressively.

**Code Example**:
```javascript
app.post("/webhooks/stripe", express.raw({ type: "application/json" }), (req, res) => {
  const sig = req.header("stripe-signature");   // t=...,v1=...
  const event = stripe.webhooks.constructEvent(req.body, sig, process.env.STRIPE_WEBHOOK_SECRET);
  queue.add("stripe-event", event);             // async processing
  res.sendStatus(200);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q80"></a>
### Q80: What are TOCTOU race conditions in web apps (and beyond)?

**Difficulty**: Expert

**Strategy**:
Time-of-check-to-time-of-use gaps let concurrent requests exploit stale validation: double-spend via parallel GET-then-POST, withdrawal overdraws, follower-count inflation. Enforce atomicity at the state layer — conditional UPDATE with the predicate inside SQL, unique constraints, transactions with proper isolation, or serialized queues — never check in app code then write.

**Code Example**:
```sql
-- VULNERABLE: app reads balance, then updates
-- Atomic conditional write:
UPDATE accounts SET balance = balance - $1
 WHERE id = $2 AND balance >= $1
RETURNING balance;          -- 0 rows = insufficient, no partial state
-- uniqueness for exactly-once:
INSERT INTO redemptions (user_id, promo) VALUES ($1,$2)
 ON CONFLICT DO NOTHING;    -- second concurrent request gets no row
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q81"></a>
### Q81: HTTP request smuggling (CL.TE/TE.CL) — mechanism and defenses?

**Difficulty**: Expert

**Strategy**:
Front-end and back-end disagree on message boundaries when a request carries both Content-Length and Transfer-Encoding — attacker-crafted desync lets poisoned "prefixes" hijack the next user's request (auth captured, cache poisoned). Defenses: HTTP/2 end-to-end where possible, normalize/reject requests containing both headers, identical header parsing across tiers (WAF+server config audit), and reject obs-fold/whitespace anomalies.

**Code Example**:
```text
POST / HTTP/1.1
Content-Length: 6
Transfer-Encoding: chunked

0

X   # front-end (CL) forwards 6 bytes; back-end (TE) reads chunked -> "X" prefixes next request
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q82"></a>
### Q82: What was HTTP/2 Rapid Reset and what design lesson does it teach?

**Difficulty**: Expert

**Strategy**:
HTTP/2 lets clients cancel streams instantly (RST_STREAM); opening unbounded streams and immediately resetting them exhausted server CPU before rate meters noticed (CVE-2023-44487). Lessons: rate-limit by work-cost (concurrent streams, resets/sec), not just requests; enforce `SETTINGS_MAX_CONCURRENT_STREAMS`; patch runtimes; and treat protocol-level knobs as abuse surfaces in design reviews.

**Code Example**:
```nginx
http2_max_concurrent_streams 16;
limit_req_zone $binary_remote_addr zone=rst:10m rate=100r/s;    # track resets via log field
limit_conn_zone $binary_remote_addr zone=perip:10m;
limit_conn perip 50;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q83"></a>
### Q83: What is web cache deception/poisoning at a high level?

**Difficulty**: Expert

**Strategy**:
Deception: victim's browser is tricked into fetching `/profile/nonexistent.css`; the cache stores the authenticated response, attacker fetches it later. Poisoning: unkeyed inputs (headers, query params the cache ignores) alter what gets cached for everyone. Defenses: never cache authenticated responses to extension-suffixed dynamic paths, standardize cache keys, `Cache-Control: private/no-store` on personalization, and Vary correctly.

**Code Example**:
```javascript
app.get("/profile/*", (req, res) => {
  res.setHeader("Cache-Control", "no-store, private");   // never cacheable
  res.json(profile(req.user));
});
// CDN rule: only cache /assets/*; everything else origin-direct
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q84"></a>
### Q84: How do you architect against DDoS at L3/L4 and L7?

**Difficulty**: Advanced

**Strategy**:
L3/L4 (SYN/UDP floods, amplification): upstream scrubbing/anycast absorbs before your edge; SYN cookies. L7 (HTTP floods, expensive endpoints): CDN+WAF fronting, per-IP/per-session token buckets at the edge, proof-of-work or JS challenges for bots, request coalescing, and cost-asymmetric-route protection (cheap rejects first — static responses, cached errors). Capacity-test your rate limiter; the attack finds the untested path.

**Code Example**:
```nginx
limit_req_zone $binary_remote_addr zone=api:10m rate=20r/s;
location /api/ {
  limit_req zone=api burst=40 nodelay;
  limit_req_status 429;
}
location /search { limit_req zone=api burst=5; }   # expensive route = tighter budget
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q85"></a>
### Q85: What can and can't a WAF do?

**Difficulty**: Beginner

**Strategy**:
A WAF blocks known payload patterns (SQLi/XSS signatures, obvious scanners) and provides virtual patching lead-time, but bypasses are a cottage industry (encoding, grammar quirks, logic attacks) and it's blind to business-logic flaws, authz bugs, and encrypted-internal traffic. Treat it as one layer — input validation, parameterization, and authz must stand alone.

**Code Example**:
```text
WAF catches:  ' OR 1=1--, <script>alert(1)</script>, /etc/passwd traversal payloads
WAF misses:   IDOR (GET /api/invoices/1043), mass assignment, race conditions,
              SSRF via DNS-rebinding, business logic (coupon stacking)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q86"></a>
### Q86: What are the core Zero Trust principles?

**Difficulty**: Intermediate

**Strategy**:
Never trust network location; authenticate and authorize every request (identity + device posture + context), assume breach, segment by policy not topology, use short-lived credentials, and log everything for continuous verification. Implementation: strong identity (SPFFE/mTLS or IdP tokens), policy-as-code deny-by-default (OPA/Cedar), and microsegmentation east-west.

**Code Example**:
```rego
# OPA policy: default deny; allow only matching identity+action+resource
default allow = false
allow {
  input.identity.trust == "high"
  input.action == "read"
  input.resource.namespace == "public-data"
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q87"></a>
### Q87: RBAC vs ABAC vs ReBAC — where does each fit?

**Difficulty**: Advanced

**Strategy**:
RBAC maps user→roles→permissions: simple, auditable, but role explosion for fine-grained needs. ABAC decides via attributes (user dept, resource sensitivity, time, device): expressive, contextual, harder to audit. ReBAC (Zanzibar/SpiceDB/OpenFGA) evaluates relationship tuples (owner, editor-of, member-of): best for nested sharing (docs, orgs). Real systems mix: RBAC coarse-grain + ReBAC resource graphs.

**Code Example**:
```text
RBAC:  role=editor -> document:write (any document)
ABAC:  user.dept==doc.dept && hour in 9..17 && device.managed
ReBAC: document#editor@user (tuple check via graph, inherits group membership)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q88"></a>
### Q88: Container runtime hardening checklist?

**Difficulty**: Advanced

**Strategy**:
Run as non-root with dropped capabilities and no privilege escalation; read-only rootfs with tmpfs for writable paths; seccompProfile RuntimeDefault (or custom); deny hostIPC/hostPID/hostNetwork; pinned digest images scanned at build and admission; no docker.sock mounts; resource limits; and Pod Security Standards `restricted` as the namespace baseline.

**Code Example**:
```yaml
securityContext:
  runAsNonRoot: true
  runAsUser: 10001
  readOnlyRootFilesystem: true
  allowPrivilegeEscalation: false
  capabilities: { drop: ["ALL"] }
  seccompProfile: { type: RuntimeDefault }
volumes:
  - { name: tmp, emptyDir: { medium: Memory } }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q89"></a>
### Q89: How do you log securely for audit without leaking PII?

**Difficulty**: Intermediate

**Strategy**:
Classify fields before logging; tokenize/hash identifiers (pseudonymization), never log credentials/tokens/PII/card data (PCI), centralize with append-only storage and integrity chaining for forensics, and alert on audit-log gaps. Give every request a correlation ID and make user actions replayable (actor, action, resource, before/after) for incident forensics.

**Code Example**:
```python
SAFE_FIELDS = {"actor_id", "action", "resource", "result", "trace_id"}
def audit(event):
    clean = {k: v for k, v in event.items() if k in SAFE_FIELDS}
    clean["actor_id"] = hmac_sha256(pepper, str(clean["actor_id"]))[:16]
    logger.info(json.dumps(clean, sort_keys=True))  # structured + deterministic
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q90"></a>
### Q90: GDPR engineering basics: minimization, purpose limitation, erasure?

**Difficulty**: Intermediate

**Strategy**:
Collect the minimum for a stated purpose; tag PII at the schema level (data inventory) with retention policies enforced by jobs; erasure (right to be forgotten) propagates across primaries, replicas, backups (documented expiry strategy), logs (pseudonymized by design), and analytics (aggregate models documented); breaches need detection + 72h notification capability — rehearse it.

**Code Example**:
```python
class User(Base):
    __retention_days__ = 730
    email = Column(PIIEmail)          # flagged: encryption + erasure cascade
async def erase(user_id):
    async with db.transaction():
        await db.execute(users.delete().where(users.c.id == user_id))
        await analytics.forget_subject(user_id)   # documented downstream jobs
    await backup_catalog.flag_erasure(user_id)    # expiry at next rotation
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q91"></a>
### Q91: How does STRIDE map to concrete controls in design review?

**Difficulty**: Intermediate

**Strategy**:
Per data-flow element ask each threat: Spoofing (authn, mTLS, signatures), Tampering (MACs, signatures, immutable logs), Repudiation (audit trails), Info Disclosure (encryption, access control), DoS (quotas, backpressure), Elevation (least privilege, sandboxing). Output: a table of element × threat → control → ticket — making review actionable rather than theoretical.

**Code Example**:
```text
Element: Payments API (trust boundary crossing)
Spoofing      -> mTLS client certs + short-lived service tokens
Tampering     -> HMAC request signing + TLS
Repudiation   -> signed audit log with request IDs
InfoDisclose  -> field-level encryption of PAN, no PAN in logs
DoS           -> per-merchant token bucket, queue depth caps
Elevation     -> separate deploy vs runtime credentials
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q92"></a>
### Q92: What belongs in a security code-review checklist?

**Difficulty**: Beginner

**Strategy**:
Authn on every route; authz server-side per resource (never client-enforced); input validation at trust boundaries with schema; output encoding per context; secrets absent (scan); rate limits on sensitive endpoints; safe defaults (deny, secure cookies); error handling without stack traces; and dependencies pinned with scan evidence. If any row fails, block merge — consistency beats heroics.

**Code Example**:
```yaml
security_review:
  authn_on_route: true
  authz_resource_scoped: true
  input_schema_validated: true
  secrets_in_diff: none
  rate_limit_sensitive: true
  error_handling_no_trace: true
  deps_pinned_and_scanned: true
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q93"></a>
### Q93: SAST vs DAST vs SCA vs fuzzing — what does each catch?

**Difficulty**: Intermediate

**Strategy**:
SAST reads code (taint flows, insecure APIs — early, FP-heavy), DAST attacks the running app (config, auth, injection — environment-real), SCA versions dependencies (known CVEs), fuzzing throws malformed inputs at parsers/IPC (memory bugs, crashes — coverage-guided afl/libFuzzer/OSS-Fuzz). Pipeline them at PR (SAST/SCA fast gates) and nightly/deploy (DAST/fuzz).

**Code Example**:
```yaml
pull_request: [gitleaks, semgrep --error, npm audit --audit-level=high]
main nightly: [zap-baseline against staging, trivy fs, cargo fuzz --max-time 10m]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q94"></a>
### Q94: Why is verbose error handling a vulnerability (information disclosure)?

**Difficulty**: Beginner

**Strategy**:
Stack traces leak framework versions, file paths, SQL fragments, and internal hosts — reconnaissance gold. Return generic, logged-by-correlation-ID errors to clients; log full detail server-side; disable debug modes and source maps in prod; and normalize 401/403/404 semantics to avoid behavior-based probing.

**Code Example**:
```javascript
app.use((err, req, res, next) => {
  const id = req.id;
  logger.error({ err, id });                          // full detail internally
  res.status(500).json({ error: "internal_error", id }); // client sees reference only
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q95"></a>
### Q95: What are COOP, CORP, and COEP (modern isolation headers)?

**Difficulty**: Expert

**Strategy**:
Cross-Origin-Opener-Policy isolates browsing contexts (blocks window references from other origins — blocks some XS-Leaks); CORP marks who may EMBED a resource; COEP enforces that a document loads only CORP-opted-in (or same-origin) subresources — the foundation for Spectre-side-channel mitigation and enabling SharedArrayBuffer. Roll out COEP=credentialless where third-party iframes block require-corp.

**Code Example**:
```text
Cross-Origin-Opener-Policy: same-origin
Cross-Origin-Embedder-Policy: credentialless
Cross-Origin-Resource-Policy: same-origin
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q96"></a>
### Q96: What's the complete modern security-headers checklist?

**Difficulty**: Intermediate

**Strategy**:
CSP (nonce+strict-dynamic), HSTS (preload), X-Content-Type-Options: nosniff, X-Frame-Options/CSP frame-ancestors, Referrer-Policy: strict-origin-when-cross-origin, Permissions-Policy (disable unneeded APIs), COOP/CORP/COEP for isolation, and Cache-Control on sensitive responses. Verify with securityheaders.com A+ as a regression gate, not a one-off.

**Code Example**:
```javascript
helmet({
  contentSecurityPolicy: { useDefaults: true, directives: { scriptSrc: ["'self'", "'nonce-r4nd0m'", "'strict-dynamic'"], objectSrc: ["'none'"], baseUri: ["'none'"] } },
  hsts: { maxAge: 63072000, preload: true },
  referrerPolicy: { policy: "strict-origin-when-cross-origin" },
  crossOriginOpenerPolicy: { policy: "same-origin" },
  crossOriginEmbedderPolicy: { policy: "credentialless" },
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q97"></a>
### Q97: How do you secure a BFF (backend-for-frontend) pattern?

**Difficulty**: Advanced

**Strategy**:
The BFF holds refresh tokens and third-party credentials server-side; cookies to the browser must be SameSite=Strict + HttpOnly + Secure with CSRF tokens where Lax isn't enough; the BFF strips/normalizes upstream tokens (no passthrough of raw user JWTs to the client); per-origin CORS exact-match; and the BFF itself is a public attack surface — rate limits, schema validation, and no business secrets in the bundle.

**Code Example**:
```javascript
app.post("/auth/refresh", (req, res) => {
  const rt = req.cookies["__Host-rt"];
  const tokens = await idp.refresh(rt);            // server-side exchange
  res.cookie("__Host-rt", tokens.refresh_token, { httpOnly: true, secure: true, sameSite: "strict", path: "/auth" });
  res.json({ access_token: tokens.access_token }); // short-lived, memory in SPA
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q98"></a>
### Q98: How do you run a coordinated vulnerability disclosure / bug bounty?

**Difficulty**: Intermediate

**Strategy**:
Publish a security.txt and scope, triage with SLAs by severity, maintain a private disclosure channel (not GitHub issues), pay or credit fast, and have an incident path for valid criticals (mitigation → rollout → public advisory with CVE after fix window). Internal prep: labeled test accounts, sandbox bounty environment, and a legal framework that welcomes researchers.

**Code Example**:
```text
# /.well-known/security.txt
Contact: mailto:security@example.com
Preferred-Languages: en
Policy: https://example.com/.well-known/security-policy.md
Hiring: https://example.com/careers
Canonical: https://example.com/.well-known/security.txt
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q99"></a>
### Q99: How do you respond to an active incident (contain, eradicate, recover)?

**Difficulty**: Advanced

**Strategy**:
Detect and declare with severity tiers; assign IC/comms/lead roles (no hero debugging); contain laterally (revoke creds, isolate segments, block IOCs) while preserving forensic evidence; eradicate root cause (patch, rotate all possibly-exposed secrets); recover with monitoring elevated; then blameless postmortem with tracked actions. Rehearse with game-days — incident speed is a muscle.

**Code Example**:
```yaml
sev1_runbook:
  declare: page oncall + IC within 5m
  contain:
    - revoke: [api_keys, tokens, certs] possibly exposed
    - network: isolate affected pods/AZ, block IOCs at edge
  eradicate: patch CVE, purge persistence, rotate KMS-adjacent secrets
  recover: canary traffic 5%->100%, monitor error/abuse dashboards 24h
  postmortem: 48h doc + action items with owners
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q100"></a>
### Q100: How do you build security into CI/CD end-to-end?

**Difficulty**: Advanced

**Strategy**:
Pipeline stages: pre-commit secret scan → PR (SAST, SCA gates, license check) → build (provenance-attested artifacts, digest-pinned images) → admission (signature + policy verification, no `latest`) → deploy (least-privilege OIDC creds) → runtime (drift detection, scanning scheduled). Feedback in minutes at PR, depth nightly — and every gate must be breakable, or it's theater.

**Code Example**:
```yaml
stages:
  - { name: secrets, run: gitleaks protect --staged --redact }
  - { name: sast-sca, run: semgrep --error --config auto && trivy fs --severity HIGH,CRITICAL --exit-code 1 . }
  - { name: build,   run: ko build --sbom=spdx && cosign sign $(digest) }
  - { name: verify-deploy, run: cosign verify $IMAGE && kubectl apply -f k8s/ }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---
