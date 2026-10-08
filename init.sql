-- ==============================================================================
-- Interview Guide Platform - PostgreSQL Database Initialization (init.sql)
-- Complete schema for setting up a fresh production / staging database server
-- ==============================================================================

-- Enable UUID extension for cryptographically secure identifiers
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- 1. Topics / Categories Table
CREATE TABLE IF NOT EXISTS categories (
    id VARCHAR(64) PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    description TEXT,
    icon_path VARCHAR(255) DEFAULT 'html-css-js-icon.svg',
    total_questions INT DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2. Questions & Answers Table
CREATE TABLE IF NOT EXISTS questions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    category_id VARCHAR(64) NOT NULL REFERENCES categories(id) ON DELETE CASCADE,
    question_number INT NOT NULL,
    title VARCHAR(512) NOT NULL,
    difficulty VARCHAR(32) CHECK (difficulty IN ('Beginner', 'Intermediate', 'Advanced', 'Expert')),
    strategy TEXT,
    answer_markdown TEXT NOT NULL,
    code_example TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uq_category_qnum UNIQUE (category_id, question_number)
);

-- 3. Users Table (Authentication & Accounts)
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(128),
    role VARCHAR(32) DEFAULT 'user' CHECK (role IN ('user', 'admin', 'editor')),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 4. User Bookmarks / Saved Questions
CREATE TABLE IF NOT EXISTS user_bookmarks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    question_id UUID NOT NULL REFERENCES questions(id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uq_user_bookmark UNIQUE (user_id, question_id)
);

-- 5. User Custom Notes on Questions
CREATE TABLE IF NOT EXISTS user_question_notes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    question_id UUID NOT NULL REFERENCES questions(id) ON DELETE CASCADE,
    note_content TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uq_user_note UNIQUE (user_id, question_id)
);

