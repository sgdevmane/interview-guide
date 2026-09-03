use crate::models::{Category, Question, SearchResult};
use regex::Regex;
use std::collections::HashMap;
use std::fs;
use std::path::Path;
use std::sync::Arc;
use tokio::sync::RwLock;

#[derive(Clone, Default)]
pub struct ContentStore {
    pub categories: Vec<Category>,
    pub questions: HashMap<String, Vec<Question>>,
}

pub type SharedStore = Arc<RwLock<ContentStore>>;

pub fn load_content_from_markdowns(base_path: &Path) -> ContentStore {
    let mut store = ContentStore::default();
    let q_regex = Regex::new(r#"(?s)<a id="q(\d+)"></a>\s*\n### Q\d+:\s*(.*?)\n\*\*Difficulty\*\*:\s*<span class=".*?">(.*?)</span>\s*(.*?)(?:---|<a id="q\d+">|$)"#).unwrap();
    let strat_regex = Regex::new(r#"\*\*Strategy\*\*:\s*(.*?)(?:\n\n|\n\*\*Code Example\*\*)"#).unwrap();
    let code_regex = Regex::new(r#"(?s)\*\*Code Example\*\*:\s*```(?:\w+)?\n(.*?)```"#).unwrap();

    let category_dirs = vec![
        ("javascript", "JavaScript", "Core JS, ES6+, Closures, Event Loop, Memory, Promises", "html-css-js-icon.svg"),
        ("react", "React.js", "React 18/19, Hooks, Fiber Architecture, Server Components, Suspense", "html-css-js-icon.svg"),
        ("nextjs", "Next.js", "App Router, Server Actions, Caching, Middleware, ISR", "html-css-js-icon.svg"),
        ("angular", "Angular 14-18", "Standalone Components, Signals, RxJS, DI, Directives", "html-css-js-icon.svg"),
        ("vue", "Vue.js 3", "Composition API, Reactivity, Pinia, Nuxt 3, Teleport", "html-css-js-icon.svg"),
        ("html", "HTML5 & Web APIs", "Semantic HTML, Accessibility, Web Components, Service Workers", "html-css-js-icon.svg"),
        ("tailwind-bootstrap", "Tailwind & Bootstrap", "Tailwind JIT, Design Tokens, CSS Grid, Utility API", "html-css-js-icon.svg"),
        ("webpack-babel-vite", "Webpack, Babel & Vite", "Native ESM, Module Federation, AST Plugins, HMR", "html-css-js-icon.svg"),
        ("ngrx", "NgRx", "Store, Effects, Entity, ComponentStore, SignalStore", "html-css-js-icon.svg"),
        ("redux-zustand", "Redux & Zustand", "RTK Query, Immer, Zustand Slices, State Optimization", "html-css-js-icon.svg"),
        ("nodejs", "Node.js", "Event Loop, libuv, Streams, Worker Threads, Microservices", "html-css-js-icon.svg"),
        ("java", "Java & Spring Boot", "Virtual Threads, JVM Memory, Spring Boot 3, Concurrency", "html-css-js-icon.svg"),
        ("cpp", "Modern C++", "Move Semantics, RAII, Memory Model, Concepts, C++20/23", "html-css-js-icon.svg"),
        ("dotnet", ".NET 8 & C# 12", "CLR GC, Span<T>, Async State Machines, ASP.NET Core", "html-css-js-icon.svg"),
        ("rust", "Rust 2024 & Tokio", "Ownership, Lifetimes, Tokio Async, Pinning, Memory Safety", "html-css-js-icon.svg"),
        ("swift-swiftui", "Swift & SwiftUI", "Swift Concurrency, SwiftUI, ARC, SwiftData, iOS Architecture", "html-css-js-icon.svg"),
        ("kotlin", "Kotlin & Android", "Coroutines, Jetpack Compose, Flows, KMP, Android Lifecycle", "html-css-js-icon.svg"),
        ("flutter", "Flutter & Dart", "Widget Trees, Isolates, Bloc, Riverpod, Impeller Engine", "html-css-js-icon.svg"),
        ("react-native", "React Native", "New Architecture, Fabric, JSI, Hermes, Reanimated 3", "html-css-js-icon.svg"),
        ("docker", "Docker & Containers", "Namespaces, Cgroups, Multi-Stage Builds, OverlayFS", "html-css-js-icon.svg"),
        ("aws", "AWS Cloud Architecture", "Serverless, Well-Architected Framework, DynamoDB, IAM", "html-css-js-icon.svg"),
        ("performance", "Web Performance", "Core Web Vitals, Critical Rendering Path, GPU Compositing", "html-css-js-icon.svg"),
        ("integration", "Integration & APIs", "REST, GraphQL, gRPC, OAuth2 PKCE, Webhooks, API Gateways", "html-css-js-icon.svg"),
        ("typescript", "TypeScript", "Type System, Generics, Conditional Types, tsconfig", "html-css-js-icon.svg"),
        ("security", "Application Security", "XSS, CSRF, SQLi, CSP, JWT Security, Cryptography", "html-css-js-icon.svg"),
        ("testing", "Testing & QA", "Unit Testing, MSW, RTL, Playwright, Mocking", "html-css-js-icon.svg"),
        ("data-structures", "Data Structures", "Arrays, Trees, Graphs, Heaps, Hash Tables, Big-O", "html-css-js-icon.svg"),
        ("algorithms", "Algorithms", "Dynamic Programming, Graph Traversal, Sorting, Searching", "html-css-js-icon.svg"),
        ("css", "CSS3 & Modern Styling", "Flexbox, CSS Grid, Custom Properties, Animations", "html-css-js-icon.svg"),
        ("database", "Database & SQL", "Indexing, ACID, Query Optimization, Sharding, Replication", "html-css-js-icon.svg"),
        ("design-patterns", "Design Patterns", "Creational, Structural, Behavioral, Clean Code", "html-css-js-icon.svg"),
        ("git", "Git Version Control", "Branching, Rebasing, Worktrees, Cherry-pick, Reflog", "html-css-js-icon.svg"),
        ("golang", "Go (Golang)", "Goroutines, Channels, Interfaces, Garbage Collector", "html-css-js-icon.svg"),
        ("graphql", "GraphQL", "Schema Design, Resolvers, Subscriptions, DataLoader", "html-css-js-icon.svg"),
        ("kubernetes", "Kubernetes", "Pods, Deployments, Services, Ingress, Operators, Helm", "html-css-js-icon.svg"),
        ("linux", "Linux & Shell", "Kernel, Inodes, Systemd, Process Signals, Bash Scripting", "html-css-js-icon.svg"),
        ("material-radix-ui", "Material & Radix UI", "Component Primitives, WAI-ARIA, Theming, Customization", "html-css-js-icon.svg"),
        ("microfrontend", "Micro-frontends", "Module Federation, Single-SPA, Web Components, Routing", "html-css-js-icon.svg"),
        ("microservices", "Microservices", "Service Discovery, Saga Pattern, Circuit Breakers, Kafka", "html-css-js-icon.svg"),
        ("python", "Python & Django", "GIL, Asyncio, Generators, Metaclasses, Django ORM", "html-css-js-icon.svg"),
        ("svelte", "Svelte & SvelteKit", "Runes, Svelte 5, Compiler Reactivity, SSR, Hydration", "html-css-js-icon.svg"),
        ("system-design", "System Design", "Scalability, Load Balancing, Caching, CAP Theorem, Event-Driven", "html-css-js-icon.svg"),
        ("behavioral", "Behavioral & Leadership (STAR)", "STAR Method, Conflict Resolution, System Outages, and Leadership", "html-css-js-icon.svg"),
        ("devsecops", "DevSecOps & Threat Modeling", "STRIDE, Zero-Trust, Supply Chain Security, SBOM, and Container Hardening", "html-css-js-icon.svg"),
        ("ai-engineering", "AI Engineering & LLMs", "RAG, Transformers, LoRA, Vector Databases, and Agents", "html-css-js-icon.svg"),
        ("sre", "Site Reliability Engineering (SRE)", "SLOs, Error Budgets, OpenTelemetry, Incident Response, and Chaos Engineering", "html-css-js-icon.svg"),
        ("fintech", "Low-Latency FinTech & High-Frequency Systems", "Kernel Bypass, DPDK, LMAX Disruptor, Limit Order Books, and FIX Protocol", "html-css-js-icon.svg"),
        ("embedded", "Embedded Systems & RTOS", "FreeRTOS, Priority Inversion, Memory-Mapped I/O, ISRs, and DMA", "html-css-js-icon.svg"),
        ("web3-solidity", "Web3 & Solidity Security", "Reentrancy, Storage Slot Packing, Flash Loans, EVM Internals, and MEV", "html-css-js-icon.svg"),
        ("compiler-design", "Compiler Design & LLVM", "SSA Form, LR Parsers, JIT Compilation, LLVM IR, and Register Allocation", "html-css-js-icon.svg"),
        ("linux-kernel-ebpf", "Linux Kernel & eBPF Engineering", "eBPF Verifier, XDP Line-Rate Packet Filtering, Ring Buffers, and Kernel Internals", "html-css-js-icon.svg"),
        ("distributed-storage", "Distributed Storage & Filesystems", "Ceph CRUSH, LSM Trees, NVMe-oF, Erasure Coding, and ZFS", "html-css-js-icon.svg"),
        ("cryptography-zk", "Applied Cryptography & Zero-Knowledge", "ECDSA, zk-SNARKs, AES-GCM AEAD, Constant-Time Implementations, and R1CS", "html-css-js-icon.svg"),
        ("graphics-webgpu", "Computer Graphics & WebGPU", "WebGPU Compute Pipelines, WGSL, Memory Coalescing, PSOs, and Workgroups", "html-css-js-icon.svg"),
        ("networking-protocols", "Modern Networking Protocols (HTTP/3, QUIC, gRPC)", "HTTP/3, QUIC 0-RTT, Head-of-Line Blocking, Protobuf Varints, and BBR", "html-css-js-icon.svg"),
    ];

    for (cat_id, name, desc, icon) in category_dirs {
        let mut questions_vec = Vec::new();
        // Look for file in base_path/cat_id/
        let cat_folder = base_path.join(cat_id);
        if cat_folder.exists() {
            if let Ok(entries) = fs::read_dir(&cat_folder) {
                for entry in entries.flatten() {
                    let path = entry.path();
                    if path.extension().and_then(|s| s.to_str()) == Some("md") {
                        if let Ok(content) = fs::read_to_string(&path) {
                            for cap in q_regex.captures_iter(&content) {
                                let q_num = cap.get(1).and_then(|m| m.as_str().parse::<i32>().ok()).unwrap_or(1);
                                let title = cap.get(2).map(|m| m.as_str().trim().to_string()).unwrap_or_default();
                                let diff = cap.get(3).map(|m| m.as_str().trim().to_string()).unwrap_or_else(|| "Intermediate".to_string());
                                let body = cap.get(4).map(|m| m.as_str().trim()).unwrap_or_default();

                                let strategy = strat_regex.captures(body).map(|m| m.get(1).unwrap().as_str().trim().to_string());
                                let code_example = code_regex.captures(body).map(|m| m.get(1).unwrap().as_str().trim().to_string());

                                questions_vec.push(Question {
                                    id: format!("{}-{}", cat_id, q_num),
                                    category_id: cat_id.to_string(),
                                    question_number: q_num,
                                    title,
                                    difficulty: diff,
                                    strategy,
                                    answer_markdown: body.to_string(),
                                    code_example,
                                });
                            }
                        }
                    }
                }
            }
        }

        let total_q = questions_vec.len() as i32;
        store.categories.push(Category {
            id: cat_id.to_string(),
            name: name.to_string(),
            description: desc.to_string(),
            icon_path: icon.to_string(),
            total_questions: total_q,
        });
        store.questions.insert(cat_id.to_string(), questions_vec);
    }

    store
}

pub fn search_questions(store: &ContentStore, query: &str) -> Vec<SearchResult> {
    let lower_q = query.trim().to_lowercase();
    if lower_q.is_empty() {
        return Vec::new();
    }

    let mut results = Vec::new();
    for (_, q_list) in &store.questions {
        for q in q_list {
            let title_lower = q.title.to_lowercase();
            let body_lower = q.answer_markdown.to_lowercase();

            if title_lower.contains(&lower_q) {
                results.push(SearchResult {
                    question: q.clone(),
                    match_field: "title".to_string(),
                    score: 1.0,
                });
            } else if body_lower.contains(&lower_q) {
                results.push(SearchResult {
                    question: q.clone(),
                    match_field: "body".to_string(),
                    score: 0.5,
                });
            }
        }
    }

    results.sort_by(|a, b| b.score.partial_cmp(&a.score).unwrap());
    results.truncate(50);
    results
}
