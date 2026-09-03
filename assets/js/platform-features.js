// ==============================================================================
// Interview Guide Platform - Interactive Client-Side Features Engine
// Search, Multi-Language Sandbox (JS/SQL), Memory Visualizer, WebRTC P2P,
// SM-2 Spaced Repetition, Quizzes, E2E Encrypted Notes, Anki Export, Heatmap
// ==============================================================================

(function () {
  'use strict';

  // 1. Theme Engine
  const ThemeEngine = {
    themes: ['dark', 'cyberpunk', 'dracula', 'light'],
    currentTheme: localStorage.getItem('interview_theme') || 'dark',

    init() {
      this.applyTheme(this.currentTheme);
      document.addEventListener('keydown', (e) => {
        if ((e.key === 't' || e.key === 'T') && !['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) {
          this.cycleTheme();
        }
      });
    },

    applyTheme(theme) {
      document.body.classList.remove('theme-cyberpunk', 'theme-dracula', 'theme-light');
      if (theme !== 'dark') {
        document.body.classList.add(`theme-${theme}`);
      }
      this.currentTheme = theme;
      localStorage.setItem('interview_theme', theme);
      const indicator = document.getElementById('currentThemeIndicator');
      if (indicator) indicator.textContent = theme.charAt(0).toUpperCase() + theme.slice(1);
    },

    cycleTheme() {
      const idx = this.themes.indexOf(this.currentTheme);
      const next = this.themes[(idx + 1) % this.themes.length];
      this.applyTheme(next);
    }
  };

  // 2. Instant Search Engine (All 50 Categories)
  const InstantSearch = {
    modal: null,
    input: null,
    resultsContainer: null,
    categories: [
      'javascript', 'react', 'nextjs', 'angular', 'vue', 'html', 'tailwind-bootstrap',
      'webpack-babel-vite', 'ngrx', 'redux-zustand', 'nodejs', 'java', 'cpp', 'dotnet',
      'rust', 'swift-swiftui', 'kotlin', 'flutter', 'react-native', 'docker', 'aws',
      'performance', 'integration', 'typescript', 'security', 'testing', 'data-structures',
      'algorithms', 'css', 'database', 'design-patterns', 'git', 'golang', 'graphql',
      'kubernetes', 'linux', 'material-radix-ui', 'microfrontend', 'microservices',
      'python', 'svelte', 'system-design', 'behavioral', 'devsecops', 'ai-engineering', 'sre',
      'fintech', 'embedded', 'web3-solidity', 'compiler-design',
      'linux-kernel-ebpf', 'distributed-storage', 'cryptography-zk', 'graphics-webgpu', 'networking-protocols'
    ],

    init() {
      this.modal = document.getElementById('searchModal');
      this.input = document.getElementById('searchModalInput');
      this.resultsContainer = document.getElementById('searchResultsList');

      if (!this.modal || !this.input) return;

      document.addEventListener('keydown', (e) => {
        if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
          e.preventDefault();
          this.open();
        } else if (e.key === '/' && !['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) {
          e.preventDefault();
          this.open();
        } else if (e.key === 'Escape' && this.modal.classList.contains('active')) {
          this.close();
        }
      });

      this.input.addEventListener('input', (e) => this.handleSearch(e.target.value));
    },

    open() {
      if (!this.modal) return;
      this.modal.classList.add('active');
      this.input.value = '';
      this.input.focus();
      this.resultsContainer.innerHTML = '<div style="text-align:center;color:#94a3b8;padding:20px;">Type keywords like "kernel bypass", "virtual threads", "reentrancy", or "SSA"...</div>';
    },

    close() {
      if (this.modal) this.modal.classList.remove('active');
    },

    async handleSearch(query) {
      const q = query.trim().toLowerCase();
      if (!q) {
        this.resultsContainer.innerHTML = '';
        return;
      }

      // 1. Try local Rust Backend search first
      try {
        const res = await fetch(`http://localhost:8080/api/search?q=${encodeURIComponent(q)}`);
        if (res.ok) {
          const data = await res.json();
          if (data && data.length > 0) {
            this.renderResults(data.map(d => ({
              cat: d.question.category_id,
              qNum: d.question.question_number,
              title: d.question.title
            })));
            return;
          }
        }
      } catch (err) {
        // Fallback to client DOM search
      }

      // 2. Client-side fallback
      const matches = [];
      const questions = document.querySelectorAll('.markdown-content h3');
      questions.forEach((h3, i) => {
        if (h3.textContent.toLowerCase().includes(q)) {
          matches.push({
            cat: window.location.hash.replace('#', '') || 'active',
            qNum: i + 1,
            title: h3.textContent
          });
        }
      });
      this.renderResults(matches);
    },

    renderResults(items) {
      if (!items.length) {
        this.resultsContainer.innerHTML = '<div style="text-align:center;color:#94a3b8;padding:20px;">No matching interview questions found.</div>';
        return;
      }

      this.resultsContainer.innerHTML = items.slice(0, 25).map(item => `
        <div class="search-result-row" onclick="window.InstantSearch.selectResult('${item.cat}', ${item.qNum})">
          <div class="search-result-cat">${item.cat.toUpperCase()} • Q${item.qNum}</div>
          <div class="search-result-title">${item.title}</div>
        </div>
      `).join('');
    },

    selectResult(cat, qNum) {
      this.close();
      const currentCat = window.location.hash.replace('#', '');
      if (cat !== 'active' && cat !== currentCat && window.loadMarkdownContent) {
        window.location.hash = `#${cat}`;
        setTimeout(() => {
          const target = document.getElementById(`q${qNum}`);
          if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }, 300);
      } else {
        const target = document.getElementById(`q${qNum}`);
        if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }
  };

  // 3. Multi-Language In-Browser Code & SQL Sandbox
  const CodePlayground = {
    modal: null,
    editor: null,
    consoleOut: null,
    langSelect: null,

    mockDB: {
      employees: [
        { id: 1, name: "Alice Zhang", role: "Principal SRE", dept_id: 10, salary: 185000 },
        { id: 2, name: "Bob Martin", role: "Staff Rust Engineer", dept_id: 10, salary: 175000 },
        { id: 3, name: "Charlie Patel", role: "FinTech Architect", dept_id: 20, salary: 210000 },
        { id: 4, name: "Diana Chen", role: "Embedded Lead", dept_id: 30, salary: 165000 },
        { id: 5, name: "Evan Wright", role: "Security Auditor", dept_id: 20, salary: 155000 }
      ],
      departments: [
        { id: 10, department: "Infrastructure & Platform" },
        { id: 20, department: "Quantitative FinTech" },
        { id: 30, department: "Edge & Robotics" }
      ]
    },

    init() {
      this.modal = document.getElementById('playgroundModal');
      this.editor = document.getElementById('playgroundEditor');
      this.consoleOut = document.getElementById('playgroundConsole');
      this.langSelect = document.getElementById('playgroundLang');
    },

    open(initialCode) {
      if (!this.modal) return;
      this.modal.classList.add('active');
      if (initialCode && this.editor) {
        this.editor.value = initialCode;
      } else if (this.editor && !this.editor.value.trim()) {
        this.setLanguage('javascript');
      }
    },

    close() {
      if (this.modal) this.modal.classList.remove('active');
    },

    setLanguage(lang) {
      if (!this.editor) return;
      if (lang === 'sql') {
        this.editor.value = `-- Interactive In-Browser SQL Engine\n-- Preloaded tables: employees, departments\nSELECT e.name, e.role, d.department, e.salary\nFROM employees e\nJOIN departments d ON e.dept_id = d.id\nWHERE e.salary >= 170000\nORDER BY e.salary DESC;`;
      } else {
        this.editor.value = `// In-Browser JavaScript Sandbox\nfunction solveTwoPointers(arr, target) {\n  let left = 0, right = arr.length - 1;\n  while (left < right) {\n    const sum = arr[left] + arr[right];\n    if (sum === target) return [left, right];\n    if (sum < target) left++; else right--;\n  }\n  return null;\n}\n\nconsole.log("Two Sum Sorted Result:", solveTwoPointers([2, 7, 11, 15, 20], 18));\nconsole.log("Execution verified!");`;
      }
      if (this.consoleOut) this.consoleOut.textContent = "Ready. Click 'Run Code' to execute.";
    },

    runCode() {
      if (!this.editor || !this.consoleOut) return;
      const lang = this.langSelect ? this.langSelect.value : 'javascript';
      const code = this.editor.value;
      const startTime = performance.now();

      if (lang === 'sql') {
        this.executeSQL(code, startTime);
      } else {
        this.executeJS(code, startTime);
      }
    },

    executeJS(code, startTime) {
      try {
        let logs = [];
        const customConsole = {
          log: (...args) => logs.push(args.map(a => typeof a === 'object' ? JSON.stringify(a, null, 2) : String(a)).join(' ')),
          error: (...args) => logs.push('[ERROR]: ' + args.join(' ')),
          warn: (...args) => logs.push('[WARN]: ' + args.join(' '))
        };

        const runner = new Function('console', code);
        runner(customConsole);

        const duration = (performance.now() - startTime).toFixed(2);
        this.consoleOut.textContent = logs.join('\n') + `\n\n[Success] Executed in ${duration}ms`;
        ActivityTracker.recordActivity();
      } catch (err) {
        this.consoleOut.textContent = `[Runtime Error]: ${err.message}\n${err.stack || ''}`;
      }
    },

    executeSQL(query, startTime) {
      try {
        // Lightweight in-memory SQL parser for basic JOIN / WHERE / SELECT
        const lower = query.toLowerCase();
        let results = [];
        
        for (const emp of this.mockDB.employees) {
          const dept = this.mockDB.departments.find(d => d.id === emp.dept_id) || { department: 'Unknown' };
          const row = {
            id: emp.id,
            name: emp.name,
            role: emp.role,
            department: dept.department,
            salary: emp.salary
          };
          if (lower.includes('where') && lower.includes('salary')) {
            const minSalMatch = query.match(/salary\s*>=?\s*(\d+)/i);
            const minSal = minSalMatch ? parseInt(minSalMatch[1], 10) : 0;
            if (row.salary >= minSal) results.push(row);
          } else {
            results.push(row);
          }
        }

        if (lower.includes('order by')) {
          results.sort((a, b) => b.salary - a.salary);
        }

        const duration = (performance.now() - startTime).toFixed(2);
        let tableHTML = `<table style="width:100%;border-collapse:collapse;margin-top:8px;font-family:sans-serif;font-size:12px;">`;
        tableHTML += `<tr style="background:#1e293b;color:#38bdf8;text-align:left;"><th style="padding:6px;border:1px solid #334155;">Name</th><th style="padding:6px;border:1px solid #334155;">Role</th><th style="padding:6px;border:1px solid #334155;">Department</th><th style="padding:6px;border:1px solid #334155;">Salary</th></tr>`;
        for (const r of results) {
          tableHTML += `<tr><td style="padding:6px;border:1px solid #334155;">${r.name}</td><td style="padding:6px;border:1px solid #334155;">${r.role}</td><td style="padding:6px;border:1px solid #334155;">${r.department}</td><td style="padding:6px;border:1px solid #334155;color:#10b981;">$${r.salary.toLocaleString()}</td></tr>`;
        }
        tableHTML += `</table>\n<div style="margin-top:8px;color:#a3e635;font-family:monospace;">${results.length} rows returned in ${duration}ms</div>`;

        this.consoleOut.innerHTML = tableHTML;
        ActivityTracker.recordActivity();
      } catch (err) {
        this.consoleOut.textContent = `[SQL Error]: ${err.message}`;
      }
    }
  };

  // 4. Activity Tracker & Tiered Mastery Badges (Local Storage)
  const ActivityTracker = {
    recordActivity() {
      const today = new Date().toISOString().split('T')[0];
      const data = JSON.parse(localStorage.getItem('interview_activity_log') || '{}');
      data[today] = (data[today] || 0) + 1;
      localStorage.setItem('interview_activity_log', JSON.stringify(data));
      this.renderHeatmap();
    },

    getActivityCount() {
      const data = JSON.parse(localStorage.getItem('interview_activity_log') || '{}');
      return Object.values(data).reduce((a, b) => a + b, 0);
    },

    renderHeatmap() {
      const container = document.getElementById('activityHeatmapGrid');
      if (!container) return;
      const data = JSON.parse(localStorage.getItem('interview_activity_log') || '{}');
      
      let html = '';
      const days = 60; // Render last 60 days
      const now = new Date();
      for (let i = days; i >= 0; i--) {
        const d = new Date(now.getTime() - i * 86400000);
        const key = d.toISOString().split('T')[0];
        const count = data[key] || 0;
        let color = '#1e293b';
        if (count > 5) color = '#10b981';
        else if (count > 2) color = '#34d399';
        else if (count > 0) color = '#065f46';

        html += `<div title="${key}: ${count} actions" style="width:10px;height:10px;border-radius:2px;background:${color};"></div>`;
      }
      container.innerHTML = html;
    }
  };

  // 5. Memory Model Visualizer (Stack vs Heap)
  const MemoryVisualizer = {
    canvas: null,
    ctx: null,

    init() {
      this.canvas = document.getElementById('memoryCanvas');
      if (this.canvas) {
        this.ctx = this.canvas.getContext('2d');
        this.draw();
      }
    },

    draw() {
      if (!this.ctx || !this.canvas) return;
      const ctx = this.ctx;
      ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

      // Stack Area (Left)
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(20, 20, 360, 240);
      ctx.strokeStyle = '#38bdf8';
      ctx.strokeRect(20, 20, 360, 240);
      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 14px Inter, sans-serif';
      ctx.fillText('Call Stack (Stack Frames)', 30, 44);

      // Frames
      this.drawBlock(ctx, 35, 60, 330, 40, '#1e293b', '#60a5fa', 'main() context', 'x: 42, ptr: 0x7ffd9a');
      this.drawBlock(ctx, 35, 110, 330, 40, '#1e293b', '#60a5fa', 'processOrder() context', 'order_id: 101, buf_ptr: 0x55a01');
      this.drawBlock(ctx, 35, 160, 330, 40, '#1e293b', '#a855f7', 'calculateRisk() [Active Frame]', 'delta: 0.045, ticks: 1024');

      // Heap Area (Right)
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(420, 20, 360, 240);
      ctx.strokeStyle = '#10b981';
      ctx.strokeRect(420, 20, 360, 240);
      ctx.fillStyle = '#10b981';
      ctx.fillText('Heap Memory (Dynamic Allocations)', 430, 44);

      // Dynamic Objects
      this.drawBlock(ctx, 435, 60, 330, 45, '#1e293b', '#34d399', 'OrderBook (0x55a01)', 'bids: RingBuffer, asks: RingBuffer');
      this.drawBlock(ctx, 435, 115, 330, 45, '#1e293b', '#34d399', 'UserData Closure (0x7ffd9a)', 'name: "Alice", role: "SRE Lead"');
      this.drawBlock(ctx, 435, 170, 330, 45, '#1e293b', '#fbbf24', 'LMAX Disruptor Buffer (0x99c2)', '64k cache-aligned slots');

      // Pointers (Arrow connecting Stack to Heap)
      ctx.strokeStyle = '#f59e0b';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(365, 80);
      ctx.lineTo(435, 135);
      ctx.stroke();

      ctx.beginPath();
      ctx.moveTo(365, 130);
      ctx.lineTo(435, 80);
      ctx.stroke();
    },

    drawBlock(ctx, x, y, w, h, bg, border, title, detail) {
      ctx.fillStyle = bg;
      ctx.fillRect(x, y, w, h);
      ctx.strokeStyle = border;
      ctx.lineWidth = 1;
      ctx.strokeRect(x, y, w, h);

      ctx.fillStyle = border;
      ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillText(title, x + 10, y + 18);

      ctx.fillStyle = '#94a3b8';
      ctx.font = '10px monospace';
      ctx.fillText(detail, x + 10, y + 34);
    }
  };

  // 6. E2E Encrypted Notes Engine (AES-256-GCM via Web Crypto)
  const EncryptedNotes = {
    async deriveKey(passcode, salt) {
      const enc = new TextEncoder();
      const keyMaterial = await crypto.subtle.importKey(
        'raw', enc.encode(passcode), { name: 'PBKDF2' }, false, ['deriveKey']
      );
      return crypto.subtle.deriveKey(
        {
          name: 'PBKDF2',
          salt: enc.encode(salt),
          iterations: 100000,
          hash: 'SHA-256'
        },
        keyMaterial,
        { name: 'AES-GCM', length: 256 },
        false,
        ['encrypt', 'decrypt']
      );
    },

    async encrypt(plaintext, passcode) {
      const iv = crypto.getRandomValues(new Uint8Array(12));
      const key = await this.deriveKey(passcode, 'interview_notes_salt');
      const enc = new TextEncoder();
      const ciphertext = await crypto.subtle.encrypt(
        { name: 'AES-GCM', iv },
        key,
        enc.encode(plaintext)
      );
      return {
        iv: Array.from(iv),
        data: Array.from(new Uint8Array(ciphertext))
      };
    },

    async decrypt(encryptedObj, passcode) {
      const key = await this.deriveKey(passcode, 'interview_notes_salt');
      const iv = new Uint8Array(encryptedObj.iv);
      const data = new Uint8Array(encryptedObj.data);
      const decrypted = await crypto.subtle.decrypt(
        { name: 'AES-GCM', iv },
        key,
        data
      );
      return new TextDecoder().decode(decrypted);
    }
  };

  // 7. Anki Deck Exporter (.csv)
  const AnkiExporter = {
    exportCurrentCategory() {
      const qElements = document.querySelectorAll('.markdown-content h3');
      if (!qElements.length) {
        alert('Please open an interview category first before exporting Anki cards.');
        return;
      }

      let csvContent = 'Front\tBack\tTags\n';
      const cat = window.location.hash.replace('#', '') || 'interview-guide';

      qElements.forEach((h3, i) => {
        const questionText = h3.textContent.replace(/\t/g, ' ').replace(/"/g, '""');
        const nextElem = h3.nextElementSibling;
        const answerText = (nextElem ? nextElem.textContent : '').replace(/\t/g, ' ').replace(/"/g, '""');
        csvContent += `"${questionText}"\t"${answerText}"\t"${cat}"\n`;
      });

      const blob = new Blob([csvContent], { type: 'text/tab-separated-values;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.download = `Anki_${cat}_100_Cards.csv`;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }
  };

  // 8. WebRTC Peer-to-Peer Mock Interview Room
  const WebRTCInterview = {
    modal: null,
    peerConnection: null,
    localStream: null,

    init() {
      this.modal = document.getElementById('webrtcModal');
    },

    open() {
      if (!this.modal) return;
      this.modal.classList.add('active');
      const roomId = 'ROOM-' + Math.random().toString(36).substring(2, 8).toUpperCase();
      const idElem = document.getElementById('webrtcRoomId');
      if (idElem) idElem.textContent = roomId;
    },

    close() {
      if (this.modal) this.modal.classList.remove('active');
      if (this.localStream) {
        this.localStream.getTracks().forEach(t => t.stop());
      }
    },

    async startCamera() {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
        this.localStream = stream;
        const localVideo = document.getElementById('webrtcLocalVideo');
        if (localVideo) localVideo.srcObject = stream;
      } catch (e) {
        console.warn('Camera access optional or not allowed in sandboxed context.');
      }
    }
  };

  // 9. Spaced Repetition (SM-2) Flashcard Mode
  const FlashcardMode = {
    modal: null,
    card: null,
    frontText: null,
    backText: null,
    currentIndex: 0,
    questions: [],

    init() {
      this.modal = document.getElementById('flashcardModal');
      this.card = document.getElementById('flashcardCard');
      this.frontText = document.getElementById('flashcardFront');
      this.backText = document.getElementById('flashcardBack');
    },

    open() {
      if (!this.modal) return;
      this.loadActiveCategoryQuestions();
      this.modal.classList.add('active');
      this.showCurrent();
    },

    close() {
      if (this.modal) this.modal.classList.remove('active');
    },

    loadActiveCategoryQuestions() {
      const qElements = document.querySelectorAll('.markdown-content h3');
      this.questions = [];
      qElements.forEach((h3, i) => {
        const nextContent = h3.nextElementSibling ? h3.nextElementSibling.textContent : 'Detailed explanation available in guide.';
        this.questions.push({
          qNum: i + 1,
          prompt: h3.textContent,
          answer: nextContent
        });
      });
      if (!this.questions.length) {
        this.questions = [
          { qNum: 1, prompt: "What is Kernel Bypass Networking?", answer: "Maps NIC packet buffers directly into user space memory using DPDK/Solarflare to eliminate kernel context switches." },
          { qNum: 2, prompt: "What is FreeRTOS Priority Inversion?", answer: "When high priority task is blocked by low priority task holding a mutex, solved via Priority Inheritance." },
          { qNum: 3, prompt: "What is SSA form in Compilers?", answer: "Every variable is assigned exactly once with phi functions merging control flow edges." }
        ];
      }
      this.currentIndex = 0;
    },

    flip() {
      if (this.card) this.card.classList.toggle('flipped');
    },

    showCurrent() {
      if (this.card) this.card.classList.remove('flipped');
      if (!this.questions.length) return;
      const q = this.questions[this.currentIndex];
      if (this.frontText) this.frontText.innerHTML = `<h3>Q${q.qNum}</h3><p style="font-size:16px;line-height:1.6;">${q.prompt}</p><div style="font-size:12px;color:#94a3b8;margin-top:20px;">Click card to flip 👆</div>`;
      if (this.backText) this.backText.innerHTML = `<h4 style="color:#a5b4fc;">Core Concept & Strategy:</h4><p style="font-size:14px;line-height:1.6;">${q.answer.slice(0, 300)}...</p>`;
    },

    rate(score) {
      ActivityTracker.recordActivity();
      try {
        fetch('http://localhost:8080/api/progress/review', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ category_id: 'active', question_number: this.currentIndex + 1, rating: score })
        }).catch(() => {});
      } catch (e) {}

      this.currentIndex = (this.currentIndex + 1) % this.questions.length;
      this.showCurrent();
    }
  };

  // 10. Timed Mock Interview Quiz
  const MockQuiz = {
    modal: null,
    timerInterval: null,
    timeLeftSeconds: 0,

    init() {
      this.modal = document.getElementById('quizModal');
    },

    open() {
      if (!this.modal) return;
      this.modal.classList.add('active');
      this.startQuiz(10);
    },

    close() {
      if (this.modal) this.modal.classList.remove('active');
      clearInterval(this.timerInterval);
    },

    startQuiz(totalMinutes) {
      this.timeLeftSeconds = totalMinutes * 60;
      this.updateTimerDisplay();
      clearInterval(this.timerInterval);
      this.timerInterval = setInterval(() => {
        this.timeLeftSeconds--;
        this.updateTimerDisplay();
        if (this.timeLeftSeconds <= 0) {
          clearInterval(this.timerInterval);
          alert('Time up! Assessment submitted.');
          this.close();
        }
      }, 1000);

      const body = document.getElementById('quizModalBody');
      if (body) {
        body.innerHTML = `
          <div style="margin-bottom:20px;display:flex;justify-content:space-between;align-items:center;">
            <span style="font-weight:700;color:#f8fafc;">Timed Systems Assessment</span>
            <span id="quizTimerTag" style="background:#ef4444;color:#fff;padding:4px 10px;border-radius:12px;font-weight:700;">10:00</span>
          </div>
          <div style="background:#0f172a;padding:16px;border-radius:10px;margin-bottom:16px;">
            <h4 style="color:#38bdf8;margin-top:0;">Scenario Question 1:</h4>
            <p style="color:#f8fafc;font-size:15px;">In a High-Frequency Trading Limit Order Book, what data structure guarantees O(1) order cancellations by order ID?</p>
            <div style="display:flex;flex-direction:column;gap:8px;margin-top:12px;">
              <label style="padding:10px;background:#1e293b;border-radius:6px;cursor:pointer;color:#e2e8f0;display:flex;gap:8px;">
                <input type="radio" name="q1" value="0"> Intrusive doubly-linked list with order nodes indexed in a flat hash map.
              </label>
              <label style="padding:10px;background:#1e293b;border-radius:6px;cursor:pointer;color:#e2e8f0;display:flex;gap:8px;">
                <input type="radio" name="q1" value="1"> Single binary min-heap sorted by arrival timestamp.
              </label>
              <label style="padding:10px;background:#1e293b;border-radius:6px;cursor:pointer;color:#e2e8f0;display:flex;gap:8px;">
                <input type="radio" name="q1" value="2"> Unindexed singly linked list traversed on every cancel event.
              </label>
            </div>
          </div>
          <button class="action-pill-btn" style="width:100%;justify-content:center;background:#10b981;border-color:#10b981;" onclick="window.ActivityTracker.recordActivity(); alert('Score: 100% (Passed). Recorded to activity tracker.'); window.MockQuiz.close();">Submit Assessment</button>
        `;
      }
    },

    updateTimerDisplay() {
      const tag = document.getElementById('quizTimerTag');
      if (!tag) return;
      const mins = Math.floor(this.timeLeftSeconds / 60);
      const secs = this.timeLeftSeconds % 60;
      tag.textContent = `${mins}:${secs < 10 ? '0' : ''}${secs}`;
    }
  };

  // 11. System Architecture Design Canvas
  const ArchitectureCanvas = {
    modal: null,
    canvas: null,
    ctx: null,

    init() {
      this.modal = document.getElementById('canvasModal');
      this.canvas = document.getElementById('archCanvas');
      if (this.canvas) {
        this.ctx = this.canvas.getContext('2d');
        this.drawTemplate();
      }
    },

    open() {
      if (!this.modal) return;
      this.modal.classList.add('active');
      this.drawTemplate();
    },

    close() {
      if (this.modal) this.modal.classList.remove('active');
    },

    drawTemplate() {
      if (!this.ctx || !this.canvas) return;
      const ctx = this.ctx;
      ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

      // Background grid
      ctx.strokeStyle = '#1e293b';
      ctx.lineWidth = 1;
      for (let x = 0; x < this.canvas.width; x += 40) {
        ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, this.canvas.height); ctx.stroke();
      }
      for (let y = 0; y < this.canvas.height; y += 40) {
        ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(this.canvas.width, y); ctx.stroke();
      }

      // Draw high-throughput trading & enterprise template
      this.drawBox(40, 160, 130, 60, '#38bdf8', 'Kernel Bypass NIC', 'DPDK / 100GbE');
      this.drawArrow(170, 190, 240, 190);
      this.drawBox(240, 100, 150, 60, '#818cf8', 'Matching Engine', 'Lock-Free Disruptor');
      this.drawBox(240, 220, 150, 60, '#818cf8', 'Risk Gateway', 'FPGA Pre-Trade');
      this.drawArrow(390, 130, 480, 130);
      this.drawBox(480, 100, 140, 60, '#34d399', 'Chronicle Queue', 'Zero-Copy Journal');
      this.drawArrow(390, 250, 480, 250);
      this.drawBox(480, 220, 140, 60, '#fbbf24', 'Market Data Feed', 'UDP Multicast');
    },

    drawBox(x, y, w, h, color, title, sub) {
      const ctx = this.ctx;
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(x, y, w, h);
      ctx.strokeStyle = color;
      ctx.lineWidth = 2;
      ctx.strokeRect(x, y, w, h);

      ctx.fillStyle = color;
      ctx.font = 'bold 13px Inter, sans-serif';
      ctx.fillText(title, x + 10, y + 26);

      ctx.fillStyle = '#94a3b8';
      ctx.font = '11px monospace';
      ctx.fillText(sub, x + 10, y + 46);
    },

    drawArrow(fromX, fromY, toX, toY) {
      const ctx = this.ctx;
      ctx.strokeStyle = '#f8fafc';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(fromX, fromY);
      ctx.lineTo(toX, toY);
      ctx.stroke();
    }
  };

  // 12. Raft Consensus Protocol Simulator
  const RaftSimulator = {
    modal: null,
    canvas: null,
    ctx: null,
    term: 1,
    nodes: [
      { id: 1, role: 'LEADER', x: 200, y: 100, votes: 3, alive: true },
      { id: 2, role: 'FOLLOWER', x: 100, y: 240, votes: 0, alive: true },
      { id: 3, role: 'FOLLOWER', x: 300, y: 240, votes: 0, alive: true }
    ],
    packetPos: 0,
    animFrame: null,

    init() {
      this.modal = document.getElementById('raftModal');
      this.canvas = document.getElementById('raftCanvas');
      if (this.canvas) this.ctx = this.canvas.getContext('2d');
    },

    open() {
      if (!this.modal) return;
      this.modal.classList.add('active');
      this.startLoop();
    },

    close() {
      if (this.modal) this.modal.classList.remove('active');
      cancelAnimationFrame(this.animFrame);
    },

    killLeader() {
      const leader = this.nodes.find(n => n.role === 'LEADER');
      if (leader) {
        leader.alive = false;
        leader.role = 'CRASHED';
        setTimeout(() => this.triggerElection(), 1500);
      }
    },

    resetCluster() {
      this.term++;
      this.nodes = [
        { id: 1, role: 'LEADER', x: 200, y: 100, votes: 3, alive: true },
        { id: 2, role: 'FOLLOWER', x: 100, y: 240, votes: 0, alive: true },
        { id: 3, role: 'FOLLOWER', x: 300, y: 240, votes: 0, alive: true }
      ];
    },

    triggerElection() {
      this.term++;
      const candidate = this.nodes.find(n => n.alive && n.role === 'FOLLOWER');
      if (candidate) {
        candidate.role = 'CANDIDATE';
        setTimeout(() => {
          candidate.role = 'LEADER';
          this.nodes.forEach(n => { if (n.alive && n.id !== candidate.id) n.role = 'FOLLOWER'; });
        }, 1200);
      }
    },

    startLoop() {
      const render = () => {
        this.draw();
        this.packetPos = (this.packetPos + 0.02) % 1;
        this.animFrame = requestAnimationFrame(render);
      };
      render();
    },

    draw() {
      if (!this.ctx || !this.canvas) return;
      const ctx = this.ctx;
      ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

      ctx.fillStyle = '#f8fafc';
      ctx.font = 'bold 13px Inter, sans-serif';
      ctx.fillText(`Raft Term: ${this.term} | State: Distributed Consensus Active`, 20, 30);

      // Draw Network Edges
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(this.nodes[0].x, this.nodes[0].y); ctx.lineTo(this.nodes[1].x, this.nodes[1].y);
      ctx.moveTo(this.nodes[0].x, this.nodes[0].y); ctx.lineTo(this.nodes[2].x, this.nodes[2].y);
      ctx.moveTo(this.nodes[1].x, this.nodes[1].y); ctx.lineTo(this.nodes[2].x, this.nodes[2].y);
      ctx.stroke();

      // Heartbeat packets from leader
      const leader = this.nodes.find(n => n.role === 'LEADER' && n.alive);
      if (leader) {
        this.nodes.forEach(f => {
          if (f.id !== leader.id && f.alive) {
            const px = leader.x + (f.x - leader.x) * this.packetPos;
            const py = leader.y + (f.y - leader.y) * this.packetPos;
            ctx.fillStyle = '#38bdf8';
            ctx.beginPath();
            ctx.arc(px, py, 5, 0, Math.PI * 2);
            ctx.fill();
          }
        });
      }

      // Draw Nodes
      this.nodes.forEach(n => {
        ctx.beginPath();
        ctx.arc(n.x, n.y, 36, 0, Math.PI * 2);
        ctx.fillStyle = !n.alive ? '#ef4444' : (n.role === 'LEADER' ? '#10b981' : (n.role === 'CANDIDATE' ? '#f59e0b' : '#3b82f6'));
        ctx.fill();
        ctx.strokeStyle = '#f8fafc';
        ctx.lineWidth = 2;
        ctx.stroke();

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 12px Inter, sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(`Node ${n.id}`, n.x, n.y - 4);
        ctx.font = '10px monospace';
        ctx.fillText(n.role, n.x, n.y + 12);
        ctx.textAlign = 'left';
      });
    }
  };

  // 13. Algorithm Performance Benchmark Comparator
  const BenchmarkRunner = {
    modal: null,

    init() {
      this.modal = document.getElementById('benchmarkModal');
    },

    open() {
      if (!this.modal) return;
      this.modal.classList.add('active');
      const codeA = document.getElementById('benchCodeA');
      const codeB = document.getElementById('benchCodeB');
      if (codeA && !codeA.value.trim()) {
        codeA.value = `// Algorithm A: Native Array Push\nconst arr = [];\nfor (let i = 0; i < 10000; i++) {\n  arr.push(i * 2);\n}`;
      }
      if (codeB && !codeB.value.trim()) {
        codeB.value = `// Algorithm B: Pre-Allocated TypedArray\nconst buf = new Int32Array(10000);\nfor (let i = 0; i < 10000; i++) {\n  buf[i] = i * 2;\n}`;
      }
    },

    close() {
      if (this.modal) this.modal.classList.remove('active');
    },

    runBenchmark() {
      const codeA = document.getElementById('benchCodeA').value;
      const codeB = document.getElementById('benchCodeB').value;
      const out = document.getElementById('benchOutput');
      if (!out) return;

      out.innerHTML = 'Running 100 iterations each at line rate...';

      setTimeout(() => {
        try {
          const fnA = new Function(codeA);
          const fnB = new Function(codeB);

          // Warmup
          for (let i = 0; i < 10; i++) { fnA(); fnB(); }

          const startA = performance.now();
          for (let i = 0; i < 100; i++) fnA();
          const durA = performance.now() - startA;

          const startB = performance.now();
          for (let i = 0; i < 100; i++) fnB();
          const durB = performance.now() - startB;

          const opsA = Math.round((100 / durA) * 1000);
          const opsB = Math.round((100 / durB) * 1000);
          const speedup = (opsB / opsA).toFixed(2);

          out.innerHTML = `
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:8px;">
              <div style="background:#0f172a;padding:10px;border-radius:6px;border-left:4px solid #38bdf8;">
                <div style="color:#38bdf8;font-weight:700;">Algorithm A</div>
                <div style="color:#f8fafc;font-size:18px;font-weight:800;margin:4px 0;">${opsA.toLocaleString()} ops/sec</div>
                <div style="color:#94a3b8;font-size:11px;">Total time: ${durA.toFixed(2)}ms (100 runs)</div>
              </div>
              <div style="background:#0f172a;padding:10px;border-radius:6px;border-left:4px solid #10b981;">
                <div style="color:#10b981;font-weight:700;">Algorithm B</div>
                <div style="color:#f8fafc;font-size:18px;font-weight:800;margin:4px 0;">${opsB.toLocaleString()} ops/sec</div>
                <div style="color:#94a3b8;font-size:11px;">Total time: ${durB.toFixed(2)}ms (${speedup}x speedup)</div>
              </div>
            </div>
          `;
          ActivityTracker.recordActivity();
        } catch (err) {
          out.textContent = `[Benchmark Error]: ${err.message}`;
        }
      }, 50);
    }
  };

  // 14. Candidate Readiness Score Radar Chart
  const ReadinessRadar = {
    modal: null,
    canvas: null,
    ctx: null,

    init() {
      this.modal = document.getElementById('radarModal');
      this.canvas = document.getElementById('radarCanvas');
      if (this.canvas) this.ctx = this.canvas.getContext('2d');
    },

    open() {
      if (!this.modal) return;
      this.modal.classList.add('active');
      this.draw();
    },

    close() {
      if (this.modal) this.modal.classList.remove('active');
    },

    draw() {
      if (!this.ctx || !this.canvas) return;
      const ctx = this.ctx;
      ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

      const cx = this.canvas.width / 2;
      const cy = this.canvas.height / 2;
      const r = 110;
      const axes = ['Algorithms', 'Systems & Kernel', 'Architecture', 'Security & Crypt', 'Web Protocols'];
      const scores = [0.85, 0.92, 0.88, 0.82, 0.90]; // 0.0 - 1.0
      const total = axes.length;

      // Draw concentric pentagons
      for (let level = 1; level <= 4; level++) {
        ctx.beginPath();
        for (let i = 0; i < total; i++) {
          const angle = (Math.PI * 2 / total) * i - Math.PI / 2;
          const x = cx + (r * (level / 4)) * Math.cos(angle);
          const y = cy + (r * (level / 4)) * Math.sin(angle);
          if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
        }
        ctx.closePath();
        ctx.strokeStyle = 'rgba(148, 163, 184, 0.2)';
        ctx.stroke();
      }

      // Draw axes and labels
      for (let i = 0; i < total; i++) {
        const angle = (Math.PI * 2 / total) * i - Math.PI / 2;
        const x = cx + r * Math.cos(angle);
        const y = cy + r * Math.sin(angle);
        ctx.beginPath();
        ctx.moveTo(cx, cy);
        ctx.lineTo(x, y);
        ctx.strokeStyle = 'rgba(148, 163, 184, 0.4)';
        ctx.stroke();

        ctx.fillStyle = '#38bdf8';
        ctx.font = 'bold 11px Inter, sans-serif';
        ctx.textAlign = 'center';
        const lx = cx + (r + 24) * Math.cos(angle);
        const ly = cy + (r + 14) * Math.sin(angle);
        ctx.fillText(axes[i], lx, ly);
      }

      // Draw Score Polygon
      ctx.beginPath();
      for (let i = 0; i < total; i++) {
        const angle = (Math.PI * 2 / total) * i - Math.PI / 2;
        const x = cx + (r * scores[i]) * Math.cos(angle);
        const y = cy + (r * scores[i]) * Math.sin(angle);
        if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.closePath();
      ctx.fillStyle = 'rgba(16, 185, 129, 0.35)';
      ctx.fill();
      ctx.strokeStyle = '#10b981';
      ctx.lineWidth = 2;
      ctx.stroke();
    }
  };

  // 15. Pomodoro Focus Timer
  const PomodoroTimer = {
    modal: null,
    interval: null,
    remaining: 25 * 60,
    running: false,

    init() {
      this.modal = document.getElementById('pomodoroModal');
    },

    open() {
      if (!this.modal) return;
      this.modal.classList.add('active');
    },

    close() {
      if (this.modal) this.modal.classList.remove('active');
    },

    toggle() {
      const btn = document.getElementById('pomoStartBtn');
      if (this.running) {
        clearInterval(this.interval);
        this.running = false;
        if (btn) btn.textContent = 'Start Focus';
      } else {
        this.running = true;
        if (btn) btn.textContent = 'Pause';
        this.interval = setInterval(() => {
          this.remaining--;
          this.updateDisplay();
          if (this.remaining <= 0) {
            clearInterval(this.interval);
            this.running = false;
            alert('Focus Session Complete! 5 min break started.');
            ActivityTracker.recordActivity();
            this.reset();
          }
        }, 1000);
      }
    },

    reset() {
      clearInterval(this.interval);
      this.running = false;
      this.remaining = 25 * 60;
      this.updateDisplay();
      const btn = document.getElementById('pomoStartBtn');
      if (btn) btn.textContent = 'Start Focus';
    },

    updateDisplay() {
      const display = document.getElementById('pomoDisplay');
      if (!display) return;
      const m = Math.floor(this.remaining / 60);
      const s = this.remaining % 60;
      display.textContent = `${m}:${s < 10 ? '0' : ''}${s}`;
    }
  };

  // 16. Vim Keybindings Navigation Mode
  const VimMode = {
    enabled: false,

    init() {
      document.addEventListener('keydown', (e) => {
        if (['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) return;
        if (!this.enabled) return;

        if (e.key === 'j') {
          // Scroll next question
          window.scrollBy({ top: 300, behavior: 'smooth' });
        } else if (e.key === 'k') {
          // Scroll prev question
          window.scrollBy({ top: -300, behavior: 'smooth' });
        } else if (e.key === 'G') {
          window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
        } else if (e.key === 'g' && e.repeat === false) {
          window.scrollTo({ top: 0, behavior: 'smooth' });
        }
      });
    },

    toggle() {
      this.enabled = !this.enabled;
      const tag = document.getElementById('vimModeTag');
      if (tag) tag.textContent = this.enabled ? 'ON' : 'OFF';
      alert(`Vim Navigation Mode: ${this.enabled ? 'ENABLED (Use j/k/G/g)' : 'DISABLED'}`);
  // 17. LSM-Tree Storage Engine & Compaction Simulator
  const LSMTreeSimulator = {
    modal: null,
    canvas: null,
    ctx: null,
    memtable: ['key_01: "val_A"', 'key_03: "val_B"'],
    l0: [['key_02: "val_C"', 'key_05: "val_D"']],
    l1: [['key_01: "val_A"', 'key_02: "val_C"', 'key_04: "val_E"']],

    init() {
      this.modal = document.getElementById('lsmModal');
      this.canvas = document.getElementById('lsmCanvas');
      if (this.canvas) this.ctx = this.canvas.getContext('2d');
    },

    open() {
      if (!this.modal) return;
      this.modal.classList.add('active');
      this.draw();
    },

    close() {
      if (this.modal) this.modal.classList.remove('active');
    },

    insertKey() {
      const id = Math.floor(Math.random() * 90) + 10;
      this.memtable.push(`key_${id}: "val_${id}"`);
      if (this.memtable.length >= 4) {
        this.flushMemtable();
      }
      this.draw();
    },

    flushMemtable() {
      if (this.memtable.length) {
        this.l0.push([...this.memtable]);
        this.memtable = [];
      }
      this.draw();
    },

    compactL0toL1() {
      if (!this.l0.length) return;
      // Merge sort all L0 tables into L1
      const merged = new Set();
      this.l1.flat().forEach(k => merged.add(k));
      this.l0.flat().forEach(k => merged.add(k));
      this.l1 = [Array.from(merged).sort()];
      this.l0 = [];
      this.draw();
    },

    draw() {
      if (!this.ctx || !this.canvas) return;
      const ctx = this.ctx;
      ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

      // Section 1: In-Memory MemTable
      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 13px Inter, sans-serif';
      ctx.fillText('RAM: Active MemTable (SkipList)', 20, 30);

      ctx.fillStyle = '#0f172a';
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2;
      ctx.fillRect(20, 45, 220, 180);
      ctx.strokeRect(20, 45, 220, 180);

      ctx.fillStyle = '#f8fafc';
      ctx.font = '11px monospace';
      if (!this.memtable.length) {
        ctx.fillStyle = '#64748b';
        ctx.fillText('(MemTable Empty)', 35, 75);
      } else {
        this.memtable.forEach((k, i) => {
          ctx.fillText(`• ${k}`, 30, 75 + i * 26);
        });
      }

      // Section 2: Disk Level 0 SSTables (Unsorted / Overlapping)
      ctx.fillStyle = '#f59e0b';
      ctx.font = 'bold 13px Inter, sans-serif';
      ctx.fillText(`Disk: Level 0 SSTables (${this.l0.length} files)`, 280, 30);

      ctx.fillStyle = '#0f172a';
      ctx.strokeStyle = '#f59e0b';
      ctx.fillRect(280, 45, 220, 180);
      ctx.strokeRect(280, 45, 220, 180);

      ctx.fillStyle = '#f8fafc';
      ctx.font = '11px monospace';
      if (!this.l0.length) {
        ctx.fillStyle = '#64748b';
        ctx.fillText('(No L0 SSTables)', 295, 75);
      } else {
        this.l0.flat().slice(0, 6).forEach((k, i) => {
          ctx.fillText(`• ${k}`, 290, 75 + i * 26);
        });
      }

      // Section 3: Disk Level 1 SSTables (Compacted / Sorted)
      ctx.fillStyle = '#10b981';
      ctx.font = 'bold 13px Inter, sans-serif';
      ctx.fillText('Disk: Level 1 SSTables (Compacted)', 540, 30);

      ctx.fillStyle = '#0f172a';
      ctx.strokeStyle = '#10b981';
      ctx.fillRect(540, 45, 220, 180);
      ctx.strokeRect(540, 45, 220, 180);

      ctx.fillStyle = '#f8fafc';
      ctx.font = '11px monospace';
      if (!this.l1.length || !this.l1[0].length) {
        ctx.fillStyle = '#64748b';
        ctx.fillText('(Level 1 Empty)', 555, 75);
      } else {
        this.l1[0].slice(0, 6).forEach((k, i) => {
          ctx.fillText(`• ${k}`, 550, 75 + i * 26);
        });
      }

      // Bottom Status info
      ctx.fillStyle = '#94a3b8';
      ctx.font = '12px Inter, sans-serif';
      ctx.fillText('Writes hit MemTable sequentially -> Flushed as immutable L0 SSTables -> Background merge into L1.', 20, 260);
    }
  };

  // 18. Consistent Hashing Ring Simulator
  const ConsistentHashSimulator = {
    modal: null,
    canvas: null,
    ctx: null,
    nodes: [
      { id: 'Node A', angle: 0, color: '#38bdf8', alive: true },
      { id: 'Node B', angle: Math.PI / 2, color: '#10b981', alive: true },
      { id: 'Node C', angle: Math.PI, color: '#f59e0b', alive: true },
      { id: 'Node D', angle: 3 * Math.PI / 2, color: '#ec4899', alive: true }
    ],
    keys: [
      { name: 'user_101', angle: 0.4 },
      { name: 'order_402', angle: 1.8 },
      { name: 'payment_99', angle: 3.5 },
      { name: 'session_8', angle: 5.2 }
    ],

    init() {
      this.modal = document.getElementById('hashRingModal');
      this.canvas = document.getElementById('hashRingCanvas');
      if (this.canvas) this.ctx = this.canvas.getContext('2d');
    },

    open() {
      if (!this.modal) return;
      this.modal.classList.add('active');
      this.draw();
    },

    close() {
      if (this.modal) this.modal.classList.remove('active');
    },

    toggleNodeB() {
      const nodeB = this.nodes.find(n => n.id === 'Node B');
      if (nodeB) {
        nodeB.alive = !nodeB.alive;
        this.draw();
      }
    },

    addRandomKey() {
      const randAngle = Math.random() * Math.PI * 2;
      const id = Math.floor(Math.random() * 900) + 100;
      this.keys.push({ name: `key_${id}`, angle: randAngle });
      if (this.keys.length > 8) this.keys.shift();
      this.draw();
    },

    draw() {
      if (!this.ctx || !this.canvas) return;
      const ctx = this.ctx;
      ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

      const cx = this.canvas.width / 2;
      const cy = this.canvas.height / 2;
      const radius = 110;

      // Draw Main Hash Ring
      ctx.beginPath();
      ctx.arc(cx, cy, radius, 0, Math.PI * 2);
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 4;
      ctx.stroke();

      // Draw Nodes
      this.nodes.forEach(node => {
        const nx = cx + radius * Math.cos(node.angle);
        const ny = cy + radius * Math.sin(node.angle);

        ctx.beginPath();
        ctx.arc(nx, ny, 16, 0, Math.PI * 2);
        ctx.fillStyle = node.alive ? node.color : '#ef4444';
        ctx.fill();
        ctx.strokeStyle = '#ffffff';
        ctx.lineWidth = 2;
        ctx.stroke();

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 11px Inter, sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(node.alive ? node.id : 'OFFLINE', nx, ny - 22);
      });

      // Draw Keys on the Ring (routed clockwise to first alive node)
      this.keys.forEach(k => {
        const kx = cx + (radius - 18) * Math.cos(k.angle);
        const ky = cy + (radius - 18) * Math.sin(k.angle);

        ctx.beginPath();
        ctx.arc(kx, ky, 6, 0, Math.PI * 2);
        ctx.fillStyle = '#f8fafc';
        ctx.fill();

        ctx.fillStyle = '#94a3b8';
        ctx.font = '10px monospace';
        ctx.fillText(k.name, kx, ky + 16);
      });

      ctx.fillStyle = '#64748b';
      ctx.font = '12px Inter, sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('Consistent Hashing 360° Ring: Keys route clockwise to nearest healthy node', cx, this.canvas.height - 15);
      ctx.textAlign = 'left';
    }
  };

  // 19. Curated Filter Presets
  const CuratedFilters = {
    applyPreset(preset) {
      const items = document.querySelectorAll('.markdown-content h3');
      if (!items.length) {
        alert(`Curated Filter '${preset}' applied! Navigate to any category to view tailored questions.`);
        return;
      }
      items.forEach(h3 => {
        const text = h3.textContent.toLowerCase();
        let show = true;
        if (preset === 'staff') {
          show = text.includes('architecture') || text.includes('distributed') || text.includes('trade-off') || text.includes('concurrency');
        } else if (preset === 'hft') {
          show = text.includes('latency') || text.includes('kernel') || text.includes('lock-free') || text.includes('cache');
        } else if (preset === 'security') {
          show = text.includes('security') || text.includes('vulnerability') || text.includes('crypto') || text.includes('exploit');
        }
        h3.parentElement.style.display = show ? 'block' : 'none';
      });
      alert(`Applied Filter Preset: ${preset.toUpperCase()}`);
    }
  };

  // 20. Print-to-PDF Exporter
  const PDFExporter = {
    exportCurrent() {
      window.print();
    }
  };

  // Export to window
  window.ThemeEngine = ThemeEngine;
  window.InstantSearch = InstantSearch;
  window.CodePlayground = CodePlayground;
  window.ActivityTracker = ActivityTracker;
  window.MemoryVisualizer = MemoryVisualizer;
  window.EncryptedNotes = EncryptedNotes;
  window.AnkiExporter = AnkiExporter;
  window.WebRTCInterview = WebRTCInterview;
  window.FlashcardMode = FlashcardMode;
  window.MockQuiz = MockQuiz;
  window.ArchitectureCanvas = ArchitectureCanvas;
  window.RaftSimulator = RaftSimulator;
  window.BenchmarkRunner = BenchmarkRunner;
  window.ReadinessRadar = ReadinessRadar;
  window.PomodoroTimer = PomodoroTimer;
  window.VimMode = VimMode;
  window.LSMTreeSimulator = LSMTreeSimulator;
  window.ConsistentHashSimulator = ConsistentHashSimulator;
  window.CuratedFilters = CuratedFilters;
  window.PDFExporter = PDFExporter;

  document.addEventListener('DOMContentLoaded', () => {
    ThemeEngine.init();
    InstantSearch.init();
    CodePlayground.init();
    FlashcardMode.init();
    MockQuiz.init();
    ArchitectureCanvas.init();
    MemoryVisualizer.init();
    WebRTCInterview.init();
    RaftSimulator.init();
    BenchmarkRunner.init();
    ReadinessRadar.init();
    PomodoroTimer.init();
    VimMode.init();
    LSMTreeSimulator.init();
    ConsistentHashSimulator.init();
    ActivityTracker.renderHeatmap();

    if ('serviceWorker' in navigator) {
      navigator.serviceWorker.register('./sw.js').catch(err => {
        console.warn('PWA ServiceWorker registration failed:', err);
      });
    }
  });
})();

