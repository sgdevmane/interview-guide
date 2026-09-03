import os
import re

# ==============================================================================
# 1. FIX JAVASCRIPT DUPE (Q99)
# ==============================================================================
js_path = "markdowns/javascript/javascript-questions.md"
if os.path.exists(js_path):
    with open(js_path, "r", encoding="utf-8") as f:
        js_content = f.read()
    
    # Replace duplicate TDZ question in TOC and Body
    js_content = js_content.replace(
        "[What is Temporal Dead Zone (TDZ)?](#q99)",
        "[What is the difference between `Object.freeze()` and `Object.seal()`?](#q99)"
    )
    
    old_q99 = """<a id="q99"></a>
### Q99: What is Temporal Dead Zone (TDZ)?
**Difficulty**: <span class="intermediate">Intermediate</span>  
**Category**: JavaScript Fundamentals  

**Strategy**: Explain how `let` and `const` variables are hoisted but uninitialized until evaluation.

The Temporal Dead Zone (TDZ) is the period between entering a scope and the actual variable declaration where accessing `let` or `const` variables throws a `ReferenceError`.

**Code Example**:
```javascript
// TDZ Example
console.log(x); // ReferenceError: Cannot access 'x' before initialization
let x = 10;
```"""

    new_q99 = """<a id="q99"></a>
### Q99: What is the difference between `Object.freeze()` and `Object.seal()`?
**Difficulty**: <span class="intermediate">Intermediate</span>  
**Category**: Objects & Immutability  

**Strategy**: Explain property configuration, addition, deletion, and value mutability.

`Object.freeze()` makes an object completely immutable: existing properties cannot be modified, added, or removed (writable: false, configurable: false). `Object.seal()` prevents adding or deleting properties, but allows modifying existing property values (writable: true, configurable: false).

**Code Example**:
```javascript
const sealed = Object.seal({ a: 1 });
sealed.a = 2; // Allowed
delete sealed.a; // Error in strict mode

const frozen = Object.freeze({ b: 1 });
frozen.b = 2; // Error in strict mode
```"""
    if old_q99 in js_content:
        js_content = js_content.replace(old_q99, new_q99)
    else:
        # Generic regex replace
        js_content = re.sub(r'<a id="q99"></a>\s*### Q99:.*?(?=<a id="q100">|$)', new_q99 + "\n\n---\n\n", js_content, flags=re.DOTALL)
    
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(js_content)
    print("Fixed JavaScript Q99.")

# ==============================================================================
# 2. FIX GOLANG DUPE (Q63)
# ==============================================================================
go_path = "markdowns/golang/golang-questions.md"
if os.path.exists(go_path):
    with open(go_path, "r", encoding="utf-8") as f:
        go_content = f.read()
    
    go_content = go_content.replace(
        "[How do you use `sync.Cond` for complex synchronization?](#q63)",
        "[How does Go's `runtime.Gosched()` yield execution to other goroutines?](#q63)"
    )
    
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
    go_content = re.sub(r'<a id="q63"></a>\s*### Q63:.*?(?=<a id="q64">|$)', new_go_q63 + "\n\n---\n\n", go_content, flags=re.DOTALL)
    with open(go_path, "w", encoding="utf-8") as f:
        f.write(go_content)
    print("Fixed Golang Q63.")

# ==============================================================================
# 3. FIX GIT DUPE (Q85)
# ==============================================================================
git_path = "markdowns/git/git-questions.md"
if os.path.exists(git_path):
    with open(git_path, "r", encoding="utf-8") as f:
        git_content = f.read()
    
    git_content = git_content.replace(
        "[How do you stash specific files only?](#q85)",
        "[How do you use `git rerere` (Reuse Recorded Resolution)?](#q85)"
    )
    
    new_git_q85 = """<a id="q85"></a>
### Q85: How do you use `git rerere` (Reuse Recorded Resolution)?
**Difficulty**: <span class="advanced">Advanced</span>  
**Category**: Merge & Conflict Resolution  

**Strategy**: Explain how git records conflict resolutions and auto-applies them to repeated merges.

`git rerere` stands for 'reuse recorded resolution'. When enabled (`git config --global rerere.enabled true`), Git records how you resolve conflict hunks. When identical conflicts happen again (e.g. during rebase), Git resolves them automatically.

**Code Example**:
```bash
# Enable git rerere globally
git config --global rerere.enabled true

# Check rerere status
git rerere status
git rerere diff
```"""
    git_content = re.sub(r'<a id="q85"></a>\s*### Q85:.*?(?=<a id="q86">|$)', new_git_q85 + "\n\n---\n\n", git_content, flags=re.DOTALL)
    with open(git_path, "w", encoding="utf-8") as f:
        f.write(git_content)
    print("Fixed Git Q85.")

