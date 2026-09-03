import os
import re

# 1. GIT Q85 -> Git hooks
with open("markdowns/git/git-questions.md", "r", encoding="utf-8") as f:
    git = f.read()
git = git.replace("[What is `git worktree` and how does it allow working on multiple branches simultaneously?](#q85)", "[How do you configure Git Hooks (pre-commit, commit-msg, pre-push) and automate them with Husky?](#q85)")
new_git_q85 = """<a id="q85"></a>
### Q85: How do you configure Git Hooks (pre-commit, commit-msg, pre-push) and automate them with Husky?
**Difficulty**: <span class="intermediate">Intermediate</span>  
**Category**: Automation & Git Hooks  

**Strategy**: Explain client-side scripts in `.git/hooks/` and how tools like Husky manage version-controlled hooks across teams.

Git hooks are scripts triggered automatically when key version control events occur (e.g. `pre-commit`, `commit-msg`, `pre-push`). Husky and `lint-staged` automate sharing these hooks across teams in git repositories.

**Code Example**:
```bash
# Initialize Husky
npx husky init

# Add pre-commit lint hook
echo "npx lint-staged" > .husky/pre-commit
```"""
git = re.sub(r'<a id="q85"></a>\s*### Q85:.*?(?=<a id="q86">|$)', new_git_q85 + "\n\n---\n\n", git, flags=re.DOTALL)
with open("markdowns/git/git-questions.md", "w", encoding="utf-8") as f:
    f.write(git)

# 2. LINUX Q94 -> systemd unit
with open("markdowns/linux/linux-questions.md", "r", encoding="utf-8") as f:
    linux = f.read()
linux = linux.replace("[What is the difference between Hard Links and Soft (Symbolic) Links in Linux?](#q94)", "[What is `systemd` and how do you create and manage a custom Linux service unit file?](#q94)")
new_linux_q94 = """<a id="q94"></a>
### Q94: What is `systemd` and how do you create and manage a custom Linux service unit file?
**Difficulty**: <span class="advanced">Advanced</span>  
**Category**: Service Management & Init Systems  

**Strategy**: Explain systemd init system, unit file syntax in /etc/systemd/system/, and systemctl daemon management.

`systemd` is the standard Linux init system and service manager. Services are defined in `.service` unit files specifying startup commands, restart policies, user permissions, and dependency ordering.

**Code Example**:
```ini
# /etc/systemd/system/myapp.service
[Unit]
Description=My Node.js Application Service
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/var/www/myapp
ExecStart=/usr/bin/node /var/www/myapp/dist/server.js
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```
```bash
# Enable and start service
sudo systemctl daemon-reload
sudo systemctl enable --now myapp
sudo systemctl status myapp
```"""
linux = re.sub(r'<a id="q94"></a>\s*### Q94:.*?(?=<a id="q95">|$)', new_linux_q94 + "\n\n---\n\n", linux, flags=re.DOTALL)
with open("markdowns/linux/linux-questions.md", "w", encoding="utf-8") as f:
    f.write(linux)

# 3. DESIGN PATTERNS Q25 -> Null Object Pattern
with open("markdowns/design-patterns/design-patterns-questions.md", "r", encoding="utf-8") as f:
    dp = f.read()
dp = dp.replace("[What is the State Pattern?](#q25)", "[What is the Null Object Pattern?](#q25)")
new_dp_q25 = """<a id="q25"></a>
### Q25: What is the Null Object Pattern?
**Difficulty**: <span class="intermediate">Intermediate</span>  
**Category**: Behavioral Patterns  

**Strategy**: Explain how substituting a do-nothing object eliminates repetitive null checks.

The Null Object Pattern provides an object that conforms to the expected interface but has empty or default behavior, avoiding defensive `if (object != null)` checks throughout the codebase.

**Code Example**:
```typescript
interface Logger {
  log(message: string): void;
}

class ConsoleLogger implements Logger {
  log(msg: string) { console.log(`[LOG]: ${msg}`); }
}

class NullLogger implements Logger {
  log(msg: string) { /* Do nothing safely */ }
}

class OrderProcessor {
  constructor(private logger: Logger = new NullLogger()) {}
  processOrder() {
    this.logger.log("Order processed"); // Never throws null pointer error
  }
}
```"""
dp = re.sub(r'<a id="q25"></a>\s*### Q25:.*?(?=<a id="q26">|$)', new_dp_q25 + "\n\n---\n\n", dp, flags=re.DOTALL)
with open("markdowns/design-patterns/design-patterns-questions.md", "w", encoding="utf-8") as f:
    f.write(dp)

print("Cleaned git, linux, design-patterns.")
