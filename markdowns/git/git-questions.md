# Git Interview Questions

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

<div id="q1" class="question">1. Merge vs Rebase? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p><strong>Merge:</strong> Preserves history, creates merge commit. Safe.<br><strong>Rebase:</strong> Rewrites history, linear. Dangerous on shared branches.</p>
</div>

<div id="q2" class="question">2. Squash commits? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Combine multiple commits into one.</p>
  <pre><code class="language-bash">git rebase -i HEAD~3</code></pre>
  <p>Change `pick` to `squash`.</p>
</div>

<div id="q3" class="question">3. Git Bisect? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Binary search to find a bug.</p>
  <pre><code class="language-bash">git bisect start
git bisect bad  # Current is broken
git bisect good v1.0 # Old was good</code></pre>
</div>

<div id="q4" class="question">4. Undo last commit? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">git reset --soft HEAD~1</code></pre>
  <p>Keeps changes in staging.</p>
</div>

<div id="q5" class="question">5. Cherry-pick? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Apply a specific commit from another branch.</p>
  <pre><code class="language-bash">git cherry-pick <commit-hash></code></pre>
</div>

<div id="q6" class="question">6. Fetch vs Pull? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p><strong>Fetch:</strong> Download changes, don't merge.<br><strong>Pull:</strong> Fetch + Merge.</p>
</div>

<div id="q7" class="question">7. Amend commit message? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">git commit --amend -m "New Message"</code></pre>
</div>

<div id="q8" class="question">8. Detached HEAD? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>HEAD points to a Commit, not a Branch. Commits made here are lost unless a branch is created.</p>
</div>

<div id="q9" class="question">9. Stash specific files? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <pre><code class="language-bash">git stash push -p</code></pre>
</div>

<div id="q10" class="question">10. Reflog? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Log of all HEAD movements. Used to recover lost commits/branches.</p>
  <pre><code class="language-bash">git reflog</code></pre>
</div>

<div id="q11" class="question">11. Git Flow vs Trunk? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p><strong>Git Flow:</strong> Complex branching (Feature, Develop, Release, Master).<br><strong>Trunk:</strong> Commit to Main, use Feature Flags.</p>
</div>

<div id="q12" class="question">12. Resolve Conflicts? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Edit file, remove markers <code><<<<</code>, <code>>>>></code>, then <code>git add</code> and <code>git commit</code>.</p>
</div>

<div id="q13" class="question">13. Reset Hard vs Soft? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p><strong>Hard:</strong> Discard changes.<br><strong>Soft:</strong> Keep changes staged.<br><strong>Mixed:</strong> Keep changes unstaged.</p>
</div>

<div id="q14" class="question">14. Revert public commit? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">git revert <commit-hash></code></pre>
  <p>Creates a new commit that undoes changes.</p>
</div>

<div id="q15" class="question">15. Ignore tracked files? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">git rm --cached <file></code></pre>
  <p>Then add to `.gitignore`.</p>
</div>

<div id="q16" class="question">16. Git Hooks? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Scripts in `.git/hooks` triggered by events (pre-commit, pre-push).</p>
</div>

<div id="q17" class="question">17. Git Blame? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Show who changed each line.</p>
  <pre><code class="language-bash">git blame <file></code></pre>
</div>

<div id="q18" class="question">18. Fork vs Branch? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p><strong>Fork:</strong> Copy of repo on server.<br><strong>Branch:</strong> Parallel version within repo.</p>
</div>

<div id="q19" class="question">19. List files in commit? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">git show --name-only <commit></code></pre>
</div>

<div id="q20" class="question">20. Find common ancestor? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">git merge-base branchA branchB</code></pre>
</div>

<div id="q21" class="question">21. What is the Staging Area (Index)? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Area where changes are prepared before committing. Allows selective committing.</p>
</div>

