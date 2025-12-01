<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Web security Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [How do you prevent SQL Injection in a Node.js application using raw SQL?](#q1-how-do-you-prevent-sql-injection-in-a-node.js-application-using-raw-sql) <span class="intermediate">Intermediate</span>
2. [How do you prevent Cross-Site Scripting (XSS) in a React application?](#q2-how-do-you-prevent-cross-site-scripting-xss-in-a-react-application) <span class="intermediate">Intermediate</span>
3. [How do you securely store user passwords in a database?](#q3-how-do-you-securely-store-user-passwords-in-a-database) <span class="intermediate">Intermediate</span>
4. [How do you implement Cross-Site Request Forgery (CSRF) protection?](#q4-how-do-you-implement-cross-site-request-forgery-csrf-protection) <span class="intermediate">Intermediate</span>
5. [How do you securely implement JWT authentication?](#q5-how-do-you-securely-implement-jwt-authentication) <span class="advanced">Advanced</span>
6. [How do you implement Rate Limiting to prevent DoS and Brute-Force attacks?](#q6-how-do-you-implement-rate-limiting-to-prevent-dos-and-brute-force-attacks) <span class="intermediate">Intermediate</span>
7. [How do you secure HTTP headers using Helmet?](#q7-how-do-you-secure-http-headers-using-helmet) <span class="beginner">Beginner</span>
8. [How do you prevent Server-Side Request Forgery (SSRF)?](#q8-how-do-you-prevent-server-side-request-forgery-ssrf) <span class="advanced">Advanced</span>
9. [How do you fix Insecure Direct Object References (IDOR)?](#q9-how-do-you-fix-insecure-direct-object-references-idor) <span class="intermediate">Intermediate</span>
10. [How do you securely handle file uploads?](#q10-how-do-you-securely-handle-file-uploads) <span class="intermediate">Intermediate</span>
11. [How do you manage secrets and environment variables securely?](#q11-how-do-you-manage-secrets-and-environment-variables-securely) <span class="beginner">Beginner</span>
12. [How do you prevent XML External Entity (XXE) attacks?](#q12-how-do-you-prevent-xml-external-entity-xxe-attacks) <span class="advanced">Advanced</span>
13. [How do you prevent Clickjacking?](#q13-how-do-you-prevent-clickjacking) <span class="beginner">Beginner</span>
14. [How do you implement secure Open Redirect protection?](#q14-how-do-you-implement-secure-open-redirect-protection) <span class="intermediate">Intermediate</span>
15. [How do you implement Role-Based Access Control (RBAC)?](#q15-how-do-you-implement-role-based-access-control-rbac) <span class="intermediate">Intermediate</span>
16. [How do you implement Multi-Factor Authentication (MFA) using TOTP?](#q16-how-do-you-implement-multi-factor-authentication-mfa-using-totp) <span class="intermediate">Intermediate</span>
17. [How do you prevent Query Depth attacks in GraphQL?](#q17-how-do-you-prevent-query-depth-attacks-in-graphql) <span class="intermediate">Intermediate</span>
18. [How do you prevent Regular Expression Denial of Service (ReDoS)?](#q18-how-do-you-prevent-regular-expression-denial-of-service-redos) <span class="advanced">Advanced</span>
19. [How do you properly configure Session Cookies?](#q19-how-do-you-properly-configure-session-cookies) <span class="beginner">Beginner</span>
20. [How do you use Nonces with Content Security Policy (CSP)?](#q20-how-do-you-use-nonces-with-content-security-policy-csp) <span class="advanced">Advanced</span>
21. [How do you secure WebSocket connections?](#q21-how-do-you-secure-websocket-connections) <span class="intermediate">Intermediate</span>
22. [How do you prevent Session Fixation?](#q22-how-do-you-prevent-session-fixation) <span class="intermediate">Intermediate</span>
23. [How do you implement Account Lockout securely?](#q23-how-do-you-implement-account-lockout-securely) <span class="intermediate">Intermediate</span>
24. [How do you prevent Supply Chain Attacks in Node.js?](#q24-how-do-you-prevent-supply-chain-attacks-in-node.js) <span class="intermediate">Intermediate</span>
25. [How do you implement Field-Level Encryption?](#q25-how-do-you-implement-field-level-encryption) <span class="advanced">Advanced</span>
26. [What is Perfect Forward Secrecy (PFS)?](#q26-what-is-perfect-forward-secrecy-pfs) <span class="advanced">Advanced</span>
27. [How do you implement mTLS (Mutual TLS)?](#q27-how-do-you-implement-mtls-mutual-tls) <span class="advanced">Advanced</span>
28. [How do you validate an OIDC ID Token?](#q28-how-do-you-validate-an-oidc-id-token) <span class="intermediate">Intermediate</span>
29. [How do you prevent HTTP Parameter Pollution (HPP)?](#q29-how-do-you-prevent-http-parameter-pollution-hpp) <span class="intermediate">Intermediate</span>
30. [How do you secure Serverless Functions (Least Privilege)?](#q30-how-do-you-secure-serverless-functions-least-privilege) <span class="intermediate">Intermediate</span>
31. [What is Zero Trust Architecture?](#q31-what-is-zero-trust-architecture) <span class="advanced">Advanced</span>
32. [How do you automate Key Rotation?](#q32-how-do-you-automate-key-rotation) <span class="advanced">Advanced</span>
33. [How do you detect secrets in code commits?](#q33-how-do-you-detect-secrets-in-code-commits) <span class="intermediate">Intermediate</span>
34. [How do you prevent LDAP Injection?](#q34-how-do-you-prevent-ldap-injection) <span class="intermediate">Intermediate</span>
35. [What are `Referrer-Policy` and `Permissions-Policy`?](#q35-what-are-referrer-policy-and-permissions-policy) <span class="intermediate">Intermediate</span>
36. [How do you run Docker in Rootless Mode?](#q36-how-do-you-run-docker-in-rootless-mode) <span class="intermediate">Intermediate</span>
37. [Why use PKCE in OAuth 2.0?](#q37-why-use-pkce-in-oauth-2.0) <span class="advanced">Advanced</span>
38. [How do you handle PII (Personally Identifiable Information)?](#q38-how-do-you-handle-pii-personally-identifiable-information) <span class="intermediate">Intermediate</span>
39. [How do you secure API Keys in Mobile Apps?](#q39-how-do-you-secure-api-keys-in-mobile-apps) <span class="intermediate">Intermediate</span>
40. [How do you prevent Man-in-the-Middle (MitM) attacks?](#q40-how-do-you-prevent-man-in-the-middle-mitm-attacks) <span class="beginner">Beginner</span>
41. [How do you prevent Timing Attacks?](#q41-how-do-you-prevent-timing-attacks) <span class="advanced">Advanced</span>
42. [How do you secure Audit Logs?](#q42-how-do-you-secure-audit-logs) <span class="advanced">Advanced</span>
43. [How do you implement a secure Password Reset flow?](#q43-how-do-you-implement-a-secure-password-reset-flow) <span class="intermediate">Intermediate</span>
44. [How do you secure gRPC services?](#q44-how-do-you-secure-grpc-services) <span class="advanced">Advanced</span>
45. [How do you configure CORS securely?](#q45-how-do-you-configure-cors-securely) <span class="beginner">Beginner</span>
46. [What is Subresource Integrity (SRI)?](#q46-what-is-subresource-integrity-sri) <span class="beginner">Beginner</span>
47. [How do you prevent Host Header Injection?](#q47-how-do-you-prevent-host-header-injection) <span class="intermediate">Intermediate</span>
48. [How do you prevent Directory Traversal?](#q48-how-do-you-prevent-directory-traversal) <span class="intermediate">Intermediate</span>
49. [How do you prevent Deserialization vulnerabilities?](#q49-how-do-you-prevent-deserialization-vulnerabilities) <span class="advanced">Advanced</span>
50. [How do you implement 'Defense in Depth'?](#q50-how-do-you-implement-defense-in-depth) <span class="advanced">Advanced</span>
51. [How do you handle Security state management in large scale applications?](#q51-how-do-you-handle-security-state-management-in-large-scale-applications) <span class="advanced">Advanced</span>
52. [How do you perform Security data validation in microservices?](#q52-how-do-you-perform-security-data-validation-in-microservices) <span class="beginner">Beginner</span>
53. [How do you automate Security deployment for mobile devices?](#q53-how-do-you-automate-security-deployment-for-mobile-devices) <span class="advanced">Advanced</span>
54. [How do you handle Security concurrency issues in legacy systems?](#q54-how-do-you-handle-security-concurrency-issues-in-legacy-systems) <span class="advanced">Advanced</span>
55. [How do you implement Security caching in cloud infrastructure?](#q55-how-do-you-implement-security-caching-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
56. [How do you manage Security configuration for real-time systems?](#q56-how-do-you-manage-security-configuration-for-real-time-systems) <span class="beginner">Beginner</span>
57. [How do you handle Security internationalization (i18n) in distributed systems?](#q57-how-do-you-handle-security-internationalization-i18n-in-distributed-systems) <span class="intermediate">Intermediate</span>
58. [How do you ensure Security accessibility (a11y) in high-traffic sites?](#q58-how-do-you-ensure-security-accessibility-a11y-in-high-traffic-sites) <span class="beginner">Beginner</span>
59. [How do you optimize Security network requests in embedded systems?](#q59-how-do-you-optimize-security-network-requests-in-embedded-systems) <span class="advanced">Advanced</span>
60. [How do you handle Security performance optimization for production environments?](#q60-how-do-you-handle-security-performance-optimization-for-production-environments) <span class="advanced">Advanced</span>
61. [What are the security implications of Security in large scale applications?](#q61-what-are-the-security-implications-of-security-in-large-scale-applications) <span class="intermediate">Intermediate</span>
62. [How do you debug Security memory leaks in microservices?](#q62-how-do-you-debug-security-memory-leaks-in-microservices) <span class="advanced">Advanced</span>
63. [Best practices for Security code organization in mobile devices?](#q63-best-practices-for-security-code-organization-in-mobile-devices) <span class="beginner">Beginner</span>
64. [How do you implement Security error handling for legacy systems?](#q64-how-do-you-implement-security-error-handling-for-legacy-systems) <span class="intermediate">Intermediate</span>
65. [How do you test Security functionality in cloud infrastructure?](#q65-how-do-you-test-security-functionality-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
66. [How do you handle Security state management in real-time systems?](#q66-how-do-you-handle-security-state-management-in-real-time-systems) <span class="advanced">Advanced</span>
67. [How do you perform Security data validation in distributed systems?](#q67-how-do-you-perform-security-data-validation-in-distributed-systems) <span class="beginner">Beginner</span>
68. [How do you automate Security deployment for high-traffic sites?](#q68-how-do-you-automate-security-deployment-for-high-traffic-sites) <span class="advanced">Advanced</span>
69. [How do you handle Security concurrency issues in embedded systems?](#q69-how-do-you-handle-security-concurrency-issues-in-embedded-systems) <span class="advanced">Advanced</span>
70. [How do you implement Security caching in production environments?](#q70-how-do-you-implement-security-caching-in-production-environments) <span class="intermediate">Intermediate</span>
71. [How do you manage Security configuration for large scale applications?](#q71-how-do-you-manage-security-configuration-for-large-scale-applications) <span class="beginner">Beginner</span>
72. [How do you handle Security internationalization (i18n) in microservices?](#q72-how-do-you-handle-security-internationalization-i18n-in-microservices) <span class="intermediate">Intermediate</span>
73. [How do you ensure Security accessibility (a11y) in mobile devices?](#q73-how-do-you-ensure-security-accessibility-a11y-in-mobile-devices) <span class="beginner">Beginner</span>
74. [How do you optimize Security network requests in legacy systems?](#q74-how-do-you-optimize-security-network-requests-in-legacy-systems) <span class="advanced">Advanced</span>
75. [How do you handle Security performance optimization for cloud infrastructure?](#q75-how-do-you-handle-security-performance-optimization-for-cloud-infrastructure) <span class="advanced">Advanced</span>
76. [What are the security implications of Security in real-time systems?](#q76-what-are-the-security-implications-of-security-in-real-time-systems) <span class="intermediate">Intermediate</span>
77. [How do you debug Security memory leaks in distributed systems?](#q77-how-do-you-debug-security-memory-leaks-in-distributed-systems) <span class="advanced">Advanced</span>
78. [Best practices for Security code organization in high-traffic sites?](#q78-best-practices-for-security-code-organization-in-high-traffic-sites) <span class="beginner">Beginner</span>
79. [How do you implement Security error handling for embedded systems?](#q79-how-do-you-implement-security-error-handling-for-embedded-systems) <span class="intermediate">Intermediate</span>
80. [How do you test Security functionality in production environments?](#q80-how-do-you-test-security-functionality-in-production-environments) <span class="intermediate">Intermediate</span>
81. [How do you handle Security state management in large scale applications?](#q81-how-do-you-handle-security-state-management-in-large-scale-applications) <span class="advanced">Advanced</span>
82. [How do you perform Security data validation in microservices?](#q82-how-do-you-perform-security-data-validation-in-microservices) <span class="beginner">Beginner</span>
83. [How do you automate Security deployment for mobile devices?](#q83-how-do-you-automate-security-deployment-for-mobile-devices) <span class="advanced">Advanced</span>
84. [How do you handle Security concurrency issues in legacy systems?](#q84-how-do-you-handle-security-concurrency-issues-in-legacy-systems) <span class="advanced">Advanced</span>
85. [How do you implement Security caching in cloud infrastructure?](#q85-how-do-you-implement-security-caching-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
86. [How do you manage Security configuration for real-time systems?](#q86-how-do-you-manage-security-configuration-for-real-time-systems) <span class="beginner">Beginner</span>
87. [How do you handle Security internationalization (i18n) in distributed systems?](#q87-how-do-you-handle-security-internationalization-i18n-in-distributed-systems) <span class="intermediate">Intermediate</span>
88. [How do you ensure Security accessibility (a11y) in high-traffic sites?](#q88-how-do-you-ensure-security-accessibility-a11y-in-high-traffic-sites) <span class="beginner">Beginner</span>
89. [How do you optimize Security network requests in embedded systems?](#q89-how-do-you-optimize-security-network-requests-in-embedded-systems) <span class="advanced">Advanced</span>
90. [How do you handle Security performance optimization for production environments?](#q90-how-do-you-handle-security-performance-optimization-for-production-environments) <span class="advanced">Advanced</span>
91. [What are the security implications of Security in large scale applications?](#q91-what-are-the-security-implications-of-security-in-large-scale-applications) <span class="intermediate">Intermediate</span>
92. [How do you debug Security memory leaks in microservices?](#q92-how-do-you-debug-security-memory-leaks-in-microservices) <span class="advanced">Advanced</span>
93. [Best practices for Security code organization in mobile devices?](#q93-best-practices-for-security-code-organization-in-mobile-devices) <span class="beginner">Beginner</span>
94. [How do you implement Security error handling for legacy systems?](#q94-how-do-you-implement-security-error-handling-for-legacy-systems) <span class="intermediate">Intermediate</span>
95. [How do you test Security functionality in cloud infrastructure?](#q95-how-do-you-test-security-functionality-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
96. [How do you handle Security state management in real-time systems?](#q96-how-do-you-handle-security-state-management-in-real-time-systems) <span class="advanced">Advanced</span>
97. [How do you perform Security data validation in distributed systems?](#q97-how-do-you-perform-security-data-validation-in-distributed-systems) <span class="beginner">Beginner</span>
98. [How do you automate Security deployment for high-traffic sites?](#q98-how-do-you-automate-security-deployment-for-high-traffic-sites) <span class="advanced">Advanced</span>
99. [How do you handle Security concurrency issues in embedded systems?](#q99-how-do-you-handle-security-concurrency-issues-in-embedded-systems) <span class="advanced">Advanced</span>
100. [How do you implement Security caching in production environments?](#q100-how-do-you-implement-security-caching-in-production-environments) <span class="intermediate">Intermediate</span>

---

<a id="q1"></a>
### Q1: How do you prevent SQL Injection in a Node.js application using raw SQL?

**Difficulty**: Intermediate


To prevent SQL Injection, **never** concatenate user input directly into SQL query strings. Instead, use **Parameterized Queries** (Prepared Statements).

### Strategy:
1.  **Use Placeholders:** Use `?` (or `$1` in Postgres) placeholders for user input.
2.  **Separate Data from Code:** The database driver sends the query template and data separately, preventing the database from executing input as code.
3.  **Input Validation:** Validate input types (e.g., ensure `id` is an integer) before reaching the database.

### Code Example (using `pg` library for PostgreSQL):

```javascript
const { Pool } = require('pg');
const pool = new Pool();

async function getUserById(userId) {
  // ❌ BAD: Vulnerable to SQL Injection
  // const query = "SELECT * FROM users WHERE id = " + userId;
  
  // ✅ GOOD: Parameterized Query
  const query = 'SELECT * FROM users WHERE id = $1';
  const values = [userId];

  try {
    const res = await pool.query(query, values);
    return res.rows[0];
  } catch (err) {
    console.error('Database error', err);
    throw err;
  }
}

// Usage
getUserById(5).then(user => console.log(user));
// Even if userId is "5; DROP TABLE users;", it is treated as a string literal, not code.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q2"></a>
### Q2: How do you prevent Cross-Site Scripting (XSS) in a React application?

**Difficulty**: Intermediate


React escapes content by default, but XSS is still possible if you use `dangerouslySetInnerHTML` or accept user input in attributes like `href`.

### Strategy:
1.  **Avoid `dangerouslySetInnerHTML`:** Only use it if absolutely necessary and sanitize the content first.
2.  **Sanitize HTML:** Use a library like `dompurify` to strip dangerous tags (e.g., `<script>`) from HTML strings before rendering.
3.  **Validate URL inputs:** Ensure links start with `http://` or `https://` to prevent `javascript:` URI attacks.
4.  **Use Content Security Policy (CSP):** Restrict sources of executable scripts.

### Code Example:

```javascript
import DOMPurify from 'dompurify';

function Comment({ content, userUrl }) {
  // ✅ Sanitize HTML content before rendering
  const cleanContent = DOMPurify.sanitize(content);

  // ✅ Validate URL protocol to prevent javascript: attacks
  const safeUrl = userUrl.match(/^https?:\/\//) ? userUrl : '#';

  return (
    <div className="comment">
      {/* ❌ BAD: <div dangerouslySetInnerHTML={{ __html: content }} /> */}
      
      {/* ✅ GOOD: Sanitized content */}
      <div dangerouslySetInnerHTML={{ __html: cleanContent }} />
      
      <a href={safeUrl}>User Profile</a>
    </div>
  );
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q3"></a>
### Q3: How do you securely store user passwords in a database?

**Difficulty**: Intermediate


**Never** store passwords in plain text. Use a strong, slow hashing algorithm specifically designed for passwords, such as **Argon2**, **bcrypt**, or **scrypt**.

### Strategy:
1.  **Salt:** Generate a unique random salt for each user to prevent Rainbow Table attacks.
2.  **Hash:** Use a slow hashing algorithm (Argon2id is recommended by OWASP).
3.  **Work Factor:** Configure the algorithm to be slow enough to resist brute-force attacks but fast enough for valid logins.

### Code Example (using `argon2`):

```javascript
const argon2 = require('argon2');

async function registerUser(username, plainPassword) {
  try {
    // ✅ Hash the password (salt is generated automatically)
    const hashedPassword = await argon2.hash(plainPassword, {
      type: argon2.argon2id,
      memoryCost: 2 ** 16,
      timeCost: 3,
      parallelism: 1,
    });

    // Store 'username' and 'hashedPassword' in DB
    await db.saveUser(username, hashedPassword);
    console.log('User registered securely');
  } catch (err) {
    console.error('Registration failed', err);
  }
}

async function verifyUser(username, inputPassword) {
  const user = await db.findUser(username);
  
  // ✅ Verify the password against the hash
  const isValid = await argon2.verify(user.passwordHash, inputPassword);
  
  if (isValid) {
    console.log('Login successful');
  } else {
    console.log('Invalid credentials');
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q4"></a>
### Q4: How do you implement Cross-Site Request Forgery (CSRF) protection?

**Difficulty**: Intermediate


CSRF attacks trick a user into executing unwanted actions on a web application where they are authenticated.

### Strategy:
1.  **Anti-CSRF Tokens:** The server sends a unique, random token to the client. The client must include this token in state-changing requests (POST, PUT, DELETE).
2.  **SameSite Cookie Attribute:** Set the `SameSite` attribute on session cookies to `Strict` or `Lax` to prevent the browser from sending cookies with cross-site requests.
3.  **Verify Origin/Referer:** Check standard headers (though these can be spoofed or missing).

### Code Example (Express.js with `csurf` middleware logic):

```javascript
const express = require('express');
const cookieParser = require('cookie-parser');
const csrf = require('csurf'); // Note: csurf is deprecated, use explicit token strategy or similar library

const app = express();
app.use(cookieParser());

// ✅ Setup CSRF protection
const csrfProtection = csrf({ cookie: true });

// Route to get the CSRF token (e.g., for a React form)
app.get('/api/csrf-token', csrfProtection, (req, res) => {
  res.json({ csrfToken: req.csrfToken() });
});

// Protected route
app.post('/api/transfer', csrfProtection, (req, res) => {
  // If token is missing or invalid, this throws 'EBADCSRFTOKEN'
  res.send('Funds transferred securely');
});

// ✅ Alternative: Using SameSite cookies
app.use(session({
  secret: 'secret',
  cookie: {
    httpOnly: true,
    secure: true, // Requires HTTPS
    sameSite: 'Strict' // Prevents CSRF
  }
}));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q5"></a>
### Q5: How do you securely implement JWT authentication?

**Difficulty**: Advanced


JSON Web Tokens (JWT) are often used for stateless authentication.

### Strategy:
1.  **Signature:** Always verify the signature using a secret key (HS256) or private key (RS256).
2.  **Storage:** Store tokens securely.
    *   **Access Token:** Short-lived (e.g., 15 min). Ideally stored in memory (JS variable) or `HttpOnly` cookie.
    *   **Refresh Token:** Long-lived. Store in an `HttpOnly`, `Secure`, `SameSite=Strict` cookie.
3.  **Algorithm:** Enforce strong algorithms; do not allow `None` algorithm.
4.  **Expiration:** Always set an expiration (`exp`) claim.

### Code Example:

```javascript
const jwt = require('jsonwebtoken');

// ✅ Sign a token
function generateAccessToken(user) {
  return jwt.sign({ id: user.id, role: user.role }, process.env.ACCESS_TOKEN_SECRET, {
    expiresIn: '15m', // Short expiration
    algorithm: 'HS256'
  });
}

// ✅ Verify a token middleware
function authenticateToken(req, res, next) {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1]; // Bearer TOKEN

  if (!token) return res.sendStatus(401);

  jwt.verify(token, process.env.ACCESS_TOKEN_SECRET, (err, user) => {
    if (err) return res.sendStatus(403); // Invalid or expired
    req.user = user;
    next();
  });
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q6"></a>
### Q6: How do you implement Rate Limiting to prevent DoS and Brute-Force attacks?

**Difficulty**: Intermediate


Rate limiting restricts the number of requests a user/IP can make in a given timeframe.

### Strategy:
1.  **Identify Client:** Use IP address or User ID (if logged in).
2.  **Store Counters:** Use a fast, in-memory store like Redis to track request counts.
3.  **Middleware:** Reject requests that exceed the limit with `429 Too Many Requests`.

### Code Example (using `express-rate-limit`):

```javascript
const rateLimit = require('express-rate-limit');

// ✅ General limiter for all routes
const apiLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // Limit each IP to 100 requests per windowMs
  message: 'Too many requests from this IP, please try again later.',
  standardHeaders: true, // Return rate limit info in the `RateLimit-*` headers
  legacyHeaders: false, // Disable the `X-RateLimit-*` headers
});

// ✅ Stricter limiter for login (Brute-force protection)
const loginLimiter = rateLimit({
  windowMs: 60 * 60 * 1000, // 1 hour
  max: 5, // Limit each IP to 5 login attempts per hour
  message: 'Too many login attempts, please try again later.'
});

app.use('/api/', apiLimiter);
app.post('/api/login', loginLimiter, loginHandler);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q7"></a>
### Q7: How do you secure HTTP headers using Helmet?

**Difficulty**: Beginner


HTTP headers can provide significant security improvements by enabling browser protections.

### Strategy:
1.  **HSTS (Strict-Transport-Security):** Enforce HTTPS.
2.  **X-Frame-Options:** Prevent clickjacking.
3.  **X-Content-Type-Options:** Prevent MIME sniffing.
4.  **CSP (Content-Security-Policy):** Control resources the user agent is allowed to load.

### Code Example (Express with `helmet`):

```javascript
const express = require('express');
const helmet = require('helmet');

const app = express();

// ✅ Use Helmet to set secure headers
app.use(helmet());

// Customizing CSP
app.use(
  helmet.contentSecurityPolicy({
    directives: {
      defaultSrc: ["'self'"],
      scriptSrc: ["'self'", "trusted-scripts.com"],
      objectSrc: ["'none'"],
      upgradeInsecureRequests: [],
    },
  })
);

app.get('/', (req, res) => {
  res.send('Secure headers set!');
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q8"></a>
### Q8: How do you prevent Server-Side Request Forgery (SSRF)?

**Difficulty**: Advanced


SSRF occurs when an attacker can make the server send requests to unintended locations (e.g., internal networks, AWS metadata service).

### Strategy:
1.  **Input Validation:** Validate URL schemes (allow only `http`/`https`) and domains.
2.  **Allowlist:** Only allow requests to known, trusted domains.
3.  **Block Private IP Ranges:** Prevent the server from connecting to `localhost`, `127.0.0.1`, `192.168.x.x`, `10.x.x.x`, or cloud metadata IPs (`169.254.169.254`).
4.  **Network Segmentation:** Run the application in a restricted network environment.

### Code Example (Validating URL):

```javascript
const ip = require('ip');
const { URL } = require('url');

function fetchExternalUrl(userUrl) {
  try {
    const parsedUrl = new URL(userUrl);

    // ✅ 1. Check Protocol
    if (!['http:', 'https:'].includes(parsedUrl.protocol)) {
      throw new Error('Invalid protocol');
    }

    // ✅ 2. Resolve DNS and check IP
    // (Simplified: In production, use a library like 'ssrf-agent' to handle DNS rebinding attacks)
    if (ip.isPrivate(parsedUrl.hostname)) {
      throw new Error('Access to private network denied');
    }

    // Proceed with request
    // axios.get(userUrl)...

  } catch (err) {
    console.error('SSRF Attempt blocked:', err.message);
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q9"></a>
### Q9: How do you fix Insecure Direct Object References (IDOR)?

**Difficulty**: Intermediate


IDOR happens when an application exposes a reference to an internal implementation object (like a file or database key) without access control.

### Strategy:
1.  **Access Control Checks:** Always check if the logged-in user has permission to access the requested resource ID.
2.  **Indirect References:** Use random UUIDs or mapped tokens instead of sequential database IDs (1, 2, 3...) to make guessing harder (though this is security through obscurity; access control is the real fix).

### Code Example:

```javascript
// ❌ BAD: No check
app.get('/invoices/:id', async (req, res) => {
  const invoice = await db.getInvoice(req.params.id);
  res.json(invoice);
});

// ✅ GOOD: Authorization Check
app.get('/invoices/:id', async (req, res) => {
  const invoice = await db.getInvoice(req.params.id);

  if (!invoice) return res.status(404).send('Not Found');

  // Check if the invoice belongs to the current user
  if (invoice.userId !== req.user.id) {
    return res.status(403).send('Forbidden');
  }

  res.json(invoice);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q10"></a>
### Q10: How do you securely handle file uploads?

**Difficulty**: Intermediate


File uploads can be a vector for malware, shell scripts, or disk exhaustion.

### Strategy:
1.  **Validate File Type:** Check the "Magic Numbers" (file signature), not just the extension or MIME type sent by the client.
2.  **Rename Files:** Generate a new random filename to prevent overwriting or directory traversal attacks.
3.  **Storage:** Store uploaded files outside the web root or on a separate cloud storage (S3).
4.  **Size Limit:** Enforce strict file size limits.
5.  **Permissions:** Ensure uploaded files are not executable.

### Code Example (using `multer`):

```javascript
const multer = require('multer');
const path = require('path');
const { v4: uuidv4 } = require('uuid');

const storage = multer.diskStorage({
  destination: './uploads/',
  filename: function (req, file, cb) {
    // ✅ Rename file with UUID
    cb(null, uuidv4() + path.extname(file.originalname));
  }
});

const upload = multer({
  storage: storage,
  limits: { fileSize: 1000000 }, // ✅ Limit 1MB
  fileFilter: function (req, file, cb) {
    // ✅ Validate type (Extension check is weak, magic number check is better)
    const filetypes = /jpeg|jpg|png|gif/;
    const mimetype = filetypes.test(file.mimetype);
    const extname = filetypes.test(path.extname(file.originalname).toLowerCase());

    if (mimetype && extname) {
      return cb(null, true);
    }
    cb(new Error('Error: Images Only!'));
  }
}).single('myImage');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q11"></a>
### Q11: How do you manage secrets and environment variables securely?

**Difficulty**: Beginner


Secrets (API keys, DB passwords) should never be hardcoded in source control.

### Strategy:
1.  **Environment Variables:** Store secrets in environment variables (`.env` file for local dev, platform config for production).
2.  **Gitignore:** Add `.env` to `.gitignore`.
3.  **Secret Managers:** Use tools like AWS Secrets Manager or HashiCorp Vault for enterprise rotation and management.

### Code Example:

```javascript
// .env file
// DB_PASSWORD=supersecret

// app.js
require('dotenv').config(); // Load .env file

const dbConfig = {
  host: 'localhost',
  user: 'admin',
  // ✅ Access secret via process.env
  password: process.env.DB_PASSWORD 
};

if (!process.env.DB_PASSWORD) {
  console.error('Missing DB_PASSWORD!');
  process.exit(1);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q12"></a>
### Q12: How do you prevent XML External Entity (XXE) attacks?

**Difficulty**: Advanced


XXE attacks exploit XML parsers that parse external entities, allowing attackers to read local files or perform SSRF.

### Strategy:
1.  **Disable DTDs:** Configure the XML parser to disable Document Type Definitions (DTDs) and external entities.
2.  **Use JSON:** Prefer JSON over XML for APIs if possible.

### Code Example (using `libxmljs`):

```javascript
const libxmljs = require('libxmljs');

function parseXML(xmlString) {
  try {
    // ✅ Disable external entities and DTDs
    const doc = libxmljs.parseXml(xmlString, {
      noent: false,  // Do not substitute entities
      dtdload: false, // Do not load external DTDs
      dtdvalid: false // Do not validate DTD
    });
    return doc;
  } catch (e) {
    console.error('XML Parsing Error');
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q13"></a>
### Q13: How do you prevent Clickjacking?

**Difficulty**: Beginner


Clickjacking uses transparent iframes to trick users into clicking on something different from what they see.

### Strategy:
1.  **X-Frame-Options:** Set this header to `DENY` or `SAMEORIGIN`.
2.  **CSP frame-ancestors:** A modern replacement for X-Frame-Options.

### Code Example (Express with Helmet):

```javascript
// Helmet sets X-Frame-Options: SAMEORIGIN by default
app.use(helmet());

// Or manually:
app.use((req, res, next) => {
  // ✅ Deny embedding in frames
  res.setHeader('X-Frame-Options', 'DENY');
  
  // ✅ CSP method
  res.setHeader('Content-Security-Policy', "frame-ancestors 'none'");
  
  next();
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q14"></a>
### Q14: How do you implement secure Open Redirect protection?

**Difficulty**: Intermediate


Open Redirect vulnerabilities allow attackers to redirect users to malicious sites using your domain's credibility (e.g., `example.com/login?redirect=http://evil.com`).

### Strategy:
1.  **Validate Target:** Ensure the redirect URL is relative (starts with `/` but not `//`) or matches a specific allowlist of domains.
2.  **Force Local Redirect:** Strip the domain part and only use the path.

### Code Example:

```javascript
app.get('/login', (req, res) => {
  const redirectTo = req.query.redirect || '/dashboard';

  // ❌ BAD: res.redirect(redirectTo);

  // ✅ GOOD: Validate URL
  try {
    const url = new URL(redirectTo, 'http://mysite.com'); // Base for relative checking
    
    // Only allow relative paths or specific trusted domains
    if (url.origin !== 'http://mysite.com') {
      return res.redirect('/dashboard');
    }
    
    res.redirect(url.pathname + url.search);
  } catch (e) {
    res.redirect('/dashboard');
  }
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q15"></a>
### Q15: How do you implement Role-Based Access Control (RBAC)?

**Difficulty**: Intermediate


RBAC restricts access based on user roles (e.g., Admin, Editor, Viewer).

### Strategy:
1.  **Define Roles & Permissions:** Map roles to specific actions.
2.  **Middleware:** Check if the authenticated user's role allows the requested action.

### Code Example:

```javascript
const roles = {
  admin: ['read', 'write', 'delete'],
  editor: ['read', 'write'],
  viewer: ['read']
};

function authorize(requiredPermission) {
  return (req, res, next) => {
    const userRole = req.user.role; // Assumes user is authenticated
    const permissions = roles[userRole];

    if (permissions && permissions.includes(requiredPermission)) {
      // ✅ User has permission
      next();
    } else {
      // ❌ Access denied
      res.status(403).json({ message: 'Forbidden' });
    }
  };
}

// Usage
app.delete('/api/posts/:id', authenticate, authorize('delete'), deletePostHandler);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q16"></a>
### Q16: How do you implement Multi-Factor Authentication (MFA) using TOTP?

**Difficulty**: Intermediate

**Strategy:**
Use a library like `speakeasy` or `otplib`. Generate a secret, show a QR code to the user, and verify the token they provide.

**Code Example:**
const speakeasy = require('speakeasy');

// Generate secret
const secret = speakeasy.generateSecret();

// Verify token
const verified = speakeasy.totp.verify({
  secret: secret.base32,
  encoding: 'base32',
  token: userProvidedToken
});

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q17"></a>
### Q17: How do you prevent Query Depth attacks in GraphQL?

**Difficulty**: Intermediate

**Strategy:**
Use `graphql-depth-limit` middleware to reject queries that are too deep (nested).

**Code Example:**
const depthLimit = require('graphql-depth-limit');

app.use('/graphql', graphqlHTTP({
  schema,
  validationRules: [depthLimit(5)] // Max depth 5
}));

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q18"></a>
### Q18: How do you prevent Regular Expression Denial of Service (ReDoS)?

**Difficulty**: Advanced

**Strategy:**
Avoid nested quantifiers (e.g., `(a+)+`). Use libraries like `safe-regex` to detect vulnerable patterns or set a timeout for regex execution.

**Code Example:**
// Vulnerable: /(a+)+$/
// Safe: Use 're2' or simple string methods if possible.
// Timeout approach:
const match = await runRegexWithTimeout(/pattern/, input, 100);

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q19"></a>
### Q19: How do you properly configure Session Cookies?

**Difficulty**: Beginner

**Strategy:**
Set `HttpOnly` (prevent JS access), `Secure` (HTTPS only), and `SameSite` (prevent CSRF).

**Code Example:**
res.cookie('session_id', '123', {
  httpOnly: true,
  secure: true,
  sameSite: 'Strict',
  maxAge: 3600000
});

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q20"></a>
### Q20: How do you use Nonces with Content Security Policy (CSP)?

**Difficulty**: Advanced

**Strategy:**
Generate a random nonce per request. Add it to the CSP header and to authorized `<script>` tags. This allows inline scripts only if they have the correct nonce.

**Code Example:**
// Server
res.setHeader('Content-Security-Policy', `script-src 'nonce-${nonce}'`);

// HTML
<script nonce="${nonce}">...</script>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q21"></a>
### Q21: How do you secure WebSocket connections?

**Difficulty**: Intermediate

**Strategy:**
Use `wss://` (encrypted). Validate the `Origin` header during the handshake. Authenticate using a token (e.g., in query param or initial message).

**Code Example:**
wss.on('connection', (ws, req) => {
  if (req.headers.origin !== 'https://trusted.com') {
    ws.close();
  }
});

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q22"></a>
### Q22: How do you prevent Session Fixation?

**Difficulty**: Intermediate

**Strategy:**
Regenerate the Session ID immediately after a user logs in. This ensures they don't use a session ID known to an attacker.

**Code Example:**
req.session.regenerate((err) => {
  // Session ID is now new
  req.session.user = user;
});

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q23"></a>
### Q23: How do you implement Account Lockout securely?

**Difficulty**: Intermediate

**Strategy:**
Track failed attempts. Lock account after N failures for a duration. Use exponential backoff. Don't reveal if the username exists.

**Code Example:**
if (attempts > 5) {
  throw new Error('Account locked. Try again in 15 minutes.');
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q24"></a>
### Q24: How do you prevent Supply Chain Attacks in Node.js?

**Difficulty**: Intermediate

**Strategy:**
Use `npm audit` or `snyk`. Commit `package-lock.json`. Pin dependencies. Review updates.

**Code Example:**
npm audit fix
# Use 'npm ci' for clean installs

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q25"></a>
### Q25: How do you implement Field-Level Encryption?

**Difficulty**: Advanced

**Strategy:**
Encrypt sensitive fields (like SSN) in the application before saving to DB. Decrypt only when needed.

**Code Example:**
const cipher = crypto.createCipheriv('aes-256-gcm', key, iv);
let encrypted = cipher.update(ssn, 'utf8', 'hex');
encrypted += cipher.final('hex');

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q26"></a>
### Q26: What is Perfect Forward Secrecy (PFS)?

**Difficulty**: Advanced

**Strategy:**
Ensures that if a private key is compromised, past sessions remain secure. Use ephemeral key exchange algorithms like ECDHE (Elliptic Curve Diffie-Hellman Ephemeral).

**Code Example:**
// Configure Web Server (Nginx)
ssl_ciphers 'ECDHE-RSA-AES256-GCM-SHA384:...';

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q27"></a>
### Q27: How do you implement mTLS (Mutual TLS)?

**Difficulty**: Advanced

**Strategy:**
Both client and server verify each other's certificates. Configure the server to request a client certificate and validate it against a CA.

**Code Example:**
const options = {
  key: fs.readFileSync('server-key.pem'),
  cert: fs.readFileSync('server-crt.pem'),
  ca: fs.readFileSync('ca-crt.pem'),
  requestCert: true,
  rejectUnauthorized: true
};

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q28"></a>
### Q28: How do you validate an OIDC ID Token?

**Difficulty**: Intermediate

**Strategy:**
Verify the signature (JWT), issuer (`iss`), audience (`aud`), and expiration (`exp`).

**Code Example:**
const ticket = await client.verifyIdToken({
  idToken: token,
  audience: CLIENT_ID
});

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q29"></a>
### Q29: How do you prevent HTTP Parameter Pollution (HPP)?

**Difficulty**: Intermediate

**Strategy:**
Use middleware like `hpp` to ignore or consolidate duplicate query parameters (e.g., `?id=1&id=2`).

**Code Example:**
const hpp = require('hpp');
app.use(hpp());

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q30"></a>
### Q30: How do you secure Serverless Functions (Least Privilege)?

**Difficulty**: Intermediate

**Strategy:**
Assign IAM roles with only necessary permissions. Avoid wildcard (`*`) permissions.

**Code Example:**
{
  "Effect": "Allow",
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::my-bucket/*"
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q31"></a>
### Q31: What is Zero Trust Architecture?

**Difficulty**: Advanced

**Strategy:**
Never trust, always verify. Authenticate and authorize every request, regardless of origin (internal vs external network). Use mTLS for service-to-service communication.

**Code Example:**
```javascript
// Service A calling Service B
const certs = {
  key: fs.readFileSync('service-a-key.pem'),
  cert: fs.readFileSync('service-a-cert.pem'),
  ca: fs.readFileSync('ca-crt.pem')
};

// Service B verifies Service A's certificate
const server = https.createServer({ ...certs, requestCert: true, rejectUnauthorized: true }, (req, res) => {
  const cert = req.socket.getPeerCertificate();
  if (req.client.authorized) {
    res.end(`Hello ${cert.subject.CN}, you are authorized.`);
  } else {
    res.statusCode = 401;
    res.end('Unauthorized');
  }
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q32"></a>
### Q32: How do you automate Key Rotation?

**Difficulty**: Advanced

**Strategy:**
Use a KMS (Key Management Service) with automatic rotation enabled. Ensure apps fetch the latest key version dynamically or use an alias that points to the current key.

**Code Example:**
```javascript
const { KMSClient, EncryptCommand } = require("@aws-sdk/client-kms");
const client = new KMSClient({ region: "us-west-2" });

async function encryptData(data) {
  // Always uses the current backing key for the alias
  const command = new EncryptCommand({
    KeyId: "alias/my-key-alias", 
    Plaintext: Buffer.from(data)
  });
  const response = await client.send(command);
  return response.CiphertextBlob;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q33"></a>
### Q33: How do you detect secrets in code commits?

**Difficulty**: Intermediate

**Strategy:**
Use tools like `git-secrets`, `trufflehog`, or GitHub Secret Scanning as a pre-commit hook or CI step.

**Code Example:**
```bash
# Install git-secrets
brew install git-secrets

# Register AWS patterns
git secrets --register-aws

# Scan repo
git secrets --scan

# Pre-commit hook is installed automatically to prevent committing secrets
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q34"></a>
### Q34: How do you prevent LDAP Injection?

**Difficulty**: Intermediate

**Strategy:**
Sanitize input used in LDAP filters. Escape special characters like `(`, `)`, `*`, `\`, `NUL`.

**Code Example:**
```javascript
function escapeLDAP(input) {
  return input.replace(/[ \(\)\*\]/g, (char) => {
    switch (char) {
      case '(': return '\28';
      case ')': return '\29';
      case '*': return '\2a';
      case '\': return '\5c';
      case ' ': return '\00';
      default: return char;
    }
  });
}

const safeUser = escapeLDAP(userInput);
const filter = `(uid=${safeUser})`;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q35"></a>
### Q35: What are `Referrer-Policy` and `Permissions-Policy`?

**Difficulty**: Intermediate

**Strategy:**
- `Referrer-Policy`: Controls how much referrer info is sent (`no-referrer`, `strict-origin`).
- `Permissions-Policy`: Controls browser features (camera, geolocation) to reduce attack surface.

**Code Example:**
```http
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), geolocation=(), microphone=()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q36"></a>
### Q36: How do you run Docker in Rootless Mode?

**Difficulty**: Intermediate

**Strategy:**
Install Docker Rootless. It runs the daemon and containers as a non-root user, mitigating container breakout attacks.

**Code Example:**
```bash
# Install
dockerd-rootless-setuptool.sh install

# Export DOCKER_HOST
export DOCKER_HOST=unix:///run/user/1000/docker.sock

# Run container (runs as user 1000 on host)
docker run -d -p 8080:80 nginx
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q37"></a>
### Q37: Why use PKCE in OAuth 2.0?

**Difficulty**: Advanced

**Strategy:**
It prevents authorization code interception attacks on public clients (mobile/SPA) by requiring a `code_verifier` during the token exchange.

**Code Example:**
```javascript
// 1. Generate Code Verifier
const verifier = base64URLEncode(crypto.randomBytes(32));

// 2. Generate Code Challenge
const challenge = base64URLEncode(sha256(verifier));

// 3. Send Challenge in Auth Request
// GET /authorize?response_type=code&code_challenge=challenge&code_challenge_method=S256

// 4. Send Verifier in Token Request
// POST /token (code, code_verifier=verifier)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q38"></a>
### Q38: How do you handle PII (Personally Identifiable Information)?

**Difficulty**: Intermediate

**Strategy:**
Minimize collection. Encrypt at rest (DB). Encrypt in transit. Mask in logs. Implement data retention policies.

**Code Example:**
```javascript
function logUserAction(user, action) {
  const maskedEmail = user.email.replace(/(^.{2}).+(@.+)/, '$1***$2');
  logger.info(`User ${maskedEmail} performed ${action}`);
}

// Output: User jo***@example.com performed login
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q39"></a>
### Q39: How do you secure API Keys in Mobile Apps?

**Difficulty**: Intermediate

**Strategy:**
Don't store them in the app. Use a proxy server (Backend-for-Frontend) to hold the keys and forward requests. Use App Attestation to verify the request comes from your genuine app.

**Code Example:**
```javascript
// Mobile App -> Calls YOUR Backend (Authenticated)
await fetch('https://api.myapp.com/weather');

// Your Backend -> Calls 3rd Party API (Injects Key)
app.get('/weather', (req, res) => {
  const apiKey = process.env.WEATHER_API_KEY;
  const data = await fetch(`https://weather.com/api?key=${apiKey}`);
  res.json(data);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q40"></a>
### Q40: How do you prevent Man-in-the-Middle (MitM) attacks?

**Difficulty**: Beginner

**Strategy:**
Use HTTPS everywhere. Use HSTS. Validate certificates properly (don't disable SSL verification). Use Certificate Pinning (for mobile apps).

**Code Example:**
```javascript
// ❌ BAD: Disabling SSL verification
process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0'; 

// ✅ GOOD: Default behavior verifies CA chain.
// For Certificate Pinning in Node.js:
const agent = new https.Agent({
  ca: fs.readFileSync('expected-cert.pem') // Only trust this cert/CA
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q41"></a>
### Q41: How do you prevent Timing Attacks?

**Difficulty**: Advanced

**Strategy:**
Use constant-time comparison functions for secrets (hashes, tokens). Regular string comparison returns early on mismatch, leaking length/content info.

**Code Example:**
```javascript
const crypto = require('crypto');

function checkToken(userToken, secretToken) {
  const buf1 = Buffer.from(userToken);
  const buf2 = Buffer.from(secretToken);
  
  if (buf1.length !== buf2.length) return false; // Leak length (acceptable trade-off sometimes)
  
  // ✅ Constant-time comparison
  return crypto.timingSafeEqual(buf1, buf2);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q42"></a>
### Q42: How do you secure Audit Logs?

**Difficulty**: Advanced

**Strategy:**
Write logs to a Write-Once-Read-Many (WORM) storage (e.g., S3 Object Lock). Use HMAC chaining to detect tampering.

**Code Example:**
```javascript
// Conceptual HMAC Chaining
let previousHash = '0000';

function writeLog(entry) {
  const logEntry = {
    ...entry,
    prevHash: previousHash,
    timestamp: Date.now()
  };
  
  const currentHash = crypto.createHmac('sha256', secret)
                            .update(JSON.stringify(logEntry))
                            .digest('hex');
                            
  previousHash = currentHash;
  db.saveLog(logEntry, currentHash);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q43"></a>
### Q43: How do you implement a secure Password Reset flow?

**Difficulty**: Intermediate

**Strategy:**
Generate a cryptographically strong random token. Store hash of token with expiration. Send link. Verify token hash. Don't reuse tokens.

**Code Example:**
```javascript
// 1. Generate
const token = crypto.randomBytes(32).toString('hex');
const hash = await argon2.hash(token);

// 2. Store
await db.saveResetToken(userId, hash, Date.now() + 3600000); // 1 hr expiry

// 3. Send Link
sendEmail(user.email, `https://app.com/reset?token=${token}`);

// 4. Verify
const isValid = await argon2.verify(storedHash, inputToken);
if (isValid && !isExpired) { /* Allow reset */ }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q44"></a>
### Q44: How do you secure gRPC services?

**Difficulty**: Advanced

**Strategy:**
Use TLS for transport security. Use Call Credentials (tokens) for authentication. Use Interceptors for authorization.

**Code Example:**
```javascript
// Server
const server = new grpc.Server();
const credentials = grpc.ServerCredentials.createSsl(
  fs.readFileSync('ca.crt'), 
  [{
    private_key: fs.readFileSync('server.key'),
    cert_chain: fs.readFileSync('server.crt')
  }], 
  true // Request client cert (mTLS)
);
server.bindAsync('0.0.0.0:50051', credentials, () => server.start());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q45"></a>
### Q45: How do you configure CORS securely?

**Difficulty**: Beginner

**Strategy:**
Avoid `Access-Control-Allow-Origin: *` if auth is involved. Allow specific origins. Handle preflight requests (`OPTIONS`).

**Code Example:**
```javascript
const cors = require('cors');

const corsOptions = {
  origin: (origin, callback) => {
    const allowedOrigins = ['https://myapp.com', 'https://admin.myapp.com'];
    if (allowedOrigins.indexOf(origin) !== -1 || !origin) {
      callback(null, true);
    } else {
      callback(new Error('Not allowed by CORS'));
    }
  },
  credentials: true // Allow cookies
};

app.use(cors(corsOptions));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q46"></a>
### Q46: What is Subresource Integrity (SRI)?

**Difficulty**: Beginner

**Strategy:**
Ensures that files fetched from CDNs haven't been modified. Use the `integrity` attribute with a hash.

**Code Example:**
```html
<!-- Generate hash: openssl dgst -sha384 -binary lib.js | openssl base64 -A -->
<script 
  src="https://cdn.example.com/library.js"
  integrity="sha384-Li9vy3DqF8tnTXuiaAJuML3ky+er10rcgNR/VqsVpcw+ThHmYcwiB1pbOxEbzJr7"
  crossorigin="anonymous">
</script>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q47"></a>
### Q47: How do you prevent Host Header Injection?

**Difficulty**: Intermediate

**Strategy:**
Validate the `Host` header against a whitelist of allowed domains. Configure the web server to drop requests with unknown hosts.

**Code Example:**
```nginx
# Nginx Configuration
server {
  listen 80;
  server_name example.com; # Only accept this host
  
  # Default catch-all for unknown hosts
}

server {
  listen 80 default_server;
  return 444; # Drop connection
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q48"></a>
### Q48: How do you prevent Directory Traversal?

**Difficulty**: Intermediate

**Strategy:**
Normalize paths using `path.normalize`. Ensure the resolved path starts with the expected root directory.

**Code Example:**
```javascript
const path = require('path');
const baseDir = path.resolve('/var/www/uploads');

app.get('/file', (req, res) => {
  const filename = req.query.name;
  const fullPath = path.join(baseDir, filename);
  const normalizedPath = path.normalize(fullPath);

  // ✅ Ensure we are still inside baseDir
  if (!normalizedPath.startsWith(baseDir)) {
    return res.status(403).send('Access Denied');
  }

  res.sendFile(normalizedPath);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q49"></a>
### Q49: How do you prevent Deserialization vulnerabilities?

**Difficulty**: Advanced

**Strategy:**
Avoid deserializing untrusted data (e.g., Java `ObjectInputStream`, Python `pickle`). Use safe formats like JSON. If serialization is needed, sign the data.

**Code Example:**
```javascript
// ❌ BAD: Using 'node-serialize' on user input
// const obj = serialize.unserialize(req.body.data);

// ✅ GOOD: Use JSON.parse
try {
  const obj = JSON.parse(req.body.data);
  // Validate structure
} catch (e) {
  // Handle error
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q50"></a>
### Q50: How do you implement 'Defense in Depth'?

**Difficulty**: Advanced

**Strategy:**
Layer multiple security controls. If one fails, others protect the system.
1.  **Network:** WAF, VPC, Private Subnets.
2.  **App:** Input Validation, Authentication, Authorization.
3.  **Data:** Encryption at rest/transit, Backups.
4.  **Monitoring:** Audit logs, Alerts.

**Code Example:**
```javascript
// Example of layered defense for an API endpoint:
app.post('/transfer',
  rateLimiter,          // Layer 1: Availability
  authenticateToken,    // Layer 2: Identity
  authorizeRole('user'),// Layer 3: Access Control
  validateInput,        // Layer 4: Integrity
  async (req, res) => {
    // Layer 5: Logic & Data Security
    await db.transaction(async (trx) => {
      // ...
    });
  }
);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q51"></a>
### Q51: How do you handle Security state management in large scale applications?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```javascript
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q52"></a>
### Q52: How do you perform Security data validation in microservices?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```javascript
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q53"></a>
### Q53: How do you automate Security deployment for mobile devices?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q54"></a>
### Q54: How do you handle Security concurrency issues in legacy systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q55"></a>
### Q55: How do you implement Security caching in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q56"></a>
### Q56: How do you manage Security configuration for real-time systems?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q57"></a>
### Q57: How do you handle Security internationalization (i18n) in distributed systems?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```javascript
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q58"></a>
### Q58: How do you ensure Security accessibility (a11y) in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q59"></a>
### Q59: How do you optimize Security network requests in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q60"></a>
### Q60: How do you handle Security performance optimization for production environments?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```javascript
const start = performance.now();
// Security logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q61"></a>
### Q61: What are the security implications of Security in large scale applications?

**Difficulty**: Intermediate

**Strategy**:
Validate all inputs. Sanitize data. Use least privilege principle.

**Code Example**:
```javascript
// Sanitize input
const clean = input.replace(/<script>/g, '');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q62"></a>
### Q62: How do you debug Security memory leaks in microservices?

**Difficulty**: Advanced

**Strategy**:
Use heap snapshots and look for detached DOM nodes or uncleared listeners.

**Code Example**:
```javascript
// Check listeners
process.on('exit', () => cleanup());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q63"></a>
### Q63: Best practices for Security code organization in mobile devices?

**Difficulty**: Beginner

**Strategy**:
Follow SOLID principles. Keep functions small and focused.

**Code Example**:
```javascript
// Single responsibility
function doOneThing() { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q64"></a>
### Q64: How do you implement Security error handling for legacy systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```javascript
try {
  await SecurityOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q65"></a>
### Q65: How do you test Security functionality in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```javascript
test('Security works', () => {
  expect(Security()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q66"></a>
### Q66: How do you handle Security state management in real-time systems?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```javascript
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q67"></a>
### Q67: How do you perform Security data validation in distributed systems?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```javascript
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q68"></a>
### Q68: How do you automate Security deployment for high-traffic sites?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q69"></a>
### Q69: How do you handle Security concurrency issues in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q70"></a>
### Q70: How do you implement Security caching in production environments?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q71"></a>
### Q71: How do you manage Security configuration for large scale applications?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q72"></a>
### Q72: How do you handle Security internationalization (i18n) in microservices?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```javascript
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q73"></a>
### Q73: How do you ensure Security accessibility (a11y) in mobile devices?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q74"></a>
### Q74: How do you optimize Security network requests in legacy systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q75"></a>
### Q75: How do you handle Security performance optimization for cloud infrastructure?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```javascript
const start = performance.now();
// Security logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q76"></a>
### Q76: What are the security implications of Security in real-time systems?

**Difficulty**: Intermediate

**Strategy**:
Validate all inputs. Sanitize data. Use least privilege principle.

**Code Example**:
```javascript
// Sanitize input
const clean = input.replace(/<script>/g, '');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q77"></a>
### Q77: How do you debug Security memory leaks in distributed systems?

**Difficulty**: Advanced

**Strategy**:
Use heap snapshots and look for detached DOM nodes or uncleared listeners.

**Code Example**:
```javascript
// Check listeners
process.on('exit', () => cleanup());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q78"></a>
### Q78: Best practices for Security code organization in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Follow SOLID principles. Keep functions small and focused.

**Code Example**:
```javascript
// Single responsibility
function doOneThing() { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q79"></a>
### Q79: How do you implement Security error handling for embedded systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```javascript
try {
  await SecurityOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q80"></a>
### Q80: How do you test Security functionality in production environments?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```javascript
test('Security works', () => {
  expect(Security()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q81"></a>
### Q81: How do you handle Security state management in large scale applications?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```javascript
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q82"></a>
### Q82: How do you perform Security data validation in microservices?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```javascript
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q83"></a>
### Q83: How do you automate Security deployment for mobile devices?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q84"></a>
### Q84: How do you handle Security concurrency issues in legacy systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q85"></a>
### Q85: How do you implement Security caching in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q86"></a>
### Q86: How do you manage Security configuration for real-time systems?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q87"></a>
### Q87: How do you handle Security internationalization (i18n) in distributed systems?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```javascript
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q88"></a>
### Q88: How do you ensure Security accessibility (a11y) in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q89"></a>
### Q89: How do you optimize Security network requests in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q90"></a>
### Q90: How do you handle Security performance optimization for production environments?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```javascript
const start = performance.now();
// Security logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q91"></a>
### Q91: What are the security implications of Security in large scale applications?

**Difficulty**: Intermediate

**Strategy**:
Validate all inputs. Sanitize data. Use least privilege principle.

**Code Example**:
```javascript
// Sanitize input
const clean = input.replace(/<script>/g, '');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q92"></a>
### Q92: How do you debug Security memory leaks in microservices?

**Difficulty**: Advanced

**Strategy**:
Use heap snapshots and look for detached DOM nodes or uncleared listeners.

**Code Example**:
```javascript
// Check listeners
process.on('exit', () => cleanup());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q93"></a>
### Q93: Best practices for Security code organization in mobile devices?

**Difficulty**: Beginner

**Strategy**:
Follow SOLID principles. Keep functions small and focused.

**Code Example**:
```javascript
// Single responsibility
function doOneThing() { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q94"></a>
### Q94: How do you implement Security error handling for legacy systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```javascript
try {
  await SecurityOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q95"></a>
### Q95: How do you test Security functionality in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```javascript
test('Security works', () => {
  expect(Security()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q96"></a>
### Q96: How do you handle Security state management in real-time systems?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```javascript
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q97"></a>
### Q97: How do you perform Security data validation in distributed systems?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```javascript
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q98"></a>
### Q98: How do you automate Security deployment for high-traffic sites?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q99"></a>
### Q99: How do you handle Security concurrency issues in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q100"></a>
### Q100: How do you implement Security caching in production environments?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---
