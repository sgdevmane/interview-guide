# Git Interview Questions

## Table of Contents

1. [Difference between `git merge` and `git rebase`?](#q1-difference-between-git-merge-and-git-rebase) <span class="intermediate">Intermediate</span>
2. [How do you squash multiple commits into one?](#q2-how-do-you-squash-multiple-commits-into-one) <span class="intermediate">Intermediate</span>
3. [What is `git bisect` and how do you use it?](#q3-what-is-git-bisect-and-how-do-you-use-it) <span class="advanced">Advanced</span>
4. [How to undo the last commit (keep changes)?](#q4-how-to-undo-the-last-commit-keep-changes) <span class="beginner">Beginner</span>
5. [Explain `git cherry-pick`?](#q5-explain-git-cherry-pick) <span class="intermediate">Intermediate</span>
6. [What is the difference between `git fetch` and `git pull`?](#q6-what-is-the-difference-between-git-fetch-and-git-pull) <span class="beginner">Beginner</span>
7. [How to fix a broken commit message (amend)?](#q7-how-to-fix-a-broken-commit-message-amend) <span class="beginner">Beginner</span>
8. [What is a Detached HEAD state?](#q8-what-is-a-detached-head-state) <span class="intermediate">Intermediate</span>
9. [How do you stash specific files only?](#q9-how-do-you-stash-specific-files-only) <span class="advanced">Advanced</span>
10. [How to recover a deleted branch/commit (reflog)?](#q10-how-to-recover-a-deleted-branchcommit-reflog) <span class="advanced">Advanced</span>
11. [Explain Git Flow vs Trunk Based Development?](#q11-explain-git-flow-vs-trunk-based-development) <span class="advanced">Advanced</span>
12. [How do you resolve a merge conflict?](#q12-how-do-you-resolve-a-merge-conflict) <span class="beginner">Beginner</span>
13. [What is `git reset --hard` vs `git reset --soft`?](#q13-what-is-git-reset-hard-vs-git-reset-soft) <span class="intermediate">Intermediate</span>
14. [How to revert a public commit safely?](#q14-how-to-revert-a-public-commit-safely) <span class="intermediate">Intermediate</span>
15. [How to ignore files already tracked by Git?](#q15-how-to-ignore-files-already-tracked-by-git) <span class="intermediate">Intermediate</span>
16. [What are Git Hooks?](#q16-what-are-git-hooks) <span class="advanced">Advanced</span>
17. [How to check who modified a specific line (blame)?](#q17-how-to-check-who-modified-a-specific-line-blame) <span class="beginner">Beginner</span>
18. [Difference between Fork and Branch?](#q18-difference-between-fork-and-branch) <span class="beginner">Beginner</span>
19. [How to list all files in a commit?](#q19-how-to-list-all-files-in-a-commit) <span class="beginner">Beginner</span>
20. [How to find the common ancestor of two branches?](#q20-how-to-find-the-common-ancestor-of-two-branches) <span class="intermediate">Intermediate</span>

---

<div id="q1-difference-between-git-merge-and-git-rebase" class="question">
  1. Difference between `git merge` and `git rebase`?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <p>Both integrate changes from one branch into another.</p>
  <ul>
    <li><strong>Merge:</strong> Creates a new "merge commit" tying the histories together. It preserves the exact history of when changes happened. <strong>Non-destructive</strong>.</li>
    <li><strong>Rebase:</strong> Moves the entire feature branch to begin on the tip of the master branch. It rewrites history to create a linear progression. <strong>Destructive</strong> (changes commit hashes).</li>
    <li><strong>Rule of Thumb:</strong> Never rebase public/shared branches.</li>
  </ul>
</div>

<div id="q2-how-do-you-squash-multiple-commits-into-one" class="question">
  2. How do you squash multiple commits into one?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <p>Use interactive rebase.</p>
  <pre><code class="language-bash">git rebase -i HEAD~3</code></pre>
  <p>This opens an editor showing the last 3 commits. Change <code>pick</code> to <code>squash</code> (or <code>s</code>) for the commits you want to combine into the previous one.</p>
</div>

<div id="q3-what-is-git-bisect-and-how-do-you-use-it" class="question">
  3. What is `git bisect` and how do you use it?
  <span class="difficulty advanced">Advanced</span>
</div>

<div class="answer">
  <p><code>git bisect</code> uses binary search to find the commit that introduced a bug.</p>
  <ol>
    <li>Start: <code>git bisect start</code></li>
    <li>Mark bad: <code>git bisect bad</code> (current version is broken)</li>
    <li>Mark good: <code>git bisect good <commit-hash></code> (a past version that worked)</li>
    <li>Git checks out a middle commit. You test it and say <code>git bisect good</code> or <code>git bisect bad</code>.</li>
    <li>Repeat until the culprit is found.</li>
  </ol>
</div>

<div id="q4-how-to-undo-the-last-commit-keep-changes" class="question">
  4. How to undo the last commit (keep changes)?
  <span class="difficulty beginner">Beginner</span>
</div>

<div class="answer">
  <pre><code class="language-bash">git reset --soft HEAD~1</code></pre>
  <p>This moves the HEAD pointer back one step but keeps your changes in the staging area (index). Useful if you forgot to add a file to the last commit.</p>
</div>

<div id="q5-explain-git-cherry-pick" class="question">
  5. Explain `git cherry-pick`?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <p><code>git cherry-pick <commit-hash></code> allows you to pick a specific commit from another branch and apply it to your current branch.</p>
  <p><strong>Use Case:</strong> You fixed a bug on `development` but need to apply that specific hotfix to `production` without merging all other experimental changes.</p>
</div>

<div id="q6-what-is-the-difference-between-git-fetch-and-git-pull" class="question">
  6. What is the difference between `git fetch` and `git pull`?
  <span class="difficulty beginner">Beginner</span>
</div>

<div class="answer">
  <ul>
    <li><code>git fetch</code>: Downloads new data (commits, branches) from the remote repository but <strong>does not</strong> integrate them into your working files. It's safe.</li>
    <li><code>git pull</code>: Automatically does <code>git fetch</code> followed by <code>git merge</code>. It updates your current branch with the remote changes.</li>
  </ul>
</div>

<div id="q7-how-to-fix-a-broken-commit-message-amend" class="question">
  7. How to fix a broken commit message (amend)?
  <span class="difficulty beginner">Beginner</span>
</div>

<div class="answer">
  <p>If it is the very last commit and you haven't pushed it yet:</p>
  <pre><code class="language-bash">git commit --amend -m "New correct message"</code></pre>
  <p>This replaces the last commit with a new one.</p>
</div>

<div id="q8-what-is-a-detached-head-state" class="question">
  8. What is a Detached HEAD state?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <p>Usually, HEAD points to a branch name (like `main`). When you checkout a specific commit hash directly (<code>git checkout 1a2b3c</code>), HEAD points directly to that commit, not a branch.</p>
  <p>If you make commits here, they don't belong to any branch and can be easily lost if you checkout something else. To save them, create a branch: <code>git checkout -b new-branch-name</code>.</p>
</div>

<div id="q9-how-do-you-stash-specific-files-only" class="question">
  9. How do you stash specific files only?
  <span class="difficulty advanced">Advanced</span>
</div>

<div class="answer">
  <p>By default, <code>git stash</code> stashes all tracked files.</p>
  <p>To stash specific files:</p>
  <pre><code class="language-bash">git stash push -p</code></pre>
  <p>This enters "patch mode", allowing you to interactively choose which hunks (changes) to stash.</p>
</div>

<div id="q10-how-to-recover-a-deleted-branchcommit-reflog" class="question">
  10. How to recover a deleted branch/commit (reflog)?
  <span class="difficulty advanced">Advanced</span>
</div>

<div class="answer">
  <p>Git keeps a log of where HEAD has been for the last few months.</p>
  <ol>
    <li>Run <code>git reflog</code>. You will see a list like <code>HEAD@{0}: checkout...</code>.</li>
    <li>Find the SHA of the commit that was at the tip of your deleted branch.</li>
    <li>Recover it: <code>git checkout -b recovered-branch <commit-hash></code>.</li>
  </ol>
</div>

<div id="q11-explain-git-flow-vs-trunk-based-development" class="question">
  11. Explain Git Flow vs Trunk Based Development?
  <span class="difficulty advanced">Advanced</span>
</div>

<div class="answer">
  <ul>
    <li><strong>Git Flow:</strong> Strict branching model. Uses `develop`, `feature/*`, `release/*`, `hotfix/*`, and `master`. Good for scheduled releases.</li>
    <li><strong>Trunk Based:</strong> Developers merge small, frequent updates to a core "trunk" (main) branch. Uses feature flags to hide unfinished work. Encourages CI/CD and fast iteration.</li>
  </ul>
</div>

<div id="q12-how-do-you-resolve-a-merge-conflict" class="question">
  12. How do you resolve a merge conflict?
  <span class="difficulty beginner">Beginner</span>
</div>

<div class="answer">
  <ol>
    <li>Git pauses the merge and marks conflicting files.</li>
    <li>Open files. Look for <code><<<<<<<</code>, <code>=======</code>, and <code>>>>>>>></code> markers.</li>
    <li>Edit the file to choose the correct code (or combine both).</li>
    <li>Save and run <code>git add <file></code>.</li>
    <li>Finish with <code>git commit</code>.</li>
  </ol>
</div>

<div id="q13-what-is-git-reset-hard-vs-git-reset-soft" class="question">
  13. What is `git reset --hard` vs `git reset --soft`?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <ul>
    <li><code>--soft</code>: Moves HEAD back. Changes are left in "Staging". (Safe).</li>
    <li><code>--mixed</code> (default): Moves HEAD back. Changes are left in "Working Directory" (Unstaged).</li>
    <li><code>--hard</code>: Moves HEAD back. <strong>Destroys</strong> all changes in Staging and Working Directory. (Dangerous).</li>
  </ul>
</div>

<div id="q14-how-to-revert-a-public-commit-safely" class="question">
  14. How to revert a public commit safely?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <p>Do not use <code>reset</code> on public branches (it rewrites history). Use <code>git revert</code>.</p>
  <pre><code class="language-bash">git revert <commit-hash></code></pre>
  <p>This creates a <em>new</em> commit that is the exact opposite of the target commit, effectively undoing the changes while preserving history.</p>
</div>

<div id="q15-how-to-ignore-files-already-tracked-by-git" class="question">
  15. How to ignore files already tracked by Git?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <p>Simply adding to `.gitignore` won't work if the file is already tracked.</p>
  <ol>
    <li>Add file to <code>.gitignore</code>.</li>
    <li>Remove it from the index (cache) but keep the file:
      <pre><code class="language-bash">git rm --cached <filename></code></pre>
    </li>
    <li>Commit the change.</li>
  </ol>
</div>

<div id="q16-what-are-git-hooks" class="question">
  16. What are Git Hooks?
  <span class="difficulty advanced">Advanced</span>
</div>

<div class="answer">
  <p>Scripts that Git executes before or after events such as: commit, push, and receive.</p>
  <ul>
    <li><strong>pre-commit:</strong> Runs before a commit is created. Good for linting, testing.</li>
    <li><strong>pre-push:</strong> Runs before pushing. Good for running integration tests.</li>
    <li>Stored in <code>.git/hooks</code> directory.</li>
  </ul>
</div>

<div id="q17-how-to-check-who-modified-a-specific-line-blame" class="question">
  17. How to check who modified a specific line (blame)?
  <span class="difficulty beginner">Beginner</span>
</div>

<div class="answer">
  <pre><code class="language-bash">git blame <filename></code></pre>
  <p>Shows the author, commit hash, and timestamp for every line in the file. Useful for finding out <em>why</em> a change was made.</p>
</div>

<div id="q18-difference-between-fork-and-branch" class="question">
  18. Difference between Fork and Branch?
  <span class="difficulty beginner">Beginner</span>
</div>

<div class="answer">
  <ul>
    <li><strong>Branch:</strong> A separate line of development <em>within</em> the same repository.</li>
    <li><strong>Fork:</strong> A complete <em>copy</em> of the repository under your own account. Used in Open Source to propose changes (via Pull Request) without having write access to the original repo.</li>
  </ul>
</div>

<div id="q19-how-to-list-all-files-in-a-commit" class="question">
  19. How to list all files in a commit?
  <span class="difficulty beginner">Beginner</span>
</div>

<div class="answer">
  <pre><code class="language-bash">git show --name-only <commit-hash></code></pre>
  <p>Or <code>git diff-tree --no-commit-id --name-only -r <commit-hash></code> for just the filenames.</p>
</div>

<div id="q20-how-to-find-the-common-ancestor-of-two-branches" class="question">
  20. How to find the common ancestor of two branches?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <pre><code class="language-bash">git merge-base branch1 branch2</code></pre>
  <p>This outputs the hash of the best common ancestor commit.</p>
</div>