-- 6. User Study Progress & Mastery Tracking (SM-18 Spaced Repetition Item #11)
CREATE TABLE IF NOT EXISTS user_study_progress (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    question_id UUID NOT NULL REFERENCES questions(id) ON DELETE CASCADE,
    status VARCHAR(32) DEFAULT 'unseen' CHECK (status IN ('unseen', 'learning', 'mastered', 'needs_review')),
    review_count INT DEFAULT 0,
    interval_days INT DEFAULT 1,
    stability NUMERIC(6, 3) DEFAULT 2.5,
    retrievability NUMERIC(5, 4) DEFAULT 1.0,
    difficulty NUMERIC(5, 3) DEFAULT 0.3,
    next_review_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_reviewed_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uq_user_progress UNIQUE (user_id, question_id)
);

-- 7. Platform Telemetry & Search Logs
CREATE TABLE IF NOT EXISTS search_telemetry (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE SET NULL,
    search_query VARCHAR(255) NOT NULL,
    results_count INT DEFAULT 0,
    execution_time_ms NUMERIC(8, 2),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for Ultra-Fast Lookups
CREATE INDEX IF NOT EXISTS idx_questions_cat ON questions(category_id);
CREATE INDEX IF NOT EXISTS idx_questions_diff ON questions(difficulty);
CREATE INDEX IF NOT EXISTS idx_bookmarks_user ON user_bookmarks(user_id);
CREATE INDEX IF NOT EXISTS idx_progress_user ON user_study_progress(user_id, status);
CREATE INDEX IF NOT EXISTS idx_telemetry_created ON search_telemetry(created_at);

-- Initial Category Seed Data
INSERT INTO categories (id, name, description, total_questions) VALUES
('javascript', 'JavaScript', 'Core JS, ES6+, Closures, Event Loop, Memory, Promises', 100),
('react', 'React.js', 'React 18/19, Hooks, Fiber Architecture, Server Components, Suspense', 100),
('nextjs', 'Next.js', 'App Router, Server Actions, Caching, Middleware, ISR', 100),
('angular', 'Angular 14-18', 'Standalone Components, Signals, RxJS, DI, Directives', 100),
('vue', 'Vue.js 3', 'Composition API, Reactivity, Pinia, Nuxt 3, Teleport', 100),
('html', 'HTML5 & Web APIs', 'Semantic HTML, Accessibility, Web Components, Service Workers', 100),
('tailwind-bootstrap', 'Tailwind & Bootstrap', 'Tailwind JIT, Design Tokens, CSS Grid, Utility API', 100),
('webpack-babel-vite', 'Webpack, Babel & Vite', 'Native ESM, Module Federation, AST Plugins, HMR', 100),
('ngrx', 'NgRx', 'Store, Effects, Entity, ComponentStore, SignalStore', 100),
('redux-zustand', 'Redux & Zustand', 'RTK Query, Immer, Zustand Slices, State Optimization', 100),
('nodejs', 'Node.js', 'Event Loop, libuv, Streams, Worker Threads, Microservices', 100),
('java', 'Java & Spring Boot', 'Virtual Threads, JVM Memory, Spring Boot 3, Concurrency', 100),
('cpp', 'Modern C++', 'Move Semantics, RAII, Memory Model, Concepts, C++20/23', 100),
('dotnet', '.NET 8 & C# 12', 'CLR GC, Span<T>, Async State Machines, ASP.NET Core', 100),
('rust', 'Rust 2024 & Tokio', 'Ownership, Lifetimes, Tokio Async, Pinning, Memory Safety', 100),
('swift-swiftui', 'Swift & SwiftUI', 'Swift Concurrency, SwiftUI, ARC, SwiftData, iOS Architecture', 100),
('kotlin', 'Kotlin & Android', 'Coroutines, Jetpack Compose, Flows, KMP, Android Lifecycle', 100),
('flutter', 'Flutter & Dart', 'Widget Trees, Isolates, Bloc, Riverpod, Impeller Engine', 100),
('react-native', 'React Native', 'New Architecture, Fabric, JSI, Hermes, Reanimated 3', 100),
('docker', 'Docker & Containers', 'Namespaces, Cgroups, Multi-Stage Builds, OverlayFS', 100),
('aws', 'AWS Cloud Architecture', 'Serverless, Well-Architected Framework, DynamoDB, IAM', 100),
('performance', 'Web Performance', 'Core Web Vitals, Critical Rendering Path, GPU Compositing', 100),
('integration', 'Integration & APIs', 'REST, GraphQL, gRPC, OAuth2 PKCE, Webhooks, API Gateways', 209),
('typescript', 'TypeScript', 'Type System, Generics, Conditional Types, tsconfig', 100),
('security', 'Application Security', 'XSS, CSRF, SQLi, CSP, JWT Security, Cryptography', 100),
('testing', 'Testing & QA', 'Unit Testing, MSW, RTL, Playwright, Mocking', 100),
('data-structures', 'Data Structures', 'Arrays, Trees, Graphs, Heaps, Hash Tables, Big-O', 100),
('algorithms', 'Algorithms', 'Dynamic Programming, Graph Traversal, Sorting, Searching', 100),
('css', 'CSS3 & Modern Styling', 'Flexbox, CSS Grid, Custom Properties, Animations', 103),
('database', 'Database & SQL', 'Indexing, ACID, Query Optimization, Sharding, Replication', 101),
('design-patterns', 'Design Patterns', 'Creational, Structural, Behavioral, Clean Code', 101),
('git', 'Git Version Control', 'Branching, Rebasing, Worktrees, Cherry-pick, Reflog', 100),
('golang', 'Go (Golang)', 'Goroutines, Channels, Interfaces, Garbage Collector', 100),
('graphql', 'GraphQL', 'Schema Design, Resolvers, Subscriptions, DataLoader', 101),
('kubernetes', 'Kubernetes', 'Pods, Deployments, Services, Ingress, Operators, Helm', 100),
('linux', 'Linux & Shell', 'Kernel, Inodes, Systemd, Process Signals, Bash Scripting', 100),
('material-radix-ui', 'Material & Radix UI', 'Component Primitives, WAI-ARIA, Theming, Customization', 100),
('microfrontend', 'Micro-frontends', 'Module Federation, Single-SPA, Web Components, Routing', 101),
('microservices', 'Microservices', 'Service Discovery, Saga Pattern, Circuit Breakers, Kafka', 101),
('python', 'Python & Django', 'GIL, Asyncio, Generators, Metaclasses, Django ORM', 100),
('svelte', 'Svelte & SvelteKit', 'Runes, Svelte 5, Compiler Reactivity, SSR, Hydration', 102),
('system-design', 'System Design', 'Scalability, Load Balancing, Caching, CAP Theorem, Event-Driven', 132),
('behavioral', 'Behavioral & Leadership (STAR)', 'STAR Method, Conflict Resolution, System Outages, and Leadership', 100),
('devsecops', 'DevSecOps & Threat Modeling', 'STRIDE, Zero-Trust, Supply Chain Security, SBOM, and Container Hardening', 100),
('ai-engineering', 'AI Engineering & LLMs', 'RAG, Transformers, LoRA, Vector Databases, and Agents', 100),
('sre', 'Site Reliability Engineering (SRE)', 'SLOs, Error Budgets, OpenTelemetry, Incident Response, and Chaos Engineering', 100),
('fintech', 'Low-Latency FinTech & High-Frequency Systems', 'Kernel Bypass, DPDK, LMAX Disruptor, Limit Order Books, and FIX Protocol', 100),
('embedded', 'Embedded Systems & RTOS', 'FreeRTOS, Priority Inversion, Memory-Mapped I/O, ISRs, and DMA', 100),
('web3-solidity', 'Web3 & Solidity Security', 'Reentrancy, Storage Slot Packing, Flash Loans, EVM Internals, and MEV', 100),
('compiler-design', 'Compiler Design & LLVM', 'SSA Form, LR Parsers, JIT Compilation, LLVM IR, and Register Allocation', 100),
('linux-kernel-ebpf', 'Linux Kernel & eBPF Engineering', 'eBPF Verifier, XDP Line-Rate Packet Filtering, Ring Buffers, and Kernel Internals', 100),
('distributed-storage', 'Distributed Storage & Filesystems', 'Ceph CRUSH, LSM Trees, NVMe-oF, Erasure Coding, and ZFS', 100),
('cryptography-zk', 'Applied Cryptography & Zero-Knowledge', 'ECDSA, zk-SNARKs, AES-GCM AEAD, Constant-Time Implementations, and R1CS', 100),
('graphics-webgpu', 'Computer Graphics & WebGPU', 'WebGPU Compute Pipelines, WGSL, Memory Coalescing, PSOs, and Workgroups', 100),
('networking-protocols', 'Modern Networking Protocols (HTTP/3, QUIC, gRPC)', 'HTTP/3, QUIC 0-RTT, Head-of-Line Blocking, Protobuf Varints, and BBR', 100)
ON CONFLICT (id) DO UPDATE SET 
    name = EXCLUDED.name,
    description = EXCLUDED.description,
    total_questions = EXCLUDED.total_questions,
    updated_at = CURRENT_TIMESTAMP;

-- 8. Mock Quizzes & Test Sessions Table
CREATE TABLE IF NOT EXISTS mock_quizzes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE SET NULL,
    category_id VARCHAR(64) REFERENCES categories(id) ON DELETE SET NULL,
    title VARCHAR(255) NOT NULL,
    duration_minutes INT DEFAULT 45,
    score_percentage NUMERIC(5, 2),
    total_questions INT NOT NULL,
    correct_answers INT DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 9. Code Playground Submissions Table
CREATE TABLE IF NOT EXISTS code_playground_submissions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE SET NULL,
    language VARCHAR(32) NOT NULL,
    code_content TEXT NOT NULL,
    execution_output TEXT,
    execution_time_ms NUMERIC(8, 2),
    status VARCHAR(32) DEFAULT 'success',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_quizzes_user ON mock_quizzes(user_id);
CREATE INDEX IF NOT EXISTS idx_playground_user ON code_playground_submissions(user_id);

-- 10. User Daily Streaks & Elo Ratings
CREATE TABLE IF NOT EXISTS user_streaks (
    user_id UUID PRIMARY KEY REFERENCES users(id) ON DELETE CASCADE,
    current_streak INT DEFAULT 0,
    longest_streak INT DEFAULT 0,
    elo_rating INT DEFAULT 1500,
    last_activity_date DATE DEFAULT CURRENT_DATE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 11. Gamification Achievement Badges
CREATE TABLE IF NOT EXISTS user_badges (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    badge_id VARCHAR(64) NOT NULL,
    badge_name VARCHAR(128) NOT NULL,
    badge_description TEXT,
    icon VARCHAR(64),
    unlocked_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uq_user_badge UNIQUE (user_id, badge_id)
);

-- 12. Company Specific Interview Tracks
CREATE TABLE IF NOT EXISTS company_tracks (
    id VARCHAR(64) PRIMARY KEY,
    company_name VARCHAR(128) NOT NULL,
    description TEXT,
    difficulty VARCHAR(32) DEFAULT 'Advanced',
    target_roles TEXT[],
    total_questions INT DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 13. Candidate Readiness Index Certificates
CREATE TABLE IF NOT EXISTS candidate_certificates (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    certificate_number VARCHAR(64) UNIQUE NOT NULL,
    candidate_name VARCHAR(128) NOT NULL,
    candidate_email VARCHAR(255) NOT NULL,
    score_percentage NUMERIC(5, 2) NOT NULL,
    domains_mastered TEXT[] NOT NULL,
    signature_sha256 VARCHAR(64) NOT NULL,
    issued_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 14. B2B Recruiter Assessments
CREATE TABLE IF NOT EXISTS recruiter_assessments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    token VARCHAR(64) UNIQUE NOT NULL,
    recruiter_email VARCHAR(255) NOT NULL,
    title VARCHAR(255) NOT NULL,
    target_role VARCHAR(128) NOT NULL,
    duration_minutes INT DEFAULT 60,
    categories TEXT[] NOT NULL,
    question_count INT DEFAULT 15,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 15. Candidate Assessment Submissions & Anti-Cheating Telemetry
CREATE TABLE IF NOT EXISTS recruiter_submissions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    assessment_id UUID NOT NULL REFERENCES recruiter_assessments(id) ON DELETE CASCADE,
    candidate_name VARCHAR(128) NOT NULL,
    candidate_email VARCHAR(255) NOT NULL,
    score_percentage NUMERIC(5, 2) NOT NULL,
    tab_blur_count INT DEFAULT 0,
    full_screen_exit_count INT DEFAULT 0,
    duration_seconds INT NOT NULL,
    submitted_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 16. Assessment Audit Logs (Anti-Cheating Trail)
CREATE TABLE IF NOT EXISTS assessment_audit_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    submission_id UUID REFERENCES recruiter_submissions(id) ON DELETE CASCADE,
    event_type VARCHAR(64) NOT NULL, -- 'window_blur', 'window_focus', 'copy_paste', 'devtools_open'
    event_payload JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 17. ATS Integration Hooks (Greenhouse, Lever, Ashby)
CREATE TABLE IF NOT EXISTS ats_integrations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    provider VARCHAR(64) NOT NULL, -- 'greenhouse', 'lever', 'ashby'
    webhook_url VARCHAR(512) NOT NULL,
    api_key_hash VARCHAR(255) NOT NULL,
    is_enabled BOOLEAN DEFAULT TRUE,
    last_synced_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_badges_user ON user_badges(user_id);
CREATE INDEX IF NOT EXISTS idx_cert_number ON candidate_certificates(certificate_number);
CREATE INDEX IF NOT EXISTS idx_assessment_token ON recruiter_assessments(token);
CREATE INDEX IF NOT EXISTS idx_submissions_assessment ON recruiter_submissions(assessment_id);
CREATE INDEX IF NOT EXISTS idx_audit_submission ON assessment_audit_logs(submission_id);

-- 18. Global Competency Leaderboard
CREATE TABLE IF NOT EXISTS leaderboard_entries (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username VARCHAR(64) NOT NULL,
    elo_rating INT DEFAULT 1200,
    tier VARCHAR(32) DEFAULT 'Junior',
    battles_won INT DEFAULT 0,
    battles_lost INT DEFAULT 0,
    questions_solved INT DEFAULT 0,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 19. Real-Time P2P Coding Battles
CREATE TABLE IF NOT EXISTS coding_battles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    battle_token VARCHAR(64) UNIQUE NOT NULL,
    category_id VARCHAR(64) NOT NULL,
    question_number INT NOT NULL,
    host_username VARCHAR(64) NOT NULL,
    peer_username VARCHAR(64),
    winner_username VARCHAR(64),
    status VARCHAR(32) DEFAULT 'WAITING', -- 'WAITING', 'ACTIVE', 'COMPLETED', 'ABORTED'
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 20. Candidate Custom Curated Decks
CREATE TABLE IF NOT EXISTS custom_decks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id VARCHAR(64) NOT NULL,
    title VARCHAR(128) NOT NULL,
    description TEXT,
    tags TEXT[],
    questions JSONB NOT NULL DEFAULT '[]'::jsonb,
    is_public BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 21. Keystroke Dynamics Biometric Fingerprints
CREATE TABLE IF NOT EXISTS keystroke_fingerprints (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    submission_id UUID REFERENCES recruiter_submissions(id) ON DELETE CASCADE,
    flight_time_avg_ms NUMERIC(6, 2) NOT NULL,
    dwell_time_avg_ms NUMERIC(6, 2) NOT NULL,
    entropy_score NUMERIC(5, 2) NOT NULL,
    anomaly_detected BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 22. W3C-Compatible Verifiable Credentials
CREATE TABLE IF NOT EXISTS verifiable_credentials (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    credential_id VARCHAR(128) UNIQUE NOT NULL,
    candidate_did VARCHAR(128) NOT NULL,
    issuer_did VARCHAR(128) NOT NULL,
    certificate_number VARCHAR(64) REFERENCES candidate_certificates(certificate_number) ON DELETE CASCADE,
    proof_signature VARCHAR(256) NOT NULL,
    claim_data JSONB NOT NULL,
    issued_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 23. Daily Streak Freeze Bank
CREATE TABLE IF NOT EXISTS streak_freezes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id VARCHAR(64) UNIQUE NOT NULL,
    available_freezes INT DEFAULT 2,
    used_freezes INT DEFAULT 0,
    last_freeze_applied_at TIMESTAMP WITH TIME ZONE,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_leaderboard_elo ON leaderboard_entries(elo_rating DESC);
CREATE INDEX IF NOT EXISTS idx_battle_token ON coding_battles(battle_token);
CREATE INDEX IF NOT EXISTS idx_custom_decks_user ON custom_decks(user_id);
CREATE INDEX IF NOT EXISTS idx_credentials_id ON verifiable_credentials(credential_id);

-- 23b. Auth Refresh Tokens (only SHA-256 hashes are stored; rotated on every refresh)
CREATE TABLE IF NOT EXISTS refresh_tokens (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    token_hash VARCHAR(64) UNIQUE NOT NULL,
    user_agent VARCHAR(255),
    expires_at TIMESTAMP WITH TIME ZONE NOT NULL,
    revoked_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_refresh_tokens_user ON refresh_tokens(user_id);
CREATE INDEX IF NOT EXISTS idx_refresh_tokens_expiry ON refresh_tokens(expires_at);

-- 23c. Append-Only Tamper-Evident Audit Ledger (SHA-256 Hash Chained)
CREATE TABLE IF NOT EXISTS platform_audit_ledger (
    sequence_id BIGSERIAL PRIMARY KEY,
    event_type VARCHAR(64) NOT NULL,
    actor_id UUID REFERENCES users(id) ON DELETE SET NULL,
    target_id VARCHAR(128),
    payload_json JSONB NOT NULL DEFAULT '{}'::jsonb,
    prev_hash VARCHAR(64) NOT NULL,
    curr_hash VARCHAR(64) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_audit_actor ON platform_audit_ledger(actor_id);
CREATE INDEX IF NOT EXISTS idx_audit_event ON platform_audit_ledger(event_type);

-- 23d. WebAuthn / Passkey Registered Credentials
CREATE TABLE IF NOT EXISTS webauthn_credentials (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    credential_id TEXT NOT NULL UNIQUE,
    public_key BYTEA NOT NULL,
    counter BIGINT NOT NULL DEFAULT 0,
    aaguid UUID,
    transports TEXT[],
    nickname VARCHAR(100) NOT NULL DEFAULT 'Passkey',
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_used_at TIMESTAMP WITH TIME ZONE
);
CREATE INDEX IF NOT EXISTS idx_webauthn_user ON webauthn_credentials(user_id);

-- 23e. WebAuthn Transient Challenges
CREATE TABLE IF NOT EXISTS webauthn_challenges (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    challenge TEXT NOT NULL,
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    challenge_type VARCHAR(32) NOT NULL,
    expires_at TIMESTAMP WITH TIME ZONE NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_webauthn_challenge_exp ON webauthn_challenges(expires_at);

-- 23f. Web Push Subscriptions (Item #15)
CREATE TABLE IF NOT EXISTS push_subscriptions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    endpoint TEXT NOT NULL UNIQUE,
    p256dh TEXT NOT NULL,
    auth TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_push_subs_user ON push_subscriptions(user_id);

-- 23g. Timed Contests (Item #12)
CREATE TABLE IF NOT EXISTS timed_contests (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    contest_code VARCHAR(64) UNIQUE NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    difficulty VARCHAR(32) DEFAULT 'medium',
    category VARCHAR(64),
    start_time TIMESTAMP WITH TIME ZONE NOT NULL,
    duration_minutes INT DEFAULT 60,
    created_by UUID REFERENCES users(id) ON DELETE SET NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 23h. Contest Participants (Item #12)
CREATE TABLE IF NOT EXISTS contest_participants (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    contest_id UUID REFERENCES timed_contests(id) ON DELETE CASCADE,
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    score INT DEFAULT 0,
    time_taken_seconds INT DEFAULT 0,
    finished_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(contest_id, user_id)
);
CREATE INDEX IF NOT EXISTS idx_contest_part_contest ON contest_participants(contest_id);
CREATE INDEX IF NOT EXISTS idx_contest_part_user ON contest_participants(user_id);

-- 23i. Platform Webhooks (Item #13)
CREATE TABLE IF NOT EXISTS platform_webhooks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    service_name VARCHAR(50) NOT NULL,
    webhook_url TEXT NOT NULL,
    events_subscribed TEXT[] NOT NULL DEFAULT '{"contest_completed", "streak_milestone"}',
    is_active BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_webhooks_user ON platform_webhooks(user_id);

-- 24. Initial Seed Data: Users
-- Passwords are random and unknown (locked accounts). Set a real password after setup:
--   UPDATE users SET password_hash = crypt('<new-password>', gen_salt('bf')) WHERE email = 'admin@interviewguide.internal';
INSERT INTO users (id, email, password_hash, full_name, role) VALUES
('00000000-0000-0000-0000-000000000001', 'admin@interviewguide.internal', crypt(gen_random_uuid()::text, gen_salt('bf')), 'Platform Administrator', 'admin'),
('00000000-0000-0000-0000-000000000002', 'demo@interviewguide.internal', crypt(gen_random_uuid()::text, gen_salt('bf')), 'Demo Candidate', 'user')
ON CONFLICT (email) DO NOTHING;

-- 25. Initial Seed Data: Company Tracks
INSERT INTO company_tracks (id, company_name, description, difficulty, target_roles, total_questions) VALUES
('google', 'Google L5/L6 Core Systems Track', 'Deep distributed systems, Paxos/Raft, high-throughput caching, and complex concurrent algorithms.', 'Expert', ARRAY['Staff Engineer', 'Senior Systems Architect'], 85),
('meta', 'Meta Production Engineering Track', 'Linux kernel internals, eBPF telemetry, high-scale service architecture, and performance profiling.', 'Expert', ARRAY['Production Engineer', 'Senior Infrastructure Engineer'], 92),
('amazon', 'Amazon Principal SDE Track', 'Distributed storage (Dynamo), cell-based architecture, multi-region active-active resilience, and leadership principles.', 'Advanced', ARRAY['Principal SDE', 'Senior Cloud Architect'], 78),
('netflix', 'Netflix Reliability & Resilience Track', 'Chaos engineering, Envoy service mesh, zero-downtime deployments, and global low-latency streaming pipelines.', 'Advanced', ARRAY['Chaos Engineer', 'Senior Backend Engineer'], 64),
('apple', 'Apple Core OS & Low-Latency Track', 'C/C++ runtime internals, memory barriers, RTOS primitives, and hardware-software co-design.', 'Expert', ARRAY['Embedded Software Engineer', 'CoreOS Engineer'], 70)
ON CONFLICT (id) DO NOTHING;

-- 26. Initial Seed Data: Global Leaderboard
INSERT INTO leaderboard_entries (username, elo_rating, tier, battles_won, battles_lost, questions_solved) VALUES
('alex_systems', 2150, 'Principal', 42, 3, 420),
('maria_algo', 1980, 'Staff', 36, 6, 385),
('chen_distributed', 1890, 'Staff', 31, 8, 350),
('david_kernel', 1820, 'Senior', 27, 9, 310),
('priya_frontend', 1760, 'Senior', 24, 11, 295)
ON CONFLICT DO NOTHING;

-- 27. Initial Seed Data: Streak Freeze Bank
INSERT INTO streak_freezes (user_id, available_freezes, used_freezes) VALUES
('00000000-0000-0000-0000-000000000002', 2, 0)
ON CONFLICT (user_id) DO NOTHING;

-- 28. Initial Seed Data: Timed Contests
INSERT INTO timed_contests (contest_code, title, description, difficulty, category, start_time, duration_minutes) VALUES
('WEEKLY-CONTEST-101', 'Distributed Consensus & Raft Challenge', 'Deep dive contest on Paxos, Raft leader election, log replication, and split-brain resolution under partition.', 'expert', 'distributed-storage', NOW() - INTERVAL '1 hour', 60),
('WEEKLY-CONTEST-102', 'High-Throughput Linux Kernel & eBPF Sprint', 'Profiling XDP packet steering, ring buffers, memory maps, and kernel bypass zero-copy networking.', 'advanced', 'linux-kernel-ebpf', NOW() + INTERVAL '2 hours', 45),
('WEEKLY-CONTEST-103', 'Algorithms: Graph & Dynamic Programming Sprint', 'Competitive algorithms contest covering Bellman-Ford, Tarjan SCC, bitmask DP, and max-flow min-cut.', 'intermediate', 'algorithms', NOW() + INTERVAL '1 day', 90)
ON CONFLICT (contest_code) DO NOTHING;



