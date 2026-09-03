import os

interactive_css = """
/* ==============================================================================
   INTERACTIVE PLATFORM ENHANCEMENTS: SEARCH, PLAYGROUND, QUIZ, FLASHCARDS, THEMES
   ============================================================================== */

/* Top Action Toolbar */
.platform-action-toolbar {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 20px;
  background: rgba(30, 41, 59, 0.7);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  position: sticky;
  top: 0;
  z-index: 99;
  flex-wrap: wrap;
}

.action-pill-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.15);
  color: #f8fafc;
  padding: 6px 14px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

.action-pill-btn:hover {
  background: var(--primary-color, #e53935);
  border-color: var(--primary-color, #e53935);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(229, 57, 53, 0.3);
}

.kbd-shortcut {
  background: rgba(0, 0, 0, 0.3);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 4px;
  padding: 2px 6px;
  font-size: 11px;
  font-family: monospace;
  opacity: 0.8;
}

/* Modals Overlay */
.platform-modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.75);
  backdrop-filter: blur(8px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10000;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.25s ease;
  padding: 16px;
}

.platform-modal-overlay.active {
  opacity: 1;
  pointer-events: auto;
}

.platform-modal-content {
  background: #1e293b;
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 16px;
  width: 100%;
  max-width: 800px;
  max-height: 90vh;
  display: flex;
  flex-direction: column;
  box-shadow: 0 24px 48px rgba(0, 0, 0, 0.5);
  overflow: hidden;
  transform: scale(0.95);
  transition: transform 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}

.platform-modal-overlay.active .platform-modal-content {
  transform: scale(1);
}

.modal-header {
  padding: 16px 20px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: rgba(15, 23, 42, 0.6);
}

.modal-header h3 {
  margin: 0;
  font-size: 18px;
  color: #f8fafc;
  display: flex;
  align-items: center;
  gap: 8px;
}

.modal-close-btn {
  background: none;
  border: none;
  color: #94a3b8;
  font-size: 24px;
  cursor: pointer;
  line-height: 1;
  padding: 4px;
  border-radius: 6px;
  transition: color 0.15s;
}

.modal-close-btn:hover {
  color: #ffffff;
}

.modal-body {
  padding: 20px;
  overflow-y: auto;
  flex: 1;
}

/* Instant Search Modal */
.search-input-wrapper {
  position: relative;
  margin-bottom: 16px;
}

.search-modal-input {
  width: 100%;
  background: #0f172a;
  border: 2px solid rgba(255, 255, 255, 0.15);
  border-radius: 10px;
  padding: 12px 16px;
  color: #f8fafc;
  font-size: 16px;
  outline: none;
  transition: border-color 0.2s;
  box-sizing: border-box;
}

.search-modal-input:focus {
  border-color: #e53935;
}

.search-results-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
  max-height: 480px;
  overflow-y: auto;
}

.search-result-row {
  padding: 12px 14px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.15s;
}

.search-result-row:hover {
  background: rgba(229, 57, 53, 0.12);
  border-color: #e53935;
  transform: translateX(4px);
}

.search-result-cat {
  font-size: 11px;
  text-transform: uppercase;
  color: #e53935;
  font-weight: 700;
  margin-bottom: 4px;
}

.search-result-title {
  font-size: 14px;
  font-weight: 600;
  color: #f1f5f9;
}

/* Code Playground */
.playground-container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  height: 420px;
}

@media (max-width: 768px) {
  .playground-container {
    grid-template-columns: 1fr;
    height: auto;
  }
}

.playground-editor-area {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.playground-textarea {
  flex: 1;
  background: #0f172a;
  color: #38bdf8;
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 8px;
  padding: 12px;
  font-family: 'Fira Code', 'Courier New', monospace;
  font-size: 13px;
  line-height: 1.5;
  resize: none;
  outline: none;
  min-height: 250px;
}

.playground-console {
  background: #020617;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  padding: 12px;
  color: #a3e635;
  font-family: monospace;
  font-size: 12px;
  overflow-y: auto;
  white-space: pre-wrap;
  min-height: 250px;
}

/* Flashcard 3D Card */
.flashcard-scene {
  perspective: 1000px;
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.flashcard-card {
  width: 100%;
  min-height: 260px;
  position: relative;
  transform-style: preserve-3d;
  transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
}

.flashcard-card.flipped {
  transform: rotateY(180deg);
}

.flashcard-face {
  position: absolute;
  inset: 0;
  backface-visibility: hidden;
  border-radius: 12px;
  padding: 24px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  background: #0f172a;
  border: 1px solid rgba(255, 255, 255, 0.15);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
}

.flashcard-back {
  transform: rotateY(180deg);
  background: #1e1b4b;
  border-color: #6366f1;
}

.sm2-rating-bar {
  display: flex;
  justify-content: center;
  gap: 10px;
  flex-wrap: wrap;
}

.sm2-btn {
  padding: 8px 16px;
  border-radius: 8px;
  border: none;
  font-weight: 600;
  cursor: pointer;
  color: #ffffff;
  transition: transform 0.15s;
}

.sm2-btn:hover {
  transform: scale(1.05);
}

.sm2-again { background: #ef4444; }
.sm2-hard { background: #f97316; }
.sm2-good { background: #3b82f6; }
.sm2-easy { background: #10b981; }

/* Themes */
body.theme-cyberpunk {
  --primary-color: #00ffcc;
  --secondary-color: #ff007f;
  background: #050510 !important;
  color: #00ffcc !important;
}

body.theme-cyberpunk .sidebar,
body.theme-cyberpunk .platform-action-toolbar,
body.theme-cyberpunk .platform-modal-content {
  background: #0b0c22 !important;
  border-color: #ff007f !important;
}

body.theme-dracula {
  --primary-color: #ff79c6;
  --secondary-color: #bd93f9;
  background: #282a36 !important;
  color: #f8f8f2 !important;
}

body.theme-dracula .sidebar,
body.theme-dracula .platform-action-toolbar,
body.theme-dracula .platform-modal-content {
  background: #1e1f29 !important;
  border-color: #6272a4 !important;
}

body.theme-light {
  --primary-color: #d32f2f;
  background: #f8fafc !important;
  color: #0f172a !important;
}

body.theme-light .sidebar,
body.theme-light .platform-action-toolbar,
body.theme-light .platform-modal-content {
  background: #ffffff !important;
  color: #0f172a !important;
  border-color: #e2e8f0 !important;
}

body.theme-light .search-result-row {
  background: #f1f5f9;
  border-color: #cbd5e1;
}

body.theme-light .search-result-title {
  color: #0f172a;
}
"""

with open("assets/css/inline-styles.css", "a", encoding="utf-8") as f:
    f.write("\n" + interactive_css)

print("Interactive CSS appended successfully.")