<div id="q22" class="question">22. Git Config Scopes? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>System (<code>/etc/gitconfig</code>), Global (<code>~/.gitconfig</code>), Local (<code>.git/config</code>).</p>
</div>

<div id="q23" class="question">23. Remove untracked files (clean)? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">git clean -fd</code></pre>
  <p>Force delete untracked files and directories.</p>
</div>

<div id="q24" class="question">24. Git Tags (Lightweight vs Annotated)? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p><strong>Lightweight:</strong> Pointer to commit.<br><strong>Annotated:</strong> Stores message, author, date, checksum (Full object).</p>
</div>

<div id="q25" class="question">25. What is a Submodule? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Git repo inside another Git repo. Points to specific commit of child repo.</p>
</div>

<div id="q26" class="question">26. What is a Subtree? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Alternative to submodules. Merges child repo code into main repo history.</p>
</div>

<div id="q27" class="question">27. Git Worktree? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Allows multiple working directories attached to same repo. Work on multiple branches simultaneously without switching.</p>
</div>

<div id="q28" class="question">28. Diff Staged vs Unstaged? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p><code>git diff</code> (Unstaged).<br><code>git diff --staged</code> (Staged).</p>
</div>

<div id="q29" class="question">29. Rename a branch? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">git branch -m new-name</code></pre>
</div>

<div id="q30" class="question">30. Delete a remote branch? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">git push origin --delete branch-name</code></pre>
</div>

<div id="q31" class="question">31. Show commit history for one file? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">git log -p filename</code></pre>
</div>

<div id="q32" class="question">32. Git Log Graph? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">git log --graph --oneline --all</code></pre>
</div>

<div id="q33" class="question">33. Search in commit messages? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">git log --grep="fix"</code></pre>
</div>

<div id="q34" class="question">34. Search code in history? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <pre><code class="language-bash">git log -S "functionName"</code></pre>
  <p>Pickaxe search: finds commits that added/removed string.</p>
</div>

<div id="q35" class="question">35. What is `git gc`? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Garbage Collector. Compresses file revisions, removes unreachable objects.</p>
</div>

<div id="q36" class="question">36. Bare vs Non-Bare Repo? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p><strong>Bare:</strong> No working directory. For servers.<br><strong>Non-Bare:</strong> Has working directory. For users.</p>
</div>

<div id="q37" class="question">37. Git Objects (Blob, Tree, Commit)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p><strong>Blob:</strong> File content.<br><strong>Tree:</strong> Directory structure.<br><strong>Commit:</strong> Metadata + Pointer to Tree.</p>
</div>

<div id="q38" class="question">38. How to create an Alias? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">git config --global alias.co checkout</code></pre>
</div>

<div id="q39" class="question">39. Push to multiple remotes? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Add multiple Push URLs to a single remote in config.</p>
</div>

<div id="q40" class="question">40. Git LFS (Large File Storage)? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Extension to store large binaries (PSD, MP4) on separate server, keeping pointers in Git.</p>
</div>

<div id="q41" class="question">41. Restore deleted file? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">git checkout <commit> -- <file></code></pre>
  <p>Or <code>git restore</code>.</p>
</div>

<div id="q42" class="question">42. Difference `checkout` vs `switch`? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p><code>switch</code> is newer, safer, specifically for changing branches. <code>checkout</code> does files and branches.</p>
</div>

<div id="q43" class="question">43. Difference `checkout` vs `restore`? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p><code>restore</code> is for restoring files from index/commit. <code>checkout</code> is overloaded.</p>
</div>

<div id="q44" class="question">44. Git Rebase Interactive? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Allows editing, reordering, squashing, dropping commits.</p>
</div>

<div id="q45" class="question">45. Rebase onto another branch? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">git rebase master</code></pre>
  <p>Replays current branch commits on top of master.</p>
</div>

<div id="q46" class="question">46. Abort a merge? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">git merge --abort</code></pre>
</div>

<div id="q47" class="question">47. What is `origin`? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Default alias for the remote repository URL.</p>
</div>

