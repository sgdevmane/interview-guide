// ==============================================================================
// Lightweight, High-Performance Canvas Confetti Engine (Zero-Dependency)
// Supports multi-color particles, physics, wobble, and custom burst bursts
// ==============================================================================

(function(window) {
  'use strict';

  let canvas = null;
  let ctx = null;
  let animationId = null;
  const particles = [];
  const colors = ['#06b6d4', '#3b82f6', '#8b5cf6', '#ec4899', '#10b981', '#f59e0b', '#22c55e', '#6366f1'];

  function initCanvas() {
    if (canvas) return;
    canvas = document.createElement('canvas');
    canvas.id = 'confetti-canvas';
    canvas.style.position = 'fixed';
    canvas.style.top = '0';
    canvas.style.left = '0';
    canvas.style.width = '100vw';
    canvas.style.height = '100vh';
    canvas.style.pointerEvents = 'none';
    canvas.style.zIndex = '99999';
    document.body.appendChild(canvas);
    ctx = canvas.getContext('2d');
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);
  }

  function resizeCanvas() {
    if (!canvas) return;
    canvas.width = window.innerWidth * window.devicePixelRatio;
    canvas.height = window.innerHeight * window.devicePixelRatio;
    ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
  }

  class ConfettiParticle {
    constructor(x, y, vx, vy) {
      this.x = x;
      this.y = y;
      this.vx = vx || (Math.random() - 0.5) * 16;
      this.vy = vy || (Math.random() * -18 - 4);
      this.gravity = 0.45;
      this.wobble = Math.random() * Math.PI * 2;
      this.wobbleSpeed = Math.random() * 0.15 + 0.05;
      this.size = Math.random() * 8 + 6;
      this.color = colors[Math.floor(Math.random() * colors.length)];
      this.opacity = 1;
      this.decay = Math.random() * 0.015 + 0.008;
      this.shape = Math.random() > 0.3 ? 'rect' : 'circle';
    }

    update() {
      this.x += this.vx;
      this.y += this.vy;
      this.vy += this.gravity;
      this.vx *= 0.96;
      this.wobble += this.wobbleSpeed;
      this.opacity -= this.decay;
    }

    draw(ctx) {
      if (this.opacity <= 0) return;
      ctx.save();
      ctx.globalAlpha = Math.max(0, this.opacity);
      ctx.translate(this.x, this.y);
      ctx.rotate(this.wobble);

      ctx.fillStyle = this.color;
      if (this.shape === 'rect') {
        ctx.fillRect(-this.size / 2, -this.size / 4, this.size, this.size / 2);
      } else {
        ctx.beginPath();
        ctx.arc(0, 0, this.size / 2, 0, Math.PI * 2);
        ctx.fill();
      }
      ctx.restore();
    }
  }

  function loop() {
    if (!ctx) return;
    ctx.clearRect(0, 0, window.innerWidth, window.innerHeight);

    for (let i = particles.length - 1; i >= 0; i--) {
      const p = particles[i];
      p.update();
      p.draw(ctx);
      if (p.opacity <= 0 || p.y > window.innerHeight + 50) {
        particles.splice(i, 1);
      }
    }

    if (particles.length > 0) {
      animationId = requestAnimationFrame(loop);
    } else {
      cancelAnimationFrame(animationId);
      animationId = null;
    }
  }

  function launchConfetti(originX, originY, count) {
    initCanvas();
    const x = originX !== undefined ? originX : window.innerWidth / 2;
    const y = originY !== undefined ? originY : window.innerHeight * 0.65;
    const total = count || 120;

    for (let i = 0; i < total; i++) {
      const angle = (Math.PI * 2 * i) / total + (Math.random() - 0.5) * 0.5;
      const speed = Math.random() * 14 + 6;
      const vx = Math.cos(angle) * speed;
      const vy = Math.sin(angle) * speed - 6;
      particles.push(new ConfettiParticle(x, y, vx, vy));
    }

    if (!animationId) {
      animationId = requestAnimationFrame(loop);
    }
  }

  // Multi-cannon celebration burst
  function celebrate() {
    launchConfetti(window.innerWidth * 0.2, window.innerHeight * 0.8, 80);
    setTimeout(() => launchConfetti(window.innerWidth * 0.8, window.innerHeight * 0.8, 80), 200);
    setTimeout(() => launchConfetti(window.innerWidth * 0.5, window.innerHeight * 0.6, 120), 450);
  }

  window.ConfettiEngine = {
    burst: launchConfetti,
    celebrate: celebrate
  };

})(window);
