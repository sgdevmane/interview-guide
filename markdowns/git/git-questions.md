<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/git-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Git Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [What is the difference between `git merge` and `git rebase`?](#q1) <span class="intermediate">Intermediate</span>
2. [How do you squash multiple commits into one?](#q2) <span class="intermediate">Intermediate</span>
3. [How do you find a bug using `git bisect`?](#q3) <span class="advanced">Advanced</span>
4. [How do you undo the last commit but keep changes?](#q4) <span class="beginner">Beginner</span>
5. [What is `git cherry-pick`?](#q5) <span class="intermediate">Intermediate</span>
6. [What is the difference between `git fetch` and `git pull`?](#q6) <span class="beginner">Beginner</span>
7. [How do you modify the last commit message?](#q7) <span class="beginner">Beginner</span>
8. [What is a "Detached HEAD" state?](#q8) <span class="intermediate">Intermediate</span>
9. [How do you stash specific files only?](#q9) <span class="advanced">Advanced</span>
10. [What is `git reflog` and when to use it?](#q10) <span class="advanced">Advanced</span>
11. [Explain Git Flow vs Trunk Based Development?](#q11) <span class="advanced">Advanced</span>
12. [How do you resolve a merge conflict?](#q12) <span class="beginner">Beginner</span>
13. [Difference between `git reset` Soft, Mixed, and Hard?](#q13) <span class="intermediate">Intermediate</span>
14. [How do you revert a public commit safely?](#q14) <span class="intermediate">Intermediate</span>
15. [How do you stop tracking a file without deleting it?](#q15) <span class="intermediate">Intermediate</span>
16. [What are Git Hooks?](#q16) <span class="advanced">Advanced</span>
17. [How do you find who changed a specific line (Blame)?](#q17) <span class="beginner">Beginner</span>
18. [What is `git switch` vs `git checkout`?](#q18) <span class="beginner">Beginner</span>
19. [How do you clean untracked files?](#q19) <span class="intermediate">Intermediate</span>
20. [What is a Fork vs a Branch?](#q20) <span class="beginner">Beginner</span>
21. [How do you rename a local branch?](#q21) <span class="beginner">Beginner</span>
22. [How do you sync a fork with the original repo (upstream)?](#q22) <span class="intermediate">Intermediate</span>
23. [What is `git diff` vs `git diff --staged`?](#q23) <span class="beginner">Beginner</span>
24. [How do you tag a specific commit?](#q24) <span class="beginner">Beginner</span>
25. [What is `git submodule`?](#q25) <span class="advanced">Advanced</span>

---

<a id="q1"></a>
### Q1: What is the difference between `git merge` and `git rebase`?

**Difficulty**: Intermediate

**Strategy**:
Both integrate changes from one branch into another, but they do it differently.
*   **Merge:** Creates a new "Merge Commit" tying the two histories together. Preserves the exact history of events. Non-destructive. Safe for shared branches.
*   **Rebase:** Moves the entire feature branch to begin on the tip of the main branch. Rewrites history to create a linear progression. Cleaner history but dangerous on shared branches (can overwrite others' work).

**Code Example**:
```bash
# Merge feature into main
git checkout main
git merge feature

# Rebase feature onto main
git checkout feature
git rebase main
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q2"></a>
### Q2: How do you squash multiple commits into one?

**Difficulty**: Intermediate

**Strategy**:
Squashing cleans up history by combining multiple small "WIP" commits into a single meaningful commit before merging.
*   **Interactive Rebase:** The standard way to squash.
*   **Merge Squash:** Squashes all commits when merging into target.

**Code Example**:
```bash
# Interactive rebase of last 3 commits
git rebase -i HEAD~3

# In the editor, change 'pick' to 'squash' (or 's') for the commits you want to merge into the previous one.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q3"></a>
### Q3: How do you find a bug using `git bisect`?

**Difficulty**: Advanced

**Strategy**:
`git bisect` performs a binary search on the commit history to identify exactly which commit introduced a bug. It's extremely fast for finding regressions in large histories.

**Code Example**:
```bash
git bisect start
git bisect bad            # Current version is broken
git bisect good v1.0.0    # Version 1.0.0 was working

# Git checks out a middle commit. You test it.
git bisect good           # If this version works
# Git checks out the next half... repeat until found.

git bisect reset          # Finish
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q4"></a>
### Q4: How do you undo the last commit but keep changes?

**Difficulty**: Beginner

**Strategy**:
Use `git reset`.
*   **Soft:** Moves HEAD back, keeps changes in Staging (Index). Good for fixing a commit.
*   **Mixed (Default):** Moves HEAD back, keeps changes in Working Directory (Unstaged).
*   **Hard:** Moves HEAD back, DESTROYS changes.

**Code Example**:
```bash
# Undo commit, keep changes staged
git reset --soft HEAD~1

# Undo commit, keep changes unstaged
git reset HEAD~1
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q5"></a>
### Q5: What is `git cherry-pick`?

**Difficulty**: Intermediate

**Strategy**:
Cherry-picking allows you to pick a specific commit from one branch and apply it to another, without merging the entire branch. Useful for hotfixes or grabbing a specific feature.

**Code Example**:
```bash
# Apply specific commit (a1b2c3d) to current branch
git cherry-pick a1b2c3d
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q6"></a>
### Q6: What is the difference between `git fetch` and `git pull`?

**Difficulty**: Beginner

**Strategy**:
*   **`git fetch`:** Downloads commits, files, and refs from a remote repository into your local repo. It does **NOT** merge them into your working files. It updates `origin/main`. Safe to run anytime.
*   **`git pull`:** Downloads changes AND merges them into your current branch. Essentially `git fetch` + `git merge`.

**Code Example**:
```bash
# Download changes only
git fetch origin

# Download and Merge
git pull origin main
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q7"></a>
### Q7: How do you modify the last commit message?

**Difficulty**: Beginner

**Strategy**:
Use `--amend`. This rewrites the last commit ID, so **never** do this if you have already pushed the commit to a shared branch (unless you force push and warn team).

**Code Example**:
```bash
git commit --amend -m "New correct message"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q8"></a>
### Q8: What is a "Detached HEAD" state?

**Difficulty**: Intermediate

**Strategy**:
Normally, HEAD points to a Branch name (e.g., main). If you checkout a specific Commit ID (or Tag), HEAD points directly to that commit. You are in "Detached HEAD" state.
*   **Risk:** If you make commits here, they belong to no branch. If you checkout another branch, these commits will be lost (garbage collected).
*   **Fix:** Create a branch if you want to save changes.

**Code Example**:
```bash
# Checkout a specific commit (Detached HEAD)
git checkout a1b2c3d

# Save these changes to a new branch
git checkout -b new-feature-branch
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q9"></a>
### Q9: How do you stash specific files only?

**Difficulty**: Advanced

**Strategy**:
`git stash` saves dirty changes to a temporary area (stack) and cleans the working directory. By default, it stashes everything.
*   Use `push -p` (patch) to interactively select hunks.
*   Use `push path/to/file` to stash specific files.

**Code Example**:
```bash
# Stash only specific file
git stash push -m "config changes" config.json

# List stashes
git stash list

# Apply stash
git stash pop
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q10"></a>
### Q10: What is `git reflog` and when to use it?

**Difficulty**: Advanced

**Strategy**:
**Reflog (Reference Logs)** records *every* update to the tip of branches (HEAD changes). This includes commits, resets, merges, and even amends.
*   **Use Case:** Recovering "lost" commits after a bad `git reset --hard` or a bad rebase. As long as it was in the reflog recently (default 90 days), it can be recovered.

**Code Example**:
```bash
# View history of HEAD movements
git reflog

# Reset to a state before the mistake (e.g., 5 moves ago)
git reset --hard HEAD@{5}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q11"></a>
### Q11: Explain Git Flow vs Trunk Based Development?

**Difficulty**: Advanced

**Strategy**:
*   **Git Flow:** Strict branching model. `main` (prod), `develop` (integration), `feature/*`, `release/*`, `hotfix/*`. Good for scheduled releases. Complexity is high.
*   **Trunk Based:** Developers commit directly to `main` (or short-lived branches merged daily). Uses Feature Flags to hide unfinished work. Good for CI/CD and fast iteration.

**Code Example**:
```bash
# Git Flow Init
git flow init
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q12"></a>
### Q12: How do you resolve a merge conflict?

**Difficulty**: Beginner

**Strategy**:
1.  Git pauses merge and marks conflicted files.
2.  Open files, look for markers `<<<<<<<` (Current Change), `=======`, `>>>>>>>` (Incoming Change).
3.  Edit file to keep desired code. Remove markers.
4.  `git add` the file.
5.  `git commit` to finish merge.

**Code Example**:
```bash
# After fixing conflicts manually
git add file.txt
git commit
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q13"></a>
### Q13: Difference between `git reset` Soft, Mixed, and Hard?

**Difficulty**: Intermediate

**Strategy**:
Assume we want to undo the last commit (`HEAD~1`):
*   **--soft:** Uncommits. Changes are left in **Staging**. Ready to commit again.
*   **--mixed (default):** Uncommits. Changes are left in **Working Directory**. Need to `git add` again.
*   **--hard:** Uncommits. Changes are **Deleted**. Files match the state of the previous commit exactly.

**Code Example**:
```bash
# Dangerous: Wipes all uncommitted changes
git reset --hard HEAD
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q14"></a>
### Q14: How do you revert a public commit safely?

**Difficulty**: Intermediate

**Strategy**:
If a commit has already been pushed, do not use `reset` (rewrites history). Use `revert`.
*   `git revert` creates a *new* commit that is the exact opposite of the target commit. It adds to history rather than deleting it.

**Code Example**:
```bash
# Revert specific commit
git revert <commit-hash>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q15"></a>
### Q15: How do you stop tracking a file without deleting it?

**Difficulty**: Intermediate

**Strategy**:
Often used when you accidentally commit a config file or `.env` that should be ignored.
*   `git rm --cached`: Removes from index (staging) but keeps file on disk.
*   Then add to `.gitignore`.

**Code Example**:
```bash
git rm --cached config.env
echo "config.env" >> .gitignore
git commit -m "Stop tracking config"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q16"></a>
### Q16: What are Git Hooks?

**Difficulty**: Advanced

**Strategy**:
Scripts located in `.git/hooks/` that run automatically on specific events.
*   **Client-side:** `pre-commit` (linting), `commit-msg` (format check), `pre-push` (run tests).
*   **Server-side:** `pre-receive` (enforce policy), `post-receive` (deploy).
*   Tools like `husky` make managing hooks easier in JS projects.

**Code Example**:
```bash
# .git/hooks/pre-commit
#!/bin/sh
npm test
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q17"></a>
### Q17: How do you find who changed a specific line (Blame)?

**Difficulty**: Beginner

**Strategy**:
`git blame` annotates each line of a file with the revision, author, and time of the last change. Useful for debugging "why was this added?".

**Code Example**:
```bash
git blame app.js

# Show only lines 10-20
git blame -L 10,20 app.js
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q18"></a>
### Q18: What is `git switch` vs `git checkout`?

**Difficulty**: Beginner

**Strategy**:
`git checkout` is overloaded (switches branches AND restores files). Git 2.23 introduced simpler commands:
*   **`git switch`**: Specifically for changing branches.
*   **`git restore`**: Specifically for restoring files.

**Code Example**:
```bash
# Switch to existing branch
git switch main

# Create and switch
git switch -c new-feature
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q19"></a>
### Q19: How do you clean untracked files?

**Difficulty**: Intermediate

**Strategy**:
`git clean` removes untracked files (files not in git).
*   `-n`: Dry run (show what will be deleted).
*   `-f`: Force delete.
*   `-d`: Include directories.

**Code Example**:
```bash
# Preview deletion
git clean -n -d

# Delete untracked files/folders
git clean -f -d
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q20"></a>
### Q20: What is a Fork vs a Branch?

**Difficulty**: Beginner

**Strategy**:
*   **Branch:** Parallel version of code *within the same repository*. Lightweight.
*   **Fork:** Copy of the *entire repository* under your own account (server-side concept, not Git core). Used for Open Source contributions where you don't have write access to the original repo.

**Code Example**:
```bash
# Clone your fork
git clone https://github.com/me/repo.git
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q21"></a>
### Q21: How do you rename a local branch?

**Difficulty**: Beginner

**Strategy**:
Rename current branch or specific branch.

**Code Example**:
```bash
# Rename current branch
git branch -m new-name

# Rename specific branch
git branch -m old-name new-name
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q22"></a>
### Q22: How do you sync a fork with the original repo (upstream)?

**Difficulty**: Intermediate

**Strategy**:
1.  Add the original repo as a remote named `upstream`.
2.  Fetch upstream.
3.  Merge `upstream/main` into your local `main`.

**Code Example**:
```bash
git remote add upstream https://github.com/original/repo.git
git fetch upstream
git checkout main
git merge upstream/main
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q23"></a>
### Q23: What is `git diff` vs `git diff --staged`?

**Difficulty**: Beginner

**Strategy**:
*   **`git diff`**: Shows changes in Working Directory (unstaged) vs Staging.
*   **`git diff --staged`** (or `--cached`): Shows changes in Staging vs Last Commit.

**Code Example**:
```bash
git diff
git diff --staged
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q24"></a>
### Q24: How do you tag a specific commit?

**Difficulty**: Beginner

**Strategy**:
Tags are immutable refs to specific commits, usually used for releases (v1.0).
*   **Lightweight:** Just a pointer.
*   **Annotated:** Includes message, date, author (stored as full object).

**Code Example**:
```bash
# Lightweight
git tag v1.0

# Annotated
git tag -a v1.1 -m "Release version 1.1"

# Push tags to remote
git push origin --tags
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q25"></a>
### Q25: What is `git submodule`?

**Difficulty**: Advanced

**Strategy**:
Allows keeping another Git repository in a subdirectory of your repository. The submodule tracks a specific commit of the other repo.
*   Useful for shared libraries.
*   Complex to manage (requires separate pull/update).

**Code Example**:
```bash
# Add submodule
git submodule add https://github.com/lib/lib.git

# Clone repo with submodules
git clone --recursive https://github.com/my/app.git
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>
