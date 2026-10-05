/**
 * Interview Guide Platform - Landing Page Interactive Logic
 * Features: Instant Hero Search, Category Filter Tabs, Live 3D Flashcard Flip, Parallax Physics
 */

(function () {
  'use strict';

  // Categories Dataset (55 Verified Stacks)
  const categoriesData = [
    // Frontend & Web
    { id: 'javascript', name: 'JavaScript', domain: 'frontend', icon: '📜', count: 100, desc: 'Core JS, ES6+, Closures, Event Loop, Memory Model, Promises & V8 Internals' },
    { id: 'typescript', name: 'TypeScript', domain: 'frontend', icon: '🔷', count: 100, desc: 'Type System, Generics, Conditional & Mapped Types, AST & tsconfig' },
    { id: 'react', name: 'React.js', domain: 'frontend', icon: '⚛️', count: 100, desc: 'React 18/19, Hooks, Fiber Architecture, Server Components & Suspense' },
    { id: 'nextjs', name: 'Next.js', domain: 'frontend', icon: '▲', count: 100, desc: 'App Router, Server Actions, Incremental Static Regeneration, Caching & Middleware' },
    { id: 'angular', name: 'Angular 14-18', domain: 'frontend', icon: '🅰️', count: 100, desc: 'Standalone Components, Signals, RxJS Reactive Streams, DI & Zoneless' },
    { id: 'vue', name: 'Vue.js 3', domain: 'frontend', icon: '💚', count: 100, desc: 'Composition API, Reactivity System, Pinia, Nuxt 3 & Teleport' },
    { id: 'svelte', name: 'Svelte & SvelteKit', domain: 'frontend', icon: '🔥', count: 102, desc: 'Runes, Svelte 5, Zero-Runtime Compiler Reactivity, SSR & Hydration' },
    { id: 'html', name: 'HTML5 & Web APIs', domain: 'frontend', icon: '🌐', count: 100, desc: 'Semantic HTML, WAI-ARIA Accessibility, Web Components & Service Workers' },
    { id: 'css', name: 'CSS3 & Modern Styling', domain: 'frontend', icon: '🎨', count: 103, desc: 'CSS Grid, Flexbox, Subgrid, Container Queries, Cascade Layers & Animations' },
    { id: 'tailwind-bootstrap', name: 'Tailwind & Bootstrap', domain: 'frontend', icon: '🌊', count: 100, desc: 'Tailwind JIT Engine, Design Tokens, Utility Architecture & Responsive Systems' },
    { id: 'material-radix-ui', name: 'Material & Radix UI', domain: 'frontend', icon: '📐', count: 100, desc: 'Accessible Headless Primitives, Theming, Focus Trapping & WAI-ARIA' },
    { id: 'webpack-babel-vite', name: 'Webpack, Babel & Vite', domain: 'frontend', icon: '⚡', count: 100, desc: 'Native ESM, Rollup, Module Federation, AST Transformers & Vite HMR' },
    { id: 'performance', name: 'Web Performance', domain: 'frontend', icon: '🚀', count: 100, desc: 'Core Web Vitals (LCP/INP/CLS), Critical Rendering Path, GPU Offloading' },
    { id: 'microfrontend', name: 'Micro-frontends', domain: 'frontend', icon: '🧩', count: 101, desc: 'Module Federation, Single-SPA, Web Components & Cross-App Event Busses' },

    // Backend & Languages
    { id: 'nodejs', name: 'Node.js', domain: 'backend', icon: '🟢', count: 100, desc: 'Event Loop, libuv Phases, Streams, Worker Threads, Buffers & Backpressure' },
    { id: 'python', name: 'Python & Django', domain: 'backend', icon: '🐍', count: 100, desc: 'GIL Internals, Asyncio Event Loop, Metaclasses, Generators & Django ORM' },
    { id: 'java', name: 'Java & Spring Boot', domain: 'backend', icon: '☕', count: 100, desc: 'Virtual Threads (Project Loom), JVM GCs (ZGC/G1), Spring Boot 3 & Concurrency' },
    { id: 'golang', name: 'Go (Golang)', domain: 'backend', icon: '🐹', count: 100, desc: 'Goroutines M:N Scheduler, Channels, Interface Tables & Concurrent GC' },
    { id: 'rust', name: 'Rust 2024 & Tokio', domain: 'backend', icon: '🦀', count: 100, desc: 'Ownership, Lifetimes, Tokio Async Runtimes, Pinning & Memory Safety' },
    { id: 'dotnet', name: '.NET 8 & C# 12', domain: 'backend', icon: '🟣', count: 100, desc: 'CLR Internals, Span<T>, Memory<T>, Async State Machines & ASP.NET Core' },
    { id: 'cpp', name: 'Modern C++', domain: 'backend', icon: '⚙️', count: 100, desc: 'Move Semantics, RAII, Memory Models, Concepts, Coroutines & C++20/23' },
    { id: 'graphql', name: 'GraphQL', domain: 'backend', icon: '📡', count: 101, desc: 'Schema Federation, Resolvers, Subscriptions, DataLoader N+1 Caching' },
    { id: 'database', name: 'Database & SQL', domain: 'backend', icon: '🗄️', count: 101, desc: 'B-Trees, Write-Ahead Logs, Isolation Levels (MVCC), Sharding & Replication' },
    { id: 'integration', name: 'Integration & APIs', domain: 'backend', icon: '🔗', count: 209, desc: 'REST, gRPC, Protobuf, Webhooks, Idempotency Keys, OAuth2 PKCE & Gateways' },

    // Cloud, Containers & DevOps
    { id: 'docker', name: 'Docker & Containers', domain: 'devops', icon: '🐳', count: 100, desc: 'Linux Namespaces, Cgroups v2, OverlayFS, Multi-Stage Builds & Distroless' },
    { id: 'kubernetes', name: 'Kubernetes', domain: 'devops', icon: '☸️', count: 100, desc: 'Pods, Operators, CRDs, CNI, Service Meshes, Ingress & Helm Deployments' },
    { id: 'aws', name: 'AWS Cloud Architecture', domain: 'devops', icon: '☁️', count: 100, desc: 'Well-Architected Framework, DynamoDB Single-Table Design, IAM & Serverless' },
    { id: 'microservices', name: 'Microservices', domain: 'devops', icon: '🏛️', count: 101, desc: 'Distributed Sagas, Outbox Pattern, Circuit Breakers, Kafka Event-Driven' },
    { id: 'git', name: 'Git Version Control', domain: 'devops', icon: '🐙', count: 100, desc: 'Directed Acyclic Graphs, Reflog, Interactive Rebase, Bisect & Worktrees' },
    { id: 'linux', name: 'Linux & Shell', domain: 'devops', icon: '🐧', count: 100, desc: 'Kernel System Calls, Inodes, Virtual Memory, Systemd & Bash Scripting' },

    // Systems & Low-Level
    { id: 'fintech', name: 'Low-Latency FinTech (HFT)', domain: 'systems', icon: '📈', count: 100, desc: 'Kernel Bypass, Solarflare OpenOnload, DPDK, LMAX Disruptor & Order Books' },
    { id: 'linux-kernel-ebpf', name: 'Linux Kernel & eBPF', domain: 'systems', icon: '⚡', count: 100, desc: 'eBPF Verifier, XDP Line-Rate Packet Filtering, Ring Buffers & Kernel Internals' },
    { id: 'distributed-storage', name: 'Distributed Storage & Filesystems', domain: 'systems', icon: '💽', count: 100, desc: 'Ceph CRUSH Maps, LSM Trees, NVMe-oF, Erasure Coding, Raft & ZFS Pools' },
    { id: 'compiler-design', name: 'Compiler Design & LLVM', domain: 'systems', icon: '⚙️', count: 100, desc: 'Static Single Assignment (SSA), LR Parsers, JIT Tiered Compilation & LLVM IR' },
    { id: 'embedded', name: 'Embedded Systems & RTOS', domain: 'systems', icon: '🔌', count: 100, desc: 'FreeRTOS Schedulers, Priority Inversion, Memory-Mapped I/O, ISRs & DMA' },
    { id: 'cryptography-zk', name: 'Applied Cryptography & ZK', domain: 'systems', icon: '🔐', count: 100, desc: 'ECDSA, zk-SNARKs, Constant-Time AEAD, R1CS Constraints & Key Derivation' },
    { id: 'graphics-webgpu', name: 'Computer Graphics & WebGPU', domain: 'systems', icon: '🎮', count: 100, desc: 'WebGPU Compute Pipelines, WGSL, Memory Coalescing, PSOs & Shaders' },
    { id: 'networking-protocols', name: 'Networking Protocols (HTTP/3)', domain: 'systems', icon: '🌐', count: 100, desc: 'QUIC 0-RTT Handshake, Head-of-Line Blocking, Protobuf Varints & BBR' },
    { id: 'web3-solidity', name: 'Web3 & Solidity Security', domain: 'systems', icon: '⛓️', count: 100, desc: 'EVM Storage Slot Packing, Reentrancy Guards, Flash Loans & MEV Protection' },

    // Mobile Apps
    { id: 'swift-swiftui', name: 'Swift & SwiftUI', domain: 'mobile', icon: '🍏', count: 100, desc: 'Swift Structured Concurrency, Actors, SwiftUI Dependency Graph & ARC' },
    { id: 'kotlin', name: 'Kotlin & Android', domain: 'mobile', icon: '🤖', count: 100, desc: 'Kotlin Coroutines, Flows, Jetpack Compose Recomposition & KMP' },
    { id: 'flutter', name: 'Flutter & Dart', domain: 'mobile', icon: '💙', count: 100, desc: 'Dart Event Loop, Isolates, RenderObjects, Bloc & Impeller Graphic Engine' },
    { id: 'react-native', name: 'React Native', domain: 'mobile', icon: '📱', count: 100, desc: 'New Architecture, JSI Native Modules, TurboModules, Fabric & Hermes Engine' },

    // CS, State & Testing
    { id: 'algorithms', name: 'Algorithms', domain: 'cs', icon: '🧮', count: 100, desc: 'Dynamic Programming, Graph Theory, Network Flow, Backtracking & Sorting' },
    { id: 'data-structures', name: 'Data Structures', domain: 'cs', icon: '🌲', count: 100, desc: 'Skip Lists, Red-Black Trees, Heaps, Trie, Segment Trees & Bloom Filters' },
    { id: 'system-design', name: 'System Design', domain: 'cs', icon: '📐', count: 132, desc: 'Consistent Hashing, CAP Theorem, Rate Limiters, Distributed Caching & CDC' },
    { id: 'design-patterns', name: 'Design Patterns', domain: 'cs', icon: '🏛️', count: 101, desc: 'Gang of Four Patterns, Clean Architecture, CQRS & Event Sourcing' },
    { id: 'testing', name: 'Testing & QA', domain: 'cs', icon: '🧪', count: 100, desc: 'Property-Based Testing, MSW Mocking, Playwright E2E & Chaos Engineering' },
    { id: 'ngrx', name: 'NgRx', domain: 'cs', icon: '🔄', count: 100, desc: 'Redux Pattern in Angular, Effects, Entity Adapters & SignalStore' },
    { id: 'redux-zustand', name: 'Redux & Zustand', domain: 'cs', icon: '🟣', count: 100, desc: 'RTK Query, Immer Mutability Abstraction, Zustand Slices & Selective Subscriptions' },

    // Leadership & Reliability
    { id: 'behavioral', name: 'Behavioral & Leadership', domain: 'leadership', icon: '👔', count: 100, desc: 'STAR Framework, Executive Stakeholder Alignment, Outage Management & Mentorship' },
    { id: 'devsecops', name: 'DevSecOps & Threat Modeling', domain: 'leadership', icon: '🛡️', count: 100, desc: 'STRIDE Model, Zero-Trust Architecture, Software Supply Chain & SBOM' },
    { id: 'ai-engineering', name: 'AI Engineering & LLMs', domain: 'leadership', icon: '🤖', count: 100, desc: 'Retrieval-Augmented Generation (RAG), Fine-Tuning LoRA, Embeddings & Agents' },
    { id: 'sre', name: 'Site Reliability Engineering', domain: 'leadership', icon: '⏱️', count: 100, desc: 'SLOs, Error Budgets, OpenTelemetry Distributed Tracing & Post-Mortems' },
    { id: 'security', name: 'Application Security', domain: 'leadership', icon: '🔒', count: 100, desc: 'XSS, CSRF, CSP Level 3, JWT Signature Vulnerabilities, Constant-Time Crypto' }
  ];

  // Sample Interactive Flashcards
  const sampleFlashcards = [
    {
      topic: 'Rust 2024 & Tokio',
      question: 'What is the precise role of Pin<P<T>> in Rust async/await, and why is structural pinning dangerous?',
      answer: 'Pin guarantees that a type implementing !Unpin will not be moved in memory once pinned. This is strictly required for self-referential generator state machines created by async blocks, which store internal pointers to stack-allocated variables across yield points. Structural pinning requires careful unsafe contract enforcement: if a struct claims to pin its fields, it must never expose &mut access to them without Unpin.'
    },
    {
      topic: 'Low-Latency FinTech (HFT)',
      question: 'How does Solarflare OpenOnload achieve sub-microsecond latency by bypassing the Linux kernel TCP/IP stack?',
      answer: 'Kernel bypass redirects NIC packet queues directly into user-space memory via memory-mapped I/O (MMIO) and PCIe DMA ring buffers. By eliminating context switches, CPU interrupt handling, and Linux socket buffer (sk_buff) copies, network frames are processed entirely on dedicated CPU core pin assignments with spin-polling.'
    },
    {
      topic: 'Distributed Systems & Raft',
      question: 'How does Raft prevent split-brain during network partitions, and what role does the term number play?',
      answer: 'Raft enforces that a candidate node can only be elected Leader if it gathers votes from a strict majority (N/2 + 1) of cluster nodes. A network partition cannot form two majorities simultaneously. Monotonically increasing term numbers ensure that any stale leader receiving a message from a higher term immediately steps down into Follower state.'
    },
    {
      topic: 'Linux Kernel & eBPF',
      question: 'How does XDP (eXpress Data Path) drop malicious DDoS packets at line rate before sk_buff allocation?',
      answer: 'XDP runs eBPF byte-code directly inside the network interface card (NIC) driver ring buffer at the earliest possible hook in the kernel packet receive path. If the eBPF program returns XDP_DROP, the packet is instantly discarded without allocating an sk_buff data structure, allowing a single commodity server to drop over 20 million packets/second.'
    },
    {
      topic: 'Go Runtime Scheduler',
      question: 'How does the Go runtime handle goroutine stack growth without causing memory fragmentation?',
      answer: 'Go uses contiguous stacks. Goroutines begin with a small 2KB stack. When a function preamble detects that stack allocation exceeds the current segment (stack split check), the runtime allocates a contiguous memory block of double the size, copies the previous stack contents, updates all interior pointers via pointer maps, and frees the old block.'
    }
  ];

  let currentCardIndex = 0;

  // Initialize DOM
  document.addEventListener('DOMContentLoaded', () => {
    initNavbarScroll();
    initHeroSearch();
    initDirectoryGrid();
    initDirectoryFilterTabs();
    initDirectorySearchInput();
    initInteractiveFlashcard();
    initParallaxTilt();
    initFabScrollTop();
  });

  // 1. Navbar Scroll Effect
  function initNavbarScroll() {
    const navbar = document.querySelector('.navbar');
    if (!navbar) return;

    window.addEventListener('scroll', () => {
      if (window.scrollY > 40) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
    }, { passive: true });
  }

  // 2. Hero Instant Search & Keyboard Shortcuts
  function initHeroSearch() {
    const searchInput = document.getElementById('heroSearchInput');
    const dropdown = document.getElementById('heroSearchDropdown');
    const shortcutPill = document.getElementById('searchShortcutPill');

    if (!searchInput || !dropdown) return;

    // Keyboard Shortcuts: Cmd+K, Ctrl+K, or "/"
    window.addEventListener('keydown', (e) => {
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault();
        searchInput.focus();
        searchInput.select();
      } else if (e.key === '/' && document.activeElement !== searchInput) {
        const activeTag = document.activeElement.tagName.toLowerCase();
        if (activeTag !== 'input' && activeTag !== 'textarea') {
          e.preventDefault();
          searchInput.focus();
          searchInput.select();
        }
      } else if (e.key === 'Escape') {
        dropdown.classList.remove('active');
        searchInput.blur();
      }
    });

    if (shortcutPill) {
      shortcutPill.addEventListener('click', () => {
        searchInput.focus();
        searchInput.select();
      });
    }

    searchInput.addEventListener('input', () => {
      const query = searchInput.value.trim().toLowerCase();
      if (!query) {
        dropdown.classList.remove('active');
        dropdown.innerHTML = '';
        return;
      }

      const matches = categoriesData.filter(item => 
        item.name.toLowerCase().includes(query) ||
        item.desc.toLowerCase().includes(query) ||
        item.id.toLowerCase().includes(query)
      ).slice(0, 8);

      if (matches.length === 0) {
        dropdown.innerHTML = `
          <div style="padding: 16px; color: var(--text-muted); font-size: 0.9rem; text-align: center;">
            No specialized categories match "<strong>${escapeHtml(query)}</strong>"
          </div>
        `;
        dropdown.classList.add('active');
        return;
      }

      dropdown.innerHTML = matches.map(item => `
        <a href="dashboard.html#${item.id}" class="search-dropdown-item">
          <div class="search-item-left">
            <span style="font-size: 1.25rem;">${item.icon}</span>
            <div>
              <div style="font-weight: 700; color: var(--text-primary); font-size: 0.95rem;">${escapeHtml(item.name)}</div>
              <div style="font-size: 0.775rem; color: var(--text-muted);">${escapeHtml(item.desc.substring(0, 60))}...</div>
            </div>
          </div>
          <span class="search-item-badge">${item.count}+ Qs</span>
        </a>
      `).join('');

      dropdown.classList.add('active');
    });

    // Close dropdown on click outside
    document.addEventListener('click', (e) => {
      if (!searchInput.contains(e.target) && !dropdown.contains(e.target)) {
        dropdown.classList.remove('active');
      }
    });
  }

  // 3. Render 55 Directory Cards
  function initDirectoryGrid() {
    const grid = document.getElementById('directoryGrid');
    if (!grid) return;

    grid.innerHTML = categoriesData.map(cat => `
      <a href="dashboard.html#${cat.id}" 
         class="category-card" 
         data-domain="${cat.domain}"
         data-id="${cat.id}"
         data-name="${escapeHtml(cat.name).toLowerCase()}"
         data-desc="${escapeHtml(cat.desc).toLowerCase()}"
         title="Explore ${cat.name} Interview Questions">
        <div>
          <div class="card-top">
            <div class="card-icon-wrapper">${cat.icon}</div>
            <span class="card-badge-count">${cat.count}+ Verified</span>
          </div>
          <h3 class="card-title">${escapeHtml(cat.name)}</h3>
          <p class="card-description">${escapeHtml(cat.desc)}</p>
        </div>
        <div class="card-footer-tags">
          <span class="card-domain-tag">${formatDomainName(cat.domain)}</span>
          <span class="card-enter-arrow">Explore →</span>
        </div>
      </a>
    `).join('');
  }

  function formatDomainName(domain) {
    const map = {
      'frontend': 'Frontend & Web',
      'backend': 'Backend & Systems',
      'devops': 'Cloud & DevOps',
      'systems': 'Systems & Low-Level',
      'mobile': 'Mobile Apps',
      'cs': 'CS & Architecture',
      'leadership': 'Leadership & Reliability'
    };
    return map[domain] || domain;
  }

  // 4. Directory Filter Tabs
  function initDirectoryFilterTabs() {
    const tabs = document.querySelectorAll('.filter-tab');
    const cards = document.querySelectorAll('.category-card');
    const counter = document.getElementById('visibleCategoryCount');

    tabs.forEach(tab => {
      tab.addEventListener('click', () => {
        tabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');

        const domain = tab.getAttribute('data-domain');
        let visibleCount = 0;

        cards.forEach(card => {
          const cardDomain = card.getAttribute('data-domain');
          const matches = (domain === 'all' || cardDomain === domain);

          if (matches) {
            card.classList.remove('hidden');
            visibleCount++;
          } else {
            card.classList.add('hidden');
          }
        });

        if (counter) {
          counter.textContent = visibleCount;
        }
      });
    });
  }

  // 5. Directory Search Input
  function initDirectorySearchInput() {
    const input = document.getElementById('dirSearchInput');
    const cards = document.querySelectorAll('.category-card');
    const counter = document.getElementById('visibleCategoryCount');
    const tabs = document.querySelectorAll('.filter-tab');

    if (!input) return;

    input.addEventListener('input', () => {
      const q = input.value.trim().toLowerCase();
      let visibleCount = 0;

      // Reset tabs to 'All' when actively typing in search
      if (q.length > 0) {
        tabs.forEach(t => t.classList.remove('active'));
        const allTab = document.querySelector('.filter-tab[data-domain="all"]');
        if (allTab) allTab.classList.add('active');
      }

      cards.forEach(card => {
        const name = card.getAttribute('data-name');
        const desc = card.getAttribute('data-desc');
        const id = card.getAttribute('data-id');

        const matches = !q || name.includes(q) || desc.includes(q) || id.includes(q);
        if (matches) {
          card.classList.remove('hidden');
          visibleCount++;
        } else {
          card.classList.add('hidden');
        }
      });

      if (counter) {
        counter.textContent = visibleCount;
      }
    });
  }

  // 6. Interactive 3D Flashcard Demonstration
  function initInteractiveFlashcard() {
    const card = document.getElementById('demoFlashcard');
    const nextBtn = document.getElementById('btnNextFlashcard');
    const topicEl = document.getElementById('flashcardTopic');
    const questionEl = document.getElementById('flashcardQuestion');
    const answerEl = document.getElementById('flashcardAnswer');
    const counterEl = document.getElementById('flashcardCounter');

    if (!card || !nextBtn || !questionEl || !answerEl) return;

    function renderCard(index) {
      const item = sampleFlashcards[index];
      if (!item) return;

      card.classList.remove('flipped');
      setTimeout(() => {
        if (topicEl) topicEl.textContent = item.topic;
        questionEl.textContent = item.question;
        answerEl.textContent = item.answer;
        if (counterEl) counterEl.textContent = `${index + 1} / ${sampleFlashcards.length}`;
      }, 150);
    }

    card.addEventListener('click', () => {
      card.classList.toggle('flipped');
    });

    nextBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      currentCardIndex = (currentCardIndex + 1) % sampleFlashcards.length;
      renderCard(currentCardIndex);
    });

    renderCard(0);
  }

  // 7. 3D Parallax Tilt Effect on Category Cards
  function initParallaxTilt() {
    // Only apply on non-touch screens with mouse
    if (window.matchMedia('(hover: hover)').matches) {
      document.addEventListener('mousemove', (e) => {
        const card = e.target.closest('.category-card');
        if (!card) return;

        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left - rect.width / 2;
        const y = e.clientY - rect.top - rect.height / 2;
        const rotateX = (-y / (rect.height / 2)) * 6;
        const rotateY = (x / (rect.width / 2)) * 6;

        card.style.transform = `perspective(1000px) rotateX(${rotateX.toFixed(2)}deg) rotateY(${rotateY.toFixed(2)}deg) translateY(-6px)`;
      });

      document.addEventListener('mouseout', (e) => {
        const card = e.target.closest('.category-card');
        if (!card || card.contains(e.relatedTarget)) return;

        card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0)';
      });
    }
  }

  // 8. Scroll To Top Floating Action Button
  function initFabScrollTop() {
    const fab = document.getElementById('fabScrollTop');
    if (!fab) return;

    window.addEventListener('scroll', () => {
      if (window.scrollY > 300) {
        fab.classList.add('visible');
      } else {
        fab.classList.remove('visible');
      }
    }, { passive: true });

    fab.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // Utility to escape HTML strings safely
  function escapeHtml(str) {
    if (!str) return '';
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

})();