# ==============================================================================
# 4. FIX LINUX DUPE (Q94)
# ==============================================================================
linux_path = "markdowns/linux/linux-questions.md"
if os.path.exists(linux_path):
    with open(linux_path, "r", encoding="utf-8") as f:
        linux_content = f.read()
    
    linux_content = linux_content.replace(
        "[What is the `/proc` filesystem?](#q94)",
        "[What is the difference between `/dev/null`, `/dev/zero`, and `/dev/random` in Linux?](#q94)"
    )
    
    new_linux_q94 = """<a id="q94"></a>
### Q94: What is the difference between `/dev/null`, `/dev/zero`, and `/dev/random` in Linux?
**Difficulty**: <span class="intermediate">Intermediate</span>  
**Category**: Device Files  

**Strategy**: Explain standard virtual device files and their use cases.

- `/dev/null`: Discards all data written to it (black hole), returns EOF on read.
- `/dev/zero`: Provides infinite null bytes (`0x00`) on read; used for initializing files or memory buffers.
- `/dev/random`: Generates cryptographically secure random bytes from kernel entropy.

**Code Example**:
```bash
# Create a 100MB blank file filled with zeros
dd if=/dev/zero of=testfile.bin bs=1M count=100

# Discard command stderr
curl https://example.com 2> /dev/null
```"""
    linux_content = re.sub(r'<a id="q94"></a>\s*### Q94:.*?(?=<a id="q95">|$)', new_linux_q94 + "\n\n---\n\n", linux_content, flags=re.DOTALL)
    with open(linux_path, "w", encoding="utf-8") as f:
        f.write(linux_content)
    print("Fixed Linux Q94.")

# ==============================================================================
# 5. FIX GRAPHQL DUPES (Q43 & Q97)
# ==============================================================================
gql_path = "markdowns/graphql/graphql-questions.md"
if os.path.exists(gql_path):
    with open(gql_path, "r", encoding="utf-8") as f:
        gql_content = f.read()
    
    gql_content = gql_content.replace(
        "[What is Schema Stitching?](#q43)",
        "[What are GraphQL Directives (`@deprecated`, `@include`, `@skip`)?](#q43)"
    )
    gql_content = gql_content.replace(
        "[How do you limit Query Depth?](#q97)",
        "[How does DataLoader batching prevent the N+1 Query problem in GraphQL?](#q97)"
    )
    
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
    gql_content = re.sub(r'<a id="q43"></a>\s*### Q43:.*?(?=<a id="q44">|$)', new_gql_q43 + "\n\n---\n\n", gql_content, flags=re.DOTALL)
    gql_content = re.sub(r'<a id="q97"></a>\s*### Q97:.*?(?=<a id="q98">|$)', new_gql_q97 + "\n\n---\n\n", gql_content, flags=re.DOTALL)
    with open(gql_path, "w", encoding="utf-8") as f:
        f.write(gql_content)
    print("Fixed GraphQL Q43 & Q97.")

# ==============================================================================
# 6. FIX DESIGN PATTERNS DUPE (Q25)
# ==============================================================================
dp_path = "markdowns/design-patterns/design-patterns-questions.md"
if os.path.exists(dp_path):
    with open(dp_path, "r", encoding="utf-8") as f:
        dp_content = f.read()
    
    dp_content = dp_content.replace(
        "[What is the Iterator Pattern?](#q25)",
        "[What is the Visitor Pattern?](#q25)"
    )
    
    new_dp_q25 = """<a id="q25"></a>
### Q25: What is the Visitor Pattern?
**Difficulty**: <span class="advanced">Advanced</span>  
**Category**: Behavioral Patterns  

**Strategy**: Explain double dispatch and separating algorithms from object structures.

The Visitor Pattern allows adding new operations to an existing object hierarchy without modifying the classes. It uses double dispatch where elements accept a visitor object (`element.accept(visitor)`), and the visitor executes the corresponding method (`visitor.visitElement(this)`).

**Code Example**:
```typescript
interface Visitor {
  visitCircle(c: Circle): void;
  visitSquare(s: Square): void;
}

interface Shape {
  accept(v: Visitor): void;
}

class Circle implements Shape {
  accept(v: Visitor) { v.visitCircle(this); }
}

class Square implements Shape {
  accept(v: Visitor) { v.visitSquare(this); }
}
```"""
    dp_content = re.sub(r'<a id="q25"></a>\s*### Q25:.*?(?=<a id="q26">|$)', new_dp_q25 + "\n\n---\n\n", dp_content, flags=re.DOTALL)
    with open(dp_path, "w", encoding="utf-8") as f:
        f.write(dp_content)
    print("Fixed Design Patterns Q25.")

print("Dupes fixed successfully.")
