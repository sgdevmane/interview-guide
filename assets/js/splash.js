// ==============================================================================
// Animated Mobile & PWA Splashscreen Controller with Confetti Celebration
// ==============================================================================

(function(window, document) {
  'use strict';

  function initSplashScreen() {
    // Only show once per session or on standalone PWA launch
    const isPWA = window.matchMedia('(display-mode: standalone)').matches || window.navigator.standalone === true;
    const hasSeenSplash = sessionStorage.getItem('interview_guide_splash_seen');

    // Create splash screen element if not present
    if (!document.getElementById('app-splash-screen')) {
      const splash = document.createElement('div');
      splash.id = 'app-splash-screen';
      splash.innerHTML = `
        <div class="splash-content">
          <div class="splash-logo-wrapper">
            <div class="splash-glow-ring"></div>
            <img class="splash-logo" src="assets/icons/interview_guide_logo.png" alt="Interview Guide Logo" />
          </div>
          <h1 class="splash-title">Interview Guide</h1>
          <p class="splash-subtitle">Mastering 5,650+ Questions Across 55 Technical Domains</p>
          <div class="splash-loader-bar">
            <div class="splash-loader-progress"></div>
          </div>
        </div>
      `;
      document.body.prepend(splash);

      // Auto dismiss after progress animation
      setTimeout(() => {
        if (window.ConfettiEngine) {
          window.ConfettiEngine.celebrate();
        }
        splash.classList.add('fade-out');
        setTimeout(() => {
          splash.remove();
        }, 800);
      }, 1600);

      sessionStorage.setItem('interview_guide_splash_seen', 'true');
    }
  }

  // Trigger on DOMContentLoaded
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initSplashScreen);
  } else {
    initSplashScreen();
  }

  window.showSplashScreen = function() {
    sessionStorage.removeItem('interview_guide_splash_seen');
    initSplashScreen();
  };

})(window, document);