<div id="q48" class="question">48. Upstream branch? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>The remote branch that a local branch tracks (pushes/pulls to).</p>
</div>

<div id="q49" class="question">49. Push force vs force-with-lease? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p><strong>Force:</strong> Overwrites remote blindly.<br><strong>Force-with-lease:</strong> Overwrites only if remote hasn't changed since last fetch. Safer.</p>
</div>

<div id="q50" class="question">50. Show remote URL? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">git remote -v</code></pre>
</div>

<div id="q51" class="question">51. Change remote URL? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">git remote set-url origin <new-url></code></pre>
</div>

<div id="q52" class="question">52. Git Archive (Export)? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Create a zip/tar of the repo without .git folder.</p>
  <pre><code class="language-bash">git archive --format=zip HEAD > project.zip</code></pre>
</div>

<div id="q53" class="question">53. Bundle objects? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Pack git objects into a single file for offline transfer.</p>
</div>

<div id="q54" class="question">54. Shortlog (Summary)? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Summarize git log output. Good for release notes.</p>
</div>

<div id="q55" class="question">55. Describe commit? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <pre><code class="language-bash">git describe</code></pre>
  <p>Finds most recent tag reachable from commit and builds a name.</p>
</div>

<div id="q56" class="question">56. Git Rerere? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Reuse Recorded Resolution. Remembers how you resolved a conflict and auto-applies it next time.</p>
</div>

<div id="q57" class="question">57. Verify GPG signatures? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Ensure commits are signed by trusted keys.</p>
</div>

<div id="q58" class="question">58. What is `.gitattributes`? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Configures path-specific settings (EOL normalization, binary handling, diff drivers).</p>
</div>

<div id="q59" class="question">59. CRLF vs LF handling? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Configured via `core.autocrlf`. Windows uses CRLF, Unix uses LF. Git can convert on checkout/commit.</p>
</div>

<div id="q60" class="question">60. Excluding files without .gitignore? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Use `.git/info/exclude` for local-only ignores.</p>
</div>

<div id="q61" class="question">61. Global vs Local ignore? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Global: `~/.gitignore_global`. Applies to all repos.</p>
</div>

<div id="q62" class="question">62. Git Grep vs Unix Grep? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Git Grep searches tracked files only and is much faster.</p>
</div>

<div id="q63" class="question">63. Count commits? <span class="beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">git rev-list --count HEAD</code></pre>
</div>

<div id="q64" class="question">64. Who committed vs Who authored? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p><strong>Author:</strong> Wrote the code.<br><strong>Committer:</strong> Applied the patch (e.g., rebase/cherry-pick).</p>
</div>

<div id="q65" class="question">65. Change author of last commit? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">git commit --amend --author="Name <email>"</code></pre>
</div>

<div id="q66" class="question">66. Combine two repositories? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Add one as remote, fetch, then merge into a subdirectory (subtree).</p>
</div>

<div id="q67" class="question">67. Delete local branch? <span class="beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">git branch -d name</code></pre>
</div>

<div id="q68" class="question">68. Delete unmerged branch? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">git branch -D name</code></pre>
</div>

<div id="q69" class="question">69. Prune remote tracking branches? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">git fetch --prune</code></pre>
  <p>Removes local refs to deleted remote branches.</p>
</div>

<div id="q70" class="question">70. What is a Fast-Forward merge? <span class="beginner">Beginner</span></div>
<div class="answer">
  <p>If no divergent work, HEAD is simply moved forward. No merge commit.</p>
</div>

<div id="q71" class="question">71. Disable Fast-Forward? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">git merge --no-ff</code></pre>
  <p>Forces creation of a merge commit.</p>
</div>

<div id="q72" class="question">72. Squash merge? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">git merge --squash</code></pre>
  <p>Stages all changes from branch as one commit. Does not record merge relationship.</p>
</div>

