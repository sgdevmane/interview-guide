# Algorithms Interview Questions

## Table of Contents

1. [Explain QuickSort vs MergeSort?](#q1-explain-quicksort-vs-mergesort) <span class="intermediate">Intermediate</span>
2. [What is Dynamic Programming (DP)?](#q2-what-is-dynamic-programming-dp) <span class="intermediate">Intermediate</span>
3. [Solve the 'Climbing Stairs' problem?](#q3-solve-the-climbing-stairs-problem) <span class="beginner">Beginner</span>
4. [Explain Dijkstra's Algorithm?](#q4-explain-dijkstras-algorithm) <span class="advanced">Advanced</span>
5. [What is the Knapsack Problem (0/1)?](#q5-what-is-the-knapsack-problem-01) <span class="advanced">Advanced</span>
6. [Binary Search Implementation?](#q6-binary-search-implementation) <span class="beginner">Beginner</span>
7. [Explain Greedy Algorithms with an example?](#q7-explain-greedy-algorithms-with-an-example) <span class="intermediate">Intermediate</span>
8. [Find the Longest Palindromic Substring?](#q8-find-the-longest-palindromic-substring) <span class="advanced">Advanced</span>
9. [What is Backtracking? (N-Queens Problem)?](#q9-what-is-backtracking-n-queens-problem) <span class="advanced">Advanced</span>
10. [Explain Topological Sort?](#q10-explain-topological-sort) <span class="intermediate">Intermediate</span>
11. [Maximum Subarray Sum (Kadane's Algorithm)?](#q11-maximum-subarray-sum-kadanes-algorithm) <span class="intermediate">Intermediate</span>
12. [Detect Cycle in a Graph?](#q12-detect-cycle-in-a-graph) <span class="intermediate">Intermediate</span>
13. [Trapping Rain Water Problem?](#q13-trapping-rain-water-problem) <span class="advanced">Advanced</span>
14. [Search in Rotated Sorted Array?](#q14-search-in-rotated-sorted-array) <span class="intermediate">Intermediate</span>
15. [Merge Intervals?](#q15-merge-intervals) <span class="intermediate">Intermediate</span>
16. [Longest Increasing Subsequence (LIS)?](#q16-longest-increasing-subsequence-lis) <span class="advanced">Advanced</span>
17. [Explain Union-Find Algorithm?](#q17-explain-union-find-algorithm) <span class="advanced">Advanced</span>
18. [Median of Two Sorted Arrays?](#q18-median-of-two-sorted-arrays) <span class="advanced">Advanced</span>
19. [Generate Parentheses (Recursion)?](#q19-generate-parentheses-recursion) <span class="intermediate">Intermediate</span>
20. [Word Search (Grid DFS)?](#q20-word-search-grid-dfs) <span class="intermediate">Intermediate</span>

---

<div id="q1-explain-quicksort-vs-mergesort" class="question">
  1. Explain QuickSort vs MergeSort?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <p>Both are <strong>Divide and Conquer</strong> algorithms with O(n log n) average time complexity.</p>
  <ul>
    <li><strong>MergeSort:</strong>
      <ul>
        <li>Stable sort.</li>
        <li>Worst-case O(n log n).</li>
        <li>Requires O(n) extra space (not in-place).</li>
        <li>Good for Linked Lists and large datasets on disk.</li>
      </ul>
    </li>
    <li><strong>QuickSort:</strong>
      <ul>
        <li>Unstable sort.</li>
        <li>Worst-case O(n²) (rare, happens with bad pivots).</li>
        <li>In-place (O(log n) stack space).</li>
        <li>Generally faster in practice for arrays due to cache locality.</li>
      </ul>
    </li>
  </ul>
</div>

<div id="q2-what-is-dynamic-programming-dp" class="question">
  2. What is Dynamic Programming (DP)?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <p><strong>Dynamic Programming</strong> is an optimization technique for solving recursive problems that have overlapping subproblems and optimal substructure.</p>
  <ul>
    <li><strong>Memoization (Top-Down):</strong> Caching results of recursive calls.</li>
    <li><strong>Tabulation (Bottom-Up):</strong> Solving smaller subproblems iteratively and building up to the final solution.</li>
    <li><strong>Example:</strong> Fibonacci sequence. <code>fib(n) = fib(n-1) + fib(n-2)</code>. Without DP, it recalculates the same values exponentially. With DP, it's O(n).</li>
  </ul>
</div>

<div id="q3-solve-the-climbing-stairs-problem" class="question">
  3. Solve the 'Climbing Stairs' problem?
  <span class="difficulty beginner">Beginner</span>
</div>

<div class="answer">
  <p><strong>Problem:</strong> You are climbing a staircase with N steps. You can climb 1 or 2 steps. How many distinct ways can you reach the top?</p>
  <p><strong>Solution:</strong> This is essentially the Fibonacci sequence.</p>
  <pre><code class="language-javascript">function climbStairs(n) {
  if (n <= 2) return n;
  let first = 1, second = 2;
  for (let i = 3; i <= n; i++) {
    let third = first + second;
    first = second;
    second = third;
  }
  return second;
}</code></pre>
</div>

<div id="q4-explain-dijkstras-algorithm" class="question">
  4. Explain Dijkstra's Algorithm?
  <span class="difficulty advanced">Advanced</span>
</div>

<div class="answer">
  <p><strong>Dijkstra's Algorithm</strong> finds the shortest path from a source node to all other nodes in a weighted graph (with non-negative weights).</p>
  <ul>
    <li>Uses a <strong>Priority Queue</strong> (Min-Heap) to always expand the closest unvisited node.</li>
    <li>Maintains a `distance` array initialized to infinity.</li>
    <li><strong>Relaxation:</strong> If moving from u to v gives a shorter path than currently known for v, update v's distance and push to heap.</li>
    <li><strong>Complexity:</strong> O(E log V) using a binary heap.</li>
  </ul>
</div>

<div id="q5-what-is-the-knapsack-problem-01" class="question">
  5. What is the Knapsack Problem (0/1)?
  <span class="difficulty advanced">Advanced</span>
</div>

<div class="answer">
  <p><strong>Problem:</strong> Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. In 0/1 Knapsack, you can either take an item or leave it (cannot take fraction).</p>
  <p><strong>Solution:</strong> Uses 2D Dynamic Programming.</p>
  <p><code>dp[i][w] = max(dp[i-1][w], value[i] + dp[i-1][w-weight[i]])</code></p>
</div>

<div id="q6-binary-search-implementation" class="question">
  6. Binary Search Implementation?
  <span class="difficulty beginner">Beginner</span>
</div>

<div class="answer">
  <p>Binary search works on sorted arrays. It repeatedly divides the search interval in half.</p>
  <pre><code class="language-javascript">function binarySearch(arr, target) {
  let left = 0;
  let right = arr.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    if (arr[mid] === target) return mid;
    if (arr[mid] < target) left = mid + 1;
    else right = mid - 1;
  }
  return -1;
}</code></pre>
</div>

<div id="q7-explain-greedy-algorithms-with-an-example" class="question">
  7. Explain Greedy Algorithms with an example?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <p>A <strong>Greedy Algorithm</strong> makes the locally optimal choice at each stage with the hope of finding a global optimum.</p>
  <ul>
    <li><strong>Example: Activity Selection Problem.</strong> Given a set of activities with start and end times, select the maximum number of activities that can be performed by a single person.</li>
    <li><strong>Greedy Choice:</strong> Always pick the next activity that finishes earliest. This leaves the maximum time for remaining activities.</li>
    <li>Note: Greedy doesn't work for all problems (e.g., 0/1 Knapsack requires DP, but Fractional Knapsack can use Greedy).</li>
  </ul>
</div>

<div id="q8-find-the-longest-palindromic-substring" class="question">
  8. Find the Longest Palindromic Substring?
  <span class="difficulty advanced">Advanced</span>
</div>

<div class="answer">
  <p><strong>Approach: Expand Around Center</strong></p>
  <ul>
    <li>A palindrome mirrors around its center.</li>
    <li>There are 2N-1 centers (N single characters, N-1 spaces between characters).</li>
    <li>Iterate through each index and expand outwards as long as characters match.</li>
    <li>Time Complexity: O(n²), Space: O(1).</li>
    <li>(Manacher's algorithm exists for O(n) but is rarely asked).</li>
  </ul>
</div>

<div id="q9-what-is-backtracking-n-queens-problem" class="question">
  9. What is Backtracking? (N-Queens Problem)?
  <span class="difficulty advanced">Advanced</span>
</div>

<div class="answer">
  <p><strong>Backtracking</strong> is an algorithmic-technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, and removing those solutions that fail to satisfy the constraints of the problem at any point of time.</p>
  <p><strong>N-Queens:</strong> Place N queens on an NxN chessboard so no two queens attack each other.</p>
  <ul>
    <li>Place a queen in a row.</li>
    <li>Check safety (column, diagonals).</li>
    <li>Recurse to the next row.</li>
    <li>If no safe spot, backtrack (remove queen and try next spot).</li>
  </ul>
</div>

<div id="q10-explain-topological-sort" class="question">
  10. Explain Topological Sort?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <p><strong>Topological Sort</strong> is a linear ordering of vertices in a Directed Acyclic Graph (DAG) such that for every directed edge u -> v, vertex u comes before v in the ordering.</p>
  <ul>
    <li><strong>Use Cases:</strong> Build systems (dependencies), Course scheduling.</li>
    <li><strong>Algorithms:</strong>
      <ul>
        <li><strong>Kahn's Algorithm (BFS):</strong> Uses in-degrees. Nodes with 0 in-degree are processed first.</li>
        <li><strong>DFS Based:</strong> Call DFS on nodes. Add node to stack <em>after</em> visiting all its neighbors. Reverse stack at end.</li>
      </ul>
    </li>
  </ul>
</div>

<div id="q11-maximum-subarray-sum-kadanes-algorithm" class="question">
  11. Maximum Subarray Sum (Kadane's Algorithm)?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <p>Find the contiguous subarray within an array that has the largest sum.</p>
  <pre><code class="language-javascript">function maxSubArray(nums) {
  let currentSum = nums[0];
  let maxSum = nums[0];

  for (let i = 1; i < nums.length; i++) {
    // Either extend the previous subarray or start a new one
    currentSum = Math.max(nums[i], currentSum + nums[i]);
    maxSum = Math.max(maxSum, currentSum);
  }
  return maxSum;
}</code></pre>
  <p>Time Complexity: O(n).</p>
</div>

<div id="q12-detect-cycle-in-a-graph" class="question">
  12. Detect Cycle in a Graph?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <ul>
    <li><strong>Directed Graph:</strong> Use DFS with a recursion stack (visited + recursionStack sets). If you see a node in recursionStack, it's a cycle.</li>
    <li><strong>Undirected Graph:</strong> Use DFS/BFS with a visited set and keep track of the `parent` node. If you see a visited neighbor that is NOT the parent, it's a cycle. Or use Union-Find.</li>
  </ul>
</div>

<div id="q13-trapping-rain-water-problem" class="question">
  13. Trapping Rain Water Problem?
  <span class="difficulty advanced">Advanced</span>
</div>

<div class="answer">
  <p>Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.</p>
  <ul>
    <li><strong>Solution:</strong> For each element, the water it can store is <code>min(max_left, max_right) - height</code>.</li>
    <li><strong>Optimized Approach (Two Pointers):</strong> Maintain <code>left_max</code> and <code>right_max</code> while moving pointers inward. O(n) time, O(1) space.</li>
  </ul>
</div>

<div id="q14-search-in-rotated-sorted-array" class="question">
  14. Search in Rotated Sorted Array?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <p>Modified Binary Search. One half of the array will always be sorted.</p>
  <ol>
    <li>Find mid.</li>
    <li>Check if left half is sorted (nums[left] <= nums[mid]).</li>
    <li>If sorted, check if target is in that range. If so, search left, else search right.</li>
    <li>Else (right half is sorted), check if target is in right range.</li>
  </ol>
</div>

<div id="q15-merge-intervals" class="question">
  15. Merge Intervals?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <p>Given an array of intervals, merge all overlapping intervals.</p>
  <ul>
    <li>Sort intervals by start time.</li>
    <li>Iterate through sorted intervals.</li>
    <li>If current interval overlaps with the previous merged interval (current.start <= previous.end), merge them (new end = max(prev.end, curr.end)).</li>
    <li>Else, add current interval to result.</li>
  </ul>
</div>

<div id="q16-longest-increasing-subsequence-lis" class="question">
  16. Longest Increasing Subsequence (LIS)?
  <span class="difficulty advanced">Advanced</span>
</div>

<div class="answer">
  <p>Find the length of the longest subsequence of a given sequence such that all elements of the subsequence are sorted in increasing order.</p>
  <ul>
    <li><strong>DP Solution:</strong> <code>dp[i]</code> = length of LIS ending at index i. O(n²).</li>
    <li><strong>Patience Sorting Solution:</strong> Use a tail array and binary search to append/replace elements. O(n log n).</li>
  </ul>
</div>

<div id="q17-explain-union-find-algorithm" class="question">
  17. Explain Union-Find Algorithm?
  <span class="difficulty advanced">Advanced</span>
</div>

<div class="answer">
  <p>Also known as Disjoint Set Union (DSU). Supports <code>union(x, y)</code> and <code>find(x)</code>.</p>
  <ul>
    <li><strong>Find:</strong> Returns the representative (root) of the set containing x. Uses <strong>Path Compression</strong> to flatten the tree structure.</li>
    <li><strong>Union:</strong> Merges two sets. Uses <strong>Union by Rank/Size</strong> to attach the smaller tree to the larger one.</li>
    <li><strong>Complexity:</strong> Nearly O(1) (amortized inverse Ackermann function). Used in Kruskal's algorithm.</li>
  </ul>
</div>

<div id="q18-median-of-two-sorted-arrays" class="question">
  18. Median of Two Sorted Arrays?
  <span class="difficulty advanced">Advanced</span>
</div>

<div class="answer">
  <p>Find the median of two sorted arrays of size m and n in O(log(m+n)).</p>
  <ul>
    <li>This requires a partition-based binary search on the smaller array.</li>
    <li>We try to cut both arrays such that the left halves contain half the total elements, and every element in left halves <= every element in right halves.</li>
  </ul>
</div>

<div id="q19-generate-parentheses-recursion" class="question">
  19. Generate Parentheses (Recursion)?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <p>Generate all combinations of well-formed parentheses for n pairs.</p>
  <ul>
    <li>Use Backtracking/Recursion.</li>
    <li>Keep track of <code>open</code> and <code>close</code> counts.</li>
    <li>Add <code>(</code> if <code>open < n</code>.</li>
    <li>Add <code>)</code> if <code>close < open</code>.</li>
    <li>Base case: string length == 2*n.</li>
  </ul>
</div>

<div id="q20-word-search-grid-dfs" class="question">
  20. Word Search (Grid DFS)?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <p>Given a 2D board and a word, find if the word exists in the grid.</p>
  <ul>
    <li>Iterate through every cell. If cell matches first char, start DFS.</li>
    <li>DFS checks neighbors (up, down, left, right).</li>
    <li>Mark cells as visited (temporarily) to avoid cycles in current path.</li>
    <li>Backtrack if path fails.</li>
  </ul>
</div>
