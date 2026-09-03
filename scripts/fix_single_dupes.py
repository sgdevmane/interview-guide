import os
import re

# 1. DESIGN PATTERNS: Q25 (Interpreter is dupe of Q24). Replace Q25 with "What is the Null Object Pattern?"
dp_path = "markdowns/design-patterns/design-patterns-questions.md"
with open(dp_path, "r", encoding="utf-8") as f:
    dp = f.read()
# Replace in TOC line 25:
dp = re.sub(r'25\.\s*\[What is the Interpreter Pattern\?\]\(#q25\)', '25. [What is the Null Object Pattern?](#q25)', dp)
# Replace body Q25:
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
dp = re.sub(r'<a id="q25"></a>\s*### Q25:.*?(?=<a id="q26">)', new_dp_q25 + "\n\n---\n\n", dp, flags=re.DOTALL)
with open(dp_path, "w", encoding="utf-8") as f:
    f.write(dp)

# 2. GIT: Q85 (git bisect is dupe of Q60/Q77). Replace Q85 with "How do you configure Git Hooks (pre-commit, commit-msg, pre-push) and automate them with Husky?"
git_path = "markdowns/git/git-questions.md"
with open(git_path, "r", encoding="utf-8") as f:
    git = f.read()
git = re.sub(r'85\.\s*\[.*?\]\(#q85\)', '85. [How do you configure Git Hooks (pre-commit, commit-msg, pre-push) and automate them with Husky?](#q85)', git)
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
git = re.sub(r'<a id="q85"></a>\s*### Q85:.*?(?=<a id="q86">)', new_git_q85 + "\n\n---\n\n", git, flags=re.DOTALL)
with open(git_path, "w", encoding="utf-8") as f:
    f.write(git)

# 3. GOLANG: Q63 (sync.Cond is dupe of Q56). Replace Q63 with "How does Go's `runtime.Gosched()` yield execution to other goroutines?"
go_path = "markdowns/golang/golang-questions.md"
with open(go_path, "r", encoding="utf-8") as f:
    golang = f.read()
golang = re.sub(r'63\.\s*\[.*?\]\(#q63\)', '63. [How does Go\'s `runtime.Gosched()` yield execution to other goroutines?](#q63)', golang)
new_go_q63 = """<a id="q63"></a>
### Q63: How does Go's `runtime.Gosched()` yield execution to other goroutines?
**Difficulty**: <span class="advanced">Advanced</span>  
**Category**: Concurrency & Runtime  

**Strategy**: Explain cooperative scheduling in the Go runtime scheduler.

`runtime.Gosched()` yields the processor, allowing other goroutines to run. It does not suspend the current goroutine, so execution resumes automatically when the scheduler picks it up again.

**Code Example**:
```go
package main

import (
	"fmt"
	"runtime"
)

func main() {
	go func() {
		for i := 0; i < 5; i++ {
			fmt.Println("Goroutine working")
			runtime.Gosched() // Yield CPU
		}
	}()

	for i := 0; i < 5; i++ {
		fmt.Println("Main thread working")
		runtime.Gosched()
	}
}
```"""
golang = re.sub(r'<a id="q63"></a>\s*### Q63:.*?(?=<a id="q64">)', new_go_q63 + "\n\n---\n\n", golang, flags=re.DOTALL)
with open(go_path, "w", encoding="utf-8") as f:
    f.write(golang)

# 4. GRAPHQL: Q43 (Schema Stitching dupe of Q24) and Q97 (Query Depth dupe of Q76)
gql_path = "markdowns/graphql/graphql-questions.md"
with open(gql_path, "r", encoding="utf-8") as f:
    gql = f.read()
gql = re.sub(r'43\.\s*\[.*?\]\(#q43\)', '43. [What are GraphQL Directives (`@deprecated`, `@include`, `@skip`)?](#q43)', gql)
gql = re.sub(r'97\.\s*\[.*?\]\(#q97\)', '97. [How does DataLoader batching prevent the N+1 Query problem in GraphQL?](#q97)', gql)
new_gql_q43 = """<a id="q43"></a>
### Q43: What are GraphQL Directives (`@deprecated`, `@include`, `@skip`)?
**Difficulty**: <span class="intermediate">Intermediate</span>  
**Category**: GraphQL Schema & Query Syntax  

**Strategy**: Explain how directives dynamically alter schema behavior and query execution.

Directives decorate schema fields or queries with `@directiveName`. Built-in directives include `@deprecated(reason: "...")`, `@include(if: Boolean)`, and `@skip(if: Boolean)`.

**Code Example**:
```graphql
query GetUser($showDetails: Boolean!) {
  user(id: "101") {
    id
    name
    email @include(if: $showDetails)
    internalNotes @skip(if: $showDetails)
  }
}
```"""
new_gql_q97 = """<a id="q97"></a>
### Q97: How does DataLoader batching prevent the N+1 Query problem in GraphQL?
**Difficulty**: <span class="advanced">Advanced</span>  
**Category**: Performance & Caching  

**Strategy**: Explain how DataLoader coalesces individual ID lookups into a single batched database query using Node.js event loop ticks.

DataLoader collects individual `id` requests made across various resolvers within a single execution tick and executes a single `WHERE id IN (...)` batch query, caching the result promises.

**Code Example**:
```javascript
const DataLoader = require('dataloader');

// Batch loading function
const userLoader = new DataLoader(async (keys) => {
  const users = await db.users.find({ _id: { $in: keys } });
  return keys.map(k => users.find(u => u._id === k));
});

// Resolver
const resolvers = {
  Post: {
    author: (post) => userLoader.load(post.authorId)
  }
};
```"""
gql = re.sub(r'<a id="q43"></a>\s*### Q43:.*?(?=<a id="q44">)', new_gql_q43 + "\n\n---\n\n", gql, flags=re.DOTALL)
gql = re.sub(r'<a id="q97"></a>\s*### Q97:.*?(?=<a id="q98">)', new_gql_q97 + "\n\n---\n\n", gql, flags=re.DOTALL)
with open(gql_path, "w", encoding="utf-8") as f:
    f.write(gql)

# 5. LINUX: Q94 (cgroups dupe of Q69). Replace Q94 with "What is `systemd` and how do you create and manage a custom Linux service unit file?"
linux_path = "markdowns/linux/linux-questions.md"
with open(linux_path, "r", encoding="utf-8") as f:
    linux = f.read()
linux = re.sub(r'94\.\s*\[.*?\]\(#q94\)', '94. [What is `systemd` and how do you create and manage a custom Linux service unit file?](#q94)', linux)
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
```"""
linux = re.sub(r'<a id="q94"></a>\s*### Q94:.*?(?=<a id="q95">)', new_linux_q94 + "\n\n---\n\n", linux, flags=re.DOTALL)
with open(linux_path, "w", encoding="utf-8") as f:
    f.write(linux)

print("Fixed single dupes in DP, Git, Go, GraphQL, Linux.")
