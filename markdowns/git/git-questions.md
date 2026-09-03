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
26. [How do you find the common ancestor of two branches?](#q26) <span class="intermediate">Intermediate</span>
27. [What is `git bisect run`?](#q27) <span class="advanced">Advanced</span>
28. [How do you list all remote branches?](#q28) <span class="beginner">Beginner</span>
29. [How do you remove a file from the index (staging) but keep it in working directory?](#q29) <span class="beginner">Beginner</span>
30. [What is the `.git` directory?](#q30) <span class="intermediate">Intermediate</span>
31. [How do you view the history of a specific function in a file?](#q31) <span class="advanced">Advanced</span>
32. [What is `git stash apply` vs `git stash pop`?](#q32) <span class="intermediate">Intermediate</span>
33. [How do you search for a string in all commits (history)?](#q33) <span class="advanced">Advanced</span>
34. [How do you show changes in a specific commit?](#q34) <span class="beginner">Beginner</span>
35. [How do you prune remote-tracking branches that no longer exist on remote?](#q35) <span class="intermediate">Intermediate</span>
36. [What is `git rebase --onto`?](#q36) <span class="advanced">Advanced</span>
37. [How do you count the number of commits in a branch?](#q37) <span class="intermediate">Intermediate</span>
38. [How do you rename a remote branch?](#q38) <span class="intermediate">Intermediate</span>
39. [What is `git bundle`?](#q39) <span class="advanced">Advanced</span>
40. [How do you change the URI (URL) for a remote?](#q40) <span class="beginner">Beginner</span>
41. [What is `git shortlog`?](#q41) <span class="intermediate">Intermediate</span>
42. [How do you find the most recent tag?](#q42) <span class="intermediate">Intermediate</span>
43. [How do you stage all deleted files?](#q43) <span class="intermediate">Intermediate</span>
44. [What is `git fsck`?](#q44) <span class="advanced">Advanced</span>
45. [How do you configure global username and email?](#q45) <span class="beginner">Beginner</span>
46. [What is `git rev-parse`?](#q46) <span class="advanced">Advanced</span>
47. [How do you reorder commits?](#q47) <span class="intermediate">Intermediate</span>
48. [How do you create an empty commit?](#q48) <span class="intermediate">Intermediate</span>
49. [How do you backup untracked files?](#q49) <span class="intermediate">Intermediate</span>
50. [How do you see the diff of a stash without popping it?](#q50) <span class="intermediate">Intermediate</span>
51. [How do you create a zip archive of the repository?](#q51) <span class="intermediate">Intermediate</span>
52. [How do you find the author of a specific commit?](#q52) <span class="beginner">Beginner</span>
53. [How do you show the commit history of a file including renames?](#q53) <span class="intermediate">Intermediate</span>
54. [How do you check if a branch is merged into main?](#q54) <span class="intermediate">Intermediate</span>
55. [How do you set up an alias for a complex log graph?](#q55) <span class="intermediate">Intermediate</span>
56. [How do you count lines of code in a repo?](#q56) <span class="intermediate">Intermediate</span>
57. [How do you undo `git add .` (unstage all)?](#q57) <span class="beginner">Beginner</span>
58. [How do you push tags to remote?](#q58) <span class="beginner">Beginner</span>
59. [What is `git status -s`?](#q59) <span class="beginner">Beginner</span>
60. [How do you configure Git Hooks (pre-commit, commit-msg, pre-push) and automate them with Husky?](#q60) <span class="intermediate">Intermediate</span>
61. [How do you copy a file from another branch?](#q61) <span class="intermediate">Intermediate</span>
62. [What is `git clean -n`?](#q62) <span class="beginner">Beginner</span>
63. [How do you revert a merge commit?](#q63) <span class="advanced">Advanced</span>
64. [How do you grep commits by author?](#q64) <span class="intermediate">Intermediate</span>
65. [How do you list files with conflicts?](#q65) <span class="intermediate">Intermediate</span>
66. [How do you show only the file names that changed in a commit?](#q66) <span class="beginner">Beginner</span>
67. [How do you ignore file mode (permission) changes?](#q67) <span class="advanced">Advanced</span>
68. [What is `git fetch --all`?](#q68) <span class="beginner">Beginner</span>
69. [How do you remove a remote?](#q69) <span class="beginner">Beginner</span>
70. [How do you verify what branch `HEAD` points to?](#q70) <span class="beginner">Beginner</span>
71. [How do you apply a patch file?](#q71) <span class="advanced">Advanced</span>
72. [What is `git describe`?](#q72) <span class="intermediate">Intermediate</span>
73. [How do you reset a single file to HEAD?](#q73) <span class="beginner">Beginner</span>
74. [How do you see what you are about to push?](#q74) <span class="intermediate">Intermediate</span>
75. [What is the Reflog?](#q75) <span class="advanced">Advanced</span>
76. [How do you recover a lost commit using `reflog`?](#q76) <span class="advanced">Advanced</span>
77. [How do you automate debugging with `git bisect`?](#q77) <span class="advanced">Advanced</span>
78. [What is `git rerere`?](#q78) <span class="advanced">Advanced</span>
79. [How do you use `git worktree`?](#q79) <span class="advanced">Advanced</span>
80. [Difference between Submodules and Subtrees?](#q80) <span class="advanced">Advanced</span>
81. [How do you bypass pre-commit hooks?](#q81) <span class="intermediate">Intermediate</span>
82. [How do you cherry-pick a range of commits?](#q82) <span class="intermediate">Intermediate</span>
83. [How do you squash commits with interactive rebase?](#q83) <span class="intermediate">Intermediate</span>
84. [How do you sign commits with GPG?](#q84) <span class="advanced">Advanced</span>
85. [How do you ignore whitespace changes in `git blame`?](#q85) <span class="intermediate">Intermediate</span>
86. [How do you clean untracked files (dry run)?](#q86) <span class="beginner">Beginner</span>
87. [Difference between Annotated and Lightweight tags?](#q87) <span class="intermediate">Intermediate</span>
88. [What are Git Notes?](#q88) <span class="advanced">Advanced</span>
89. [How do you remove a file from history (BFG)?](#q89) <span class="advanced">Advanced</span>
90. [What are the 3 Git config scopes?](#q90) <span class="beginner">Beginner</span>
91. [How do you create a Git Bundle?](#q91) <span class="advanced">Advanced</span>
92. [How do you export the repo as a Zip?](#q92) <span class="intermediate">Intermediate</span>
93. [What is the 'patience' diff algorithm?](#q93) <span class="advanced">Advanced</span>
94. [How do you pretty print the git log?](#q94) <span class="intermediate">Intermediate</span>
95. [How do you prune remote tracking branches?](#q95) <span class="intermediate">Intermediate</span>
96. [How do you enforce Fast-Forward only merges?](#q96) <span class="intermediate">Intermediate</span>
97. [What does `git rev-parse` do?](#q97) <span class="advanced">Advanced</span>
98. [Who contributed most lines? (Shortlog)](#q98) <span class="intermediate">Intermediate</span>
99. [How do you verify a GPG signed commit?](#q99) <span class="advanced">Advanced</span>
100. [How do you optimize the local repository?](#q100) <span class="advanced">Advanced</span>

---

<a id="q1"></a>
### Q1: What is the difference between `git merge` and `git rebase`?
**Difficulty**: <span class="intermediate">Intermediate</span>  

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

---

<a id="q2"></a>
### Q2: How do you squash multiple commits into one?
**Difficulty**: <span class="intermediate">Intermediate</span>  

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

---

<a id="q3"></a>
### Q3: How do you find a bug using `git bisect`?
**Difficulty**: <span class="advanced">Advanced</span>  

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

---

<a id="q4"></a>
### Q4: How do you undo the last commit but keep changes?
**Difficulty**: <span class="beginner">Beginner</span>  

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

---

<a id="q5"></a>
### Q5: What is `git cherry-pick`?
**Difficulty**: <span class="intermediate">Intermediate</span>  

**Strategy**:
Cherry-picking allows you to pick a specific commit from one branch and apply it to another, without merging the entire branch. Useful for hotfixes or grabbing a specific feature.

**Code Example**:
```bash
# Apply specific commit (a1b2c3d) to current branch
git cherry-pick a1b2c3d
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q6"></a>
### Q6: What is the difference between `git fetch` and `git pull`?
**Difficulty**: <span class="beginner">Beginner</span>  

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

---

<a id="q7"></a>
### Q7: How do you modify the last commit message?
**Difficulty**: <span class="beginner">Beginner</span>  

**Strategy**:
Use `--amend`. This rewrites the last commit ID, so **never** do this if you have already pushed the commit to a shared branch (unless you force push and warn team).

**Code Example**:
```bash
git commit --amend -m "New correct message"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q8"></a>
### Q8: What is a "Detached HEAD" state?
**Difficulty**: <span class="intermediate">Intermediate</span>  

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

---

<a id="q9"></a>
### Q9: How do you stash specific files only?
**Difficulty**: <span class="advanced">Advanced</span>  

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

---

<a id="q10"></a>
### Q10: What is `git reflog` and when to use it?
**Difficulty**: <span class="advanced">Advanced</span>  

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

---

<a id="q11"></a>
### Q11: Explain Git Flow vs Trunk Based Development?
**Difficulty**: <span class="advanced">Advanced</span>  

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

---

<a id="q12"></a>
### Q12: How do you resolve a merge conflict?
**Difficulty**: <span class="beginner">Beginner</span>  

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

---

<a id="q13"></a>
### Q13: Difference between `git reset` Soft, Mixed, and Hard?
**Difficulty**: <span class="intermediate">Intermediate</span>  

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

---

<a id="q14"></a>
### Q14: How do you revert a public commit safely?
**Difficulty**: <span class="intermediate">Intermediate</span>  

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

---

<a id="q15"></a>
### Q15: How do you stop tracking a file without deleting it?
**Difficulty**: <span class="intermediate">Intermediate</span>  

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

---

<a id="q16"></a>
### Q16: What are Git Hooks?
**Difficulty**: <span class="advanced">Advanced</span>  

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

---

<a id="q17"></a>
### Q17: How do you find who changed a specific line (Blame)?
**Difficulty**: <span class="beginner">Beginner</span>  

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

---

<a id="q18"></a>
### Q18: What is `git switch` vs `git checkout`?
**Difficulty**: <span class="beginner">Beginner</span>  

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

---

<a id="q19"></a>
### Q19: How do you clean untracked files?
**Difficulty**: <span class="intermediate">Intermediate</span>  

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

---

<a id="q20"></a>
### Q20: What is a Fork vs a Branch?
**Difficulty**: <span class="beginner">Beginner</span>  

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

---

<a id="q21"></a>
### Q21: How do you rename a local branch?
**Difficulty**: <span class="beginner">Beginner</span>  

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

---

<a id="q22"></a>
### Q22: How do you sync a fork with the original repo (upstream)?
**Difficulty**: <span class="intermediate">Intermediate</span>  

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

---

<a id="q23"></a>
### Q23: What is `git diff` vs `git diff --staged`?
**Difficulty**: <span class="beginner">Beginner</span>  

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

---

<a id="q24"></a>
### Q24: How do you tag a specific commit?
**Difficulty**: <span class="beginner">Beginner</span>  

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

---

<a id="q25"></a>
### Q25: What is `git submodule`?
**Difficulty**: <span class="advanced">Advanced</span>  

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

---

<a id="q26"></a>
### Q26: How do you find the common ancestor of two branches?
**Difficulty**: <span class="intermediate">Intermediate</span>  

**Strategy:**
Use `git merge-base branch1 branch2`. It outputs the commit hash of the best common ancestor.

**Code Example:**

```bash
git merge-base main feature
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q27"></a>
### Q27: What is `git bisect run`?
**Difficulty**: <span class="advanced">Advanced</span>  

**Strategy:**
It automates the binary search process to find a bug. You provide a script that returns 0 for good and non-zero for bad. Git runs this script on each checked-out commit.

**Code Example:**

```bash
git bisect start HEAD v1.0
git bisect run npm test
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q28"></a>
### Q28: How do you list all remote branches?
**Difficulty**: <span class="beginner">Beginner</span>  

**Strategy:**
Use `git branch -r` or `git branch -a` (all).

**Code Example:**

```bash
git branch -r
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q29"></a>
### Q29: How do you remove a file from the index (staging) but keep it in working directory?
**Difficulty**: <span class="beginner">Beginner</span>  

**Strategy:**
Use `git reset HEAD <file>` (old way) or `git restore --staged <file>` (new way).

**Code Example:**

```bash
git restore --staged file.txt
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q30"></a>
### Q30: What is the `.git` directory?
**Difficulty**: <span class="intermediate">Intermediate</span>  

**Strategy:**
It contains all the metadata for the repository: objects (commits, trees, blobs), refs (heads, tags), configuration, and hooks.

**Code Example:**

```bash
ls .git
# objects/ refs/ config HEAD ...
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q31"></a>
### Q31: How do you view the history of a specific function in a file?
**Difficulty**: <span class="advanced">Advanced</span>  

**Strategy:**
Use `git log -L :funcname:filename`. This traces the evolution of a specific function block.

**Code Example:**

```bash
git log -L :myFunction:main.js
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q32"></a>
### Q32: What is `git stash apply` vs `git stash pop`?
**Difficulty**: <span class="intermediate">Intermediate</span>  

**Strategy:**
`pop` applies the stash and removes it from the stash list. `apply` applies it but keeps it in the list (useful if you want to apply it to multiple branches).

**Code Example:**

```bash
git stash apply
# stash@{0} still exists
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q33"></a>
### Q33: How do you search for a string in all commits (history)?
**Difficulty**: <span class="advanced">Advanced</span>  

**Strategy:**
Use `git grep <text> $(git rev-list --all)` or `git log -S <text>`. `git grep` searches content, `git log -S` searches for diffs adding/removing the text (pickaxe).

**Code Example:**

```bash
git log -S "password123"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q34"></a>
### Q34: How do you show changes in a specific commit?
**Difficulty**: <span class="beginner">Beginner</span>  

**Strategy:**
Use `git show <commit-hash>`.

**Code Example:**

```bash
git show a1b2c3d
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q35"></a>
### Q35: How do you prune remote-tracking branches that no longer exist on remote?
**Difficulty**: <span class="intermediate">Intermediate</span>  

**Strategy:**
Use `git fetch --prune` (or `-p`). This cleans up `origin/deleted-branch` references locally.

**Code Example:**

```bash
git fetch -p
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q36"></a>
### Q36: What is `git rebase --onto`?
**Difficulty**: <span class="advanced">Advanced</span>  

**Strategy:**
Used for advanced rebasing, like transplanting a sub-branch to a new base. `git rebase --onto newbase oldbase branch`.

**Code Example:**

```bash
# Move feature branch from old-main to new-main
git rebase --onto new-main old-main feature
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q37"></a>
### Q37: How do you count the number of commits in a branch?
**Difficulty**: <span class="intermediate">Intermediate</span>  

**Strategy:**
Use `git rev-list --count <branch>`.

**Code Example:**

```bash
git rev-list --count HEAD
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q38"></a>
### Q38: How do you rename a remote branch?
**Difficulty**: <span class="intermediate">Intermediate</span>  

**Strategy:**

1. Rename local branch. 2. Push new name. 3. Delete old remote name.

**Code Example:**

```bash
git branch -m old new
git push origin -u new
git push origin --delete old
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q39"></a>
### Q39: What is `git bundle`?
**Difficulty**: <span class="advanced">Advanced</span>  

**Strategy:**
It packages objects and references into a single archive file. Useful for transferring git data via offline means (USB drive).

**Code Example:**

```bash
git bundle create repo.bundle --all
git clone repo.bundle
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q40"></a>
### Q40: How do you change the URI (URL) for a remote?
**Difficulty**: <span class="beginner">Beginner</span>  

**Strategy:**
Use `git remote set-url origin <new-url>`.

**Code Example:**

```bash
git remote set-url origin git@github.com:user/repo.git
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q41"></a>
### Q41: What is `git shortlog`?
**Difficulty**: <span class="intermediate">Intermediate</span>  

**Strategy:**
Summarizes `git log` output. Useful for generating release notes or checking contributor stats (`-sn`).

**Code Example:**

```bash
git shortlog -sn
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q42"></a>
### Q42: How do you find the most recent tag?
**Difficulty**: <span class="intermediate">Intermediate</span>  

**Strategy:**
Use `git describe --tags`.

**Code Example:**

```bash
git describe --tags
# v1.0-4-g12345 (4 commits after v1.0)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q43"></a>
### Q43: How do you stage all deleted files?
**Difficulty**: <span class="intermediate">Intermediate</span>  

**Strategy:**
`git add -u` stages modifications and deletions, but not new files.

**Code Example:**

```bash
git add -u
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q44"></a>
### Q44: What is `git fsck`?
**Difficulty**: <span class="advanced">Advanced</span>  

**Strategy:**
"File System Check". Verifies the connectivity and validity of the objects in the database. Can find dangling objects (commits not reachable by any ref).

**Code Example:**

```bash
git fsck --lost-found
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q45"></a>
### Q45: How do you configure global username and email?
**Difficulty**: <span class="beginner">Beginner</span>  

**Strategy:**
Use `git config --global user.name` and `user.email`.

**Code Example:**

```bash
git config --global user.name "John Doe"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q46"></a>
### Q46: What is `git rev-parse`?
**Difficulty**: <span class="advanced">Advanced</span>  

**Strategy:**
An internal command (plumbing) used to parse revision specifications, flags, and retrieve internal details (like absolute path of .git dir).

**Code Example:**

```bash
git rev-parse --show-toplevel
# /path/to/repo/root
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q47"></a>
### Q47: How do you reorder commits?
**Difficulty**: <span class="intermediate">Intermediate</span>  

**Strategy:**
Use interactive rebase (`git rebase -i`). In the editor, rearrange the lines of commits.

**Code Example:**

```bash
git rebase -i HEAD~3
# Swap lines 1 and 2
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q48"></a>
### Q48: How do you create an empty commit?
**Difficulty**: <span class="intermediate">Intermediate</span>  

**Strategy:**
Use `git commit --allow-empty`. Useful for triggering CI pipelines without changing code.

**Code Example:**

```bash
git commit --allow-empty -m "Trigger build"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q49"></a>
### Q49: How do you backup untracked files?
**Difficulty**: <span class="intermediate">Intermediate</span>  

**Strategy:**
You can stash them with `git stash -u` (include untracked).

**Code Example:**

```bash
git stash -u
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q50"></a>
### Q50: How do you see the diff of a stash without popping it?
**Difficulty**: <span class="intermediate">Intermediate</span>  

**Strategy:**
Use `git stash show -p stash@{0}`.

**Code Example:**

```bash
git stash show -p
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q51"></a>
### Q51: How do you create a zip archive of the repository?
**Difficulty**: <span class="intermediate">Intermediate</span>  

**Strategy:**
Use `git archive`. It creates an archive of the specified tree (branch, tag) without the `.git` folder.

**Code Example:**

```bash
git archive --format=zip --output=v1.0.zip HEAD
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q52"></a>
### Q52: How do you find the author of a specific commit?
**Difficulty**: <span class="beginner">Beginner</span>  

**Strategy:**
Use `git show -s --format='%an' <commit>`.

**Code Example:**

```bash
git show -s --format='%an' HEAD
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q53"></a>
### Q53: How do you show the commit history of a file including renames?
**Difficulty**: <span class="intermediate">Intermediate</span>  

**Strategy:**
Use `git log --follow <file>`. This tracks the file across renames.

**Code Example:**

```bash
git log --follow src/main.js
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q54"></a>
### Q54: How do you check if a branch is merged into main?
**Difficulty**: <span class="intermediate">Intermediate</span>  

**Strategy:**
Use `git branch --merged main`. If your branch appears in the list, it is merged.

**Code Example:**

```bash
git branch --merged main
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q55"></a>
### Q55: How do you set up an alias for a complex log graph?
**Difficulty**: <span class="intermediate">Intermediate</span>  

**Strategy:**
Use `git config`.

**Code Example:**

```bash
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q56"></a>
### Q56: How do you count lines of code in a repo?
**Difficulty**: <span class="intermediate">Intermediate</span>  

**Strategy:**
Use `git ls-files` piped to `xargs wc -l`.

**Code Example:**

```bash
git ls-files | xargs wc -l
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q57"></a>
### Q57: How do you undo `git add .` (unstage all)?
**Difficulty**: <span class="beginner">Beginner</span>  

**Strategy:**
Use `git reset` (defaults to mixed reset, unstage everything but keep changes). Or `git restore --staged .`.

**Code Example:**

```bash
git reset
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q58"></a>
### Q58: How do you push tags to remote?
**Difficulty**: <span class="beginner">Beginner</span>  

**Strategy:**
`git push` does not push tags by default. Use `git push origin <tagname>` or `git push origin --tags`.

**Code Example:**

```bash
git push origin --tags
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q59"></a>
### Q59: What is `git status -s`?
**Difficulty**: <span class="beginner">Beginner</span>  

**Strategy:**
Short format status. Less verbose than standard `git status`.

**Code Example:**

```bash
git status -s
# M  file.js (modified)
# ?? new.js (untracked)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q60"></a>
### Q60: How do you configure Git Hooks (pre-commit, commit-msg, pre-push) and automate them with Husky?
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
```

---

---

<a id="q61"></a>
### Q61: How do you copy a file from another branch?
**Difficulty**: <span class="intermediate">Intermediate</span>  

**Strategy:**
Use `git checkout branch -- file`.

**Code Example:**

```bash
git checkout main -- src/utils.js
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q62"></a>
### Q62: What is `git clean -n`?
**Difficulty**: <span class="beginner">Beginner</span>  

**Strategy:**
Dry run. Shows what files *would* be removed by `git clean` without actually deleting them. Always do this before `-f`.

**Code Example:**

```bash
git clean -n
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q63"></a>
### Q63: How do you revert a merge commit?
**Difficulty**: <span class="advanced">Advanced</span>  

**Strategy:**
Use `git revert -m 1 <merge-commit>`. You must specify the parent number (`-m 1` usually main) to revert to.

**Code Example:**

```bash
git revert -m 1 abc1234
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q64"></a>
### Q64: How do you grep commits by author?
**Difficulty**: <span class="intermediate">Intermediate</span>  

**Strategy:**
Use `git log --author="Name"`.

**Code Example:**

```bash
git log --author="Alice"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q65"></a>
### Q65: How do you list files with conflicts?
**Difficulty**: <span class="intermediate">Intermediate</span>  

**Strategy:**
Use `git diff --name-only --diff-filter=U`.

**Code Example:**

```bash
git diff --name-only --diff-filter=U
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q66"></a>
### Q66: How do you show only the file names that changed in a commit?
**Difficulty**: <span class="beginner">Beginner</span>  

**Strategy:**
Use `git show --name-only <commit>`.

**Code Example:**

```bash
git show --name-only HEAD
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q67"></a>
### Q67: How do you ignore file mode (permission) changes?
**Difficulty**: <span class="advanced">Advanced</span>  

**Strategy:**
Set `core.fileMode` to false in config.

**Code Example:**

```bash
git config core.fileMode false
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q68"></a>
### Q68: What is `git fetch --all`?
**Difficulty**: <span class="beginner">Beginner</span>  

**Strategy:**
Fetches the latest changes from all configured remotes.

**Code Example:**

```bash
git fetch --all
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q69"></a>
### Q69: How do you remove a remote?
**Difficulty**: <span class="beginner">Beginner</span>  

**Strategy:**
Use `git remote remove <name>`.

**Code Example:**

```bash
git remote remove origin
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q70"></a>
### Q70: How do you verify what branch `HEAD` points to?
**Difficulty**: <span class="beginner">Beginner</span>  

**Strategy:**
Use `git symbolic-ref --short HEAD` or just `git branch --show-current`.

**Code Example:**

```bash
git branch --show-current
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q71"></a>
### Q71: How do you apply a patch file?
**Difficulty**: <span class="advanced">Advanced</span>  

**Strategy:**
Use `git apply <file.patch>`.

**Code Example:**

```bash
git apply fix.patch
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q72"></a>
### Q72: What is `git describe`?
**Difficulty**: <span class="intermediate">Intermediate</span>  

**Strategy:**
Finds the most recent tag that is reachable from a commit. Used to generate build version strings.

**Code Example:**

```bash
git describe --long
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q73"></a>
### Q73: How do you reset a single file to HEAD?
**Difficulty**: <span class="beginner">Beginner</span>  

**Strategy:**
Use `git checkout HEAD -- <file>` or `git restore <file>`.

**Code Example:**

```bash
git restore config.json
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q74"></a>
### Q74: How do you see what you are about to push?
**Difficulty**: <span class="intermediate">Intermediate</span>  

**Strategy:**
Use `git diff origin/main..HEAD` (assuming pushing to main) or `git log origin/main..HEAD`.

**Code Example:**

```bash
git log origin/main..HEAD
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q75"></a>
### Q75: What is the Reflog?
**Difficulty**: <span class="advanced">Advanced</span>  

**Strategy:**
A local log of where HEAD and branch references have been. It allows you to recover lost commits that are not referenced by any branch (e.g., after a bad rebase).

**Code Example:**

```bash
git reflog
git reset --hard HEAD@{1}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q76"></a>
### Q76: How do you recover a lost commit using `reflog`?
**Difficulty**: <span class="advanced">Advanced</span>  

**Strategy**: `git reflog` records updates to the tip of branches. If you accidentally reset --hard or deleted a branch, you can find the commit hash in the reflog and checkout or reset to it.

**Code Example**: 
```bash
git reflog
# Find the SHA, e.g., abc1234
git checkout -b recovered-branch abc1234
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q77"></a>
### Q77: How do you automate debugging with `git bisect`?
**Difficulty**: <span class="advanced">Advanced</span>  

**Strategy**: `git bisect run` automates the binary search. You provide a script that returns exit code 0 (good) or 1 (bad), and git runs it on every step until it finds the culprit.

**Code Example**: 
```bash
git bisect start HEAD v1.0
git bisect run npm test
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q78"></a>
### Q78: What is `git rerere`?
**Difficulty**: <span class="advanced">Advanced</span>  

**Strategy**: "Reuse Recorded Resolution". It remembers how you resolved a hunk conflict so that the next time it sees the same conflict, it resolves it automatically.

**Code Example**: 
```bash
git config --global rerere.enabled true
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q79"></a>
### Q79: How do you use `git worktree`?
**Difficulty**: <span class="advanced">Advanced</span>  

**Strategy**: Allows you to check out multiple branches at once in separate directories, linked to the same repository. Useful for running long tests on one branch while working on another.

**Code Example**: 
```bash
git worktree add ../hotfix-folder hotfix-branch
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q80"></a>
### Q80: Difference between Submodules and Subtrees?
**Difficulty**: <span class="advanced">Advanced</span>  

**Strategy**: **Submodules**: Separate repo links. Complex to manage, requires explicit updates. 
**Subtrees**: Copies source code into your repo. Easier for users of the repo, harder to contribute back.

**Code Example**: 
```bash
# Submodule
git submodule add https://github.com/libs/lib.git
# Subtree
git subtree add --prefix=lib https://github.com/libs/lib.git main --squash
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q81"></a>
### Q81: How do you bypass pre-commit hooks?
**Difficulty**: <span class="intermediate">Intermediate</span>  

**Strategy**: Use the `--no-verify` (or `-n`) flag. Use with caution, only when you know the hook is failing incorrectly or you have a valid reason.

**Code Example**: 
```bash
git commit -m "WIP" --no-verify
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q82"></a>
### Q82: How do you cherry-pick a range of commits?
**Difficulty**: <span class="intermediate">Intermediate</span>  

**Strategy**: Use `A..B` syntax where A is the parent of the first commit you want, and B is the last commit.

**Code Example**: 
```bash
git cherry-pick A..B
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q83"></a>
### Q83: How do you squash commits with interactive rebase?
**Difficulty**: <span class="intermediate">Intermediate</span>  

**Strategy**: Run `git rebase -i HEAD~N`. Change `pick` to `squash` (or `s`) for the commits you want to merge into the previous one.

**Code Example**: 
```bash
git rebase -i HEAD~3
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q84"></a>
### Q84: How do you sign commits with GPG?
**Difficulty**: <span class="advanced">Advanced</span>  

**Strategy**: Configure your GPG key in git config and use the `-S` flag during commit. GitHub marks these as "Verified".

**Code Example**: 
```bash
git config --global user.signingkey <KEYID>
git commit -S -m "Signed commit"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q85"></a>
### Q85: How do you ignore whitespace changes in `git blame`?
**Difficulty**: <span class="intermediate">Intermediate</span>  

**Strategy**: Use the `-w` flag. This is helpful to see the original author of a line even after re-indentation.

**Code Example**: 
```bash
git blame -w src/app.js
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q86"></a>
### Q86: How do you clean untracked files (dry run)?
**Difficulty**: <span class="beginner">Beginner</span>  

**Strategy**: Use `git clean -n` to see what would be deleted. Use `-f` to actually delete, `-d` for directories.

**Code Example**: 
```bash
git clean -n -d
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q87"></a>
### Q87: Difference between Annotated and Lightweight tags?
**Difficulty**: <span class="intermediate">Intermediate</span>  

**Strategy**: **Lightweight**: Just a pointer to a commit (like a branch that doesn't move). 
**Annotated**: Stored as a full object, contains tagger name, email, date, message. Recommended for releases.

**Code Example**: 
```bash
# Annotated
git tag -a v1.0 -m "Release 1.0"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q88"></a>
### Q88: What are Git Notes?
**Difficulty**: <span class="advanced">Advanced</span>  

**Strategy**: Git Notes allow you to add metadata to commits without changing the commit SHA (unlike amending). Useful for automated systems to attach build statuses or comments.

**Code Example**: 
```bash
git notes add -m "Build passed" <commit-hash>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q89"></a>
### Q89: How do you remove a file from history (BFG)?
**Difficulty**: <span class="advanced">Advanced</span>  

**Strategy**: Use `git filter-repo` (modern replacement for `filter-branch`) or BFG Repo-Cleaner to remove large files or secrets from all commits.

**Code Example**: 
```bash
bfg --delete-files id_rsa
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q90"></a>
### Q90: What are the 3 Git config scopes?
**Difficulty**: <span class="beginner">Beginner</span>  

**Strategy**: 1. **System** (`/etc/gitconfig`): All users. 
2. **Global** (`~/.gitconfig`): Current user. 
3. **Local** (`.git/config`): Current repository.

**Code Example**: 
```bash
git config --global user.name "John"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q91"></a>
### Q91: How do you create a Git Bundle?
**Difficulty**: <span class="advanced">Advanced</span>  

**Strategy**: Bundles archive the repo into a single file that acts like a remote. Useful for offline transfer.

**Code Example**: 
```bash
git bundle create repo.bundle master
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q92"></a>
### Q92: How do you export the repo as a Zip?
**Difficulty**: <span class="intermediate">Intermediate</span>  

**Strategy**: Use `git archive`. It ignores the `.git` folder.

**Code Example**: 
```bash
git archive --format=zip HEAD > source.zip
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q93"></a>
### Q93: What is the 'patience' diff algorithm?
**Difficulty**: <span class="advanced">Advanced</span>  

**Strategy**: It tries to match large blocks of code, providing more readable diffs when code has moved significantly.

**Code Example**: 
```bash
git diff --patience
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q94"></a>
### Q94: How do you pretty print the git log?
**Difficulty**: <span class="intermediate">Intermediate</span>  

**Strategy**: Use format placeholders like `%h` (hash), `%an` (author), `%s` (subject).

**Code Example**: 
```bash
git log --pretty=format:"%h - %an, %ar : %s"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q95"></a>
### Q95: How do you prune remote tracking branches?
**Difficulty**: <span class="intermediate">Intermediate</span>  

**Strategy**: Use `git fetch --prune` or `git remote prune origin`. Deletes local references to branches that no longer exist on the remote.

**Code Example**: 
```bash
git fetch -p
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q96"></a>
### Q96: How do you enforce Fast-Forward only merges?
**Difficulty**: <span class="intermediate">Intermediate</span>  

**Strategy**: Use `--ff-only`. The merge will fail if it requires a merge commit.

**Code Example**: 
```bash
git merge --ff-only feature-branch
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q97"></a>
### Q97: What does `git rev-parse` do?
**Difficulty**: <span class="advanced">Advanced</span>  

**Strategy**: It's a plumbing command used to parse revision parameters and return the absolute commit hash or paths. Often used in scripts.

**Code Example**: 
```bash
git rev-parse --short HEAD
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q98"></a>
### Q98: Who contributed most lines? (Shortlog)
**Difficulty**: <span class="intermediate">Intermediate</span>  

**Strategy**: `git shortlog` summarizes the git log output. `-s` for summary, `-n` to sort by number.

**Code Example**: 
```bash
git shortlog -sn
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q99"></a>
### Q99: How do you verify a GPG signed commit?
**Difficulty**: <span class="advanced">Advanced</span>  

**Strategy**: Use `git verify-commit <hash>` or enable signature display in log with `--show-signature`.

**Code Example**: 
```bash
git log --show-signature
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

---

<a id="q100"></a>
### Q100: How do you optimize the local repository?
**Difficulty**: <span class="advanced">Advanced</span>  

**Strategy**: Use `git maintenance start` (new) or `git gc` (garbage collect) to pack refs, prune loose objects, and optimize performance.

**Code Example**: 
```bash
git gc --aggressive
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---
