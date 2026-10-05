// ==============================================================================
// Advanced Simulators & Interactive Low-Level Visualizers Engine
// TCP/TLS, B-Tree, GC Mark-Sweep, CPU Cache/MESI, SQL Explain, Regex DFA,
// Deadlock RAG, Epoll vs Select, Buddy Allocator, System Trade-offs, Chaos Monkey
// ==============================================================================

(function () {
  'use strict';

  // ----------------------------------------------------------------------------
  // 1. TCP 3-Way Handshake & TLS 1.3 Simulator
  // ----------------------------------------------------------------------------
  const TcpTlsSimulator = {
    canvas: null,
    ctx: null,
    steps: [
      { sender: 'client', receiver: 'server', label: '1. SYN (seq=100, win=65535)', proto: 'TCP', color: '#38bdf8' },
      { sender: 'server', receiver: 'client', label: '2. SYN-ACK (seq=300, ack=101)', proto: 'TCP', color: '#818cf8' },
      { sender: 'client', receiver: 'server', label: '3. ACK (seq=101, ack=301) [TCP Established]', proto: 'TCP', color: '#34d399' },
      { sender: 'client', receiver: 'server', label: '4. TLS 1.3 ClientHello (CipherSuites, Curve25519 KeyShare)', proto: 'TLS', color: '#f59e0b' },
      { sender: 'server', receiver: 'client', label: '5. TLS 1.3 ServerHello + EncryptedExtensions + Finished', proto: 'TLS', color: '#fb7185' },
      { sender: 'client', receiver: 'server', label: '6. TLS Finished + Encrypted HTTP/2 GET /', proto: 'TLS/HTTP', color: '#a78bfa' }
    ],
    currentStep: 0,
    animProgress: 1.0,
    animId: null,

    init() {
      this.canvas = document.getElementById('tcpCanvas');
      if (!this.canvas) return;
      this.ctx = this.canvas.getContext('2d');
      this.draw();
    },

    open() {
      const modal = document.getElementById('tcpModal');
      if (modal) {
        modal.classList.add('active');
        this.init();
      }
    },

    close() {
      const modal = document.getElementById('tcpModal');
      if (modal) modal.classList.remove('active');
    },

    nextStep() {
      if (this.currentStep < this.steps.length) {
        this.currentStep++;
        this.draw();
      }
    },

    reset() {
      this.currentStep = 0;
      this.draw();
    },

    injectDrop() {
      if (this.currentStep > 0) {
        const statusEl = document.getElementById('tcpStatus');
        if (statusEl) {
          statusEl.textContent = '⚠️ Packet Drop Detected! Retransmission Timeout (RTO = 200ms) triggered...';
          statusEl.style.color = '#f43f5e';
          setTimeout(() => {
            statusEl.textContent = 'Retransmission successful. Flow restored.';
            statusEl.style.color = '#34d399';
          }, 1200);
        }
      }
    },

    draw() {
      if (!this.ctx) return;
      const ctx = this.ctx;
      const w = this.canvas.width;
      const h = this.canvas.height;

      ctx.clearRect(0, 0, w, h);

      // Client & Server Lifelines
      const clientX = 140;
      const serverX = w - 140;
      const topY = 60;
      const bottomY = h - 30;

      // Draw Headers
      ctx.fillStyle = '#f8fafc';
      ctx.font = 'bold 14px system-ui, sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('Client (192.168.1.50)', clientX, 35);
      ctx.fillText('Server (142.250.190.46:443)', serverX, 35);

      // Vertical lifeline dashed lines
      ctx.setLineDash([4, 4]);
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
      ctx.lineWidth = 2;

      ctx.beginPath();
      ctx.moveTo(clientX, topY);
      ctx.lineTo(clientX, bottomY);
      ctx.stroke();

      ctx.beginPath();
      ctx.moveTo(serverX, topY);
      ctx.lineTo(serverX, bottomY);
      ctx.stroke();
      ctx.setLineDash([]);

      // Draw Steps
      const stepSpacing = (bottomY - topY) / (this.steps.length + 1);

      for (let i = 0; i < this.currentStep; i++) {
        const step = this.steps[i];
        const yStart = topY + (i + 1) * stepSpacing - 15;
        const yEnd = topY + (i + 1) * stepSpacing + 15;

        const fromX = step.sender === 'client' ? clientX : serverX;
        const toX = step.receiver === 'client' ? clientX : serverX;

        ctx.strokeStyle = step.color;
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(fromX, yStart);
        ctx.lineTo(toX, yEnd);
        ctx.stroke();

        // Arrowhead
        const angle = Math.atan2(yEnd - yStart, toX - fromX);
        const headLen = 10;
        ctx.fillStyle = step.color;
        ctx.beginPath();
        ctx.moveTo(toX, yEnd);
        ctx.lineTo(toX - headLen * Math.cos(angle - Math.PI / 6), yEnd - headLen * Math.sin(angle - Math.PI / 6));
        ctx.lineTo(toX - headLen * Math.cos(angle + Math.PI / 6), yEnd - headLen * Math.sin(angle + Math.PI / 6));
        ctx.fill();

        // Step Label badge
        ctx.fillStyle = step.color;
        ctx.font = 'bold 11px system-ui, monospace';
        ctx.textAlign = 'center';
        ctx.fillText(step.label, (clientX + serverX) / 2, (yStart + yEnd) / 2 - 6);
      }

      const statusEl = document.getElementById('tcpStatus');
      if (statusEl && this.currentStep < this.steps.length) {
        statusEl.textContent = `Current Step: ${this.currentStep}/${this.steps.length} — Next: ${this.steps[this.currentStep].label}`;
        statusEl.style.color = '#cbd5e1';
      } else if (statusEl && this.currentStep === this.steps.length) {
        statusEl.textContent = '✅ Full TLS 1.3 1-RTT Handshake Complete. Encrypted Session Active.';
        statusEl.style.color = '#10b981';
      }
    }
  };

  // ----------------------------------------------------------------------------
  // 2. B-Tree / B+ Tree Dynamic Node Split Simulator
  // ----------------------------------------------------------------------------
  class BTreeNode {
    constructor(isLeaf = true) {
      this.isLeaf = isLeaf;
      this.keys = [];
      this.children = [];
    }
  }

  const BTreeSimulator = {
    canvas: null,
    ctx: null,
    root: null,
    maxKeys: 3, // Degree M=4 -> max keys 3

    init() {
      this.canvas = document.getElementById('btreeCanvas');
      if (!this.canvas) return;
      this.ctx = this.canvas.getContext('2d');
      this.reset();
    },

    open() {
      const modal = document.getElementById('btreeModal');
      if (modal) {
        modal.classList.add('active');
        this.init();
      }
    },

    close() {
      const modal = document.getElementById('btreeModal');
      if (modal) modal.classList.remove('active');
    },

    reset() {
      this.root = new BTreeNode(true);
      // Pre-seed with initial keys
      [10, 20, 30, 40, 50, 60, 70].forEach(k => this.insert(k));
      this.draw();
    },

    insertKeyFromInput() {
      const input = document.getElementById('btreeKeyInput');
      if (!input) return;
      const val = parseInt(input.value, 10);
      if (!isNaN(val)) {
        this.insert(val);
        input.value = '';
        this.draw();
      }
    },

    insertRandom() {
      const r = Math.floor(Math.random() * 90) + 10;
      this.insert(r);
      this.draw();
    },

    insert(key) {
      if (!this.root) this.root = new BTreeNode(true);
      if (this.root.keys.includes(key)) return;

      if (this.root.keys.length === this.maxKeys) {
        const s = new BTreeNode(false);
        s.children.push(this.root);
        this.splitChild(s, 0);
        this.root = s;
      }
      this.insertNonFull(this.root, key);
    },

    insertNonFull(node, key) {
      let i = node.keys.length - 1;
      if (node.isLeaf) {
        node.keys.push(key);
        node.keys.sort((a, b) => a - b);
      } else {
        while (i >= 0 && key < node.keys[i]) i--;
        i++;
        if (node.children[i].keys.length === this.maxKeys) {
          this.splitChild(node, i);
          if (key > node.keys[i]) i++;
        }
        this.insertNonFull(node.children[i], key);
      }
    },

    splitChild(parent, index) {
      const child = parent.children[index];
      const z = new BTreeNode(child.isLeaf);
      const mid = Math.floor(this.maxKeys / 2);
      const promotedKey = child.keys[mid];

      z.keys = child.keys.slice(mid + 1);
      child.keys = child.keys.slice(0, mid);

      if (!child.isLeaf) {
        z.children = child.children.slice(mid + 1);
        child.children = child.children.slice(0, mid + 1);
      }

      parent.children.splice(index + 1, 0, z);
      parent.keys.splice(index, 0, promotedKey);
    },

    draw() {
      if (!this.ctx || !this.root) return;
      const ctx = this.ctx;
      const w = this.canvas.width;
      const h = this.canvas.height;
      ctx.clearRect(0, 0, w, h);

      const renderSubtree = (node, x, y, xSpan) => {
        if (!node) return;

        // Render Node Box
        const nodeWidth = Math.max(node.keys.length * 32 + 20, 60);
        const nodeHeight = 32;

        ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
        ctx.strokeStyle = '#6366f1';
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.roundRect(x - nodeWidth / 2, y - nodeHeight / 2, nodeWidth, nodeHeight, 6);
        ctx.fill();
        ctx.stroke();

        // Render Keys
        ctx.fillStyle = '#f8fafc';
        ctx.font = 'bold 12px monospace';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        const keySpacing = nodeWidth / (node.keys.length + 1);
        node.keys.forEach((k, idx) => {
          const kx = (x - nodeWidth / 2) + (idx + 1) * keySpacing;
          ctx.fillText(k, kx, y);
        });

        // Render Child Connectors
        if (!node.isLeaf && node.children.length > 0) {
          const numChildren = node.children.length;
          const childSpan = xSpan / numChildren;
          node.children.forEach((child, cIdx) => {
            const cx = (x - xSpan / 2) + (cIdx + 0.5) * childSpan;
            const cy = y + 70;

            ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
            ctx.lineWidth = 1.5;
            ctx.beginPath();
            ctx.moveTo(x, y + nodeHeight / 2);
            ctx.lineTo(cx, cy - nodeHeight / 2);
            ctx.stroke();

            renderSubtree(child, cx, cy, childSpan);
          });
        }
      };

      renderSubtree(this.root, w / 2, 45, w - 80);
    }
  };

  // ----------------------------------------------------------------------------
  // 3. Garbage Collection Mark & Sweep Simulator (Tri-color Abstraction)
  // ----------------------------------------------------------------------------
  const GcMarkSweepSimulator = {
    canvas: null,
    ctx: null,
    objects: [],
    roots: [0], // Object 0 is Root
    phase: 'Idle', // 'Idle', 'Mark', 'Sweep', 'Compacted'

    init() {
      this.canvas = document.getElementById('gcCanvas');
      if (!this.canvas) return;
      this.ctx = this.canvas.getContext('2d');
      this.reset();
    },

    open() {
      const modal = document.getElementById('gcModal');
      if (modal) {
        modal.classList.add('active');
        this.init();
      }
    },

    close() {
      const modal = document.getElementById('gcModal');
      if (modal) modal.classList.remove('active');
    },

    reset() {
      this.phase = 'Idle';
      this.objects = [
        { id: 0, label: 'Root (Stack)', color: 'black', x: 80, y: 140, refs: [1, 2], isRoot: true },
        { id: 1, label: 'Obj A', color: 'white', x: 220, y: 80, refs: [3] },
        { id: 2, label: 'Obj B', color: 'white', x: 220, y: 200, refs: [4] },
        { id: 3, label: 'Obj C', color: 'white', x: 380, y: 80, refs: [] },
        { id: 4, label: 'Obj D', color: 'white', x: 380, y: 200, refs: [] },
        { id: 5, label: 'Obj E (Leak)', color: 'white', x: 540, y: 80, refs: [6] },
        { id: 6, label: 'Obj F (Dead)', color: 'white', x: 680, y: 80, refs: [5] } // Circular dead ref
      ];
      this.draw();
    },

    severPointer() {
      // Sever Obj B -> Obj D
      const objB = this.objects.find(o => o.id === 2);
      if (objB) objB.refs = [];
      this.draw();
      const statusEl = document.getElementById('gcStatus');
      if (statusEl) statusEl.textContent = 'Severed reference from Obj B to Obj D. Obj D is now unreachable garbage!';
    },

    stepMark() {
      this.phase = 'Mark';
      // Tri-color: Root is black, discover reachable
      const reachable = new Set();
      const queue = [...this.roots];
      while (queue.length > 0) {
        const currId = queue.shift();
        reachable.add(currId);
        const obj = this.objects.find(o => o.id === currId);
        if (obj) {
          obj.color = 'black'; // Marked alive
          obj.refs.forEach(r => {
            if (!reachable.has(r)) queue.push(r);
          });
        }
      }
      this.draw();
      const statusEl = document.getElementById('gcStatus');
      if (statusEl) statusEl.textContent = 'Mark Phase Complete: Reachable graph colored Black. Unreachable objects remain White.';
    },

    sweep() {
      this.phase = 'Sweep';
      this.objects = this.objects.filter(o => o.color === 'black');
      this.draw();
      const statusEl = document.getElementById('gcStatus');
      if (statusEl) statusEl.textContent = 'Sweep Phase Complete: White unreachable objects reclaimed into allocator free-list!';
    },

    compact() {
      this.phase = 'Compacted';
      // Shift objects linearly leftward
      this.objects.forEach((o, idx) => {
        o.x = 100 + idx * 140;
        o.y = 140;
      });
      this.draw();
      const statusEl = document.getElementById('gcStatus');
      if (statusEl) statusEl.textContent = 'Memory Compaction Complete: Free holes merged into contiguous memory block!';
    },

    draw() {
      if (!this.ctx) return;
      const ctx = this.ctx;
      const w = this.canvas.width;
      const h = this.canvas.height;
      ctx.clearRect(0, 0, w, h);

      // Draw references (arrows)
      this.objects.forEach(obj => {
        obj.refs.forEach(targetId => {
          const target = this.objects.find(o => o.id === targetId);
          if (target) {
            ctx.strokeStyle = 'rgba(255, 255, 255, 0.35)';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.moveTo(obj.x, obj.y);
            ctx.lineTo(target.x, target.y);
            ctx.stroke();

            // Arrow
            const angle = Math.atan2(target.y - obj.y, target.x - obj.x);
            const headLen = 8;
            ctx.fillStyle = 'rgba(255, 255, 255, 0.6)';
            ctx.beginPath();
            ctx.moveTo(target.x, target.y);
            ctx.lineTo(target.x - headLen * Math.cos(angle - Math.PI / 6), target.y - headLen * Math.sin(angle - Math.PI / 6));
            ctx.lineTo(target.x - headLen * Math.cos(angle + Math.PI / 6), target.y - headLen * Math.sin(angle + Math.PI / 6));
            ctx.fill();
          }
        });
      });

      // Draw object circles
      this.objects.forEach(obj => {
        ctx.fillStyle = obj.color === 'black' ? '#10b981' : (obj.color === 'white' ? '#ef4444' : '#f59e0b');
        ctx.beginPath();
        ctx.arc(obj.x, obj.y, 24, 0, Math.PI * 2);
        ctx.fill();

        ctx.strokeStyle = '#fff';
        ctx.lineWidth = obj.isRoot ? 3 : 1;
        ctx.stroke();

        ctx.fillStyle = '#fff';
        ctx.font = 'bold 10px system-ui, sans-serif';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(obj.label, obj.x, obj.y + 36);
      });
    }
  };

  // ----------------------------------------------------------------------------
  // 4. CPU Cache Line & False Sharing Simulator (MESI Protocol)
  // ----------------------------------------------------------------------------
  const CpuCacheSimulator = {
    padded: false,
    core0Writes: 0,
    core1Writes: 0,
    busInvalidations: 0,

    init() {
      this.render();
    },

    open() {
      const modal = document.getElementById('cpuModal');
      if (modal) {
        modal.classList.add('active');
        this.init();
      }
    },

    close() {
      const modal = document.getElementById('cpuModal');
      if (modal) modal.classList.remove('active');
    },

    togglePadding() {
      this.padded = !this.padded;
      this.core0Writes = 0;
      this.core1Writes = 0;
      this.busInvalidations = 0;
      this.render();
    },

    writeCore0() {
      this.core0Writes++;
      if (!this.padded) {
        this.busInvalidations++;
      }
      this.render();
    },

    writeCore1() {
      this.core1Writes++;
      if (!this.padded) {
        this.busInvalidations++;
      }
      this.render();
    },

    render() {
      const modeTag = document.getElementById('cpuPaddingMode');
      const core0State = document.getElementById('cpuCore0State');
      const core1State = document.getElementById('cpuCore1State');
      const busStats = document.getElementById('cpuBusStats');

      if (modeTag) {
        modeTag.textContent = this.padded ? 'Aligned with 64B Padding (NO False Sharing)' : 'False Sharing Vulnerable (Same 64B Line)';
        modeTag.style.color = this.padded ? '#34d399' : '#fb7185';
      }

      if (core0State) {
        core0State.innerHTML = `
          <div style="font-size:12px;color:#94a3b8;">Writes: <b>${this.core0Writes}</b></div>
          <div style="font-size:14px;font-weight:700;color:#38bdf8;">Variable A [Offset 0]</div>
          <div style="margin-top:6px;font-size:11px;padding:3px 8px;border-radius:4px;background:rgba(56, 189, 248, 0.2);display:inline-block;">MESI: Modified (M)</div>
        `;
      }

      if (core1State) {
        const stateStr = this.padded ? 'Modified (M) - Isolated Line' : (this.core0Writes > this.core1Writes ? 'Invalid (I) - Bus Invalidation' : 'Modified (M)');
        core1State.innerHTML = `
          <div style="font-size:12px;color:#94a3b8;">Writes: <b>${this.core1Writes}</b></div>
          <div style="font-size:14px;font-weight:700;color:#f43f5e;">Variable B [Offset ${this.padded ? '64' : '4'}]</div>
          <div style="margin-top:6px;font-size:11px;padding:3px 8px;border-radius:4px;background:rgba(244, 63, 94, 0.2);display:inline-block;">MESI: ${stateStr}</div>
        `;
      }

      if (busStats) {
        busStats.innerHTML = `
          <div style="display:flex;justify-content:space-around;padding:12px;background:rgba(2, 6, 23, 0.8);border-radius:8px;border:1px solid rgba(255,255,255,0.08);">
            <div><span style="color:#94a3b8;">Bus Invalidation Traffic:</span> <b style="color:${this.busInvalidations > 5 ? '#f43f5e' : '#34d399'}">${this.busInvalidations} cache line snoops</b></div>
            <div><span style="color:#94a3b8;">Memory Bus Latency Overhead:</span> <b>${this.padded ? '0.2 ns (L1 Cache Hit)' : (this.busInvalidations * 42) + ' ns (Inter-core MESI stall)'}</b></div>
          </div>
        `;
      }
    }
  };

  // ----------------------------------------------------------------------------
  // 5. SQL Execution Plan Visualizer (EXPLAIN ANALYZE)
  // ----------------------------------------------------------------------------
  const SqlExplainVisualizer = {
    plans: {
      unindexed: {
        title: 'Unindexed Table (Sequential Scan + In-Memory Sort)',
        cost: '1420.50',
        time: '32.4 ms',
        tree: [
          { node: 'Sort (cost=1420.50 rows=15000)', type: 'sort', time: '14.2 ms' },
          { node: '  -> HashAggregate (cost=850.00 rows=15000)', type: 'agg', time: '8.1 ms' },
          { node: '       -> Seq Scan on orders (cost=0.00..510.00 rows=100000)', type: 'scan-red', time: '10.1 ms' }
        ]
      },
      indexed: {
        title: 'B-Tree Index Scan + Index-Only Join',
        cost: '12.80',
        time: '0.42 ms',
        tree: [
          { node: 'Index Only Scan using idx_orders_user_date (cost=0.42..12.80 rows=40)', type: 'scan-green', time: '0.21 ms' },
          { node: '  -> Nested Loop (cost=0.28..8.40 rows=40)', type: 'join', time: '0.12 ms' },
          { node: '       -> Index Scan on users_pkey (cost=0.14..2.30 rows=1)', type: 'scan-green', time: '0.09 ms' }
        ]
      }
    },

    open() {
      const modal = document.getElementById('sqlExplainModal');
      if (modal) {
        modal.classList.add('active');
        this.render('unindexed');
      }
    },

    close() {
      const modal = document.getElementById('sqlExplainModal');
      if (modal) modal.classList.remove('active');
    },

    render(presetKey) {
      const plan = this.plans[presetKey] || this.plans.unindexed;
      const titleEl = document.getElementById('sqlExplainTitle');
      const treeEl = document.getElementById('sqlExplainTree');

      if (titleEl) {
        titleEl.innerHTML = `<b>${plan.title}</b> — Est. Cost: <span style="color:#f59e0b;">${plan.cost}</span> | Total Execution Time: <span style="color:#10b981;">${plan.time}</span>`;
      }

      if (treeEl) {
        treeEl.innerHTML = plan.tree.map(item => {
          let badgeColor = '#6366f1';
          if (item.type === 'scan-red') badgeColor = '#ef4444';
          if (item.type === 'scan-green') badgeColor = '#10b981';

          return `
            <div style="padding:10px 14px;margin-bottom:8px;background:rgba(15,23,42,0.8);border-left:4px solid ${badgeColor};border-radius:6px;display:flex;justify-content:space-between;align-items:center;">
              <span style="font-family:monospace;font-size:13px;color:#f8fafc;">${item.node}</span>
              <span style="font-size:12px;color:#94a3b8;background:rgba(255,255,255,0.06);padding:3px 8px;border-radius:4px;">⏱️ ${item.time}</span>
            </div>
          `;
        }).join('');
      }
    }
  };

  // ----------------------------------------------------------------------------
  // 6. Regex DFA/NFA Automaton Visualizer
  // ----------------------------------------------------------------------------
  const RegexAutomatonVisualizer = {
    canvas: null,
    ctx: null,
    states: [
      { id: 0, label: 'q0 (Start)', x: 100, y: 140, isAccept: false },
      { id: 1, label: 'q1', x: 260, y: 140, isAccept: false },
      { id: 2, label: 'q2', x: 420, y: 140, isAccept: false },
      { id: 3, label: 'q3 (Accept)', x: 580, y: 140, isAccept: true }
    ],
    currentState: 0,

    init() {
      this.canvas = document.getElementById('regexCanvas');
      if (!this.canvas) return;
      this.ctx = this.canvas.getContext('2d');
      this.draw();
    },

    open() {
      const modal = document.getElementById('regexModal');
      if (modal) {
        modal.classList.add('active');
        this.init();
      }
    },

    close() {
      const modal = document.getElementById('regexModal');
      if (modal) modal.classList.remove('active');
    },

    testInput() {
      const input = document.getElementById('regexTestInput');
      if (!input) return;
      const str = input.value;
      // Simulating regex (a|b)*abb
      let s = 0;
      for (const char of str) {
        if (s === 0) s = (char === 'a' ? 1 : 0);
        else if (s === 1) s = (char === 'b' ? 2 : 1);
        else if (s === 2) s = (char === 'b' ? 3 : 1);
        else if (s === 3) s = (char === 'a' ? 1 : 0);
      }
      this.currentState = s;
      this.draw();

      const resultEl = document.getElementById('regexMatchResult');
      if (resultEl) {
        const isMatch = (s === 3);
        resultEl.textContent = isMatch ? '✅ MATCH ACCEPTED by DFA!' : '❌ REJECTED (Terminated in non-accept state)';
        resultEl.style.color = isMatch ? '#10b981' : '#f43f5e';
      }
    },

    draw() {
      if (!this.ctx) return;
      const ctx = this.ctx;
      const w = this.canvas.width;
      const h = this.canvas.height;
      ctx.clearRect(0, 0, w, h);

      // Transitions
      for (let i = 0; i < this.states.length - 1; i++) {
        const from = this.states[i];
        const to = this.states[i + 1];
        ctx.strokeStyle = '#6366f1';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(from.x + 22, from.y);
        ctx.lineTo(to.x - 22, to.y);
        ctx.stroke();

        ctx.fillStyle = '#f8fafc';
        ctx.font = '11px monospace';
        ctx.textAlign = 'center';
        ctx.fillText(i === 0 ? 'a' : 'b', (from.x + to.x) / 2, from.y - 10);
      }

      // State circles
      this.states.forEach(st => {
        ctx.fillStyle = (this.currentState === st.id) ? '#38bdf8' : 'rgba(15, 23, 42, 0.9)';
        ctx.beginPath();
        ctx.arc(st.x, st.y, 22, 0, Math.PI * 2);
        ctx.fill();

        ctx.strokeStyle = st.isAccept ? '#10b981' : '#a5b4fc';
        ctx.lineWidth = st.isAccept ? 3 : 1.5;
        ctx.stroke();

        if (st.isAccept) {
          ctx.beginPath();
          ctx.arc(st.x, st.y, 18, 0, Math.PI * 2);
          ctx.stroke();
        }

        ctx.fillStyle = (this.currentState === st.id) ? '#020617' : '#f8fafc';
        ctx.font = 'bold 11px system-ui, sans-serif';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(st.label, st.x, st.y);
      });
    }
  };

  // ----------------------------------------------------------------------------
  // 7. Deadlock Visualizer (Resource Allocation Graph & Cycle Detection)
  // ----------------------------------------------------------------------------
  const DeadlockVisualizer = {
    canvas: null,
    ctx: null,
    isDeadlocked: true,

    init() {
      this.canvas = document.getElementById('deadlockCanvas');
      if (!this.canvas) return;
      this.ctx = this.canvas.getContext('2d');
      this.draw();
    },

    open() {
      const modal = document.getElementById('deadlockModal');
      if (modal) {
        modal.classList.add('active');
        this.init();
      }
    },

    close() {
      const modal = document.getElementById('deadlockModal');
      if (modal) modal.classList.remove('active');
    },

    toggleLockOrder() {
      this.isDeadlocked = !this.isDeadlocked;
      this.draw();
    },

    draw() {
      if (!this.ctx) return;
      const ctx = this.ctx;
      const w = this.canvas.width;
      const h = this.canvas.height;
      ctx.clearRect(0, 0, w, h);

      const p1 = { x: 180, y: 80, label: 'Thread P1' };
      const p2 = { x: 420, y: 220, label: 'Thread P2' };
      const r1 = { x: 420, y: 80, label: 'Mutex Lock 1' };
      const r2 = { x: 180, y: 220, label: 'Mutex Lock 2' };

      // Edges
      // P1 holds R2, requests R1
      // P2 holds R1, requests R2 (if deadlocked)
      ctx.lineWidth = 2;
      const drawArrow = (from, to, color) => {
        ctx.strokeStyle = color;
        ctx.beginPath();
        ctx.moveTo(from.x, from.y);
        ctx.lineTo(to.x, to.y);
        ctx.stroke();

        const angle = Math.atan2(to.y - from.y, to.x - from.x);
        const headLen = 10;
        ctx.fillStyle = color;
        ctx.beginPath();
        ctx.moveTo(to.x, to.y);
        ctx.lineTo(to.x - headLen * Math.cos(angle - Math.PI / 6), to.y - headLen * Math.sin(angle - Math.PI / 6));
        ctx.lineTo(to.x - headLen * Math.cos(angle + Math.PI / 6), to.y - headLen * Math.sin(angle + Math.PI / 6));
        ctx.fill();
      };

      const edgeColor = this.isDeadlocked ? '#f43f5e' : '#10b981';
      drawArrow(r2, p1, edgeColor); // R2 allocated to P1
      drawArrow(p1, r1, edgeColor); // P1 requests R1
      drawArrow(r1, p2, edgeColor); // R1 allocated to P2

      if (this.isDeadlocked) {
        drawArrow(p2, r2, '#f43f5e'); // Circular wait!
      } else {
        // P2 acquires R1 then R2 in strict ascending order
        drawArrow(p2, r1, '#10b981');
      }

      // Draw Nodes
      const drawNode = (node, isResource) => {
        ctx.fillStyle = isResource ? '#334155' : '#1e1b4b';
        ctx.strokeStyle = '#a5b4fc';
        ctx.lineWidth = 1.5;
        if (isResource) {
          ctx.fillRect(node.x - 36, node.y - 20, 72, 40);
          ctx.strokeRect(node.x - 36, node.y - 20, 72, 40);
        } else {
          ctx.beginPath();
          ctx.arc(node.x, node.y, 26, 0, Math.PI * 2);
          ctx.fill();
          ctx.stroke();
        }

        ctx.fillStyle = '#fff';
        ctx.font = 'bold 11px system-ui, sans-serif';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(node.label, node.x, node.y);
      };

      drawNode(p1, false);
      drawNode(p2, false);
      drawNode(r1, true);
      drawNode(r2, true);

      const statusEl = document.getElementById('deadlockStatus');
      if (statusEl) {
        if (this.isDeadlocked) {
          statusEl.textContent = '🚨 DEADLOCK DETECTED! Cycle: P1 -> R1 -> P2 -> R2 -> P1 (Tarjan Cycle Detection: true)';
          statusEl.style.color = '#f43f5e';
        } else {
          statusEl.textContent = '✅ Deadlock Prevented via Strict Hierarchical Lock Ordering (R1 before R2). Cycle: 0';
          statusEl.style.color = '#10b981';
        }
      }
    }
  };

  // ----------------------------------------------------------------------------
  // 8. Epoll vs Select I/O Multiplexing Simulator
  // ----------------------------------------------------------------------------
  const EpollSelectSimulator = {
    open() {
      const modal = document.getElementById('epollModal');
      if (modal) {
        modal.classList.add('active');
        this.runComparison();
      }
    },

    close() {
      const modal = document.getElementById('epollModal');
      if (modal) modal.classList.remove('active');
    },

    runComparison() {
      const container = document.getElementById('epollResults');
      if (!container) return;

      container.innerHTML = `
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;">
          <div style="background:rgba(244,63,94,0.1);border:1px solid rgba(244,63,94,0.3);border-radius:10px;padding:16px;">
            <h4 style="color:#fb7185;margin-top:0;">select() / poll() [O(N)]</h4>
            <div style="font-size:12px;color:#cbd5e1;line-height:1.5;">
              <div>• File Descriptors Monitored: <b>10,000 FDs</b></div>
              <div>• Active Ready Sockets: <b>3 FDs</b></div>
              <div>• Kernel Copy: <b>Linear bitmask copy on every invocation</b></div>
              <div>• Traversal Complexity: <b>O(N) full scan of 10,000 slots</b></div>
              <div style="margin-top:10px;font-size:14px;color:#fb7185;font-weight:700;">⏱️ Scan Overhead: ~2,400 μs</div>
            </div>
          </div>
          <div style="background:rgba(16,185,129,0.1);border:1px solid rgba(16,185,129,0.3);border-radius:10px;padding:16px;">
            <h4 style="color:#34d399;margin-top:0;">Linux epoll() [O(1)]</h4>
            <div style="font-size:12px;color:#cbd5e1;line-height:1.5;">
              <div>• File Descriptors Monitored: <b>10,000 FDs</b></div>
              <div>• Active Ready Sockets: <b>3 FDs</b></div>
              <div>• Kernel Storage: <b>Red-Black tree (epitem) persistent</b></div>
              <div>• Ready Notification: <b>O(1) Kernel callback appends to ready list</b></div>
              <div style="margin-top:10px;font-size:14px;color:#34d399;font-weight:700;">⏱️ Epoll Return Time: ~4 μs (600x Faster!)</div>
            </div>
          </div>
        </div>
      `;
    }
  };

  // ----------------------------------------------------------------------------
  // 9. Binary Buddy Memory Allocator Simulator
  // ----------------------------------------------------------------------------
  const BuddyAllocatorSimulator = {
    blocks: [{ size: 1024, allocated: false, label: 'Free' }],

    open() {
      const modal = document.getElementById('buddyModal');
      if (modal) {
        modal.classList.add('active');
        this.render();
      }
    },

    close() {
      const modal = document.getElementById('buddyModal');
      if (modal) modal.classList.remove('active');
    },

    allocate(requestedSize) {
      // Find power of 2 >= requestedSize
      let targetSize = 64;
      while (targetSize < requestedSize) targetSize *= 2;

      // Find best-fit free block and split if needed
      for (let i = 0; i < this.blocks.length; i++) {
        if (!this.blocks[i].allocated && this.blocks[i].size >= targetSize) {
          while (this.blocks[i].size > targetSize) {
            const half = this.blocks[i].size / 2;
            this.blocks.splice(i, 1,
              { size: half, allocated: false, label: 'Free' },
              { size: half, allocated: false, label: 'Free' }
            );
          }
          this.blocks[i].allocated = true;
          this.blocks[i].label = `Alloc (${requestedSize}KB in ${targetSize}KB)`;
          break;
        }
      }
      this.render();
    },

    freeAll() {
      this.blocks = [{ size: 1024, allocated: false, label: 'Free' }];
      this.render();
    },

    render() {
      const container = document.getElementById('buddyBlocksContainer');
      if (!container) return;

      container.innerHTML = this.blocks.map(b => {
        const widthPct = (b.size / 1024) * 100;
        const color = b.allocated ? '#6366f1' : 'rgba(255, 255, 255, 0.08)';
        const border = b.allocated ? '#818cf8' : 'rgba(255, 255, 255, 0.15)';
        return `
          <div style="width:${widthPct}%;background:${color};border:1px solid ${border};border-radius:6px;padding:12px 6px;text-align:center;box-sizing:border-box;">
            <div style="font-weight:700;font-size:11px;color:#fff;">${b.size} KB</div>
            <div style="font-size:10px;color:#cbd5e1;">${b.label}</div>
          </div>
        `;
      }).join('');
    }
  };

  // ----------------------------------------------------------------------------
  // 10. System Trade-off Sliders (CAP Theorem & SLA Impact)
  // ----------------------------------------------------------------------------
  const SystemTradeoffSliders = {
    open() {
      const modal = document.getElementById('tradeoffModal');
      if (modal) {
        modal.classList.add('active');
        this.updateCalculations();
      }
    },

    close() {
      const modal = document.getElementById('tradeoffModal');
      if (modal) modal.classList.remove('active');
    },

    updateCalculations() {
      const repl = parseInt(document.getElementById('sliderRepl')?.value || 3, 10);
      const writeRatio = parseInt(document.getElementById('sliderWriteRatio')?.value || 50, 10);
      const jitter = parseInt(document.getElementById('sliderJitter')?.value || 10, 10);

      const rVal = Math.floor(repl / 2) + 1;
      const wVal = Math.floor(repl / 2) + 1;
      const p99 = Math.round((jitter * 2.4) + (writeRatio * 0.8) + (repl * 3.2));

      const labelEl = document.getElementById('tradeoffOutput');
      if (labelEl) {
        labelEl.innerHTML = `
          <div style="display:grid;grid-template-columns:repeat(3, 1fr);gap:12px;margin-top:16px;">
            <div style="background:rgba(15,23,42,0.8);border:1px solid rgba(255,255,255,0.08);padding:14px;border-radius:10px;text-align:center;">
              <div style="color:#94a3b8;font-size:12px;">Quorum Equation</div>
              <div style="font-size:18px;font-weight:800;color:#38bdf8;margin-top:4px;">R (${rVal}) + W (${wVal}) > N (${repl})</div>
              <div style="font-size:11px;color:#34d399;margin-top:4px;">Strict Strong Consistency (CP)</div>
            </div>
            <div style="background:rgba(15,23,42,0.8);border:1px solid rgba(255,255,255,0.08);padding:14px;border-radius:10px;text-align:center;">
              <div style="color:#94a3b8;font-size:12px;">Predicted P99 Latency</div>
              <div style="font-size:18px;font-weight:800;color:#f59e0b;margin-top:4px;">${p99} ms</div>
              <div style="font-size:11px;color:#94a3b8;margin-top:4px;">SLA Budget: 200 ms</div>
            </div>
            <div style="background:rgba(15,23,42,0.8);border:1px solid rgba(255,255,255,0.08);padding:14px;border-radius:10px;text-align:center;">
              <div style="color:#94a3b8;font-size:12px;">Recommended Arch</div>
              <div style="font-size:18px;font-weight:800;color:#a855f7;margin-top:4px;">${writeRatio > 70 ? 'Cassandra / LSM' : 'PostgreSQL + Read Replicas'}</div>
              <div style="font-size:11px;color:#cbd5e1;margin-top:4px;">Optimized for I/O Profile</div>
            </div>
          </div>
        `;
      }
    }
  };

  // ----------------------------------------------------------------------------
  // 11. Chaos Monkey Simulator (Failure Injection for System Architecture)
  // ----------------------------------------------------------------------------
  const ChaosMonkeySimulator = {
    injectFailure(type) {
      const banner = document.getElementById('chaosBanner');
      if (!banner) return;
      banner.style.display = 'block';

      switch (type) {
        case 'partition':
          banner.innerHTML = '🐒 <b>Chaos Monkey Partition</b>: US-East and US-West network cut! Split-brain protection active. Raft quorum surviving.';
          banner.style.color = '#fbbf24';
          break;
        case 'crash':
          banner.innerHTML = '🐒 <b>Chaos Monkey Kill</b>: Redis Primary crashed! Sentinel promoting Replica to Primary in 800ms...';
          banner.style.color = '#f87171';
          break;
        case 'latency':
          banner.innerHTML = '🐒 <b>Chaos Monkey Latency</b>: +500ms network jitter injected on database connection pool. Circuit breaker tripped!';
          banner.style.color = '#c084fc';
          break;
      }

      setTimeout(() => {
        banner.innerHTML = '✅ Chaos test recovered: All cluster health checks returning 200 OK.';
        banner.style.color = '#34d399';
        setTimeout(() => { banner.style.display = 'none'; }, 2500);
      }, 3000);
    }
  };

  // ----------------------------------------------------------------------------
  // 12. Linux Virtual Memory Page Table Walker Simulator (x86-64 4-Level)
  // ----------------------------------------------------------------------------
  const PageTableWalkerSimulator = {
    canvas: null,
    ctx: null,
    step: 0,
    tlbHit: false,
    levels: [
      { name: 'CR3 Register', addr: '0x0000_1000_A000', offset: 'Base Pointer', hit: true },
      { name: 'PML4 Table', addr: '0xFFFF_8880_0001', offset: 'Bits [47:39]', hit: true },
      { name: 'PDPT (Directory Ptr)', addr: '0xFFFF_8880_0002', offset: 'Bits [38:30]', hit: true },
      { name: 'PD (Page Directory)', addr: '0xFFFF_8880_0003', offset: 'Bits [29:21]', hit: true },
      { name: 'PT (Page Table)', addr: '0xFFFF_8880_0004', offset: 'Bits [20:12]', hit: true },
      { name: 'Physical Page Frame', addr: '0x0000_7F80_4000', offset: 'Bits [11:0] (4KB Offset)', hit: true }
    ],

    open() {
      const modal = document.getElementById('pageTableModal');
      if (modal) {
        modal.classList.add('active');
        this.canvas = document.getElementById('pageTableCanvas');
        if (this.canvas) this.ctx = this.canvas.getContext('2d');
        this.step = 0;
        this.draw();
      }
    },

    close() {
      const modal = document.getElementById('pageTableModal');
      if (modal) modal.classList.remove('active');
    },

    nextStep() {
      if (this.step < this.levels.length - 1) {
        this.step++;
        this.draw();
      }
    },

    toggleTlb() {
      this.tlbHit = !this.tlbHit;
      this.step = this.tlbHit ? this.levels.length - 1 : 0;
      this.draw();
    },

    draw() {
      if (!this.ctx || !this.canvas) return;
      const ctx = this.ctx;
      const w = this.canvas.width;
      const h = this.canvas.height;
      ctx.clearRect(0, 0, w, h);

      const statusEl = document.getElementById('pageTableStatus');
      if (this.tlbHit) {
        if (statusEl) {
          statusEl.innerHTML = '<span style="color:#10b981;font-weight:700;">⚡ TLB CACHE HIT! Virtual Address translated in 0.5 ns without memory bus traversal.</span>';
        }
        ctx.fillStyle = '#10b981';
        ctx.font = 'bold 16px monospace';
        ctx.textAlign = 'center';
        ctx.fillText('⚡ L1 Data TLB Cache Hit: 0x7F804000 (0.5 ns)', w / 2, h / 2);
        return;
      }

      const total = this.levels.length;
      const boxW = 105;
      const boxH = 50;
      const spacing = (w - 40 - (boxW * total)) / (total - 1);

      this.levels.forEach((lvl, idx) => {
        const x = 20 + idx * (boxW + spacing);
        const y = h / 2 - boxH / 2;
        const isActive = idx <= this.step;
        const isCurrent = idx === this.step;

        ctx.fillStyle = isCurrent ? 'rgba(99, 102, 241, 0.4)' : (isActive ? 'rgba(15, 23, 42, 0.9)' : 'rgba(15, 23, 42, 0.3)');
        ctx.strokeStyle = isCurrent ? '#38bdf8' : (isActive ? '#6366f1' : 'rgba(255, 255, 255, 0.1)');
        ctx.lineWidth = isCurrent ? 2.5 : 1;
        ctx.beginPath();
        ctx.roundRect(x, y, boxW, boxH, 6);
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = isActive ? '#fff' : '#64748b';
        ctx.font = 'bold 10px system-ui, sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(lvl.name, x + boxW / 2, y + 18);

        ctx.fillStyle = isActive ? '#a5b4fc' : '#475569';
        ctx.font = '9px monospace';
        ctx.fillText(lvl.offset, x + boxW / 2, y + 36);

        if (idx < total - 1) {
          ctx.strokeStyle = (idx < this.step) ? '#38bdf8' : 'rgba(255, 255, 255, 0.15)';
          ctx.lineWidth = 1.5;
          ctx.beginPath();
          ctx.moveTo(x + boxW, y + boxH / 2);
          ctx.lineTo(x + boxW + spacing, y + boxH / 2);
          ctx.stroke();
        }
      });

      if (statusEl) {
        statusEl.innerHTML = `<span>Step ${this.step + 1}/${total}: Accessing <b>${this.levels[this.step].name}</b> (${this.levels[this.step].offset}) — Est Memory Latency: ~${(this.step + 1) * 12} ns</span>`;
      }
    }
  };

  // ----------------------------------------------------------------------------
  // 13. eBPF Bytecode Verifier & CFG Simulator
  // ----------------------------------------------------------------------------
  const EbpfVerifierSimulator = {
    instructions: [
      { op: 'r1 = *(u32 *)(r1 + 0)', label: 'Load sk_buff pointer', safe: true },
      { op: 'r2 = *(u32 *)(r1 + 4)', label: 'Load packet end pointer', safe: true },
      { op: 'if r1 + 14 > r2 goto +3', label: 'Bounds check Ethernet header', safe: true },
      { op: 'r0 = *(u8 *)(r1 + 12)', label: 'Dereference packet payload', safe: true },
      { op: 'exit', label: 'Return XDP_PASS (Safe Termination)', safe: true }
    ],

    open() {
      const modal = document.getElementById('ebpfModal');
      if (modal) {
        modal.classList.add('active');
        this.verify();
      }
    },

    close() {
      const modal = document.getElementById('ebpfModal');
      if (modal) modal.classList.remove('active');
    },

    verify() {
      const logEl = document.getElementById('ebpfLog');
      if (!logEl) return;

      logEl.innerHTML = this.instructions.map((ins, idx) => `
        <div style="padding:8px 12px;background:rgba(15,23,42,0.8);border-left:4px solid #10b981;border-radius:6px;margin-bottom:6px;font-family:monospace;font-size:12px;">
          <span style="color:#94a3b8;">${idx}:</span> <b style="color:#38bdf8;">${ins.op}</b> <span style="color:#cbd5e1;margin-left:10px;">// ${ins.label}</span>
          <span style="float:right;color:#10b981;font-weight:700;">VERIFIED_SAFE</span>
        </div>
      `).join('') + `
        <div style="margin-top:12px;padding:10px;background:rgba(16,185,129,0.15);border:1px solid #10b981;border-radius:8px;color:#34d399;font-weight:700;font-size:13px;text-align:center;">
          ✅ BPF Verifier: 0 memory access violations, 0 unbounded loops. Program approved for kernel execution.
        </div>
      `;
    }
  };

  // ----------------------------------------------------------------------------
  // 14. Zero-Copy Network Pipeline (`sendfile` vs `splice` vs DPDK)
  // ----------------------------------------------------------------------------
  const ZeroCopyPipelineSimulator = {
    open() {
      const modal = document.getElementById('zeroCopyModal');
      if (modal) {
        modal.classList.add('active');
        this.render();
      }
    },

    close() {
      const modal = document.getElementById('zeroCopyModal');
      if (modal) modal.classList.remove('active');
    },

    render() {
      const container = document.getElementById('zeroCopyContainer');
      if (!container) return;

      container.innerHTML = `
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
          <div style="background:rgba(244,63,94,0.1);border:1px solid rgba(244,63,94,0.3);border-radius:10px;padding:16px;">
            <h4 style="margin:0 0 10px 0;color:#fb7185;">Traditional read() / write() (4 Context Switches)</h4>
            <div style="font-size:12px;color:#cbd5e1;line-height:1.6;">
              <div>1. Disk $\\to$ OS Page Cache (DMA Copy)</div>
              <div>2. Page Cache $\\to$ User Space Buffer (CPU Copy + Syscall)</div>
              <div>3. User Space $\\to$ Socket Buffer (CPU Copy + Syscall)</div>
              <div>4. Socket Buffer $\\to$ NIC Protocol Buffer (DMA Copy)</div>
              <div style="margin-top:10px;font-weight:700;color:#fb7185;">Overhead: 4 Copies, 4 Context Switches</div>
            </div>
          </div>
          <div style="background:rgba(16,185,129,0.1);border:1px solid rgba(16,185,129,0.3);border-radius:10px;padding:16px;">
            <h4 style="margin:0 0 10px 0;color:#34d399;">Linux sendfile() / DPDK Zero-Copy</h4>
            <div style="font-size:12px;color:#cbd5e1;line-height:1.6;">
              <div>1. Disk $\\to$ OS Page Cache (DMA Copy)</div>
              <div>2. DMA Gather Copy direct to NIC Buffer (Scatter-Gather)</div>
              <div>3. Zero user-space transitions</div>
              <div>4. Zero CPU copy operations</div>
              <div style="margin-top:10px;font-weight:700;color:#34d399;">Overhead: 0 CPU Copies, 2 Context Switches (10x Throughput)</div>
            </div>
          </div>
        </div>
      `;
    }
  };

  // ----------------------------------------------------------------------------
  // 15. Spectre / Meltdown Speculative Execution Simulator
  // ----------------------------------------------------------------------------
  const SpectreMeltdownSimulator = {
    open() {
      const modal = document.getElementById('spectreModal');
      if (modal) {
        modal.classList.add('active');
        this.runAttack();
      }
    },

    close() {
      const modal = document.getElementById('spectreModal');
      if (modal) modal.classList.remove('active');
    },

    runAttack() {
      const output = document.getElementById('spectreOutput');
      if (!output) return;

      output.innerHTML = `
        <div style="font-family:monospace;font-size:12px;line-height:1.5;background:#020617;padding:14px;border-radius:8px;border:1px solid rgba(255,255,255,0.1);">
          <div style="color:#94a3b8;">// 1. Train branch predictor with valid index < array1_size</div>
          <div style="color:#cbd5e1;">for i in 0..30 { victim_function(valid_idx); }</div>
          <div style="color:#94a3b8;margin-top:8px;">// 2. Speculative out-of-bounds execution with malicious offset</div>
          <div style="color:#fb7185;">victim_function(kernel_secret_offset); // CPU transiently loads secret byte into L1 cache before rollback</div>
          <div style="color:#94a3b8;margin-top:8px;">// 3. Measure probe array access times via RDTSCP</div>
          <div style="color:#38bdf8;">probe_array[secret_byte * 4096] access time: <b style="color:#10b981;">28 CPU cycles (L1 CACHE HIT!)</b></div>
          <div style="color:#94a3b8;">probe_array[other_bytes * 4096] access time: 240 CPU cycles (RAM Latency)</div>
          <div style="margin-top:12px;color:#f59e0b;font-weight:700;">Leaked Secret Character: 'K' (ASCII 75) via Cache Timing Side-Channel.</div>
        </div>
      `;
    }
  };

  // ----------------------------------------------------------------------------
  // 16. SIMD Vectorization Visualizer (AVX-512 vs Scalar)
  // ----------------------------------------------------------------------------
  const SimdVectorSimulator = {
    open() {
      const modal = document.getElementById('simdModal');
      if (modal) {
        modal.classList.add('active');
        this.render();
      }
    },

    close() {
      const modal = document.getElementById('simdModal');
      if (modal) modal.classList.remove('active');
    },

    render() {
      const container = document.getElementById('simdContainer');
      if (!container) return;

      container.innerHTML = `
        <div style="background:rgba(15,23,42,0.8);border:1px solid rgba(255,255,255,0.08);border-radius:12px;padding:16px;">
          <h4 style="margin:0 0 12px 0;color:#38bdf8;">AVX-512 512-Bit Register Lane Parallelism (8x float64)</h4>
          <div style="display:grid;grid-template-columns:repeat(8, 1fr);gap:6px;margin-bottom:14px;">
            ${[0, 1, 2, 3, 4, 5, 6, 7].map(lane => `
              <div style="background:rgba(99,102,241,0.2);border:1px solid #6366f1;border-radius:6px;padding:10px 4px;text-align:center;">
                <div style="font-size:10px;color:#a5b4fc;">Lane ${lane}</div>
                <div style="font-size:12px;font-weight:800;color:#fff;">FMA()</div>
              </div>
            `).join('')}
          </div>
          <div style="font-size:12px;color:#cbd5e1;line-height:1.5;">
            Single CPU Cycle computes 8 fused multiply-accumulates simultaneously. Scalar throughput: 1 op/cycle $\\to$ SIMD throughput: 8 ops/cycle (800% vector speedup).
          </div>
        </div>
      `;
    }
  };

  // ----------------------------------------------------------------------------
  // 17. Thread Pool Work-Stealing Simulator (Tokio / Go Scheduler)
  // ----------------------------------------------------------------------------
  const WorkStealingSimulator = {
    workers: [
      { id: 0, queue: ['Task 1', 'Task 2', 'Task 3', 'Task 4'] },
      { id: 1, queue: ['Task 5'] },
      { id: 2, queue: [] }, // Idle, will steal
      { id: 3, queue: ['Task 6', 'Task 7'] }
    ],

    open() {
      const modal = document.getElementById('workStealingModal');
      if (modal) {
        modal.classList.add('active');
        this.render();
      }
    },

    close() {
      const modal = document.getElementById('workStealingModal');
      if (modal) modal.classList.remove('active');
    },

    steal() {
      // Worker 2 steals from Worker 0
      if (this.workers[0].queue.length > 1) {
        const stolen = this.workers[0].queue.pop();
        this.workers[2].queue.push(stolen);
      }
      this.render();
      const statusEl = document.getElementById('workStealingStatus');
      if (statusEl) {
        statusEl.innerHTML = '<span style="color:#10b981;font-weight:700;">Worker 2 was idle! Successfully stole task from Worker 0 deque using lock-free CAS.</span>';
      }
    },

    render() {
      const container = document.getElementById('workStealingGrid');
      if (!container) return;

      container.innerHTML = this.workers.map(w => `
        <div style="background:rgba(15,23,42,0.8);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:14px;">
          <h4 style="margin:0 0 10px 0;color:${w.queue.length === 0 ? '#fb7185' : '#38bdf8'};">Worker Thread ${w.id} ${w.queue.length === 0 ? '(Idle)' : ''}</h4>
          <div style="min-height:70px;">
            ${w.queue.map(t => `<div style="padding:4px 8px;margin-bottom:4px;border-radius:4px;background:rgba(99,102,241,0.25);border:1px solid #6366f1;font-size:11px;color:#fff;">${t}</div>`).join('') || '<div style="font-size:11px;color:#64748b;">Deque empty</div>'}
          </div>
        </div>
      `).join('');
    }
  };

  // ----------------------------------------------------------------------------
  // 18. Database Isolation Level Anomaly Simulator
  // ----------------------------------------------------------------------------
  const DatabaseIsolationSimulator = {
    levels: {
      read_committed: {
        name: 'Read Committed (Postgres Default)',
        dirty_read: 'Prevented',
        non_repeatable_read: 'Possible ⚠️',
        phantom_read: 'Possible ⚠️',
        write_skew: 'Possible ⚠️'
      },
      repeatable_read: {
        name: 'Repeatable Read (Snapshot Isolation)',
        dirty_read: 'Prevented',
        non_repeatable_read: 'Prevented ✅',
        phantom_read: 'Prevented (Postgres snapshot) ✅',
        write_skew: 'Possible ⚠️'
      },
      serializable: {
        name: 'Serializable (SSI - Strict Serializability)',
        dirty_read: 'Prevented ✅',
        non_repeatable_read: 'Prevented ✅',
        phantom_read: 'Prevented ✅',
        write_skew: 'Prevented (Abort on Dependency Cycle) ✅'
      }
    },

    open() {
      const modal = document.getElementById('isolationModal');
      if (modal) {
        modal.classList.add('active');
        this.selectLevel('read_committed');
      }
    },

    close() {
      const modal = document.getElementById('isolationModal');
      if (modal) modal.classList.remove('active');
    },

    selectLevel(lvlKey) {
      const lvl = this.levels[lvlKey];
      const output = document.getElementById('isolationOutput');
      if (!output || !lvl) return;

      output.innerHTML = `
        <div style="background:rgba(15,23,42,0.8);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:16px;">
          <h4 style="margin:0 0 10px 0;color:#38bdf8;">${lvl.name}</h4>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;font-size:13px;color:#cbd5e1;">
            <div>Dirty Read: <b>${lvl.dirty_read}</b></div>
            <div>Non-Repeatable Read: <b>${lvl.non_repeatable_read}</b></div>
            <div>Phantom Read: <b>${lvl.phantom_read}</b></div>
            <div>Write Skew: <b>${lvl.write_skew}</b></div>
          </div>
        </div>
      `;
    }
  };

  // ----------------------------------------------------------------------------
  // 19. MVCC Multi-Version Concurrency Control Engine
  // ----------------------------------------------------------------------------
  const MvccEngineSimulator = {
    tuples: [
      { id: 1, val: '$100', xmin: 100, xmax: 105, status: 'Superseded (Dead Tuple)' },
      { id: 1, val: '$120', xmin: 105, xmax: 0, status: 'Active (Visible to Tx >= 105)' },
      { id: 2, val: '$50', xmin: 102, xmax: 0, status: 'Active (Visible to Tx >= 102)' }
    ],

    open() {
      const modal = document.getElementById('mvccModal');
      if (modal) {
        modal.classList.add('active');
        this.render();
      }
    },

    close() {
      const modal = document.getElementById('mvccModal');
      if (modal) modal.classList.remove('active');
    },

    vacuum() {
      this.tuples = this.tuples.filter(t => t.xmax === 0);
      this.render();
      const statusEl = document.getElementById('mvccStatus');
      if (statusEl) {
        statusEl.innerHTML = '<span style="color:#10b981;font-weight:700;">VACUUM Reclaimed Dead Tuples! Page space consolidated.</span>';
      }
    },

    render() {
      const container = document.getElementById('mvccTable');
      if (!container) return;

      container.innerHTML = `
        <table style="width:100%;border-collapse:collapse;font-size:12px;color:#cbd5e1;">
          <thead>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.1);text-align:left;">
              <th style="padding:8px;">Row ID</th>
              <th style="padding:8px;">Data Value</th>
              <th style="padding:8px;">xmin (Created By)</th>
              <th style="padding:8px;">xmax (Deleted By)</th>
              <th style="padding:8px;">Visibility Status</th>
            </tr>
          </thead>
          <tbody>
            ${this.tuples.map(t => `
              <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
                <td style="padding:8px;">${t.id}</td>
                <td style="padding:8px;font-weight:700;color:#fff;">${t.val}</td>
                <td style="padding:8px;">${t.xmin}</td>
                <td style="padding:8px;">${t.xmax}</td>
                <td style="padding:8px;color:${t.xmax === 0 ? '#34d399' : '#fb7185'};">${t.status}</td>
              </tr>
            `).join('')}
          </tbody>
        </table>
      `;
    }
  };

  // ----------------------------------------------------------------------------
  // 20. Distributed 2PC vs 3PC Protocol Simulator
  // ----------------------------------------------------------------------------
  const TwoPhaseCommitSimulator = {
    step: 0,
    steps: [
      '1. Coordinator sends PREPARE to Cohorts A & B',
      '2. Cohorts write to WAL and reply VOTE_COMMIT',
      '3. Coordinator writes COMMIT decision to log',
      '4. Coordinator sends GLOBAL_COMMIT to Cohorts',
      '5. Cohorts commit transaction and reply ACK'
    ],

    open() {
      const modal = document.getElementById('twoPcModal');
      if (modal) {
        modal.classList.add('active');
        this.step = 0;
        this.render();
      }
    },

    close() {
      const modal = document.getElementById('twoPcModal');
      if (modal) modal.classList.remove('active');
    },

    next() {
      if (this.step < this.steps.length - 1) {
        this.step++;
        this.render();
      }
    },

    render() {
      const output = document.getElementById('twoPcOutput');
      if (!output) return;

      output.innerHTML = `
        <div style="background:rgba(15,23,42,0.8);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:16px;">
          <h4 style="margin:0 0 10px 0;color:#38bdf8;">Two-Phase Commit Sequence</h4>
          <div style="font-size:14px;font-weight:700;color:#34d399;margin-bottom:10px;">
            ${this.steps[this.step]}
          </div>
          <div style="font-size:11px;color:#94a3b8;">
            Step ${this.step + 1} of ${this.steps.length} — Failure during Step 3 triggers blocking recovery protocol.
          </div>
        </div>
      `;
    }
  };

  // ----------------------------------------------------------------------------
  // 21. Paxos Consensus Protocol Step-Through
  // ----------------------------------------------------------------------------
  const PaxosSimulator = {
    open() {
      const modal = document.getElementById('paxosModal');
      if (modal) modal.classList.add('active');
    },

    close() {
      const modal = document.getElementById('paxosModal');
      if (modal) modal.classList.remove('active');
    }
  };

  // Expose to window
  window.TcpTlsSimulator = TcpTlsSimulator;
  window.BTreeSimulator = BTreeSimulator;
  window.GcMarkSweepSimulator = GcMarkSweepSimulator;
  window.CpuCacheSimulator = CpuCacheSimulator;
  window.SqlExplainVisualizer = SqlExplainVisualizer;
  window.RegexAutomatonVisualizer = RegexAutomatonVisualizer;
  window.DeadlockVisualizer = DeadlockVisualizer;
  window.EpollSelectSimulator = EpollSelectSimulator;
  window.BuddyAllocatorSimulator = BuddyAllocatorSimulator;
  window.SystemTradeoffSliders = SystemTradeoffSliders;
  window.ChaosMonkeySimulator = ChaosMonkeySimulator;
  window.PageTableWalkerSimulator = PageTableWalkerSimulator;
  window.EbpfVerifierSimulator = EbpfVerifierSimulator;
  window.ZeroCopyPipelineSimulator = ZeroCopyPipelineSimulator;
  window.SpectreMeltdownSimulator = SpectreMeltdownSimulator;
  window.SimdVectorSimulator = SimdVectorSimulator;
  window.WorkStealingSimulator = WorkStealingSimulator;
  window.DatabaseIsolationSimulator = DatabaseIsolationSimulator;
  window.MvccEngineSimulator = MvccEngineSimulator;
  window.TwoPhaseCommitSimulator = TwoPhaseCommitSimulator;
  window.PaxosSimulator = PaxosSimulator;
})();
