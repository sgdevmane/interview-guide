<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Web security Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [How do you prevent SQL Injection in a Node.js application using raw SQL?](#q1) <span class="intermediate">Intermediate</span>
2. [How do you prevent Cross-Site Scripting (XSS) in a React application?](#q2) <span class="intermediate">Intermediate</span>
3. [How do you securely store user passwords in a database?](#q3) <span class="intermediate">Intermediate</span>
4. [How do you implement Cross-Site Request Forgery (CSRF) protection?](#q4) <span class="intermediate">Intermediate</span>
5. [How do you securely implement JWT authentication?](#q5) <span class="advanced">Advanced</span>
6. [How do you implement Rate Limiting to prevent DoS and Brute-Force attacks?](#q6) <span class="intermediate">Intermediate</span>
7. [How do you secure HTTP headers using Helmet?](#q7) <span class="beginner">Beginner</span>
8. [How do you prevent Server-Side Request Forgery (SSRF)?](#q8) <span class="advanced">Advanced</span>
9. [How do you fix Insecure Direct Object References (IDOR)?](#q9) <span class="intermediate">Intermediate</span>
10. [How do you securely handle file uploads?](#q10) <span class="intermediate">Intermediate</span>
11. [How do you manage secrets and environment variables securely?](#q11) <span class="beginner">Beginner</span>
12. [How do you prevent XML External Entity (XXE) attacks?](#q12) <span class="advanced">Advanced</span>
13. [How do you prevent Clickjacking?](#q13) <span class="beginner">Beginner</span>
14. [How do you implement secure Open Redirect protection?](#q14) <span class="intermediate">Intermediate</span>
15. [How do you implement Role-Based Access Control (RBAC)?](#q15) <span class="intermediate">Intermediate</span>
16. [How do you implement Multi-Factor Authentication (MFA) using TOTP?](#q16) <span class="intermediate">Intermediate</span>
17. [How do you prevent Query Depth attacks in GraphQL?](#q17) <span class="intermediate">Intermediate</span>
18. [How do you prevent Regular Expression Denial of Service (ReDoS)?](#q18) <span class="advanced">Advanced</span>
19. [How do you properly configure Session Cookies?](#q19) <span class="beginner">Beginner</span>
20. [How do you use Nonces with Content Security Policy (CSP)?](#q20) <span class="advanced">Advanced</span>
21. [How do you secure WebSocket connections?](#q21) <span class="intermediate">Intermediate</span>
22. [How do you prevent Session Fixation?](#q22) <span class="intermediate">Intermediate</span>
23. [How do you implement Account Lockout securely?](#q23) <span class="intermediate">Intermediate</span>
24. [How do you prevent Supply Chain Attacks in Node.js?](#q24) <span class="intermediate">Intermediate</span>
25. [How do you implement Field-Level Encryption?](#q25) <span class="advanced">Advanced</span>
26. [What is Perfect Forward Secrecy (PFS)?](#q26) <span class="advanced">Advanced</span>
27. [How do you implement mTLS (Mutual TLS)?](#q27) <span class="advanced">Advanced</span>
28. [How do you validate an OIDC ID Token?](#q28) <span class="intermediate">Intermediate</span>
29. [How do you prevent HTTP Parameter Pollution (HPP)?](#q29) <span class="intermediate">Intermediate</span>
30. [How do you secure Serverless Functions (Least Privilege)?](#q30) <span class="intermediate">Intermediate</span>
31. [What is Zero Trust Architecture?](#q31) <span class="advanced">Advanced</span>
32. [How do you automate Key Rotation?](#q32) <span class="advanced">Advanced</span>
33. [How do you detect secrets in code commits?](#q33) <span class="intermediate">Intermediate</span>
34. [How do you prevent LDAP Injection?](#q34) <span class="intermediate">Intermediate</span>
35. [What are `Referrer-Policy` and `Permissions-Policy`?](#q35) <span class="intermediate">Intermediate</span>
36. [How do you run Docker in Rootless Mode?](#q36) <span class="intermediate">Intermediate</span>
37. [Why use PKCE in OAuth 2.0?](#q37) <span class="advanced">Advanced</span>
38. [How do you handle PII (Personally Identifiable Information)?](#q38) <span class="intermediate">Intermediate</span>
39. [How do you secure API Keys in Mobile Apps?](#q39) <span class="intermediate">Intermediate</span>
40. [How do you prevent Man-in-the-Middle (MitM) attacks?](#q40) <span class="beginner">Beginner</span>
41. [How do you prevent Timing Attacks?](#q41) <span class="advanced">Advanced</span>
42. [How do you secure Audit Logs?](#q42) <span class="advanced">Advanced</span>
43. [How do you implement a secure Password Reset flow?](#q43) <span class="intermediate">Intermediate</span>
44. [How do you secure gRPC services?](#q44) <span class="advanced">Advanced</span>
45. [How do you configure CORS securely?](#q45) <span class="beginner">Beginner</span>
46. [What is Subresource Integrity (SRI)?](#q46) <span class="beginner">Beginner</span>
47. [How do you prevent Host Header Injection?](#q47) <span class="intermediate">Intermediate</span>
48. [How do you prevent Directory Traversal?](#q48) <span class="intermediate">Intermediate</span>
49. [How do you prevent Deserialization vulnerabilities?](#q49) <span class="advanced">Advanced</span>
50. [How do you implement 'Defense in Depth'?](#q50) <span class="advanced">Advanced</span>
51. [What is the `SameSite` cookie attribute?](#q51) <span class="intermediate">Intermediate</span>
52. [How do you prevent Content Sniffing?](#q52) <span class="beginner">Beginner</span>
53. [What is Web Cache Poisoning?](#q53) <span class="advanced">Expert</span>
54. [JWT vs Session IDs: Which is more secure?](#q54) <span class="intermediate">Intermediate</span>
55. [What is the difference between Salting and Peppering?](#q55) <span class="advanced">Advanced</span>
56. [What is HSTS (HTTP Strict Transport Security)?](#q56) <span class="beginner">Beginner</span>
57. [Are "Magic Links" secure?](#q57) <span class="intermediate">Intermediate</span>
58. [How do Race Conditions lead to security vulnerabilities?](#q58) <span class="advanced">Advanced</span>
59. [Why use a CSPRNG over `Math.random()`?](#q59) <span class="beginner">Beginner</span>
60. [How do you prevent Docker Container Breakouts?](#q60) <span class="advanced">Advanced</span>
61. [What is Kubernetes Pod Security?](#q61) <span class="advanced">Advanced</span>
62. [How do you prevent GraphQL Batching Attacks?](#q62) <span class="advanced">Advanced</span>
63. [Why is the `state` parameter important in OAuth2?](#q63) <span class="intermediate">Intermediate</span>
64. [What is an OIDC Claim?](#q64) <span class="intermediate">Intermediate</span>
65. [How do you secure an API Gateway?](#q65) <span class="advanced">Advanced</span>
66. [What is WebAuthn / Passkeys?](#q66) <span class="advanced">Advanced</span>
67. [What is Certificate Pinning?](#q67) <span class="advanced">Expert</span>
68. [What is DNS Rebinding?](#q68) <span class="advanced">Expert</span>
69. [What is a Padding Oracle Attack?](#q69) <span class="advanced">Expert</span>
70. [What is a Dependency Confusion Attack?](#q70) <span class="advanced">Advanced</span>
71. [What tools can detect secrets in code?](#q71) <span class="beginner">Beginner</span>
72. [What is a Secure Code Review Checklist?](#q72) <span class="intermediate">Intermediate</span>
73. [What is STRIDE in Threat Modeling?](#q73) <span class="intermediate">Intermediate</span>
74. [What are the phases of Penetration Testing?](#q74) <span class="intermediate">Intermediate</span>
75. [What is the Incident Response Lifecycle?](#q75) <span class="advanced">Advanced</span>
76. [What is a DevSecOps Pipeline?](#q76) <span class="intermediate">Intermediate</span>
77. [What is the difference between SAST and DAST?](#q77) <span class="intermediate">Intermediate</span>
78. [What is IAST (Interactive Application Security Testing)?](#q78) <span class="advanced">Advanced</span>
79. [What is RASP (Runtime Application Self-Protection)?](#q79) <span class="advanced">Expert</span>
80. [What is Shadow IT and why is it a risk?](#q80) <span class="beginner">Beginner</span>
81. [How do you prevent Social Engineering attacks?](#q81) <span class="beginner">Beginner</span>
82. [Why is Physical Security important for servers?](#q82) <span class="beginner">Beginner</span>
83. [What is the Cloud Shared Responsibility Model?](#q83) <span class="intermediate">Intermediate</span>
84. [Why use IAM Roles instead of IAM Users in AWS?](#q84) <span class="advanced">Advanced</span>
85. [How do you secure an S3 Bucket?](#q85) <span class="intermediate">Intermediate</span>
86. [What are the risks of VPC Peering?](#q86) <span class="advanced">Advanced</span>
87. [What does a WAF (Web Application Firewall) do?](#q87) <span class="intermediate">Intermediate</span>
88. [How do you mitigate DDoS attacks?](#q88) <span class="advanced">Advanced</span>
89. [How do you detect Bot traffic?](#q89) <span class="intermediate">Intermediate</span>
90. [What are the different types of CAPTCHA?](#q90) <span class="beginner">Beginner</span>
91. [What are the risks of Biometric Authentication?](#q91) <span class="advanced">Advanced</span>
92. [What is Privacy by Design?](#q92) <span class="intermediate">Intermediate</span>
93. [What is the GDPR "Right to be Forgotten"?](#q93) <span class="intermediate">Intermediate</span>
94. [What is PCI-DSS?](#q94) <span class="advanced">Advanced</span>
95. [What is HIPAA?](#q95) <span class="advanced">Advanced</span>
96. [What is SOC 2?](#q96) <span class="advanced">Advanced</span>
97. [What is ISO 27001?](#q97) <span class="advanced">Advanced</span>
98. [What are Zero Knowledge Proofs?](#q98) <span class="advanced">Expert</span>
99. [What is Homomorphic Encryption?](#q99) <span class="advanced">Expert</span>
100. [How does Quantum Computing threaten cryptography?](#q100) <span class="advanced">Expert</span>

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
```javascript
const speakeasy = require('speakeasy');

// Generate secret
const secret = speakeasy.generateSecret();

// Verify token
const verified = speakeasy.totp.verify({
  secret: secret.base32,
  encoding: 'base32',
  token: userProvidedToken
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q17"></a>
### Q17: How do you prevent Query Depth attacks in GraphQL?

**Difficulty**: Intermediate

**Strategy:**
Use `graphql-depth-limit` middleware to reject queries that are too deep (nested).

**Code Example:**
```javascript
const depthLimit = require('graphql-depth-limit');

app.use('/graphql', graphqlHTTP({
  schema,
  validationRules: [depthLimit(5)] // Max depth 5
}));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q18"></a>
### Q18: How do you prevent Regular Expression Denial of Service (ReDoS)?

**Difficulty**: Advanced

**Strategy:**
Avoid nested quantifiers (e.g., `(a+)+`). Use libraries like `safe-regex` to detect vulnerable patterns or set a timeout for regex execution.

**Code Example:**
```javascript
// Vulnerable: /(a+)+$/
// Safe: Use 're2' or simple string methods if possible.
// Timeout approach:
const match = await runRegexWithTimeout(/pattern/, input, 100);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q19"></a>
### Q19: How do you properly configure Session Cookies?

**Difficulty**: Beginner

**Strategy:**
Set `HttpOnly` (prevent JS access), `Secure` (HTTPS only), and `SameSite` (prevent CSRF).

**Code Example:**
```javascript
res.cookie('session_id', '123', {
  httpOnly: true,
  secure: true,
  sameSite: 'Strict',
  maxAge: 3600000
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q20"></a>
### Q20: How do you use Nonces with Content Security Policy (CSP)?

**Difficulty**: Advanced

**Strategy:**
Generate a random nonce per request. Add it to the CSP header and to authorized `<script>` tags. This allows inline scripts only if they have the correct nonce.

**Code Example:**
```javascript
// Server
res.setHeader('Content-Security-Policy', `script-src 'nonce-${nonce}'`);

// HTML
// <script nonce="${nonce}">...</script>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q21"></a>
### Q21: How do you secure WebSocket connections?

**Difficulty**: Intermediate

**Strategy:**
Use `wss://` (encrypted). Validate the `Origin` header during the handshake. Authenticate using a token (e.g., in query param or initial message).

**Code Example:**
```javascript
wss.on('connection', (ws, req) => {
  if (req.headers.origin !== 'https://trusted.com') {
    ws.close();
  }
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q22"></a>
### Q22: How do you prevent Session Fixation?

**Difficulty**: Intermediate

**Strategy:**
Regenerate the Session ID immediately after a user logs in. This ensures they don't use a session ID known to an attacker.

**Code Example:**
```javascript
req.session.regenerate((err) => {
  // Session ID is now new
  req.session.user = user;
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q23"></a>
### Q23: How do you implement Account Lockout securely?

**Difficulty**: Intermediate

**Strategy:**
Track failed attempts. Lock account after N failures for a duration. Use exponential backoff. Don't reveal if the username exists.

**Code Example:**
```javascript
if (attempts > 5) {
  throw new Error('Account locked. Try again in 15 minutes.');
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q24"></a>
### Q24: How do you prevent Supply Chain Attacks in Node.js?

**Difficulty**: Intermediate

**Strategy:**
Use `npm audit` or `snyk`. Commit `package-lock.json`. Pin dependencies. Review updates.

**Code Example:**
```bash
npm audit fix
# Use 'npm ci' for clean installs
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q25"></a>
### Q25: How do you implement Field-Level Encryption?

**Difficulty**: Advanced

**Strategy:**
Encrypt sensitive fields (like SSN) in the application before saving to DB. Decrypt only when needed.

**Code Example:**
```javascript
const cipher = crypto.createCipheriv('aes-256-gcm', key, iv);
let encrypted = cipher.update(ssn, 'utf8', 'hex');
encrypted += cipher.final('hex');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q26"></a>
### Q26: What is Perfect Forward Secrecy (PFS)?

**Difficulty**: Advanced

**Strategy:**
Ensures that if a private key is compromised, past sessions remain secure. Use ephemeral key exchange algorithms like ECDHE (Elliptic Curve Diffie-Hellman Ephemeral).

**Code Example:**
```nginx
# Configure Web Server (Nginx)
ssl_ciphers 'ECDHE-RSA-AES256-GCM-SHA384:...';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q27"></a>
### Q27: How do you implement mTLS (Mutual TLS)?

**Difficulty**: Advanced

**Strategy:**
Both client and server verify each other's certificates. Configure the server to request a client certificate and validate it against a CA.

**Code Example:**
```javascript
const options = {
  key: fs.readFileSync('server-key.pem'),
  cert: fs.readFileSync('server-crt.pem'),
  ca: fs.readFileSync('ca-crt.pem'),
  requestCert: true,
  rejectUnauthorized: true
};
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q28"></a>
### Q28: How do you validate an OIDC ID Token?

**Difficulty**: Intermediate

**Strategy:**
Verify the signature (JWT), issuer (`iss`), audience (`aud`), and expiration (`exp`).

**Code Example:**
```javascript
const ticket = await client.verifyIdToken({
  idToken: token,
  audience: CLIENT_ID
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q29"></a>
### Q29: How do you prevent HTTP Parameter Pollution (HPP)?

**Difficulty**: Intermediate

**Strategy:**
Use middleware like `hpp` to ignore or consolidate duplicate query parameters (e.g., `?id=1&id=2`).

**Code Example:**
```javascript
const hpp = require('hpp');
app.use(hpp());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q30"></a>
### Q30: How do you secure Serverless Functions (Least Privilege)?

**Difficulty**: Intermediate

**Strategy:**
Assign IAM roles with only necessary permissions. Avoid wildcard (`*`) permissions.

**Code Example:**
```json
{
  "Effect": "Allow",
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::my-bucket/*"
}
```

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
      case '\\': return '\5c';
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

### Q51: What is the `SameSite` cookie attribute?

**Difficulty**: Intermediate

**Strategy:**
`SameSite` controls whether cookies are sent with cross-site requests. `Strict` prevents all cross-site sending, `Lax` allows it for top-level navigations (links), `None` allows all (requires Secure).

**Code Example:**

```http
Set-Cookie: session_id=xyz; SameSite=Lax; Secure; HttpOnly
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q52"></a>

### Q52: How do you prevent Content Sniffing?

**Difficulty**: Beginner

**Strategy:**
Set the `X-Content-Type-Options: nosniff` header. This forces the browser to strictly follow the MIME type declared in `Content-Type`, preventing executable scripts disguised as images.

**Code Example:**

```javascript
// Express.js with Helmet
app.use(helmet.noSniff());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q53"></a>

### Q53: What is Web Cache Poisoning?

**Difficulty**: Expert

**Strategy:**
An attacker sends a request that causes the server to cache a harmful response (e.g., reflecting an XSS payload) which is then served to other users. Prevent by validating inputs and not keying cache on unverified headers.

**Code Example:**

```text
GET /en?region=<script>alert(1)</script> HTTP/1.1
Host: vulnerable.com

# If server caches this response for /en, all users get XSS.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q54"></a>

### Q54: JWT vs Session IDs: Which is more secure?

**Difficulty**: Intermediate

**Strategy:**
Session IDs (server-side) are generally more secure because they can be instantly revoked. JWTs (stateless) are harder to revoke without blacklisting. Use Session IDs for sensitive apps, JWTs for microservices/APIs.

**Code Example:**

```text
Session ID: Random string stored in HttpOnly cookie.
JWT: Base64 encoded JSON with signature. If stolen, valid until expiry.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q55"></a>

### Q55: What is the difference between Salting and Peppering?

**Difficulty**: Advanced

**Strategy:**
Salt is unique per user and stored with the hash. Pepper is a secret key shared across all hashes and stored separately (e.g., environment variable or HSM). Pepper adds defense in depth if DB is leaked.

**Code Example:**

```python
# Concept
hash = bcrypt(password + salt + pepper)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q56"></a>

### Q56: What is HSTS (HTTP Strict Transport Security)?

**Difficulty**: Beginner

**Strategy:**
A header that tells browsers to *only* access the site via HTTPS for a specified duration. Prevents SSL Stripping attacks.

**Code Example:**

```http
Strict-Transport-Security: max-age=31536000; includeSubDomains
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q57"></a>

### Q57: Are "Magic Links" secure?

**Difficulty**: Intermediate

**Strategy:**
Yes, if implemented correctly: single-use, short expiry (10-15 mins), and invalidates previous tokens. Risk: email compromise gives account access.

**Code Example:**

```text
https://app.com/login?token=random_high_entropy_string
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q58"></a>

### Q58: How do Race Conditions lead to security vulnerabilities?

**Difficulty**: Advanced

**Strategy:**
Time-of-check to time-of-use (TOCTOU) bugs can allow double spending or unauthorized access. Use database transactions with locking (e.g., `SELECT FOR UPDATE`).

**Code Example:**

```sql
-- Vulnerable:
-- Read balance
-- If balance > amount: Update balance
-- (Two requests can pass the check simultaneously)

-- Secure:
UPDATE accounts SET balance = balance - 10 WHERE id = 1 AND balance >= 10;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q59"></a>

### Q59: Why use a CSPRNG over `Math.random()`?

**Difficulty**: Beginner

**Strategy:**
`Math.random()` is predictable. CSPRNG (Cryptographically Secure Pseudo-Random Number Generator) uses OS entropy, making it unpredictable and suitable for tokens/keys.

**Code Example:**

```javascript
// Node.js
const crypto = require('crypto');
const token = crypto.randomBytes(32).toString('hex');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q60"></a>

### Q60: How do you prevent Docker Container Breakouts?

**Difficulty**: Advanced

**Strategy:**
Don't run as root (`USER nonroot`). Limit capabilities (`--cap-drop ALL`). Use seccomp profiles. Keep host kernel updated.

**Code Example:**

```dockerfile
FROM alpine
RUN adduser -D myuser
USER myuser
ENTRYPOINT ["./app"]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q61"></a>

### Q61: What is Kubernetes Pod Security?

**Difficulty**: Advanced

**Strategy:**
Use Pod Security Standards (PSS) or OPA Gatekeeper to enforce rules: no privileged containers, read-only root filesystem, restricted volume types.

**Code Example:**

```yaml
securityContext:
  runAsNonRoot: true
  readOnlyRootFilesystem: true
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q62"></a>

### Q62: How do you prevent GraphQL Batching Attacks?

**Difficulty**: Advanced

**Strategy:**
Attackers send thousands of queries in one request to DDoS the server. Limit the number of batched queries or disable batching if not needed.

**Code Example:**

```javascript
// Apollo Server
const server = new ApolloServer({
  allowBatchedHttpRequests: false
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q63"></a>

### Q63: Why is the `state` parameter important in OAuth2?

**Difficulty**: Intermediate

**Strategy:**
It prevents CSRF attacks during the OAuth flow. The client generates a random token, sends it in the auth request, and verifies it when the provider redirects back.

**Code Example:**

```text
https://auth.com/authorize?response_type=code&client_id=...&state=xyz123
# Client verifies state=xyz123 on callback
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q64"></a>

### Q64: What is an OIDC Claim?

**Difficulty**: Intermediate

**Strategy:**
OpenID Connect (OIDC) uses claims (key-value pairs) in the ID Token to assert information about the user (sub, name, email, iat, exp).

**Code Example:**

```json
{
  "sub": "12345",
  "name": "Alice",
  "iat": 1610000000
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q65"></a>

### Q65: How do you secure an API Gateway?

**Difficulty**: Advanced

**Strategy:**
Implement Rate Limiting, IP Whitelisting, Mutual TLS (mTLS), JWT Validation, and WAF protection at the gateway level (e.g., Kong, Nginx, AWS API Gateway).

**Code Example:**

```yaml
# Kong Rate Limiting Plugin
config:
  minute: 100
  policy: local
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q66"></a>

### Q66: What is WebAuthn / Passkeys?

**Difficulty**: Advanced

**Strategy:**
A standard for passwordless authentication using public-key cryptography. The user authenticates locally (FaceID, TouchID) and the device signs a challenge sent to the server.

**Code Example:**

```javascript
navigator.credentials.create({ publicKey: ... })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q67"></a>

### Q67: What is Certificate Pinning?

**Difficulty**: Expert

**Strategy:**
Hardcoding the expected SSL certificate or public key in the client (mobile app) to prevent MitM attacks even if a CA is compromised. (Note: Risky if cert rotates/expires).

**Code Example:**

```java
// Android Network Security Config
<pin-set>
  <pin digest="SHA-256">...</pin>
</pin-set>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q68"></a>

### Q68: What is DNS Rebinding?

**Difficulty**: Expert

**Strategy:**
An attacker controls a malicious DNS server that resolves a domain to the attacker's IP first (to load a script) and then to a local IP (127.0.0.1) to bypass SOP and access local services.

**Code Example:**

```text
attacker.com -> 1.2.3.4 (TTL 0)
# Script loads
attacker.com -> 127.0.0.1 (TTL 0)
# Script accesses localhost
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q69"></a>

### Q69: What is a Padding Oracle Attack?

**Difficulty**: Expert

**Strategy:**
An attack against block ciphers (like CBC mode) where the server leaks information about whether the padding of a decrypted message is valid. Allows decrypting the ciphertext. Fix: Use Authenticated Encryption (AES-GCM).

**Code Example:**

```text
Error: Invalid Padding vs Error: Decryption Failed
# Difference allows guessing bytes
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q70"></a>

### Q70: What is a Dependency Confusion Attack?

**Difficulty**: Advanced

**Strategy:**
Uploading a package with the same name as an internal private package to a public registry (npm/PyPI) with a higher version number. Build systems might pull the malicious public version.

**Code Example:**

```json
"dependencies": {
  "internal-utils": "^1.0.0" 
  // Attacker publishes 99.0.0 to public npm
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q71"></a>

### Q71: What tools can detect secrets in code?

**Difficulty**: Beginner

**Strategy:**
Tools like `trufflehog`, `gitleaks`, and GitHub Secret Scanning scan git history for patterns resembling API keys, passwords, and tokens.

**Code Example:**

```bash
gitleaks detect --source . -v
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q72"></a>

### Q72: What is a Secure Code Review Checklist?

**Difficulty**: Intermediate

**Strategy:**
A list of items to verify during code review: Input Validation, Output Encoding, Auth/Authz checks, Logging (no secrets), Error Handling (no leaks), Cryptography standards.

**Code Example:**

```markdown
- [ ] All user input is validated?
- [ ] SQL queries use parameters?
- [ ] No hardcoded secrets?
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q73"></a>

### Q73: What is STRIDE in Threat Modeling?

**Difficulty**: Intermediate

**Strategy:**
A mnemonic for threats:
**S**poofing, **T**ampering, **R**epudiation, **I**nformation Disclosure, **D**enial of Service, **E**levation of Privilege.

**Code Example:**

```text
Analyze login flow:
- Spoofing: Can I pretend to be user X?
- Tampering: Can I modify the request?
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q74"></a>

### Q74: What are the phases of Penetration Testing?

**Difficulty**: Intermediate

**Strategy:**
1. Reconnaissance (Info gathering)
2. Scanning (Vuln discovery)
3. Exploitation (Gaining access)
4. Maintaining Access (Persistence)
5. Reporting (Documentation)

**Code Example:**

```text
nmap -> burpsuite -> exploit -> report
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q75"></a>

### Q75: What is the Incident Response Lifecycle?

**Difficulty**: Advanced

**Strategy:**
NIST Framework:
1. Preparation
2. Detection & Analysis
3. Containment, Eradication, & Recovery
4. Post-Incident Activity (Lessons Learned)

**Code Example:**

```text
Alert -> Isolate Server -> Patch Vuln -> Restore Backup -> Write Report
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q76"></a>

### Q76: What is a DevSecOps Pipeline?

**Difficulty**: Intermediate

**Strategy:**
Integrating security practices within the DevOps process. It involves automated security checks (SAST, SCA, DAST) at every stage of the CI/CD pipeline, not just at the end.

**Code Example:**

```yaml
steps:
  - run: npm install
  - run: npm audit # SCA
  - run: sonar-scanner # SAST
  - run: docker build ...
  - run: trivy image ... # Container Scan
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q77"></a>

### Q77: What is the difference between SAST and DAST?

**Difficulty**: Intermediate

**Strategy:**
SAST (Static Application Security Testing) analyzes source code at rest (white-box). DAST (Dynamic AST) attacks the running application from the outside (black-box).

**Code Example:**

```text
SAST: SonarQube finding "Hardcoded Password" in code.
DAST: OWASP ZAP finding "SQL Injection" by sending payloads to login form.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q78"></a>

### Q78: What is IAST (Interactive Application Security Testing)?

**Difficulty**: Advanced

**Strategy:**
IAST combines SAST and DAST. It runs inside the application (via an agent) and analyzes code execution while the app is being tested (e.g., during QA), providing more accurate results with fewer false positives.

**Code Example:**

```text
Agent attached to Java process monitors request flow to DB and flags SQLi.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q79"></a>

### Q79: What is RASP (Runtime Application Self-Protection)?

**Difficulty**: Expert

**Strategy:**
RASP is a security technology that is built into or linked into an application or its runtime environment, capable of controlling application execution and detecting/preventing real-time attacks.

**Code Example:**

```text
RASP detects a SQL injection pattern in a query at runtime and blocks the specific database call, throwing an exception.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q80"></a>

### Q80: What is Shadow IT and why is it a risk?

**Difficulty**: Beginner

**Strategy:**
The use of IT systems, devices, software, or services without explicit IT department approval (e.g., using personal Dropbox for company files). Risks include data leaks, compliance violations, and lack of patching.

**Code Example:**

```text
Employee uses 'WeTransfer' to send sensitive customer data because the corporate VPN is slow.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q81"></a>

### Q81: How do you prevent Social Engineering attacks?

**Difficulty**: Beginner

**Strategy:**
Training and awareness are key. Verify identities, don't click suspicious links, enable MFA, and have clear procedures for sensitive actions (e.g., wire transfers).

**Code Example:**

```text
"CEO" emails asking for urgent gift cards.
Procedure: Call the CEO to verify.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q82"></a>

### Q82: Why is Physical Security important for servers?

**Difficulty**: Beginner

**Strategy:**
If an attacker has physical access to a machine, they can bypass most software controls (e.g., boot from USB, remove hard drive). Use locks, cameras, and biometrics for data centers.

**Code Example:**

```text
"Evil Maid" attack: Modifying the bootloader while the laptop is unattended in a hotel room.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q83"></a>

### Q83: What is the Cloud Shared Responsibility Model?

**Difficulty**: Intermediate

**Strategy:**
The cloud provider is responsible for security _of_ the cloud (hardware, network). The customer is responsible for security _in_ the cloud (data, OS configuration, access management).

**Code Example:**

```text
AWS protects the data center.
You protect your S3 bucket permissions.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q84"></a>

### Q84: Why use IAM Roles instead of IAM Users in AWS?

**Difficulty**: Advanced

**Strategy:**
IAM Users have long-term credentials (access keys) which can be leaked. IAM Roles provide temporary credentials and are assumed by services (EC2, Lambda) or federated users, reducing the attack surface.

**Code Example:**

```json
// Role trust policy
"Principal": { "Service": "ec2.amazonaws.com" }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q85"></a>

### Q85: How do you secure an S3 Bucket?

**Difficulty**: Intermediate

**Strategy:**
Block public access, enable versioning, enable encryption (SSE-S3/KMS), use bucket policies to restrict access to specific IPs or VPC endpoints, and enable access logging.

**Code Example:**

```json
"Effect": "Deny",
"Principal": "*",
"Action": "s3:*",
"Condition": { "Bool": { "aws:SecureTransport": "false" } }
// Enforce HTTPS
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q86"></a>

### Q86: What are the risks of VPC Peering?

**Difficulty**: Advanced

**Strategy:**
VPC Peering connects two VPCs as if they are on the same network. If one is compromised, the attacker can pivot to the other. Use Security Groups and NACLs to strictly control traffic between peered VPCs.

**Code Example:**

```text
Dev VPC peered with Prod VPC allow attacker to move laterally.
Fix: Only allow specific ports/IPs.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q87"></a>

### Q87: What does a WAF (Web Application Firewall) do?

**Difficulty**: Intermediate

**Strategy:**
A WAF sits in front of web applications and inspects HTTP traffic. It blocks common attacks like SQLi, XSS, and bad bots based on rulesets (e.g., OWASP Core Rule Set).

**Code Example:**

```text
Rule: Block request if query parameter contains "UNION SELECT".
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q88"></a>

### Q88: How do you mitigate DDoS attacks?

**Difficulty**: Advanced

**Strategy:**
Use a CDN (Cloudflare, Akamai) to absorb traffic. Implement Rate Limiting. Use Auto-Scaling groups to handle spikes. Minimize attack surface (close unused ports).

**Code Example:**

```text
SYN Flood -> Enable SYN Cookies.
Volumetric -> Anycast Network.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q89"></a>

### Q89: How do you detect Bot traffic?

**Difficulty**: Intermediate

**Strategy:**
Analyze user behavior (mouse movements, speed). Check IP reputation. Inspect User-Agent (easily spoofed) and TLS fingerprinting (JA3). Use challenges (CAPTCHA).

**Code Example:**

```text
If 100 requests/sec from one IP -> likely a bot.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q90"></a>

### Q90: What are the different types of CAPTCHA?

**Difficulty**: Beginner

**Strategy:**
Text-based (distorted text), Image-based (select traffic lights), Invisible (analyzes background behavior), and Proof-of-Work (client solves math problem).

**Code Example:**

```text
reCAPTCHA v3 returns a score (0.0 - 1.0) indicating likelihood of being a human without user interaction.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q91"></a>

### Q91: What are the risks of Biometric Authentication?

**Difficulty**: Advanced

**Strategy:**
Biometrics (fingerprint, face) cannot be changed if compromised. They can be spoofed (high-res photos, molds). Data privacy is critical; store hashes/templates locally, not raw images.

**Code Example:**

```text
Leak of 1 million passwords -> Reset passwords.
Leak of 1 million fingerprints -> Users cannot reset fingerprints.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q92"></a>

### Q92: What is Privacy by Design?

**Difficulty**: Intermediate

**Strategy:**
Integrating data protection into processing activities and business practices from the design stage, rather than as an afterthought. Minimize data collection.

**Code Example:**

```text
Don't collect DoB if you only need to know if user is 18+. Ask "Are you 18+?" instead.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q93"></a>

### Q93: What is the GDPR "Right to be Forgotten"?

**Difficulty**: Intermediate

**Strategy:**
Users have the right to request erasure of their personal data. Organizations must delete data from all systems (DB, backups, logs) unless there's a legal reason to keep it.

**Code Example:**

```sql
DELETE FROM users WHERE id = 123;
-- Also scrub logs and backups
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q94"></a>

### Q94: What is PCI-DSS?

**Difficulty**: Advanced

**Strategy:**
Payment Card Industry Data Security Standard. Requirements for companies processing credit card data. Key rules: Encrypt transmission, don't store CVV, use firewalls, regular testing.

**Code Example:**

```text
Never log the full PAN (Primary Account Number). Mask it: ****-****-****-1234.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q95"></a>

### Q95: What is HIPAA?

**Difficulty**: Advanced

**Strategy:**
Health Insurance Portability and Accountability Act. US law protecting medical information (PHI). Requires strict access controls, encryption, and audit trails.

**Code Example:**

```text
Encryption at rest for DB containing patient records is mandatory.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q96"></a>

### Q96: What is SOC 2?

**Difficulty**: Advanced

**Strategy:**
A auditing procedure ensuring service providers manage data securely. Type I reports on design of controls at a point in time. Type II reports on effectiveness of controls over a period (e.g., 6 months).

**Code Example:**

```text
Evidence: Showing 6 months of logs proving that terminated employees had access revoked within 24 hours.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q97"></a>

### Q97: What is ISO 27001?

**Difficulty**: Advanced

**Strategy:**
International standard for Information Security Management Systems (ISMS). It focuses on risk management: identifying assets, assessing risks, and implementing controls.

**Code Example:**

```text
Policy: All laptops must have full-disk encryption.
Control: MDM software enforces BitLocker.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q98"></a>

### Q98: What are Zero Knowledge Proofs?

**Difficulty**: Expert

**Strategy:**
A cryptographic method where one party (prover) can prove to another (verifier) that they know a value (e.g., password) without conveying the information itself.

**Code Example:**

```text
Proving you are over 18 without revealing your birth date.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q99"></a>

### Q99: What is Homomorphic Encryption?

**Difficulty**: Expert

**Strategy:**
Allows computation on encrypted data without decrypting it first. The result of the computation is encrypted, and when decrypted, matches the result as if operations were performed on plaintext.

**Code Example:**

```text
Cloud calculates Sum(Encrypted_Salaries) and returns Encrypted_Total. Cloud never sees individual salaries.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q100"></a>

### Q100: How does Quantum Computing threaten cryptography?

**Difficulty**: Expert

**Strategy:**
Shor's algorithm running on a powerful quantum computer could factor large integers efficiently, breaking RSA and ECC public-key encryption. Symmetric encryption (AES) is more resistant (requires larger keys).

**Code Example:**

```text
Mitigation: Post-Quantum Cryptography (Lattice-based algorithms).
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>