<div id="q73" class="question">73. Ours vs Theirs strategy? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Resolve conflicts by accepting all changes from one side.</p>
  <pre><code class="language-bash">git checkout --ours file</code></pre>
</div>

<div id="q74" class="question">74. Git Stash Pop vs Apply? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p><strong>Pop:</strong> Apply and remove from list.<br><strong>Apply:</strong> Apply and keep in list.</p>
</div>

<div id="q75" class="question">75. List stashes? <span class="beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">git stash list</code></pre>
</div>

<div id="q76" class="question">76. Clear stash? <span class="beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">git stash clear</code></pre>
</div>

<div id="q77" class="question">77. Create branch from stash? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">git stash branch <name></code></pre>
</div>

<div id="q78" class="question">78. Show content of a stash? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">git stash show -p stash@{0}</code></pre>
</div>

<div id="q79" class="question">79. Patching (Diff/Apply)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Send changes via email/file.</p>
  <pre><code class="language-bash">git diff > changes.patch
git apply changes.patch</code></pre>
</div>

<div id="q80" class="question">80. Git Format-Patch? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Prepare patches for email submission (includes commit metadata).</p>
</div>

<div id="q81" class="question">81. Git Am? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Apply series of patches from mailbox.</p>
</div>

<div id="q82" class="question">82. Recover dropped stash? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Use `git fsck` to find dangling commits.</p>
</div>

<div id="q83" class="question">83. Move uncommitted changes to new branch? <span class="beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">git checkout -b new-branch</code></pre>
</div>

<div id="q84" class="question">84. Find large files in history? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Iterate objects and sort by size. (Scripting required).</p>
</div>

<div id="q85" class="question">85. Remove sensitive data from history? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>BFG Repo-Cleaner or `git filter-repo`. Rewrites history.</p>
</div>

<div id="q86" class="question">86. Git Filter-Repo (vs Filter-Branch)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Filter-Repo is the modern, faster, Python-based replacement for the slow shell-based filter-branch.</p>
</div>

<div id="q87" class="question">87. What is `HEAD^` vs `HEAD~`? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p><code>~</code>: First parent (Ancestry line).<br><code>^</code>: Selects specific parent (Merge parent).</p>
</div>

<div id="q88" class="question">88. Checkout previous branch? <span class="beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">git checkout -</code></pre>
</div>

<div id="q89" class="question">89. List all branches (local + remote)? <span class="beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">git branch -a</code></pre>
</div>

<div id="q90" class="question">90. Fetch specific branch? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">git fetch origin branchname:branchname</code></pre>
</div>

<div id="q91" class="question">91. Clone specific branch? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">git clone -b branchname --single-branch <url></code></pre>
</div>

<div id="q92" class="question">92. Clone depth (Shallow clone)? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">git clone --depth 1 <url></code></pre>
  <p>Downloads only latest commit. Saves bandwidth.</p>
</div>

<div id="q93" class="question">93. Git Status short format? <span class="beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">git status -s</code></pre>
</div>

<div id="q94" class="question">94. Ignore file mode changes? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <pre><code class="language-bash">git config core.fileMode false</code></pre>
</div>

<div id="q95" class="question">95. Debug gitignore? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">git check-ignore -v filename</code></pre>
</div>

<div id="q96" class="question">96. Git Notes? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Attach metadata to commits without rewriting them.</p>
</div>

<div id="q97" class="question">97. Git Replace? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Replace object with another at runtime (e.g., grafting history).</p>
</div>

<div id="q98" class="question">98. Git Rev-Parse? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Plumbing command to parse refs/SHA.</p>
</div>

<div id="q99" class="question">99. Show file at specific commit? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">git show <commit>:<file></code></pre>
</div>

<div id="q100" class="question">100. Automate Git with Scripts? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Use Porcelain (high-level) vs Plumbing (low-level) commands. Prefer plumbing for stability.</p>
</div>
