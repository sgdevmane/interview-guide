import os
import re

# 1. GIT Q85 -> git worktree
with open("markdowns/git/git-questions.md", "r", encoding="utf-8") as f:
    git = f.read()
git = git.replace("[How does `git bisect` use binary search to locate bug-introducing commits?](#q85)", "[What is `git worktree` and how does it allow working on multiple branches simultaneously?](#q85)")
new_git_q85 = """<a id="q85"></a>
### Q85: What is `git worktree` and how does it allow working on multiple branches simultaneously?
**Difficulty**: <span class="advanced">Advanced</span>  
**Category**: Branching & Worktrees  

**Strategy**: Explain how git worktree checks out multiple branches to different directories without cloning the repository again.

`git worktree` allows having multiple working trees attached to the same repository, enabling you to work on hotfixes or feature branches concurrently in separate directories without switching branches or stashing.

**Code Example**:
```bash
# Add a new worktree in a separate directory
git worktree add ../hotfix-branch hotfix

# List active worktrees
git worktree list

# Remove worktree when done
git worktree remove ../hotfix-branch
```"""
git = re.sub(r'<a id="q85"></a>\s*### Q85:.*?(?=<a id="q86">|$)', new_git_q85 + "\n\n---\n\n", git, flags=re.DOTALL)
with open("markdowns/git/git-questions.md", "w", encoding="utf-8") as f:
    f.write(git)

# 2. LINUX Q94 -> hard vs soft links
with open("markdowns/linux/linux-questions.md", "r", encoding="utf-8") as f:
    linux = f.read()
linux = linux.replace("[How do `cgroups` (control groups) limit memory and CPU resources in Linux?](#q94)", "[What is the difference between Hard Links and Soft (Symbolic) Links in Linux?](#q94)")
new_linux_q94 = """<a id="q94"></a>
### Q94: What is the difference between Hard Links and Soft (Symbolic) Links in Linux?
**Difficulty**: <span class="intermediate">Intermediate</span>  
**Category**: Filesystem & Inodes  

**Strategy**: Explain inode references, filesystem boundaries, and behavior when original file is deleted.

- **Hard Link**: Direct pointer to the file's underlying inode. Shares the exact same inode number; remains valid even if the original filename is deleted; cannot span across different filesystems or link directories.
- **Soft Link (Symlink)**: Special file containing a pathname reference to another file with its own unique inode. Breaks if the target file is moved or deleted; can span across filesystems and link directories.

**Code Example**:
```bash
# Create a hard link
ln original.txt hardlink.txt

# Create a soft link (symlink)
ln -s original.txt symlink.txt

# Inspect inodes
ls -li original.txt hardlink.txt symlink.txt
```"""
linux = re.sub(r'<a id="q94"></a>\s*### Q94:.*?(?=<a id="q95">|$)', new_linux_q94 + "\n\n---\n\n", linux, flags=re.DOTALL)
with open("markdowns/linux/linux-questions.md", "w", encoding="utf-8") as f:
    f.write(linux)

# 3. DESIGN PATTERNS Q25 -> State Pattern
with open("markdowns/design-patterns/design-patterns-questions.md", "r", encoding="utf-8") as f:
    dp = f.read()
dp = dp.replace("[What is the Interpreter Pattern?](#q25)", "[What is the State Pattern?](#q25)")
new_dp_q25 = """<a id="q25"></a>
### Q25: What is the State Pattern?
**Difficulty**: <span class="intermediate">Intermediate</span>  
**Category**: Behavioral Patterns  

**Strategy**: Explain state encapsulation and dynamic behavior alteration without massive switch/if-else statements.

The State Pattern allows an object to alter its behavior when its internal state changes. The object will appear to change its class by delegating state-specific operations to polymorphic state objects.

**Code Example**:
```typescript
interface State {
  play(player: AudioPlayer): void;
}

class PlayingState implements State {
  play(player: AudioPlayer) {
    console.log("Pausing playback");
    player.setState(new PausedState());
  }
}

class PausedState implements State {
  play(player: AudioPlayer) {
    console.log("Starting playback");
    player.setState(new PlayingState());
  }
}

class AudioPlayer {
  private state: State = new PausedState();
  setState(state: State) { this.state = state; }
  play() { this.state.play(this); }
}
```"""
dp = re.sub(r'<a id="q25"></a>\s*### Q25:.*?(?=<a id="q26">|$)', new_dp_q25 + "\n\n---\n\n", dp, flags=re.DOTALL)
with open("markdowns/design-patterns/design-patterns-questions.md", "w", encoding="utf-8") as f:
    f.write(dp)

print("Final 3 unique questions updated.")
