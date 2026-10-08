/**
 * Interview Guide Platform - Client-Side Authentication Manager
 * Handles JWT token management, automatic session refresh via HTTP-only cookies,
 * user state synchronization, and UI profile widgets across all pages.
 */
(function() {
  const TOKEN_KEY = 'ig_token';
  const USER_KEY = 'ig_user';

  const AuthClient = {
    getToken() {
      return localStorage.getItem(TOKEN_KEY) || null;
    },

    getUser() {
      try {
        const raw = localStorage.getItem(USER_KEY);
        return raw ? JSON.parse(raw) : null;
      } catch (e) {
        return null;
      }
    },

    isAuthenticated() {
      return !!this.getToken();
    },

    async login(email, password) {
      const res = await fetch('/api/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password })
      });
      const data = await res.json();
      if (!res.ok) {
        throw new Error(data.error || 'Login failed');
      }
      if (data.access_token) {
        localStorage.setItem(TOKEN_KEY, data.access_token);
        if (data.user) {
          localStorage.setItem(USER_KEY, JSON.stringify(data.user));
        }
      }
      return data;
    },

    async register(email, password, fullName) {
      const res = await fetch('/api/auth/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password, full_name: fullName })
      });
      const data = await res.json();
      if (!res.ok) {
        throw new Error(data.error || 'Registration failed');
      }
      if (data.access_token) {
        localStorage.setItem(TOKEN_KEY, data.access_token);
        if (data.user) {
          localStorage.setItem(USER_KEY, JSON.stringify(data.user));
        }
      }
      return data;
    },

    async logout() {
      try {
        await fetch('/api/auth/logout', { method: 'POST' });
      } catch (e) {
        // Continue clearing client credentials
      }
      localStorage.removeItem(TOKEN_KEY);
      localStorage.removeItem(USER_KEY);
      window.location.href = 'login.html';
    },

    async refreshToken() {
      try {
        const res = await fetch('/api/auth/refresh', { method: 'POST' });
        if (res.ok) {
          const data = await res.json();
          if (data.access_token) {
            localStorage.setItem(TOKEN_KEY, data.access_token);
            if (data.user) {
              localStorage.setItem(USER_KEY, JSON.stringify(data.user));
            }
            return data.access_token;
          }
        } else if (res.status === 401) {
          // Refresh token expired or revoked
          localStorage.removeItem(TOKEN_KEY);
          localStorage.removeItem(USER_KEY);
        }
      } catch (e) {
        // Network offline
      }
      return null;
    },

    initAutoRefresh() {
      // Periodically refresh the JWT access token every 12 minutes (token expires in 15m)
      setInterval(() => {
        if (this.isAuthenticated()) {
          this.refreshToken();
        }
      }, 12 * 60 * 1000);
    },

    renderSidebarWidget() {
      const sidebar = document.getElementById('sidebar');
      if (!sidebar) return;

      let widget = document.getElementById('sidebarAuthWidget');
      if (!widget) {
        widget = document.createElement('div');
        widget.id = 'sidebarAuthWidget';
        widget.style.cssText = 'padding: 10px 14px; margin-bottom: 12px; border-radius: 10px; background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1); font-size: 13px; color: #e2e8f0; display: flex; align-items: center; justify-content: space-between;';
        
        // Insert right after the sidebar-brand
        const brand = sidebar.querySelector('.sidebar-brand');
        if (brand && brand.nextSibling) {
          sidebar.insertBefore(widget, brand.nextSibling);
        } else {
          sidebar.prepend(widget);
        }
      }

      const user = this.getUser();
      if (user) {
        const initials = (user.full_name || user.email || 'U').split(' ').map(s => s[0]).join('').slice(0, 2).toUpperCase();
        widget.innerHTML = `
          <div style="display: flex; align-items: center; gap: 8px; min-width: 0;">
            <div style="width: 28px; height: 28px; border-radius: 50%; background: linear-gradient(135deg, #6366f1, #a855f7); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 11px; flex-shrink: 0;">
              ${initials}
            </div>
            <div style="min-width: 0;">
              <div style="font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 110px;" title="${user.full_name || user.email}">
                ${user.full_name || user.email.split('@')[0]}
              </div>
              <div style="font-size: 10px; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.05em;">
                ${user.role || 'Member'}
              </div>
            </div>
          </div>
          <button id="authLogoutBtn" title="Sign out" style="background: none; border: 1px solid rgba(255, 255, 255, 0.15); color: #cbd5e1; border-radius: 6px; padding: 4px 8px; font-size: 11px; cursor: pointer; transition: all 0.2s;" onmouseover="this.style.borderColor='#f43f5e';this.style.color='#f43f5e'" onmouseout="this.style.borderColor='rgba(255,255,255,0.15)';this.style.color='#cbd5e1'">
            Exit
          </button>
        `;
        const logoutBtn = document.getElementById('authLogoutBtn');
        if (logoutBtn) {
          logoutBtn.onclick = (e) => {
            e.preventDefault();
            AuthClient.logout();
          };
        }
      } else {
        widget.innerHTML = `
          <div style="display: flex; align-items: center; gap: 8px;">
            <span style="font-size: 14px;">👤</span>
            <span style="color: #94a3b8;">Guest Mode</span>
          </div>
          <a href="login.html" style="background: linear-gradient(135deg, #6366f1, #4f46e5); color: white; text-decoration: none; padding: 4px 10px; border-radius: 6px; font-size: 11px; font-weight: 600;">
            Sign In
          </a>
        `;
      }
    },

    renderNavbarWidget() {
      const actions = document.getElementById('searchShortcutPill');
      if (!actions || !actions.parentElement) return;

      let navAuth = document.getElementById('navbarAuthPill');
      if (!navAuth) {
        navAuth = document.createElement('div');
        navAuth.id = 'navbarAuthPill';
        actions.parentElement.insertBefore(navAuth, actions);
      }

      const user = this.getUser();
      if (user) {
        navAuth.innerHTML = `
          <a href="dashboard.html" style="display: flex; align-items: center; gap: 6px; text-decoration: none; padding: 6px 12px; border-radius: 20px; background: rgba(99, 102, 241, 0.15); border: 1px solid rgba(99, 102, 241, 0.3); color: #c7d2fe; font-size: 12px; font-weight: 600;">
            <span style="width: 8px; height: 8px; border-radius: 50%; background: #22c55e;"></span>
            <span>${user.full_name || user.email.split('@')[0]}</span>
          </a>
        `;
      } else {
        navAuth.innerHTML = `
          <a href="login.html" style="text-decoration: none; padding: 6px 14px; border-radius: 20px; background: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255, 255, 255, 0.15); color: #e2e8f0; font-size: 12px; font-weight: 600; transition: background 0.2s;" onmouseover="this.style.background='rgba(255,255,255,0.15)'" onmouseout="this.style.background='rgba(255,255,255,0.08)'">
            Sign In
          </a>
        `;
      }
    }
  };

  window.AuthClient = AuthClient;

  // Auto-initialize when DOM is ready
  document.addEventListener('DOMContentLoaded', () => {
    AuthClient.initAutoRefresh();
    AuthClient.renderSidebarWidget();
    AuthClient.renderNavbarWidget();
  });
})();
