import os
import re

# 1. JS Q99
with open("markdowns/javascript/javascript-questions.md", "r", encoding="utf-8") as f:
    js = f.read()
js = js.replace("[What is the difference between `Object.freeze()` and `Object.seal()`?](#q99)", "[What are `WeakRef` and `FinalizationRegistry` in ES2021?](#q99)")
new_js_q99 = """<a id="q99"></a>
### Q99: What are `WeakRef` and `FinalizationRegistry` in ES2021?
**Difficulty**: <span class="advanced">Advanced</span>  
**Category**: Memory & Garbage Collection  

**Strategy**: Explain how WeakRef creates non-retaining object references and FinalizationRegistry executes cleanup callbacks after garbage collection.

`WeakRef` lets you hold a weak reference to an object without preventing it from being garbage-collected. `FinalizationRegistry` lets you register a callback that runs after an object is garbage-collected.

**Code Example**:
```javascript
const registry = new FinalizationRegistry((heldValue) => {
  console.log(`Object with tag ${heldValue} was garbage collected.`);
});

let obj = { data: 'large cache' };
const ref = new WeakRef(obj);
registry.register(obj, 'cacheKey_1');

// Later when dereferencing:
const cachedObj = ref.deref();
if (cachedObj) {
  console.log('Object is still in memory:', cachedObj.data);
} else {
  console.log('Object has been garbage-collected.');
}
```"""
js = re.sub(r'<a id="q99"></a>\s*### Q99:.*?(?=<a id="q100">|$)', new_js_q99 + "\n\n---\n\n", js, flags=re.DOTALL)
with open("markdowns/javascript/javascript-questions.md", "w", encoding="utf-8") as f:
    f.write(js)

# 2. GIT Q85
with open("markdowns/git/git-questions.md", "r", encoding="utf-8") as f:
    git = f.read()
git = git.replace("[How do you use `git rerere` (Reuse Recorded Resolution)?](#q85)", "[How does `git bisect` use binary search to locate bug-introducing commits?](#q85)")
new_git_q85 = """<a id="q85"></a>
### Q85: How does `git bisect` use binary search to locate bug-introducing commits?
**Difficulty**: <span class="intermediate">Intermediate</span>  
**Category**: Debugging & History  

**Strategy**: Explain the binary search workflow of git bisect start, good, bad, and run.

`git bisect` performs a binary search between a known good commit and a broken bad commit to find the exact commit that introduced a defect in O(log N) steps.

**Code Example**:
```bash
# Start bisect session
git bisect start
git bisect bad HEAD
git bisect good v1.0.0

# Automated bisect with test script
git bisect run npm test
git bisect reset
```"""
git = re.sub(r'<a id="q85"></a>\s*### Q85:.*?(?=<a id="q86">|$)', new_git_q85 + "\n\n---\n\n", git, flags=re.DOTALL)
with open("markdowns/git/git-questions.md", "w", encoding="utf-8") as f:
    f.write(git)

# 3. LINUX Q94
with open("markdowns/linux/linux-questions.md", "r", encoding="utf-8") as f:
    linux = f.read()
linux = linux.replace("[What is the difference between `/dev/null`, `/dev/zero`, and `/dev/random` in Linux?](#q94)", "[How do `cgroups` (control groups) limit memory and CPU resources in Linux?](#q94)")
new_linux_q94 = """<a id="q94"></a>
### Q94: How do `cgroups` (control groups) limit memory and CPU resources in Linux?
**Difficulty**: <span class="advanced">Advanced</span>  
**Category**: Kernel & Resource Management  

**Strategy**: Explain how cgroups v2 allocates hardware boundaries to process hierarchies.

Control Groups (`cgroups`) are a Linux kernel feature that organizes processes hierarchically and distributes system resources (CPU, Memory, Disk I/O, Network) according to configured constraints, forming the resource isolation engine of Docker and Kubernetes.

**Code Example**:
```bash
# Creating a memory limit in cgroup v2
mkdir /sys/fs/cgroup/sandbox
echo "500M" > /sys/fs/cgroup/sandbox/memory.max

# Attach current shell process to cgroup
echo $$ > /sys/fs/cgroup/sandbox/cgroup.procs
```"""
linux = re.sub(r'<a id="q94"></a>\s*### Q94:.*?(?=<a id="q95">|$)', new_linux_q94 + "\n\n---\n\n", linux, flags=re.DOTALL)
with open("markdowns/linux/linux-questions.md", "w", encoding="utf-8") as f:
    f.write(linux)

# 4. DESIGN PATTERNS Q25
with open("markdowns/design-patterns/design-patterns-questions.md", "r", encoding="utf-8") as f:
    dp = f.read()
dp = dp.replace("[What is the Visitor Pattern?](#q25)", "[What is the Interpreter Pattern?](#q25)")
new_dp_q25 = """<a id="q25"></a>
### Q25: What is the Interpreter Pattern?
**Difficulty**: <span class="advanced">Advanced</span>  
**Category**: Behavioral Patterns  

**Strategy**: Explain grammar definition, Abstract Syntax Tree representation, and evaluation.

The Interpreter Pattern defines a grammatical representation for a language and an interpreter that uses the representation to parse and evaluate sentences or mathematical expressions in the language.

**Code Example**:
```typescript
interface Expression {
  interpret(): number;
}

class NumberExpression implements Expression {
  constructor(private value: number) {}
  interpret(): number { return this.value; }
}

class AddExpression implements Expression {
  constructor(private left: Expression, private right: Expression) {}
  interpret(): number {
    return this.left.interpret() + this.right.interpret();
  }
}

// 5 + 10
const expr = new AddExpression(new NumberExpression(5), new NumberExpression(10));
console.log(expr.interpret()); // 15
```"""
dp = re.sub(r'<a id="q25"></a>\s*### Q25:.*?(?=<a id="q26">|$)', new_dp_q25 + "\n\n---\n\n", dp, flags=re.DOTALL)
with open("markdowns/design-patterns/design-patterns-questions.md", "w", encoding="utf-8") as f:
    f.write(dp)

print("4 specific dupes replaced.")
