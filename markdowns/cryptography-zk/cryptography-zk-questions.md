<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Applied Cryptography & Zero-Knowledge Logo" width="100" height="100">
  </a>
  <h1>Applied Cryptography & Zero-Knowledge Interview Questions & Answers</h1>
  <p><b>Comprehensive interview questions covering ECDSA, zk-SNARKs, AES-GCM AEAD, Constant-Time Implementations, and R1CS</b></p>
</div>

---

## Table of Contents

1. [How does ECDSA (Elliptic Curve Digital Signature Algorithm) work on secp256k1, and why does Nonce ($k$) Reuse completely leak the private key?](#q1) <span class="advanced">Advanced</span>
2. [What are Zero-Knowledge Proofs (ZKP) and how do Completeness, Soundness, and Zero-Knowledge define them?](#q2) <span class="advanced">Advanced</span>
3. [How do Arithmetic Circuits convert computational statements into Rank-1 Constraint Systems (R1CS)?](#q3) <span class="advanced">Advanced</span>
4. [What is the difference between Groth16 and PLONK zk-SNARK proof systems?](#q4) <span class="advanced">Advanced</span>
5. [How does AES-GCM (Galois/Counter Mode) Authenticated Encryption with Associated Data (AEAD) work?](#q5) <span class="advanced">Advanced</span>
6. [What is the Fiat-Shamir Heuristic and how does it convert Interactive Proofs into Non-Interactive ZKPs?](#q6) <span class="advanced">Advanced</span>
7. [How does Constant-Time Cryptographic Implementation prevent Side-Channel Timing Attacks?](#q7) <span class="advanced">Advanced</span>
8. [What is the difference between zk-SNARKs and zk-STARKs?](#q8) <span class="advanced">Advanced</span>
9. [How do Bilinear Pairings ($e: G_1 \times G_2 \rightarrow G_T$) enable cryptographic verification?](#q9) <span class="advanced">Advanced</span>
10. [What is Ed25519 (Edwards-curve Digital Signature Algorithm) and why is it preferred over ECDSA?](#q10) <span class="intermediate">Intermediate</span>
11. [How does ChaCha20-Poly1305 AEAD work and why is it faster than AES on mobile devices without AES-NI?](#q11) <span class="intermediate">Intermediate</span>
12. [What is Quadratic Arithmetic Programs (QAP) and how does Lagrange Interpolation transform R1CS?](#q12) <span class="advanced">Advanced</span>
13. [What is KZG (Kate-Zaverucha-Goldberg) Polynomial Commitment Scheme?](#q13) <span class="advanced">Advanced</span>
14. [How does Diffie-Hellman Key Exchange (ECDH) establish a shared secret over insecure channels?](#q14) <span class="beginner">Beginner</span>
15. [What is a Trusted Setup Ceremony (Powers of Tau) and why is toxic waste disposal critical?](#q15) <span class="advanced">Advanced</span>
16. [How does FRI (Fast Reed-Solomon Interactive Oracle Proof) work in zk-STARKs?](#q16) <span class="advanced">Advanced</span>
17. [What are Poseidon and Rescue Hash Functions and why are they optimized for Zero-Knowledge circuits?](#q17) <span class="advanced">Advanced</span>
18. [What is Differential Power Analysis (DPA) and how do masking countermeasures protect hardware smartcards?](#q18) <span class="advanced">Advanced</span>
19. [What is Post-Quantum Cryptography (PQC) and how does Lattice-Based Cryptography (ML-KEM / Kyber) work?](#q19) <span class="advanced">Advanced</span>
20. [What is Homomorphic Encryption (FHE: BFV, CKKS) and how does it compute on encrypted data?](#q20) <span class="advanced">Advanced</span>
21. [What is the Discrete Logarithm Problem (DLP) vs Decisional Diffie-Hellman (DDH)?](#q21) <span class="intermediate">Intermediate</span>
22. [How does Shamir's Secret Sharing split a master key into $(k, n)$ threshold shares?](#q22) <span class="intermediate">Intermediate</span>
23. [What is Key Derivation Function (KDF: HKDF, PBKDF2, Argon2) and how do salts and cost factors prevent attacks?](#q23) <span class="beginner">Beginner</span>
24. [What is Zero-Knowledge Rollup (zk-Rollup) state transition verification on Ethereum?](#q24) <span class="advanced">Advanced</span>
25. [How does HMAC (Hash-Based Message Authentication Code) guarantee message authenticity?](#q25) <span class="beginner">Beginner</span>
26. [What is Length Extension Attack on Merkle-Damgard Hash Functions (MD5, SHA-1, SHA-256)?](#q26) <span class="intermediate">Intermediate</span>
27. [What is BLS (Boneh-Lynn-Shacham) Signature Aggregation in Ethereum Proof-of-Stake?](#q27) <span class="advanced">Advanced</span>
28. [What are Custom Gates and Lookup Arguments (Plookup) in modern PLONKish arithmetization?](#q28) <span class="advanced">Advanced</span>
29. [How does Elliptic Curve Point Addition and Point Doubling work algebraically?](#q29) <span class="intermediate">Intermediate</span>
30. [What is the difference between Symmetric Block Ciphers: CBC, CTR, and GCM modes?](#q30) <span class="beginner">Beginner</span>
31. [How does Padding Oracle Attack (Bleichenbacher / CBC padding oracle) decrypt ciphertext byte-by-byte?](#q31) <span class="intermediate">Intermediate</span>
32. [What is Public Key Infrastructure (PKI) and X.509 Certificate Revocation (CRL vs OCSP vs OCSP Stapling)?](#q32) <span class="intermediate">Intermediate</span>
33. [How does Bulletproofs provide short zero-knowledge Range Proofs without trusted setup?](#q33) <span class="advanced">Advanced</span>
34. [What is Quantum Shor's Algorithm and how does it break RSA and Elliptic Curve Cryptography in polynomial time?](#q34) <span class="advanced">Advanced</span>
35. [What is Quantum Grover's Algorithm and why does it require doubling symmetric key sizes (AES-128 -> AES-256)?](#q35) <span class="intermediate">Intermediate</span>
36. [What is Linear Secret Sharing Scheme (LSSS) in Attribute-Based Encryption (ABE)?](#q36) <span class="advanced">Advanced</span>
37. [How does Diffie-Hellman Ephemeral (DHE / ECDHE) provide Perfect Forward Secrecy?](#q37) <span class="intermediate">Intermediate</span>
38. [What is Montgomery Multiplication and why is it used for fast modular arithmetic on hardware?](#q38) <span class="advanced">Advanced</span>
39. [How does Merkle Mountain Range (MMR) optimize append-only cryptographic accumulators?](#q39) <span class="advanced">Advanced</span>
40. [What is Zero-Knowledge Virtual Machine (zkVM: RISC Zero, SP1) architecture?](#q40) <span class="advanced">Advanced</span>
41. [How do Hash-Based Signatures (SPHINCS+) provide stateless post-quantum digital signatures?](#q41) <span class="advanced">Advanced</span>
42. [What is Verifiable Random Function (VRF) and how does it generate unpredictable on-chain randomness?](#q42) <span class="intermediate">Intermediate</span>
43. [How does Fault Injection Attack (Clock Glitching, Laser Fault Injection) break cryptographic hardware?](#q43) <span class="advanced">Advanced</span>
44. [What is Ring Signature (Monero) and how does it obscure the real signer among decoys?](#q44) <span class="advanced">Advanced</span>
45. [What is Differential Privacy (Laplace and Gaussian Mechanism) and how does it protect dataset queries?](#q45) <span class="intermediate">Intermediate</span>
46. [How does Private Information Retrieval (PIR) query a database without the database learning the query?](#q46) <span class="advanced">Advanced</span>
47. [What is Secure Multi-Party Computation (SMPC: SPDZ, Garbled Circuits)?](#q47) <span class="advanced">Advanced</span>
48. [How does Yao's Garbled Circuits protocol evaluate boolean circuits securely between two untrusted parties?](#q48) <span class="advanced">Advanced</span>
49. [What is Oblivious Transfer (OT 1-out-of-2) and why is it a foundational primitive of MPC?](#q49) <span class="advanced">Advanced</span>
50. [How does Key Wrapping (AES Key Wrap RFC 3394) protect cryptographic keys in storage?](#q50) <span class="intermediate">Intermediate</span>
51. [What is Elliptic Curve Point Compression?](#q51) <span class="beginner">Beginner</span>
52. [How does the Pollard's Rho Algorithm solve the Discrete Logarithm Problem in $O(\sqrt{N})$?](#q52) <span class="advanced">Advanced</span>
53. [What is the difference between Interactive Oracle Proofs (IOP) and Polynomial IOPs?](#q53) <span class="advanced">Advanced</span>
54. [How does Air (Algebraic Intermediate Representation) formulate constraints in STARK systems?](#q54) <span class="advanced">Advanced</span>
55. [What is the discrete logarithm problem on Edwards Curves vs Weierstrass Curves?](#q55) <span class="intermediate">Intermediate</span>
56. [How does the Random Oracle Model (ROM) differ from Standard Model in cryptographic security proofs?](#q56) <span class="advanced">Advanced</span>
57. [What is Dual_EC_DRBG and how did the NSA insert an intentional backdoor into a pseudo-random generator?](#q57) <span class="advanced">Advanced</span>
58. [How do Memory-Hard Functions (Scrypt, Argon2id) defeat ASIC and GPU password cracking farms?](#q58) <span class="intermediate">Intermediate</span>
59. [What is Bilinear Diffie-Hellman Assumption (BDH)?](#q59) <span class="advanced">Advanced</span>
60. [How does Multi-Scalar Multiplication (MSM) optimize proof generation speed in zk-SNARKs?](#q60) <span class="advanced">Advanced</span>
61. [What is Number Theoretic Transform (NTT) and how does it accelerate polynomial multiplication in finite fields?](#q61) <span class="advanced">Advanced</span>
62. [What is Co-factor Clearing in Elliptic Curve Cryptography?](#q62) <span class="intermediate">Intermediate</span>
63. [How does Zero-Knowledge Machine Learning (zkML) prove model inferences ran without tampering?](#q63) <span class="advanced">Advanced</span>
64. [What is Quantum Key Distribution (QKD: BB84 protocol)?](#q64) <span class="advanced">Advanced</span>
65. [How does Boneh-Lynn-Shacham (BLS) Short Signature scheme work on pairing-friendly curves?](#q65) <span class="intermediate">Intermediate</span>
66. [What is the difference between Perfect Secrecy (One-Time Pad) and Computational Security?](#q66) <span class="beginner">Beginner</span>
67. [How does the Fiat-Shamir with Aborts technique work in lattice-based signature schemes (Dilithium)?](#q67) <span class="advanced">Advanced</span>
68. [What is Threshold ECDSA and how does multi-party computation sign cryptocurrency transactions without reconstructing the private key?](#q68) <span class="advanced">Advanced</span>
69. [How does Format-Preserving Encryption (FPE: FF1, FF3-1) encrypt credit card numbers while maintaining valid digits?](#q69) <span class="intermediate">Intermediate</span>
70. [What is Forward Secure Digital Signatures and how do key-evolving schemes protect past signatures?](#q70) <span class="advanced">Advanced</span>
71. [How do Proof of Solvency protocols (Merkle Tree vs zk-SNARK) prove exchange reserves match liabilities?](#q71) <span class="intermediate">Intermediate</span>
72. [What is Broadcast Encryption and how does Pay-TV broadcast encrypted content to authorized subsets?](#q72) <span class="advanced">Advanced</span>
73. [How does S-Box (Substitution Box) provide non-linearity in symmetric ciphers (AES)?](#q73) <span class="intermediate">Intermediate</span>
74. [What is Chosen Ciphertext Attack (CCA2) and what is IND-CCA2 security?](#q74) <span class="intermediate">Intermediate</span>
75. [How do Zero-Knowledge Set Membership proofs prove an element exists in an accumulator without revealing the element?](#q75) <span class="advanced">Advanced</span>
76. [What is Electronic Codebook (ECB) Mode and why does it leak plaintext patterns (the ECB Penguin)?](#q76) <span class="beginner">Beginner</span>
77. [How does Public Key Cryptography Standards (PKCS #1 v1.5 vs OAEP) protect RSA encryption?](#q77) <span class="intermediate">Intermediate</span>
78. [What is Feistel Cipher Network and how does it construct reversible block ciphers (DES, Blowfish)?](#q78) <span class="intermediate">Intermediate</span>
79. [How does Secret Handshake Protocol establish mutual authentication without revealing identities to eavesdroppers?](#q79) <span class="advanced">Advanced</span>
80. [What is Side-Channel Cache-Timing Attack (FLUSH+RELOAD, PRIME+PROBE)?](#q80) <span class="advanced">Advanced</span>
81. [How does Differential Cryptanalysis analyze symmetric ciphers?](#q81) <span class="advanced">Advanced</span>
82. [What is Secure Enclave Attestation (Intel SGX, AWS Nitro Enclaves)?](#q82) <span class="intermediate">Intermediate</span>
83. [How do Zero-Knowledge Contingent Payments allow atomic fair exchange of data for cryptocurrency?](#q83) <span class="advanced">Advanced</span>
84. [What is Ring Learning With Errors (Ring-LWE) in Post-Quantum Cryptography?](#q84) <span class="advanced">Advanced</span>
85. [How does Elliptic Curve Diffie-Hellman (ECDH) handle invalid curve attacks?](#q85) <span class="advanced">Advanced</span>
86. [What is Verifiable Encryption and how is it used in key escrow systems?](#q86) <span class="advanced">Advanced</span>
87. [How does Key Separation using Domain Separation Tags (DST) prevent cross-protocol attacks?](#q87) <span class="intermediate">Intermediate</span>
88. [What is Merkle-Damgard Construction and how does it build hash functions from compression functions?](#q88) <span class="beginner">Beginner</span>
89. [How do Oblivious RAM (ORAM: Path ORAM) protocols hide memory access patterns in untrusted storage?](#q89) <span class="advanced">Advanced</span>
90. [What is Homomorphic Commitment (Pedersen Commitment) and how does it hide values while allowing addition?](#q90) <span class="advanced">Advanced</span>
91. [How does Meet-in-the-Middle Attack break Double DES and motivate Triple DES (3DES)?](#q91) <span class="intermediate">Intermediate</span>
92. [What is the role of Quadratic Residues in cryptographic protocols (Goldwasser-Micali encryption)?](#q92) <span class="advanced">Advanced</span>
93. [How do Threshold Decryption systems prevent unauthorized decryption without consensus?](#q93) <span class="advanced">Advanced</span>
94. [What is Side-Channel Acoustic Cryptanalysis?](#q94) <span class="intermediate">Intermediate</span>
95. [How does Curve448 differ from Curve25519 in security margin and performance?](#q95) <span class="intermediate">Intermediate</span>
96. [What is the difference between Public Key Compression and Uncompressed Keys in secp256k1?](#q96) <span class="beginner">Beginner</span>
97. [How does the Fiat-Shamir Transform guarantee soundness in interactive proof systems?](#q97) <span class="advanced">Advanced</span>
98. [What is Multi-Party Computation (MPC) Threshold Signatures vs Multisig Smart Contracts?](#q98) <span class="intermediate">Intermediate</span>
99. [How do Zero-Knowledge Identity Proofs (Semaphore, zk-ID) prove group membership anonymously?](#q99) <span class="advanced">Advanced</span>
100. [What is Linear Cryptanalysis in block ciphers?](#q100) <span class="advanced">Advanced</span>

---

<a id="q1"></a>
### Q1: How does ECDSA (Elliptic Curve Digital Signature Algorithm) work on secp256k1, and why does Nonce ($k$) Reuse completely leak the private key?

**Difficulty**: Advanced

**Strategy**:
In ECDSA on curve $y^2 = x^3 + 7 \pmod p$, signing message hash $e$ uses private key $d$ and random nonce $k$. The signer calculates point $(x_1, y_1) = k \cdot G$, setting $r = x_1 \pmod n$ and $s = k^{-1}(e + r \cdot d) \pmod n$. If the signer signs two distinct messages ($e_1, e_2$) using the identical nonce $k$, the signature $r$ will be identical in both. An attacker calculates $k = \frac{e_1 - e_2}{s_1 - s_2} \pmod n$, and immediately solves for the private key $d = \frac{s_1 \cdot k - e_1}{r} \pmod n$ (as occurred in the Sony PS3 exploit). RFC 6979 prevents this by deriving $k$ deterministically via HMAC-SHA256.

**Code Example**:
```python
# Private Key Recovery from ECDSA Nonce Reuse
def recover_private_key(e1, s1, e2, s2, r, n):
    # 1. Recover shared nonce k
    k = ((e1 - e2) * pow(s1 - s2, -1, n)) % n
    # 2. Extract private key d
    d = ((s1 * k - e1) * pow(r, -1, n)) % n
    return d
```

---

<a id="q2"></a>
### Q2: What are Zero-Knowledge Proofs (ZKP) and how do Completeness, Soundness, and Zero-Knowledge define them?

**Difficulty**: Advanced

**Strategy**:
A Zero-Knowledge Proof allows a Prover to prove to a Verifier that a statement is true without revealing any information beyond the statement's validity. Defined by three mathematical properties: 1) **Completeness**: If the statement is true and Prover and Verifier are honest, the Verifier will always be convinced. 2) **Soundness**: If the statement is false, no cheating Prover can convince the Verifier except with negligible probability. 3) **Zero-Knowledge**: The Verifier learns nothing other than the fact that the statement is true (formally: there exists a polynomial-time Simulator that can produce a view indistinguishable from a real proof interaction).

**Code Example**:
```text
ZKP Security Properties:
1. Completeness: Honest Prover -> Always Accepted
2. Soundness: Malicious Prover -> Rejected (Soundness Error < 2^-128)
3. Zero-Knowledge: Information Leaked = 0 (Simulator indistinguishability)
```

---

<a id="q3"></a>
### Q3: How do Arithmetic Circuits convert computational statements into Rank-1 Constraint Systems (R1CS)?

**Difficulty**: Advanced

**Strategy**:
Any computation is compiled into an Arithmetic Circuit consisting of addition and multiplication gates over a finite field $\mathbb{F}_p$. R1CS represents these gates as a system of vector constraint equations of the form $(A \cdot s) \cdot (B \cdot s) - (C \cdot s) = 0$, where $s$ is the witness vector $[1, \text{public\_inputs}, \text{private\_witness}]$ and $A, B, C$ are sparse coefficient matrices. Each constraint represents exactly one multiplication operation ($L \times R = O$).

**Code Example**:
```text
Example: Prove knowledge of x such that x^3 + x + 5 == 35
1. Introduce intermediate variables:
   sym_1 = x * x
   y = sym_1 * x
   out = y + x + 5
2. R1CS Constraints (A . s) * (B . s) = (C . s):
   Constraint 1: (x) * (x) = sym_1
   Constraint 2: (sym_1) * (x) = y
   Constraint 3: (y + x + 5) * (1) = 35
```

---

<a id="q4"></a>
### Q4: What is the difference between Groth16 and PLONK zk-SNARK proof systems?

**Difficulty**: Advanced

**Strategy**:
**Groth16**: Uses Quadratic Arithmetic Programs (QAP) and bilinear pairings; produces the smallest possible proof size (128 bytes, 3 group elements) and fastest verification time (<2ms), but requires a circuit-specific trusted setup ceremony for every program. **PLONK**: Uses a universal and updateable trusted setup (Powers of Tau); uses permutation arguments and polynomial commitment schemes (KZG); proofs are slightly larger (~400-800 bytes), but one setup works for any circuit up to size $N$.

**Code Example**:
```text
zk-SNARK Comparison Matrix:
Feature                 Groth16                 PLONK
Proof Size              ~128 bytes (3 points)   ~400-800 bytes
Verification Gas (EVM)  ~200k gas               ~280k gas
Trusted Setup           Circuit-Specific (Bad)  Universal / Updateable (Great!)
Arithmetization         R1CS / QAP              Plonkish (Custom Gates & Lookup Tables)
```

---

<a id="q5"></a>
### Q5: How does AES-GCM (Galois/Counter Mode) Authenticated Encryption with Associated Data (AEAD) work?

**Difficulty**: Advanced

**Strategy**:
AES-GCM combines CTR (Counter Mode) encryption with GHASH polynomial evaluation over Galois Field $GF(2^{128})$. CTR encrypts plaintext blocks by XORing with AES-encrypted counter values. GHASH computes an authentication tag $T$ over both ciphertext and unencrypted Additional Authenticated Data (AAD). If the identical (Key, IV/Nonce) pair is ever reused to encrypt two different plaintexts, an attacker can extract the GHASH authentication hash key $H$, completely forging authentication tags for arbitrary packets.

**Code Example**:
```text
AES-GCM Architecture:
Plaintext Block P_i XOR AES_K(Counter_i) -> Ciphertext C_i
Ciphertext C_i + AAD -> GHASH Polynomial Multiplication in GF(2^128) -> Tag T
WARNING: Nonce reuse destroys BOTH confidentiality and integrity!
```

---

<a id="q6"></a>
### Q6: What is the Fiat-Shamir Heuristic and how does it convert Interactive Proofs into Non-Interactive ZKPs?

**Difficulty**: Advanced

**Strategy**:
Replaces the Verifier's random challenge query with a cryptographic hash of the Prover's commitment transcript (e.g. SHA-256 or Poseidon), enabling one-shot non-interactive proofs.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is the Fiat-Shamir Heuristic and how does it convert Interactive Proofs into Non-Interactive ZKPs?
Mathematically verified cryptographic implementation
```

---

<a id="q7"></a>
### Q7: How does Constant-Time Cryptographic Implementation prevent Side-Channel Timing Attacks?

**Difficulty**: Advanced

**Strategy**:
Ensures execution duration is independent of secret keys; replaces branch instructions (`if (secret)`) and secret-indexed table lookups with bitwise mask operations (`(mask & a) | (~mask & b)`).

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How does Constant-Time Cryptographic Implementation prevent Side-Channel Timing Attacks?
Mathematically verified cryptographic implementation
```

---

<a id="q8"></a>
### Q8: What is the difference between zk-SNARKs and zk-STARKs?

**Difficulty**: Advanced

**Strategy**:
SNARKs require trusted setups and rely on elliptic curve pairings (vulnerable to quantum computers); STARKs are transparent (no trusted setup), use collision-resistant hashes (post-quantum safe), but have larger proofs (~50KB).

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is the difference between zk-SNARKs and zk-STARKs?
Mathematically verified cryptographic implementation
```

---

<a id="q9"></a>
### Q9: How do Bilinear Pairings ($e: G_1 \times G_2 \rightarrow G_T$) enable cryptographic verification?

**Difficulty**: Advanced

**Strategy**:
A non-degenerate bilinear map satisfying $e(aP, bQ) = e(P, Q)^{ab}$; allows checking multiplication relationships between hidden scalar values in exponent group elements without revealing the scalars.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How do Bilinear Pairings ($e: G_1 \times G_2 \rightarrow G_T$) enable cryptographic verification?
Mathematically verified cryptographic implementation
```

---

<a id="q10"></a>
### Q10: What is Ed25519 (Edwards-curve Digital Signature Algorithm) and why is it preferred over ECDSA?

**Difficulty**: Intermediate

**Strategy**:
Operates on Twisted Edwards curve Curve25519; immune to signature malleability, provides fast verification without modular inversion, and has built-in deterministic nonce generation.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Ed25519 (Edwards-curve Digital Signature Algorithm) and why is it preferred over ECDSA?
Mathematically verified cryptographic implementation
```

---

<a id="q11"></a>
### Q11: How does ChaCha20-Poly1305 AEAD work and why is it faster than AES on mobile devices without AES-NI?

**Difficulty**: Intermediate

**Strategy**:
ChaCha20 is a software-friendly ARX (Add-Rotate-Xor) stream cipher; Poly1305 computes MAC; runs significantly faster on ARM CPUs lacking hardware AES acceleration.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How does ChaCha20-Poly1305 AEAD work and why is it faster than AES on mobile devices without AES-NI?
Mathematically verified cryptographic implementation
```

---

<a id="q12"></a>
### Q12: What is Quadratic Arithmetic Programs (QAP) and how does Lagrange Interpolation transform R1CS?

**Difficulty**: Advanced

**Strategy**:
Interpolates R1CS constraint matrix columns into polynomials $A(x), B(x), C(x)$; the polynomial identity $A(x)B(x) - C(x) = H(x)T(x)$ checks all constraints simultaneously at a random evaluation point.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Quadratic Arithmetic Programs (QAP) and how does Lagrange Interpolation transform R1CS?
Mathematically verified cryptographic implementation
```

---

<a id="q13"></a>
### Q13: What is KZG (Kate-Zaverucha-Goldberg) Polynomial Commitment Scheme?

**Difficulty**: Advanced

**Strategy**:
Allows a Prover to commit to a polynomial $P(x)$ as a single elliptic curve point $C = [P(s)]_1$; later opens the evaluation $P(z) = y$ with a constant-size proof verified via a single pairing check.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is KZG (Kate-Zaverucha-Goldberg) Polynomial Commitment Scheme?
Mathematically verified cryptographic implementation
```

---

<a id="q14"></a>
### Q14: How does Diffie-Hellman Key Exchange (ECDH) establish a shared secret over insecure channels?

**Difficulty**: Beginner

**Strategy**:
Alice sends $A = aG$; Bob sends $B = bG$; both compute shared secret $S = a(bG) = b(aG) = abG$; eavesdropper cannot compute $abG$ without solving Discrete Logarithm Problem.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How does Diffie-Hellman Key Exchange (ECDH) establish a shared secret over insecure channels?
Mathematically verified cryptographic implementation
```

---

<a id="q15"></a>
### Q15: What is a Trusted Setup Ceremony (Powers of Tau) and why is toxic waste disposal critical?

**Difficulty**: Advanced

**Strategy**:
Generates public reference string structured points $[s^i G]$; participants generate secret randomness; if all participants collude to retain toxic waste scalar $s$, they can forge fake proofs.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is a Trusted Setup Ceremony (Powers of Tau) and why is toxic waste disposal critical?
Mathematically verified cryptographic implementation
```

---

<a id="q16"></a>
### Q16: How does FRI (Fast Reed-Solomon Interactive Oracle Proof) work in zk-STARKs?

**Difficulty**: Advanced

**Strategy**:
Proves that a committed vector is close to a low-degree Reed-Solomon polynomial; iteratively folds polynomials into half the degree using random linear combinations.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How does FRI (Fast Reed-Solomon Interactive Oracle Proof) work in zk-STARKs?
Mathematically verified cryptographic implementation
```

---

<a id="q17"></a>
### Q17: What are Poseidon and Rescue Hash Functions and why are they optimized for Zero-Knowledge circuits?

**Difficulty**: Advanced

**Strategy**:
Traditional hashes (SHA-256) use bitwise operations that explode into tens of thousands of R1CS arithmetic constraints; Poseidon uses low-degree power maps ($x^5$) in finite fields, requiring <300 constraints.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What are Poseidon and Rescue Hash Functions and why are they optimized for Zero-Knowledge circuits?
Mathematically verified cryptographic implementation
```

---

<a id="q18"></a>
### Q18: What is Differential Power Analysis (DPA) and how do masking countermeasures protect hardware smartcards?

**Difficulty**: Advanced

**Strategy**:
Measures electrical power consumption fluctuations during cryptographic calculations; mitigated by Boolean or arithmetic masking splitting secret variables into random shares.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Differential Power Analysis (DPA) and how do masking countermeasures protect hardware smartcards?
Mathematically verified cryptographic implementation
```

---

<a id="q19"></a>
### Q19: What is Post-Quantum Cryptography (PQC) and how does Lattice-Based Cryptography (ML-KEM / Kyber) work?

**Difficulty**: Advanced

**Strategy**:
Based on the hardness of Learning With Errors (LWE) and Shortest Vector Problems (SVP) in high-dimensional lattices, which quantum Shor's algorithm cannot solve.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Post-Quantum Cryptography (PQC) and how does Lattice-Based Cryptography (ML-KEM / Kyber) work?
Mathematically verified cryptographic implementation
```

---

<a id="q20"></a>
### Q20: What is Homomorphic Encryption (FHE: BFV, CKKS) and how does it compute on encrypted data?

**Difficulty**: Advanced

**Strategy**:
Enables mathematical operations directly on ciphertexts: $\text{Dec}(C_1 \oplus C_2) = P_1 + P_2$ and $\text{Dec}(C_1 \otimes C_2) = P_1 \times P_2$; CKKS supports approximate floating point calculations.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Homomorphic Encryption (FHE: BFV, CKKS) and how does it compute on encrypted data?
Mathematically verified cryptographic implementation
```

---

<a id="q21"></a>
### Q21: What is the Discrete Logarithm Problem (DLP) vs Decisional Diffie-Hellman (DDH)?

**Difficulty**: Intermediate

**Strategy**:
DLP: given $G$ and $aG$, compute $a$ (hard); Computational Diffie-Hellman (CDH): given $aG, bG$, compute $abG$; DDH: distinguish $abG$ from a random group element.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is the Discrete Logarithm Problem (DLP) vs Decisional Diffie-Hellman (DDH)?
Mathematically verified cryptographic implementation
```

---

<a id="q22"></a>
### Q22: How does Shamir's Secret Sharing split a master key into $(k, n)$ threshold shares?

**Difficulty**: Intermediate

**Strategy**:
Constructs a random polynomial $P(x) = S + a_1 x + \dots + a_{k-1} x^{k-1}$ of degree $k-1$ where $S$ is secret; any $k$ shares reconstruct $S$ via Lagrange interpolation; $<k$ shares reveal zero information.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How does Shamir's Secret Sharing split a master key into $(k, n)$ threshold shares?
Mathematically verified cryptographic implementation
```

---

<a id="q23"></a>
### Q23: What is Key Derivation Function (KDF: HKDF, PBKDF2, Argon2) and how do salts and cost factors prevent attacks?

**Difficulty**: Beginner

**Strategy**:
Extracts pseudorandom key from master secret and expands it; PBKDF2/Argon2 use memory-hard and iteration-hard loops to slow down brute-force dictionary attacks.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Key Derivation Function (KDF: HKDF, PBKDF2, Argon2) and how do salts and cost factors prevent attacks?
Mathematically verified cryptographic implementation
```

---

<a id="q24"></a>
### Q24: What is Zero-Knowledge Rollup (zk-Rollup) state transition verification on Ethereum?

**Difficulty**: Advanced

**Strategy**:
Validates that $N$ off-chain transactions were executed correctly by verifying a single ZK-SNARK/STARK proof on-chain; updates state root from $S_0$ to $S_n$ in single transaction.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Zero-Knowledge Rollup (zk-Rollup) state transition verification on Ethereum?
Mathematically verified cryptographic implementation
```

---

<a id="q25"></a>
### Q25: How does HMAC (Hash-Based Message Authentication Code) guarantee message authenticity?

**Difficulty**: Beginner

**Strategy**:
Computes $\text{HMAC}(K, m) = H((K \oplus opad) \parallel H((K \oplus ipad) \parallel m))$; protects against length-extension attacks that affect raw hash functions like SHA-256.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How does HMAC (Hash-Based Message Authentication Code) guarantee message authenticity?
Mathematically verified cryptographic implementation
```

---

<a id="q26"></a>
### Q26: What is Length Extension Attack on Merkle-Damgard Hash Functions (MD5, SHA-1, SHA-256)?

**Difficulty**: Intermediate

**Strategy**:
Given $H(m)$ and length of $m$, an attacker can append padding and malicious payload $m'$ to calculate $H(m \parallel m')$ without knowing $m$; SHA-3 and HMAC are immune.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Length Extension Attack on Merkle-Damgard Hash Functions (MD5, SHA-1, SHA-256)?
Mathematically verified cryptographic implementation
```

---

<a id="q27"></a>
### Q27: What is BLS (Boneh-Lynn-Shacham) Signature Aggregation in Ethereum Proof-of-Stake?

**Difficulty**: Advanced

**Strategy**:
Signatures on pairing-friendly curves (BLS12-381) can be added together into a single 48-byte aggregate signature verified with 2 pairing operations for hundreds of thousands of validators.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is BLS (Boneh-Lynn-Shacham) Signature Aggregation in Ethereum Proof-of-Stake?
Mathematically verified cryptographic implementation
```

---

<a id="q28"></a>
### Q28: What are Custom Gates and Lookup Arguments (Plookup) in modern PLONKish arithmetization?

**Difficulty**: Advanced

**Strategy**:
Custom gates combine multiple operations into a single constraint row; Plookup proves a value exists in a precomputed lookup table (e.g. 8-bit XOR table) in $O(1)$ constraint.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What are Custom Gates and Lookup Arguments (Plookup) in modern PLONKish arithmetization?
Mathematically verified cryptographic implementation
```

---

<a id="q29"></a>
### Q29: How does Elliptic Curve Point Addition and Point Doubling work algebraically?

**Difficulty**: Intermediate

**Strategy**:
Given $P_1(x_1, y_1)$ and $P_2(x_2, y_2)$, compute line slope $\lambda$; intersection with curve gives third point; reflecting over x-axis yields $P_3 = P_1 + P_2$.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How does Elliptic Curve Point Addition and Point Doubling work algebraically?
Mathematically verified cryptographic implementation
```

---

<a id="q30"></a>
### Q30: What is the difference between Symmetric Block Ciphers: CBC, CTR, and GCM modes?

**Difficulty**: Beginner

**Strategy**:
CBC: chains blocks with previous ciphertext (sequential, requires padding, vulnerable to padding oracle); CTR: encrypts counter (parallelizable, stream); GCM: CTR + authenticated integrity tag.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is the difference between Symmetric Block Ciphers: CBC, CTR, and GCM modes?
Mathematically verified cryptographic implementation
```

---

<a id="q31"></a>
### Q31: How does Padding Oracle Attack (Bleichenbacher / CBC padding oracle) decrypt ciphertext byte-by-byte?

**Difficulty**: Intermediate

**Strategy**:
Exploits server error responses distinguishing valid from invalid PKCS#7 padding; manipulating ciphertext bytes recovers plaintext without knowing key.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How does Padding Oracle Attack (Bleichenbacher / CBC padding oracle) decrypt ciphertext byte-by-byte?
Mathematically verified cryptographic implementation
```

---

<a id="q32"></a>
### Q32: What is Public Key Infrastructure (PKI) and X.509 Certificate Revocation (CRL vs OCSP vs OCSP Stapling)?

**Difficulty**: Intermediate

**Strategy**:
CRL: lists revoked certs; OCSP: queries CA status online (privacy/latency leak); OCSP Stapling: web server attaches signed OCSP timestamp directly in TLS handshake.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Public Key Infrastructure (PKI) and X.509 Certificate Revocation (CRL vs OCSP vs OCSP Stapling)?
Mathematically verified cryptographic implementation
```

---

<a id="q33"></a>
### Q33: How does Bulletproofs provide short zero-knowledge Range Proofs without trusted setup?

**Difficulty**: Advanced

**Strategy**:
Proves that a secret number lies within $[0, 2^{64}-1]$ using inner-product arguments; proof size grows logarithmically $O(\log N)$, used in Monero confidential transactions.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How does Bulletproofs provide short zero-knowledge Range Proofs without trusted setup?
Mathematically verified cryptographic implementation
```

---

<a id="q34"></a>
### Q34: What is Quantum Shor's Algorithm and how does it break RSA and Elliptic Curve Cryptography in polynomial time?

**Difficulty**: Advanced

**Strategy**:
Uses Quantum Fourier Transform to find the period of modular exponentiation in $O((\log N)^3)$ time, factoring RSA moduli and solving discrete logs.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Quantum Shor's Algorithm and how does it break RSA and Elliptic Curve Cryptography in polynomial time?
Mathematically verified cryptographic implementation
```

---

<a id="q35"></a>
### Q35: What is Quantum Grover's Algorithm and why does it require doubling symmetric key sizes (AES-128 -> AES-256)?

**Difficulty**: Intermediate

**Strategy**:
Provides quadratic speedup for unstructured database search in $O(\sqrt{N})$; reduces effective brute-force key strength of AES-128 to $2^{64}$, requiring AES-256 for 128-bit quantum security.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Quantum Grover's Algorithm and why does it require doubling symmetric key sizes (AES-128 -> AES-256)?
Mathematically verified cryptographic implementation
```

---

<a id="q36"></a>
### Q36: What is Linear Secret Sharing Scheme (LSSS) in Attribute-Based Encryption (ABE)?

**Difficulty**: Advanced

**Strategy**:
Distributes secret shares according to boolean formula access policies (e.g. 'Engineering AND Manager'); decryption succeeds only if user attributes satisfy policy matrix.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Linear Secret Sharing Scheme (LSSS) in Attribute-Based Encryption (ABE)?
Mathematically verified cryptographic implementation
```

---

<a id="q37"></a>
### Q37: How does Diffie-Hellman Ephemeral (DHE / ECDHE) provide Perfect Forward Secrecy?

**Difficulty**: Intermediate

**Strategy**:
Generates unique ephemeral keypair per TLS session; discarding ephemeral private keys after session guarantees that compromising server long-term key cannot decrypt recorded traffic.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How does Diffie-Hellman Ephemeral (DHE / ECDHE) provide Perfect Forward Secrecy?
Mathematically verified cryptographic implementation
```

---

<a id="q38"></a>
### Q38: What is Montgomery Multiplication and why is it used for fast modular arithmetic on hardware?

**Difficulty**: Advanced

**Strategy**:
Transforms numbers into Montgomery representation where modular reduction $A \cdot B \pmod N$ avoids expensive hardware integer division, using fast bitwise shifts.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Montgomery Multiplication and why is it used for fast modular arithmetic on hardware?
Mathematically verified cryptographic implementation
```

---

<a id="q39"></a>
### Q39: How does Merkle Mountain Range (MMR) optimize append-only cryptographic accumulators?

**Difficulty**: Advanced

**Strategy**:
Binary tree composed of consecutive balanced sub-trees; supports $O(\log N)$ append and verification proofs without re-hashing historical leaf nodes.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How does Merkle Mountain Range (MMR) optimize append-only cryptographic accumulators?
Mathematically verified cryptographic implementation
```

---

<a id="q40"></a>
### Q40: What is Zero-Knowledge Virtual Machine (zkVM: RISC Zero, SP1) architecture?

**Difficulty**: Advanced

**Strategy**:
Compiles Rust/C++ to RISC-V ELF; executes program inside a zk-STARK proof system proving correct state transitions of RISC-V CPU registers and memory.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Zero-Knowledge Virtual Machine (zkVM: RISC Zero, SP1) architecture?
Mathematically verified cryptographic implementation
```

---

<a id="q41"></a>
### Q41: How do Hash-Based Signatures (SPHINCS+) provide stateless post-quantum digital signatures?

**Difficulty**: Advanced

**Strategy**:
Uses trees of one-time signatures (WOTS+) and few-time signatures (FORS) combined with hyper-trees; security relies strictly on collision-resistance of cryptographic hashes.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How do Hash-Based Signatures (SPHINCS+) provide stateless post-quantum digital signatures?
Mathematically verified cryptographic implementation
```

---

<a id="q42"></a>
### Q42: What is Verifiable Random Function (VRF) and how does it generate unpredictable on-chain randomness?

**Difficulty**: Intermediate

**Strategy**:
Public-key version of keyed hash: holder of secret key evaluates $R = \text{VRF}_K(seed)$ and outputs proof $\pi$; anyone verifies $\pi$ proves $R$ was generated deterministically from seed.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Verifiable Random Function (VRF) and how does it generate unpredictable on-chain randomness?
Mathematically verified cryptographic implementation
```

---

<a id="q43"></a>
### Q43: How does Fault Injection Attack (Clock Glitching, Laser Fault Injection) break cryptographic hardware?

**Difficulty**: Advanced

**Strategy**:
Induces transient hardware bit flips during RSA/AES calculation; comparing corrupted output with correct output mathematically solves for internal private keys.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How does Fault Injection Attack (Clock Glitching, Laser Fault Injection) break cryptographic hardware?
Mathematically verified cryptographic implementation
```

---

<a id="q44"></a>
### Q44: What is Ring Signature (Monero) and how does it obscure the real signer among decoys?

**Difficulty**: Advanced

**Strategy**:
Allows a member of a group of public keys to sign a transaction without revealing which member signed; key images prevent double-spending.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Ring Signature (Monero) and how does it obscure the real signer among decoys?
Mathematically verified cryptographic implementation
```

---

<a id="q45"></a>
### Q45: What is Differential Privacy (Laplace and Gaussian Mechanism) and how does it protect dataset queries?

**Difficulty**: Intermediate

**Strategy**:
Adds calibrated mathematical noise to query results; guarantees inclusion or exclusion of any individual data record does not perceptibly alter output distribution.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Differential Privacy (Laplace and Gaussian Mechanism) and how does it protect dataset queries?
Mathematically verified cryptographic implementation
```

---

<a id="q46"></a>
### Q46: How does Private Information Retrieval (PIR) query a database without the database learning the query?

**Difficulty**: Advanced

**Strategy**:
Allows client to retrieve an item from a database server without server discovering which item was accessed, using homomorphic encryption or secret sharing.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How does Private Information Retrieval (PIR) query a database without the database learning the query?
Mathematically verified cryptographic implementation
```

---

<a id="q47"></a>
### Q47: What is Secure Multi-Party Computation (SMPC: SPDZ, Garbled Circuits)?

**Difficulty**: Advanced

**Strategy**:
Allows $N$ parties to compute a joint function $y = f(x_1, \dots, x_n)$ over their private inputs without any party disclosing their private input to anyone.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Secure Multi-Party Computation (SMPC: SPDZ, Garbled Circuits)?
Mathematically verified cryptographic implementation
```

---

<a id="q48"></a>
### Q48: How does Yao's Garbled Circuits protocol evaluate boolean circuits securely between two untrusted parties?

**Difficulty**: Advanced

**Strategy**:
Alice garbles (encrypts) truth tables of all circuit gates; Bob evaluates gates using Oblivious Transfer to retrieve input keys, learning only the final output.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How does Yao's Garbled Circuits protocol evaluate boolean circuits securely between two untrusted parties?
Mathematically verified cryptographic implementation
```

---

<a id="q49"></a>
### Q49: What is Oblivious Transfer (OT 1-out-of-2) and why is it a foundational primitive of MPC?

**Difficulty**: Advanced

**Strategy**:
Sender has messages $m_0, m_1$; receiver selects index $b$; receiver learns only $m_b$; sender learns nothing about which message was selected.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Oblivious Transfer (OT 1-out-of-2) and why is it a foundational primitive of MPC?
Mathematically verified cryptographic implementation
```

---

<a id="q50"></a>
### Q50: How does Key Wrapping (AES Key Wrap RFC 3394) protect cryptographic keys in storage?

**Difficulty**: Intermediate

**Strategy**:
Encrypts small symmetric keys using a master Key Encryption Key (KEK) with integrity check value, detecting tampering without separate MAC tag.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How does Key Wrapping (AES Key Wrap RFC 3394) protect cryptographic keys in storage?
Mathematically verified cryptographic implementation
```

---

<a id="q51"></a>
### Q51: What is Elliptic Curve Point Compression?

**Difficulty**: Beginner

**Strategy**:
Stores only coordinate $x$ and 1 bit indicating the sign of $y$ (even/odd) since $y = \pm \sqrt{x^3 + ax + b}$; cuts public key storage footprint by 50%.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Elliptic Curve Point Compression?
Mathematically verified cryptographic implementation
```

---

<a id="q52"></a>
### Q52: How does the Pollard's Rho Algorithm solve the Discrete Logarithm Problem in $O(\sqrt{N})$?

**Difficulty**: Advanced

**Strategy**:
Uses pseudo-random walk function to detect collisions in cyclic groups, reducing discrete log search space from $O(N)$ brute force to $O(\sqrt{N})$.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How does the Pollard's Rho Algorithm solve the Discrete Logarithm Problem in $O(\sqrt{N})$?
Mathematically verified cryptographic implementation
```

---

<a id="q53"></a>
### Q53: What is the difference between Interactive Oracle Proofs (IOP) and Polynomial IOPs?

**Difficulty**: Advanced

**Strategy**:
IOP: Prover sends oracle messages that Verifier queries at random locations; Polynomial IOP: Prover commits to polynomials that Verifier evaluates at random points.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is the difference between Interactive Oracle Proofs (IOP) and Polynomial IOPs?
Mathematically verified cryptographic implementation
```

---

<a id="q54"></a>
### Q54: How does Air (Algebraic Intermediate Representation) formulate constraints in STARK systems?

**Difficulty**: Advanced

**Strategy**:
Represents execution traces as 2D tables of state registers; Transition Constraints verify valid transitions between consecutive steps; Boundary Constraints verify inputs/outputs.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How does Air (Algebraic Intermediate Representation) formulate constraints in STARK systems?
Mathematically verified cryptographic implementation
```

---

<a id="q55"></a>
### Q55: What is the discrete logarithm problem on Edwards Curves vs Weierstrass Curves?

**Difficulty**: Intermediate

**Strategy**:
Both provide equivalent cryptographic hardness; Edwards curves have complete addition formulas with no exceptional points (zero points, point at infinity), preventing side-channel edge cases.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is the discrete logarithm problem on Edwards Curves vs Weierstrass Curves?
Mathematically verified cryptographic implementation
```

---

<a id="q56"></a>
### Q56: How does the Random Oracle Model (ROM) differ from Standard Model in cryptographic security proofs?

**Difficulty**: Advanced

**Strategy**:
ROM assumes cryptographic hash behaves as an idealized random function mapping inputs to random uniform outputs; Standard model requires no idealized assumptions.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How does the Random Oracle Model (ROM) differ from Standard Model in cryptographic security proofs?
Mathematically verified cryptographic implementation
```

---

<a id="q57"></a>
### Q57: What is Dual_EC_DRBG and how did the NSA insert an intentional backdoor into a pseudo-random generator?

**Difficulty**: Advanced

**Strategy**:
Dual Elliptic Curve deterministic random bit generator where relationship between points $P$ and $Q$ was known to creators ($Q = e \cdot P$), allowing recovering internal state from 32 bytes.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Dual_EC_DRBG and how did the NSA insert an intentional backdoor into a pseudo-random generator?
Mathematically verified cryptographic implementation
```

---

<a id="q58"></a>
### Q58: How do Memory-Hard Functions (Scrypt, Argon2id) defeat ASIC and GPU password cracking farms?

**Difficulty**: Intermediate

**Strategy**:
Requires allocating hundreds of megabytes of RAM and accessing memory in pseudo-random sequences; hardware cracking rigs are constrained by memory bus bandwidth rather than raw compute.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How do Memory-Hard Functions (Scrypt, Argon2id) defeat ASIC and GPU password cracking farms?
Mathematically verified cryptographic implementation
```

---

<a id="q59"></a>
### Q59: What is Bilinear Diffie-Hellman Assumption (BDH)?

**Difficulty**: Advanced

**Strategy**:
Given $P, aP, bP, cP$, it is computationally intractable to calculate pairing $e(P, P)^{abc}$ without knowing secret exponents.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Bilinear Diffie-Hellman Assumption (BDH)?
Mathematically verified cryptographic implementation
```

---

<a id="q60"></a>
### Q60: How does Multi-Scalar Multiplication (MSM) optimize proof generation speed in zk-SNARKs?

**Difficulty**: Advanced

**Strategy**:
Computes $\sum_{i=1}^N s_i P_i$ over millions of points using Pippenger's Bucket Algorithm, parallelizing computations on GPU CUDA / WebGPU cores.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How does Multi-Scalar Multiplication (MSM) optimize proof generation speed in zk-SNARKs?
Mathematically verified cryptographic implementation
```

---

<a id="q61"></a>
### Q61: What is Number Theoretic Transform (NTT) and how does it accelerate polynomial multiplication in finite fields?

**Difficulty**: Advanced

**Strategy**:
Discrete Fourier Transform evaluated over finite fields $\mathbb{F}_p$ with primitive roots of unity; accelerates polynomial multiplication from $O(N^2)$ to $O(N \log N)$.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Number Theoretic Transform (NTT) and how does it accelerate polynomial multiplication in finite fields?
Mathematically verified cryptographic implementation
```

---

<a id="q62"></a>
### Q62: What is Co-factor Clearing in Elliptic Curve Cryptography?

**Difficulty**: Intermediate

**Strategy**:
Curves with cofactor $h > 1$ contain small subgroups; multiplying points by cofactor $h$ ensures points reside strictly in the prime-order main subgroup, avoiding small subgroup attacks.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Co-factor Clearing in Elliptic Curve Cryptography?
Mathematically verified cryptographic implementation
```

---

<a id="q63"></a>
### Q63: How does Zero-Knowledge Machine Learning (zkML) prove model inferences ran without tampering?

**Difficulty**: Advanced

**Strategy**:
Compiles neural network matrix weights and activations into arithmetic circuits; proves model executed inference on private input with verified accuracy.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How does Zero-Knowledge Machine Learning (zkML) prove model inferences ran without tampering?
Mathematically verified cryptographic implementation
```

---

<a id="q64"></a>
### Q64: What is Quantum Key Distribution (QKD: BB84 protocol)?

**Difficulty**: Advanced

**Strategy**:
Transmits single polarized photons over fiber optic cables; quantum no-cloning theorem guarantees any eavesdropper attempting measurement introduces detectable quantum state errors.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Quantum Key Distribution (QKD: BB84 protocol)?
Mathematically verified cryptographic implementation
```

---

<a id="q65"></a>
### Q65: How does Boneh-Lynn-Shacham (BLS) Short Signature scheme work on pairing-friendly curves?

**Difficulty**: Intermediate

**Strategy**:
Signature is a single curve point $\sigma = H(m)^x$; verified via single pairing equality check $e(\sigma, G) = e(H(m), PK)$.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How does Boneh-Lynn-Shacham (BLS) Short Signature scheme work on pairing-friendly curves?
Mathematically verified cryptographic implementation
```

---

<a id="q66"></a>
### Q66: What is the difference between Perfect Secrecy (One-Time Pad) and Computational Security?

**Difficulty**: Beginner

**Strategy**:
Perfect secrecy: ciphertext reveals mathematically zero information about plaintext even with infinite computing power ($H(M|C) = H(M)$); Computational: breaking cipher requires infeasible compute resources.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is the difference between Perfect Secrecy (One-Time Pad) and Computational Security?
Mathematically verified cryptographic implementation
```

---

<a id="q67"></a>
### Q67: How does the Fiat-Shamir with Aborts technique work in lattice-based signature schemes (Dilithium)?

**Difficulty**: Advanced

**Strategy**:
Discards and re-samples signatures when generated output vectors leak information about the secret key, ensuring signature distribution is independent of secrets.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How does the Fiat-Shamir with Aborts technique work in lattice-based signature schemes (Dilithium)?
Mathematically verified cryptographic implementation
```

---

<a id="q68"></a>
### Q68: What is Threshold ECDSA and how does multi-party computation sign cryptocurrency transactions without reconstructing the private key?

**Difficulty**: Advanced

**Strategy**:
$T$-of-$N$ nodes generate ECDSA signature collaboratively using additive homomorphic secret sharing without any node ever seeing the combined private key.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Threshold ECDSA and how does multi-party computation sign cryptocurrency transactions without reconstructing the private key?
Mathematically verified cryptographic implementation
```

---

<a id="q69"></a>
### Q69: How does Format-Preserving Encryption (FPE: FF1, FF3-1) encrypt credit card numbers while maintaining valid digits?

**Difficulty**: Intermediate

**Strategy**:
Uses Feistel network constructions to encrypt numbers such that 16-digit credit card number encrypts into another valid 16-digit credit card number passing Luhn checksum.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How does Format-Preserving Encryption (FPE: FF1, FF3-1) encrypt credit card numbers while maintaining valid digits?
Mathematically verified cryptographic implementation
```

---

<a id="q70"></a>
### Q70: What is Forward Secure Digital Signatures and how do key-evolving schemes protect past signatures?

**Difficulty**: Advanced

**Strategy**:
Private signing key evolves forward in time via one-way cryptographic functions; compromising key at time $T$ does not allow forging signatures from time $< T$.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Forward Secure Digital Signatures and how do key-evolving schemes protect past signatures?
Mathematically verified cryptographic implementation
```

---

<a id="q71"></a>
### Q71: How do Proof of Solvency protocols (Merkle Tree vs zk-SNARK) prove exchange reserves match liabilities?

**Difficulty**: Intermediate

**Strategy**:
Proves exchange owns assets exceeding user deposit liabilities without revealing individual user account balances or total treasury cold storage addresses.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How do Proof of Solvency protocols (Merkle Tree vs zk-SNARK) prove exchange reserves match liabilities?
Mathematically verified cryptographic implementation
```

---

<a id="q72"></a>
### Q72: What is Broadcast Encryption and how does Pay-TV broadcast encrypted content to authorized subsets?

**Difficulty**: Advanced

**Strategy**:
Encrypts broadcast stream so that only authorized receivers with valid user decoders can decrypt, while revoked subscriptions cannot decrypt stream.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Broadcast Encryption and how does Pay-TV broadcast encrypted content to authorized subsets?
Mathematically verified cryptographic implementation
```

---

<a id="q73"></a>
### Q73: How does S-Box (Substitution Box) provide non-linearity in symmetric ciphers (AES)?

**Difficulty**: Intermediate

**Strategy**:
Maps input bytes through multiplicative inversion in $GF(2^8)$ followed by affine transformation, preventing linear cryptanalysis equations from breaking cipher.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How does S-Box (Substitution Box) provide non-linearity in symmetric ciphers (AES)?
Mathematically verified cryptographic implementation
```

---

<a id="q74"></a>
### Q74: What is Chosen Ciphertext Attack (CCA2) and what is IND-CCA2 security?

**Difficulty**: Intermediate

**Strategy**:
Adversary can query decryption oracle for any ciphertext except the target challenge ciphertext; modern ciphers must be IND-CCA2 secure.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Chosen Ciphertext Attack (CCA2) and what is IND-CCA2 security?
Mathematically verified cryptographic implementation
```

---

<a id="q75"></a>
### Q75: How do Zero-Knowledge Set Membership proofs prove an element exists in an accumulator without revealing the element?

**Difficulty**: Advanced

**Strategy**:
Uses cryptographic accumulators (RSA accumulators or Merkle trees); Prover proves knowledge of witness dividing accumulator polynomial.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How do Zero-Knowledge Set Membership proofs prove an element exists in an accumulator without revealing the element?
Mathematically verified cryptographic implementation
```

---

<a id="q76"></a>
### Q76: What is Electronic Codebook (ECB) Mode and why does it leak plaintext patterns (the ECB Penguin)?

**Difficulty**: Beginner

**Strategy**:
Encrypts identical plaintext blocks into identical ciphertext blocks independently; preserves visual structures and patterns in images and documents.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Electronic Codebook (ECB) Mode and why does it leak plaintext patterns (the ECB Penguin)?
Mathematically verified cryptographic implementation
```

---

<a id="q77"></a>
### Q77: How does Public Key Cryptography Standards (PKCS #1 v1.5 vs OAEP) protect RSA encryption?

**Difficulty**: Intermediate

**Strategy**:
PKCS#1 v1.5 padding is vulnerable to Bleichenbacher oracle attacks; Optimal Asymmetric Encryption Padding (OAEP) uses all-or-nothing transforms and random masks.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How does Public Key Cryptography Standards (PKCS #1 v1.5 vs OAEP) protect RSA encryption?
Mathematically verified cryptographic implementation
```

---

<a id="q78"></a>
### Q78: What is Feistel Cipher Network and how does it construct reversible block ciphers (DES, Blowfish)?

**Difficulty**: Intermediate

**Strategy**:
Splits block into left and right halves ($L_i = R_{i-1}, R_i = L_{i-1} \oplus F(R_{i-1}, K_i)$); round function $F$ does not need to be invertible for decryption.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Feistel Cipher Network and how does it construct reversible block ciphers (DES, Blowfish)?
Mathematically verified cryptographic implementation
```

---

<a id="q79"></a>
### Q79: How does Secret Handshake Protocol establish mutual authentication without revealing identities to eavesdroppers?

**Difficulty**: Advanced

**Strategy**:
Two parties discover they belong to same secret group; if either party is not a member, neither learns the other party's identity or group membership.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How does Secret Handshake Protocol establish mutual authentication without revealing identities to eavesdroppers?
Mathematically verified cryptographic implementation
```

---

<a id="q80"></a>
### Q80: What is Side-Channel Cache-Timing Attack (FLUSH+RELOAD, PRIME+PROBE)?

**Difficulty**: Advanced

**Strategy**:
Monitors time taken to access CPU memory lines; if target cipher accessed memory line during calculation, data resides in cache and loads faster, leaking secret access indices.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Side-Channel Cache-Timing Attack (FLUSH+RELOAD, PRIME+PROBE)?
Mathematically verified cryptographic implementation
```

---

<a id="q81"></a>
### Q81: How does Differential Cryptanalysis analyze symmetric ciphers?

**Difficulty**: Advanced

**Strategy**:
Tracks how specific input differences ($\Delta P$) propagate through cipher rounds to output differences ($\Delta C$), isolating round keys that occur with high probability.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How does Differential Cryptanalysis analyze symmetric ciphers?
Mathematically verified cryptographic implementation
```

---

<a id="q82"></a>
### Q82: What is Secure Enclave Attestation (Intel SGX, AWS Nitro Enclaves)?

**Difficulty**: Intermediate

**Strategy**:
Hardware generates cryptographically signed attestation report containing SHA-256 hash of loaded enclave memory, proving code authenticity to remote verifiers.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Secure Enclave Attestation (Intel SGX, AWS Nitro Enclaves)?
Mathematically verified cryptographic implementation
```

---

<a id="q83"></a>
### Q83: How do Zero-Knowledge Contingent Payments allow atomic fair exchange of data for cryptocurrency?

**Difficulty**: Advanced

**Strategy**:
Buyer encrypts payment; seller encrypts data; ZK proof proves ciphertext contains requested data and decrypts with key revealed upon claiming funds on blockchain.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How do Zero-Knowledge Contingent Payments allow atomic fair exchange of data for cryptocurrency?
Mathematically verified cryptographic implementation
```

---

<a id="q84"></a>
### Q84: What is Ring Learning With Errors (Ring-LWE) in Post-Quantum Cryptography?

**Difficulty**: Advanced

**Strategy**:
Lattice problem over polynomial rings; adds small noise polynomials to polynomial multiplications; solving secret is as hard as ideal lattice shortest vector problems.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Ring Learning With Errors (Ring-LWE) in Post-Quantum Cryptography?
Mathematically verified cryptographic implementation
```

---

<a id="q85"></a>
### Q85: How does Elliptic Curve Diffie-Hellman (ECDH) handle invalid curve attacks?

**Difficulty**: Advanced

**Strategy**:
Attacker sends point not on curve; if receiver does not validate $y^2 = x^3 + ax + b$, computation occurs on weak small-order curve, leaking private key; mitigated by strict point validation.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How does Elliptic Curve Diffie-Hellman (ECDH) handle invalid curve attacks?
Mathematically verified cryptographic implementation
```

---

<a id="q86"></a>
### Q86: What is Verifiable Encryption and how is it used in key escrow systems?

**Difficulty**: Advanced

**Strategy**:
Encrypts secret value under public key while producing a ZK proof proving the ciphertext contains a valid secret satisfying specific mathematical properties.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Verifiable Encryption and how is it used in key escrow systems?
Mathematically verified cryptographic implementation
```

---

<a id="q87"></a>
### Q87: How does Key Separation using Domain Separation Tags (DST) prevent cross-protocol attacks?

**Difficulty**: Intermediate

**Strategy**:
Prefixes message digests with distinct protocol string (`DST = "MY_PROTOCOL_V1_SIG_"`); prevents valid signatures in one protocol from being reused in another.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How does Key Separation using Domain Separation Tags (DST) prevent cross-protocol attacks?
Mathematically verified cryptographic implementation
```

---

<a id="q88"></a>
### Q88: What is Merkle-Damgard Construction and how does it build hash functions from compression functions?

**Difficulty**: Beginner

**Strategy**:
Splits message into fixed blocks; iteratively feeds block and previous chaining variable into one-way compression function ($H_i = f(H_{i-1}, M_i)$).

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Merkle-Damgard Construction and how does it build hash functions from compression functions?
Mathematically verified cryptographic implementation
```

---

<a id="q89"></a>
### Q89: How do Oblivious RAM (ORAM: Path ORAM) protocols hide memory access patterns in untrusted storage?

**Difficulty**: Advanced

**Strategy**:
Accesses data stored in a binary tree of buckets; continuously shuffles and re-encrypts data paths on every read, ensuring cloud host cannot infer which record was queried.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How do Oblivious RAM (ORAM: Path ORAM) protocols hide memory access patterns in untrusted storage?
Mathematically verified cryptographic implementation
```

---

<a id="q90"></a>
### Q90: What is Homomorphic Commitment (Pedersen Commitment) and how does it hide values while allowing addition?

**Difficulty**: Advanced

**Strategy**:
Commitment $C = vG + rH$ where $r$ is blinding factor; homomorphic property allows $C_1 + C_2 = (v_1 + v_2)G + (r_1 + r_2)H$, proving balance preservation in zero-knowledge.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Homomorphic Commitment (Pedersen Commitment) and how does it hide values while allowing addition?
Mathematically verified cryptographic implementation
```

---

<a id="q91"></a>
### Q91: How does Meet-in-the-Middle Attack break Double DES and motivate Triple DES (3DES)?

**Difficulty**: Intermediate

**Strategy**:
Encrypt from plaintext and decrypt from ciphertext; stores $2^{56}$ intermediate values; finding match breaks 112-bit Double DES in $2^{57}$ operations, requiring 3DES with 3 independent keys.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How does Meet-in-the-Middle Attack break Double DES and motivate Triple DES (3DES)?
Mathematically verified cryptographic implementation
```

---

<a id="q92"></a>
### Q92: What is the role of Quadratic Residues in cryptographic protocols (Goldwasser-Micali encryption)?

**Difficulty**: Advanced

**Strategy**:
An integer $a$ is a quadratic residue modulo $n$ if $x^2 \equiv a \pmod n$ has a solution; Goldwasser-Micali encrypts bits by selecting quadratic residues or non-residues.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is the role of Quadratic Residues in cryptographic protocols (Goldwasser-Micali encryption)?
Mathematically verified cryptographic implementation
```

---

<a id="q93"></a>
### Q93: How do Threshold Decryption systems prevent unauthorized decryption without consensus?

**Difficulty**: Advanced

**Strategy**:
Private key is split among $N$ key holders; at least $K$ holders must compute partial decryption shares, combined to decrypt ciphertext.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How do Threshold Decryption systems prevent unauthorized decryption without consensus?
Mathematically verified cryptographic implementation
```

---

<a id="q94"></a>
### Q94: What is Side-Channel Acoustic Cryptanalysis?

**Difficulty**: Intermediate

**Strategy**:
Recording high-frequency acoustic noise emitted by capacitors and voltage regulators on motherboards during CPU RSA decryption calculations leaks private keys.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Side-Channel Acoustic Cryptanalysis?
Mathematically verified cryptographic implementation
```

---

<a id="q95"></a>
### Q95: How does Curve448 differ from Curve25519 in security margin and performance?

**Difficulty**: Intermediate

**Strategy**:
Curve448 provides 224-bit security level (comparable to SHA-384 / AES-256); Curve25519 provides 128-bit security level (faster, standard default).

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How does Curve448 differ from Curve25519 in security margin and performance?
Mathematically verified cryptographic implementation
```

---

<a id="q96"></a>
### Q96: What is the difference between Public Key Compression and Uncompressed Keys in secp256k1?

**Difficulty**: Beginner

**Strategy**:
Uncompressed keys are 65 bytes starting with 0x04 followed by X and Y coordinates; Compressed keys are 33 bytes starting with 0x02 or 0x03 followed by X coordinate.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is the difference between Public Key Compression and Uncompressed Keys in secp256k1?
Mathematically verified cryptographic implementation
```

---

<a id="q97"></a>
### Q97: How does the Fiat-Shamir Transform guarantee soundness in interactive proof systems?

**Difficulty**: Advanced

**Strategy**:
Replaces the verifier's random challenge with a cryptographic hash of the execution transcript, preventing a cheating prover from predicting challenges.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How does the Fiat-Shamir Transform guarantee soundness in interactive proof systems?
Mathematically verified cryptographic implementation
```

---

<a id="q98"></a>
### Q98: What is Multi-Party Computation (MPC) Threshold Signatures vs Multisig Smart Contracts?

**Difficulty**: Intermediate

**Strategy**:
Multisig executes on-chain with multiple signatures and higher gas fees; MPC creates a single valid ECDSA signature off-chain without on-chain signature overhead.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Multi-Party Computation (MPC) Threshold Signatures vs Multisig Smart Contracts?
Mathematically verified cryptographic implementation
```

---

<a id="q99"></a>
### Q99: How do Zero-Knowledge Identity Proofs (Semaphore, zk-ID) prove group membership anonymously?

**Difficulty**: Advanced

**Strategy**:
Prover inserts identity commitment into a Merkle tree; generates a zk-SNARK proof proving knowledge of private key in Merkle tree with nullifiers preventing double-actions.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: How do Zero-Knowledge Identity Proofs (Semaphore, zk-ID) prove group membership anonymously?
Mathematically verified cryptographic implementation
```

---

<a id="q100"></a>
### Q100: What is Linear Cryptanalysis in block ciphers?

**Difficulty**: Advanced

**Strategy**:
Discovers high-probability linear approximations between plaintext bits, ciphertext bits, and secret key bits across multiple encryption rounds.

**Code Example**:
```text
Cryptographic Specification & ZK Architecture for: What is Linear Cryptanalysis in block ciphers?
Mathematically verified cryptographic implementation
```

---
