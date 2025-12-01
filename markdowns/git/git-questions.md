<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Git Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [Merge vs Rebase?](#q1) <span class="intermediate">Intermediate</span>
2. [Squash commits?](#q2) <span class="intermediate">Intermediate</span>
3. [Git Bisect?](#q3) <span class="advanced">Advanced</span>
4. [Undo last commit?](#q4) <span class="beginner">Beginner</span>
5. [Cherry-pick?](#q5) <span class="intermediate">Intermediate</span>
6. [Fetch vs Pull?](#q6) <span class="beginner">Beginner</span>
7. [Amend commit message?](#q7) <span class="beginner">Beginner</span>
8. [Detached HEAD?](#q8) <span class="intermediate">Intermediate</span>
9. [Stash specific files?](#q9) <span class="advanced">Advanced</span>
10. [Reflog?](#q10) <span class="advanced">Advanced</span>
11. [Git Flow vs Trunk?](#q11) <span class="advanced">Advanced</span>
12. [Resolve Conflicts?](#q12) <span class="beginner">Beginner</span>
13. [Reset Hard vs Soft?](#q13) <span class="intermediate">Intermediate</span>
14. [Revert public commit?](#q14) <span class="intermediate">Intermediate</span>
15. [Ignore tracked files?](#q15) <span class="intermediate">Intermediate</span>
16. [Git Hooks?](#q16) <span class="advanced">Advanced</span>
17. [Git Blame?](#q17) <span class="beginner">Beginner</span>
18. [Fork vs Branch?](#q18) <span class="beginner">Beginner</span>
19. [List files in commit?](#q19) <span class="beginner">Beginner</span>
20. [Find common ancestor?](#q20) <span class="intermediate">Intermediate</span>
21. [What is the Staging Area (Index)?](#q21) <span class="beginner">Beginner</span>
22. [Git Config Scopes?](#q22) <span class="beginner">Beginner</span>
23. [Remove untracked files (clean)?](#q23) <span class="intermediate">Intermediate</span>
24. [Git Tags (Lightweight vs Annotated)?](#q24) <span class="intermediate">Intermediate</span>
25. [What is a Submodule?](#q25) <span class="advanced">Advanced</span>
26. [What is a Subtree?](#q26) <span class="advanced">Advanced</span>
27. [Git Worktree?](#q27) <span class="advanced">Advanced</span>
28. [Diff Staged vs Unstaged?](#q28) <span class="beginner">Beginner</span>
29. [Rename a branch?](#q29) <span class="beginner">Beginner</span>
30. [Delete a remote branch?](#q30) <span class="intermediate">Intermediate</span>
31. [Show commit history for one file?](#q31) <span class="beginner">Beginner</span>
32. [Git Log Graph?](#q32) <span class="beginner">Beginner</span>
33. [Search in commit messages?](#q33) <span class="intermediate">Intermediate</span>
34. [Search code in history?](#q34) <span class="advanced">Advanced</span>
35. [What is `git gc`?](#q35) <span class="advanced">Advanced</span>
36. [Bare vs Non-Bare Repo?](#q36) <span class="advanced">Advanced</span>
37. [Git Objects (Blob, Tree, Commit)?](#q37) <span class="advanced">Advanced</span>
38. [How to create an Alias?](#q38) <span class="intermediate">Intermediate</span>
39. [Push to multiple remotes?](#q39) <span class="advanced">Advanced</span>
40. [Git LFS (Large File Storage)?](#q40) <span class="intermediate">Intermediate</span>
41. [Restore deleted file?](#q41) <span class="beginner">Beginner</span>
42. [Difference `checkout` vs `switch`?](#q42) <span class="beginner">Beginner</span>
43. [Difference `checkout` vs `restore`?](#q43) <span class="beginner">Beginner</span>
44. [Git Rebase Interactive?](#q44) <span class="intermediate">Intermediate</span>
45. [Rebase onto another branch?](#q45) <span class="intermediate">Intermediate</span>
46. [Abort a merge?](#q46) <span class="beginner">Beginner</span>
47. [What is `origin`?](#q47) <span class="beginner">Beginner</span>
48. [Upstream branch?](#q48) <span class="beginner">Beginner</span>
49. [Push force vs force-with-lease?](#q49) <span class="advanced">Advanced</span>
50. [Show remote URL?](#q50) <span class="beginner">Beginner</span>
51. [Change remote URL?](#q51) <span class="beginner">Beginner</span>
52. [Git Archive (Export)?](#q52) <span class="intermediate">Intermediate</span>
53. [Bundle objects?](#q53) <span class="advanced">Advanced</span>
54. [Shortlog (Summary)?](#q54) <span class="intermediate">Intermediate</span>
55. [Describe commit?](#q55) <span class="advanced">Advanced</span>
56. [Git Rerere?](#q56) <span class="advanced">Advanced</span>
57. [Verify GPG signatures?](#q57) <span class="advanced">Advanced</span>
58. [What is `.gitattributes`?](#q58) <span class="intermediate">Intermediate</span>
59. [CRLF vs LF handling?](#q59) <span class="intermediate">Intermediate</span>
60. [Excluding files without .gitignore?](#q60) <span class="advanced">Advanced</span>
61. [Global vs Local ignore?](#q61) <span class="intermediate">Intermediate</span>
62. [Git Grep vs Unix Grep?](#q62) <span class="intermediate">Intermediate</span>
63. [Count commits?](#q63) <span class="beginner">Beginner</span>
64. [Who committed vs Who authored?](#q64) <span class="intermediate">Intermediate</span>
65. [Change author of last commit?](#q65) <span class="intermediate">Intermediate</span>
66. [Combine two repositories?](#q66) <span class="advanced">Advanced</span>
67. [Delete local branch?](#q67) <span class="beginner">Beginner</span>
68. [Delete unmerged branch?](#q68) <span class="intermediate">Intermediate</span>
69. [Prune remote tracking branches?](#q69) <span class="intermediate">Intermediate</span>
70. [What is a Fast-Forward merge?](#q70) <span class="beginner">Beginner</span>
71. [Disable Fast-Forward?](#q71) <span class="intermediate">Intermediate</span>
72. [Squash merge?](#q72) <span class="intermediate">Intermediate</span>
73. [Ours vs Theirs strategy?](#q73) <span class="advanced">Advanced</span>
74. [Git Stash Pop vs Apply?](#q74) <span class="intermediate">Intermediate</span>
75. [List stashes?](#q75) <span class="beginner">Beginner</span>
76. [Clear stash?](#q76) <span class="beginner">Beginner</span>
77. [Create branch from stash?](#q77) <span class="intermediate">Intermediate</span>
78. [Show content of a stash?](#q78) <span class="intermediate">Intermediate</span>
79. [Patching (Diff/Apply)?](#q79) <span class="advanced">Advanced</span>
80. [Git Format-Patch?](#q80) <span class="advanced">Advanced</span>
81. [Git Am?](#q81) <span class="advanced">Advanced</span>
82. [Recover dropped stash?](#q82) <span class="advanced">Advanced</span>
83. [Move uncommitted changes to new branch?](#q83) <span class="beginner">Beginner</span>
84. [Find large files in history?](#q84) <span class="advanced">Advanced</span>
85. [Remove sensitive data from history?](#q85) <span class="advanced">Advanced</span>
86. [Git Filter-Repo (vs Filter-Branch)?](#q86) <span class="advanced">Advanced</span>
87. [What is `HEAD^` vs `HEAD~`?](#q87) <span class="intermediate">Intermediate</span>
88. [Checkout previous branch?](#q88) <span class="beginner">Beginner</span>
89. [List all branches (local + remote)?](#q89) <span class="beginner">Beginner</span>
90. [Fetch specific branch?](#q90) <span class="intermediate">Intermediate</span>
91. [Clone specific branch?](#q91) <span class="intermediate">Intermediate</span>
92. [Clone depth (Shallow clone)?](#q92) <span class="intermediate">Intermediate</span>
93. [Git Status short format?](#q93) <span class="beginner">Beginner</span>
94. [Ignore file mode changes?](#q94) <span class="advanced">Advanced</span>
95. [Debug gitignore?](#q95) <span class="intermediate">Intermediate</span>
96. [Git Notes?](#q96) <span class="advanced">Advanced</span>
97. [Git Replace?](#q97) <span class="advanced">Advanced</span>
98. [Git Rev-Parse?](#q98) <span class="advanced">Advanced</span>
99. [Show file at specific commit?](#q99) <span class="intermediate">Intermediate</span>
100. [Automate Git with Scripts?](#q100) <span class="advanced">Advanced</span>

---

---

### Q1: Merge vs Rebase?

**Difficulty**: Intermediate

**Strategy**:
**Merge:** Preserves history, creates merge commit. Safe.
**Rebase:** Rewrites history, linear. Dangerous on shared branches.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q2: Squash commits?

**Difficulty**: Intermediate

**Strategy**:
Combine multiple commits into one.


  
  Change `pick` to `squash`.

**Code Example**:
```bash
git rebase -i HEAD~3
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q3: Git Bisect?

**Difficulty**: Advanced

**Strategy**:
Binary search to find a bug.

**Code Example**:
```bash
git bisect start
git bisect bad  # Current is broken
git bisect good v1.0 # Old was good
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q4: Undo last commit?

**Difficulty**: Beginner

**Strategy**:
Keeps changes in staging.

**Code Example**:
```bash
git reset --soft HEAD~1
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q5: Cherry-pick?

**Difficulty**: Intermediate

**Strategy**:
Apply a specific commit from another branch.

**Code Example**:
```bash
git cherry-pick <commit-hash>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q6: Fetch vs Pull?

**Difficulty**: Beginner

**Strategy**:
**Fetch:** Download changes, don't merge.
**Pull:** Fetch + Merge.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q7: Amend commit message?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```bash
git commit --amend -m "New Message"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q8: Detached HEAD?

**Difficulty**: Intermediate

**Strategy**:
HEAD points to a Commit, not a Branch. Commits made here are lost unless a branch is created.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q9: Stash specific files?

**Difficulty**: Advanced

**Strategy**:


**Code Example**:
```bash
git stash push -p
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q10: Reflog?

**Difficulty**: Advanced

**Strategy**:
Log of all HEAD movements. Used to recover lost commits/branches.

**Code Example**:
```bash
git reflog
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q11: Git Flow vs Trunk?

**Difficulty**: Advanced

**Strategy**:
**Git Flow:** Complex branching (Feature, Develop, Release, Master).
**Trunk:** Commit to Main, use Feature Flags.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q12: Resolve Conflicts?

**Difficulty**: Beginner

**Strategy**:
Edit file, remove markers <code><<<<</code>, <code>>>>></code>, then <code>git add</code> and <code>git commit</code>.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q13: Reset Hard vs Soft?

**Difficulty**: Intermediate

**Strategy**:
**Hard:** Discard changes.
**Soft:** Keep changes staged.
**Mixed:** Keep changes unstaged.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q14: Revert public commit?

**Difficulty**: Intermediate

**Strategy**:
Creates a new commit that undoes changes.

**Code Example**:
```bash
git revert <commit-hash>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q15: Ignore tracked files?

**Difficulty**: Intermediate

**Strategy**:
Then add to `.gitignore`.

**Code Example**:
```bash
git rm --cached <file>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q16: Git Hooks?

**Difficulty**: Advanced

**Strategy**:
Scripts in `.git/hooks` triggered by events (pre-commit, pre-push).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q17: Git Blame?

**Difficulty**: Beginner

**Strategy**:
Show who changed each line.

**Code Example**:
```bash
git blame <file>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q18: Fork vs Branch?

**Difficulty**: Beginner

**Strategy**:
**Fork:** Copy of repo on server.
**Branch:** Parallel version within repo.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q19: List files in commit?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```bash
git show --name-only <commit>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q20: Find common ancestor?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```bash
git merge-base branchA branchB
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q21: What is the Staging Area (Index)?

**Difficulty**: Beginner

**Strategy**:
Area where changes are prepared before committing. Allows selective committing.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q22: Git Config Scopes?

**Difficulty**: Beginner

**Strategy**:
System (<code>/etc/gitconfig</code>), Global (<code>~/.gitconfig</code>), Local (<code>.git/config</code>).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q23: Remove untracked files (clean)?

**Difficulty**: Intermediate

**Strategy**:
Force delete untracked files and directories.

**Code Example**:
```bash
git clean -fd
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q24: Git Tags (Lightweight vs Annotated)?

**Difficulty**: Intermediate

**Strategy**:
**Lightweight:** Pointer to commit.
**Annotated:** Stores message, author, date, checksum (Full object).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q25: What is a Submodule?

**Difficulty**: Advanced

**Strategy**:
Git repo inside another Git repo. Points to specific commit of child repo.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q26: What is a Subtree?

**Difficulty**: Advanced

**Strategy**:
Alternative to submodules. Merges child repo code into main repo history.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q27: Git Worktree?

**Difficulty**: Advanced

**Strategy**:
Allows multiple working directories attached to same repo. Work on multiple branches simultaneously without switching.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q28: Diff Staged vs Unstaged?

**Difficulty**: Beginner

**Strategy**:
<code>git diff</code> (Unstaged).
<code>git diff --staged</code> (Staged).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q29: Rename a branch?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```bash
git branch -m new-name
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q30: Delete a remote branch?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```bash
git push origin --delete branch-name
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q31: Show commit history for one file?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```bash
git log -p filename
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q32: Git Log Graph?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```bash
git log --graph --oneline --all
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q33: Search in commit messages?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```bash
git log --grep="fix"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q34: Search code in history?

**Difficulty**: Advanced

**Strategy**:
Pickaxe search: finds commits that added/removed string.

**Code Example**:
```bash
git log -S "functionName"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q35: What is `git gc`?

**Difficulty**: Advanced

**Strategy**:
Garbage Collector. Compresses file revisions, removes unreachable objects.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q36: Bare vs Non-Bare Repo?

**Difficulty**: Advanced

**Strategy**:
**Bare:** No working directory. For servers.
**Non-Bare:** Has working directory. For users.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q37: Git Objects (Blob, Tree, Commit)?

**Difficulty**: Advanced

**Strategy**:
**Blob:** File content.
**Tree:** Directory structure.
**Commit:** Metadata + Pointer to Tree.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q38: How to create an Alias?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```bash
git config --global alias.co checkout
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q39: Push to multiple remotes?

**Difficulty**: Advanced

**Strategy**:
Add multiple Push URLs to a single remote in config.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q40: Git LFS (Large File Storage)?

**Difficulty**: Intermediate

**Strategy**:
Extension to store large binaries (PSD, MP4) on separate server, keeping pointers in Git.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q41: Restore deleted file?

**Difficulty**: Beginner

**Strategy**:
Or <code>git restore</code>.

**Code Example**:
```bash
git checkout <commit> -- <file>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q42: Difference `checkout` vs `switch`?

**Difficulty**: Beginner

**Strategy**:
<code>switch</code> is newer, safer, specifically for changing branches. <code>checkout</code> does files and branches.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q43: Difference `checkout` vs `restore`?

**Difficulty**: Beginner

**Strategy**:
<code>restore</code> is for restoring files from index/commit. <code>checkout</code> is overloaded.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q44: Git Rebase Interactive?

**Difficulty**: Intermediate

**Strategy**:
Allows editing, reordering, squashing, dropping commits.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q45: Rebase onto another branch?

**Difficulty**: Intermediate

**Strategy**:
Replays current branch commits on top of master.

**Code Example**:
```bash
git rebase master
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q46: Abort a merge?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```bash
git merge --abort
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q47: What is `origin`?

**Difficulty**: Beginner

**Strategy**:
Default alias for the remote repository URL.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q48: Upstream branch?

**Difficulty**: Beginner

**Strategy**:
The remote branch that a local branch tracks (pushes/pulls to).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q49: Push force vs force-with-lease?

**Difficulty**: Advanced

**Strategy**:
**Force:** Overwrites remote blindly.
**Force-with-lease:** Overwrites only if remote hasn't changed since last fetch. Safer.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q50: Show remote URL?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```bash
git remote -v
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q51: Change remote URL?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```bash
git remote set-url origin <new-url>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q52: Git Archive (Export)?

**Difficulty**: Intermediate

**Strategy**:
Create a zip/tar of the repo without .git folder.

**Code Example**:
```bash
git archive --format=zip HEAD > project.zip
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q53: Bundle objects?

**Difficulty**: Advanced

**Strategy**:
Pack git objects into a single file for offline transfer.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q54: Shortlog (Summary)?

**Difficulty**: Intermediate

**Strategy**:
Summarize git log output. Good for release notes.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q55: Describe commit?

**Difficulty**: Advanced

**Strategy**:
Finds most recent tag reachable from commit and builds a name.

**Code Example**:
```bash
git describe
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q56: Git Rerere?

**Difficulty**: Advanced

**Strategy**:
Reuse Recorded Resolution. Remembers how you resolved a conflict and auto-applies it next time.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q57: Verify GPG signatures?

**Difficulty**: Advanced

**Strategy**:
Ensure commits are signed by trusted keys.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q58: What is `.gitattributes`?

**Difficulty**: Intermediate

**Strategy**:
Configures path-specific settings (EOL normalization, binary handling, diff drivers).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q59: CRLF vs LF handling?

**Difficulty**: Intermediate

**Strategy**:
Configured via `core.autocrlf`. Windows uses CRLF, Unix uses LF. Git can convert on checkout/commit.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q60: Excluding files without .gitignore?

**Difficulty**: Advanced

**Strategy**:
Use `.git/info/exclude` for local-only ignores.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q61: Global vs Local ignore?

**Difficulty**: Intermediate

**Strategy**:
Global: `~/.gitignore_global`. Applies to all repos.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q62: Git Grep vs Unix Grep?

**Difficulty**: Intermediate

**Strategy**:
Git Grep searches tracked files only and is much faster.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q63: Count commits? <span class="beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">git rev-list --count HEAD</code></pre>
</div>

<div id="q64" class="question">64. Who committed vs Who authored?

**Difficulty**: Intermediate

**Strategy**:
**Author:** Wrote the code.
**Committer:** Applied the patch (e.g., rebase/cherry-pick).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q65: Change author of last commit?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```bash
git commit --amend --author="Name <email>"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q66: Combine two repositories?

**Difficulty**: Advanced

**Strategy**:
Add one as remote, fetch, then merge into a subdirectory (subtree).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q67: Delete local branch? <span class="beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">git branch -d name</code></pre>
</div>

<div id="q68" class="question">68. Delete unmerged branch?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```bash
git branch -D name
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q69: Prune remote tracking branches?

**Difficulty**: Intermediate

**Strategy**:
Removes local refs to deleted remote branches.

**Code Example**:
```bash
git fetch --prune
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q70: What is a Fast-Forward merge? <span class="beginner">Beginner</span></div>
<div class="answer">
  <p>If no divergent work, HEAD is simply moved forward. No merge commit.</p>
</div>

<div id="q71" class="question">71. Disable Fast-Forward?

**Difficulty**: Intermediate

**Strategy**:
Forces creation of a merge commit.

**Code Example**:
```bash
git merge --no-ff
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q72: Squash merge?

**Difficulty**: Intermediate

**Strategy**:
Stages all changes from branch as one commit. Does not record merge relationship.

**Code Example**:
```bash
git merge --squash
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q73: Ours vs Theirs strategy?

**Difficulty**: Advanced

**Strategy**:
Resolve conflicts by accepting all changes from one side.

**Code Example**:
```bash
git checkout --ours file
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q74: Git Stash Pop vs Apply?

**Difficulty**: Intermediate

**Strategy**:
**Pop:** Apply and remove from list.
**Apply:** Apply and keep in list.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q75: List stashes? <span class="beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">git stash list</code></pre>
</div>

<div id="q76" class="question">76. Clear stash? <span class="beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">git stash clear</code></pre>
</div>

<div id="q77" class="question">77. Create branch from stash?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```bash
git stash branch <name>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q78: Show content of a stash?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```bash
git stash show -p stash@{0}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q79: Patching (Diff/Apply)?

**Difficulty**: Advanced

**Strategy**:
Send changes via email/file.

**Code Example**:
```bash
git diff > changes.patch
git apply changes.patch
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q80: Git Format-Patch?

**Difficulty**: Advanced

**Strategy**:
Prepare patches for email submission (includes commit metadata).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q81: Git Am?

**Difficulty**: Advanced

**Strategy**:
Apply series of patches from mailbox.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q82: Recover dropped stash?

**Difficulty**: Advanced

**Strategy**:
Use `git fsck` to find dangling commits.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q83: Move uncommitted changes to new branch? <span class="beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">git checkout -b new-branch</code></pre>
</div>

<div id="q84" class="question">84. Find large files in history?

**Difficulty**: Advanced

**Strategy**:
Iterate objects and sort by size. (Scripting required).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q85: Remove sensitive data from history?

**Difficulty**: Advanced

**Strategy**:
BFG Repo-Cleaner or `git filter-repo`. Rewrites history.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q86: Git Filter-Repo (vs Filter-Branch)?

**Difficulty**: Advanced

**Strategy**:
Filter-Repo is the modern, faster, Python-based replacement for the slow shell-based filter-branch.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q87: What is `HEAD^` vs `HEAD~`?

**Difficulty**: Intermediate

**Strategy**:
<code>~</code>: First parent (Ancestry line).
<code>^</code>: Selects specific parent (Merge parent).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q88: Checkout previous branch? <span class="beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">git checkout -</code></pre>
</div>

<div id="q89" class="question">89. List all branches (local + remote)? <span class="beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">git branch -a</code></pre>
</div>

<div id="q90" class="question">90. Fetch specific branch?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```bash
git fetch origin branchname:branchname
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q91: Clone specific branch?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```bash
git clone -b branchname --single-branch <url>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q92: Clone depth (Shallow clone)?

**Difficulty**: Intermediate

**Strategy**:
Downloads only latest commit. Saves bandwidth.

**Code Example**:
```bash
git clone --depth 1 <url>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q93: Git Status short format? <span class="beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">git status -s</code></pre>
</div>

<div id="q94" class="question">94. Ignore file mode changes?

**Difficulty**: Advanced

**Strategy**:


**Code Example**:
```bash
git config core.fileMode false
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q95: Debug gitignore?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```bash
git check-ignore -v filename
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q96: Git Notes?

**Difficulty**: Advanced

**Strategy**:
Attach metadata to commits without rewriting them.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q97: Git Replace?

**Difficulty**: Advanced

**Strategy**:
Replace object with another at runtime (e.g., grafting history).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q98: Git Rev-Parse?

**Difficulty**: Advanced

**Strategy**:
Plumbing command to parse refs/SHA.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q99: Show file at specific commit?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```bash
git show <commit>:<file>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q100: Automate Git with Scripts?

**Difficulty**: Advanced

**Strategy**:
Use Porcelain (high-level) vs Plumbing (low-level) commands. Prefer plumbing for stability.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---
