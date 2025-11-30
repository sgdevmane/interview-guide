# Algorithms Interview Questions

## Table of Contents

1. [Explain QuickSort vs MergeSort?](#q1) <span class="intermediate">Intermediate</span>
2. [What is Dynamic Programming (DP)?](#q2) <span class="intermediate">Intermediate</span>
3. [Solve the 'Climbing Stairs' problem?](#q3) <span class="beginner">Beginner</span>
4. [Explain Dijkstra's Algorithm?](#q4) <span class="advanced">Advanced</span>
5. [What is the Knapsack Problem (0/1)?](#q5) <span class="advanced">Advanced</span>
6. [Binary Search Implementation?](#q6) <span class="beginner">Beginner</span>
7. [Explain Greedy Algorithms with an example?](#q7) <span class="intermediate">Intermediate</span>
8. [Find the Longest Palindromic Substring?](#q8) <span class="advanced">Advanced</span>
9. [What is Backtracking? (N-Queens Problem)?](#q9) <span class="advanced">Advanced</span>
10. [Explain Topological Sort?](#q10) <span class="intermediate">Intermediate</span>
11. [Maximum Subarray Sum (Kadane's Algorithm)?](#q11) <span class="intermediate">Intermediate</span>
12. [Detect Cycle in a Graph?](#q12) <span class="intermediate">Intermediate</span>
13. [Trapping Rain Water Problem?](#q13) <span class="advanced">Advanced</span>
14. [Search in Rotated Sorted Array?](#q14) <span class="intermediate">Intermediate</span>
15. [Merge Intervals?](#q15) <span class="intermediate">Intermediate</span>
16. [Longest Increasing Subsequence (LIS)?](#q16) <span class="advanced">Advanced</span>
17. [Explain Union-Find Algorithm?](#q17) <span class="advanced">Advanced</span>
18. [Median of Two Sorted Arrays?](#q18) <span class="advanced">Advanced</span>
19. [Generate Parentheses (Recursion)?](#q19) <span class="intermediate">Intermediate</span>
20. [Word Search (Grid DFS)?](#q20) <span class="intermediate">Intermediate</span>
21. [Reverse Linked List?](#q21) <span class="beginner">Beginner</span>
22. [Valid Anagram?](#q22) <span class="beginner">Beginner</span>
23. [Group Anagrams?](#q23) <span class="intermediate">Intermediate</span>
24. [Top K Frequent Elements?](#q24) <span class="intermediate">Intermediate</span>
25. [Product of Array Except Self?](#q25) <span class="intermediate">Intermediate</span>
26. [Valid Sudoku?](#q26) <span class="intermediate">Intermediate</span>
27. [Longest Consecutive Sequence?](#q27) <span class="intermediate">Intermediate</span>
28. [Valid Palindrome?](#q28) <span class="beginner">Beginner</span>
29. [3Sum Problem?](#q29) <span class="intermediate">Intermediate</span>
30. [Container With Most Water?](#q30) <span class="intermediate">Intermediate</span>
31. [Best Time to Buy and Sell Stock?](#q31) <span class="beginner">Beginner</span>
32. [Longest Substring Without Repeating Characters?](#q32) <span class="intermediate">Intermediate</span>
33. [Longest Repeating Character Replacement?](#q33) <span class="intermediate">Intermediate</span>
34. [Minimum Window Substring?](#q34) <span class="advanced">Advanced</span>
35. [Valid Parentheses?](#q35) <span class="beginner">Beginner</span>
36. [Min Stack Implementation?](#q36) <span class="intermediate">Intermediate</span>
37. [Evaluate Reverse Polish Notation?](#q37) <span class="intermediate">Intermediate</span>
38. [Daily Temperatures?](#q38) <span class="intermediate">Intermediate</span>
39. [Car Fleet?](#q39) <span class="intermediate">Intermediate</span>
40. [Largest Rectangle in Histogram?](#q40) <span class="advanced">Advanced</span>
41. [Search a 2D Matrix?](#q41) <span class="intermediate">Intermediate</span>
42. [Koko Eating Bananas?](#q42) <span class="intermediate">Intermediate</span>
43. [Find Minimum in Rotated Sorted Array?](#q43) <span class="intermediate">Intermediate</span>
44. [Time Based Key-Value Store?](#q44) <span class="intermediate">Intermediate</span>
45. [Find the Duplicate Number?](#q45) <span class="intermediate">Intermediate</span>
46. [Merge k Sorted Lists?](#q46) <span class="advanced">Advanced</span>
47. [Reverse Nodes in k-Group?](#q47) <span class="advanced">Advanced</span>
48. [Subtree of Another Tree?](#q48) <span class="beginner">Beginner</span>
49. [Lowest Common Ancestor of a BST?](#q49) <span class="intermediate">Intermediate</span>
50. [Binary Tree Level Order Traversal?](#q50) <span class="intermediate">Intermediate</span>
51. [Validate Binary Search Tree?](#q51) <span class="intermediate">Intermediate</span>
52. [Kth Smallest Element in a BST?](#q52) <span class="intermediate">Intermediate</span>
53. [Construct Binary Tree from Preorder and Inorder?](#q53) <span class="intermediate">Intermediate</span>
54. [Binary Tree Maximum Path Sum?](#q54) <span class="advanced">Advanced</span>
55. [Serialize and Deserialize Binary Tree?](#q55) <span class="advanced">Advanced</span>
56. [Implement Trie (Prefix Tree)?](#q56) <span class="intermediate">Intermediate</span>
57. [Design Add and Search Words Data Structure?](#q57) <span class="intermediate">Intermediate</span>
58. [Word Search II?](#q58) <span class="advanced">Advanced</span>
59. [Number of Islands?](#q59) <span class="intermediate">Intermediate</span>
60. [Clone Graph?](#q60) <span class="intermediate">Intermediate</span>
61. [Max Area of Island?](#q61) <span class="intermediate">Intermediate</span>
62. [Pacific Atlantic Water Flow?](#q62) <span class="intermediate">Intermediate</span>
63. [Surrounded Regions?](#q63) <span class="intermediate">Intermediate</span>
64. [Rotting Oranges?](#q64) <span class="intermediate">Intermediate</span>
65. [Walls and Gates?](#q65) <span class="intermediate">Intermediate</span>
66. [Course Schedule?](#q66) <span class="intermediate">Intermediate</span>
67. [Graph Valid Tree?](#q67) <span class="intermediate">Intermediate</span>
68. [Number of Connected Components?](#q68) <span class="intermediate">Intermediate</span>
69. [Redundant Connection?](#q69) <span class="intermediate">Intermediate</span>
70. [Min Cost Climbing Stairs?](#q70) <span class="beginner">Beginner</span>
71. [House Robber?](#q71) <span class="intermediate">Intermediate</span>
72. [House Robber II?](#q72) <span class="intermediate">Intermediate</span>
73. [Palindromic Substrings?](#q73) <span class="intermediate">Intermediate</span>
74. [Decode Ways?](#q74) <span class="intermediate">Intermediate</span>
75. [Coin Change?](#q75) <span class="intermediate">Intermediate</span>
76. [Maximum Product Subarray?](#q76) <span class="intermediate">Intermediate</span>
77. [Word Break?](#q77) <span class="intermediate">Intermediate</span>
78. [Longest Common Subsequence?](#q78) <span class="intermediate">Intermediate</span>
79. [Jump Game?](#q79) <span class="intermediate">Intermediate</span>
80. [Unique Paths?](#q80) <span class="intermediate">Intermediate</span>
81. [Partition Equal Subset Sum?](#q81) <span class="intermediate">Intermediate</span>
82. [Insert Interval?](#q82) <span class="intermediate">Intermediate</span>
83. [Non-overlapping Intervals?](#q83) <span class="intermediate">Intermediate</span>
84. [Meeting Rooms?](#q84) <span class="beginner">Beginner</span>
85. [Meeting Rooms II?](#q85) <span class="intermediate">Intermediate</span>
86. [Rotate Image?](#q86) <span class="intermediate">Intermediate</span>
87. [Spiral Matrix?](#q87) <span class="intermediate">Intermediate</span>
88. [Set Matrix Zeroes?](#q88) <span class="intermediate">Intermediate</span>
89. [Happy Number?](#q89) <span class="beginner">Beginner</span>
90. [Plus One?](#q90) <span class="beginner">Beginner</span>
91. [Pow(x, n)?](#q91) <span class="intermediate">Intermediate</span>
92. [Multiply Strings?](#q92) <span class="intermediate">Intermediate</span>
93. [Detect Squares?](#q93) <span class="intermediate">Intermediate</span>
94. [Single Number?](#q94) <span class="beginner">Beginner</span>
95. [Number of 1 Bits?](#q95) <span class="beginner">Beginner</span>
96. [Counting Bits?](#q96) <span class="beginner">Beginner</span>
97. [Reverse Bits?](#q97) <span class="beginner">Beginner</span>
98. [Missing Number?](#q98) <span class="beginner">Beginner</span>
99. [Sum of Two Integers (No + or -)?](#q99) <span class="intermediate">Intermediate</span>
100. [Alien Dictionary?](#q100) <span class="advanced">Advanced</span>

---

<div id="q1" class="question">1. Explain QuickSort vs MergeSort? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Both are <strong>Divide and Conquer</strong> algorithms.</p>
  <ul>
    <li><strong>MergeSort:</strong> Stable, O(n log n) worst-case, O(n) space. Good for Linked Lists.</li>
    <li><strong>QuickSort:</strong> Unstable, O(n²) worst-case (rare), O(log n) space. Generally faster due to cache locality.</li>
  </ul>
<pre><code class="language-javascript">// QuickSort Implementation
function quickSort(arr) {
  if (arr.length <= 1) return arr;
  const pivot = arr[arr.length - 1];
  const left = [], right = [];
  for (let i = 0; i < arr.length - 1; i++) {
    if (arr[i] < pivot) left.push(arr[i]);
    else right.push(arr[i]);
  }
  return [...quickSort(left), pivot, ...quickSort(right)];
}</code></pre>
</div>

<div id="q2" class="question">2. What is Dynamic Programming (DP)? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Optimization for recursive problems with overlapping subproblems.</p>
  <pre><code class="language-javascript">// Fibonacci with Memoization
const memo = {};
function fib(n) {
  if (n <= 1) return n;
  if (n in memo) return memo[n];
  memo[n] = fib(n - 1) + fib(n - 2);
  return memo[n];
}</code></pre>
</div>

<div id="q3" class="question">3. Solve the 'Climbing Stairs' problem? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Distinct ways to reach top of N stairs taking 1 or 2 steps.</p>
<pre><code class="language-javascript">var climbStairs = function(n) {
  if (n <= 2) return n;
  let a = 1, b = 2;
  for (let i = 3; i <= n; i++) {
    let temp = a + b;
    a = b;
    b = temp;
  }
  return b;
};</code></pre>
</div>

<div id="q4" class="question">4. Explain Dijkstra's Algorithm? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Shortest path in weighted graph using Priority Queue.</p>
<pre><code class="language-javascript">// Conceptual (requires PriorityQueue class)
function dijkstra(graph, start) {
  const distances = {};
  // Initialize distances to Infinity, start to 0
  // Loop: pop min distance node, update neighbors
}</code></pre>
</div>

<div id="q5" class="question">5. What is the Knapsack Problem (0/1)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Maximize value within weight limit.</p>
<pre><code class="language-javascript">function knapsack(weights, values, capacity) {
  const n = weights.length;
  const dp = Array(capacity + 1).fill(0);
  for (let i = 0; i < n; i++) {
    for (let w = capacity; w >= weights[i]; w--) {
      dp[w] = Math.max(dp[w], dp[w - weights[i]] + values[i]);
    }
  }
  return dp[capacity];
}</code></pre>
</div>

<div id="q6" class="question">6. Binary Search Implementation? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
<pre><code class="language-javascript">function binarySearch(nums, target) {
  let left = 0, right = nums.length - 1;
  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    if (nums[mid] === target) return mid;
    if (nums[mid] < target) left = mid + 1;
    else right = mid - 1;
  }
  return -1;
}</code></pre>
</div>

<div id="q7" class="question">7. Explain Greedy Algorithms? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Making the locally optimal choice.</p>
<pre><code class="language-javascript">// Activity Selection
function maxActivities(start, finish) {
  let i = 0, count = 1; // Select first
  for (let j = 1; j < start.length; j++) {
    if (start[j] >= finish[i]) {
      count++;
      i = j;
    }
  }
  return count;
}</code></pre>
</div>

<div id="q8" class="question">8. Find the Longest Palindromic Substring? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
<pre><code class="language-javascript">var longestPalindrome = function(s) {
  let res = "";
  for (let i = 0; i < s.length; i++) {
    // Odd length
    expand(i, i);
    // Even length
    expand(i, i + 1);
  }
  function expand(l, r) {
    while (l >= 0 && r < s.length && s[l] === s[r]) {
      if (r - l + 1 > res.length) res = s.substring(l, r + 1);
      l--; r++;
    }
  }
  return res;
};</code></pre>
</div>

<div id="q9" class="question">9. What is Backtracking? (N-Queens)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Solving incrementally and removing bad solutions.</p>
<pre><code class="language-javascript">// Core concept
function solveNQueens(n) {
  // place queen, check validity, recurse
  // if invalid, backtrack (remove queen)
}</code></pre>
</div>

<div id="q10" class="question">10. Explain Topological Sort? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Linear ordering of DAG.</p>
<pre><code class="language-javascript">// Kahn's Algorithm (BFS)
function topSort(numCourses, prerequisites) {
  let inDegree = new Array(numCourses).fill(0);
  // Build graph, count in-degrees, add 0 in-degree to queue
  // Process queue, reduce neighbor in-degrees
}</code></pre>
</div>

<div id="q11" class="question">11. Maximum Subarray Sum? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var maxSubArray = function(nums) {
  let curr = nums[0], max = nums[0];
  for (let i = 1; i < nums.length; i++) {
    curr = Math.max(nums[i], curr + nums[i]);
    max = Math.max(max, curr);
  }
  return max;
};</code></pre>
</div>

<div id="q12" class="question">12. Detect Cycle in a Graph? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">function hasCycle(graph) {
  const visited = new Set(), recursionStack = new Set();
  function dfs(node) {
    if (recursionStack.has(node)) return true;
    if (visited.has(node)) return false;
    visited.add(node);
    recursionStack.add(node);
    for (let neighbor of graph[node]) {
      if (dfs(neighbor)) return true;
    }
    recursionStack.delete(node);
    return false;
  }
  // Call DFS for all nodes
}</code></pre>
</div>

<div id="q13" class="question">13. Trapping Rain Water? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
<pre><code class="language-javascript">var trap = function(height) {
  let l = 0, r = height.length - 1, res = 0;
  let maxL = height[l], maxR = height[r];
  while (l < r) {
    if (maxL < maxR) {
      l++;
      maxL = Math.max(maxL, height[l]);
      res += maxL - height[l];
    } else {
      r--;
      maxR = Math.max(maxR, height[r]);
      res += maxR - height[r];
    }
  }
  return res;
};</code></pre>
</div>

<div id="q14" class="question">14. Search in Rotated Sorted Array? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var search = function(nums, target) {
  let l = 0, r = nums.length - 1;
  while (l <= r) {
    let mid = Math.floor((l + r) / 2);
    if (nums[mid] === target) return mid;
    if (nums[l] <= nums[mid]) { // Left sorted
      if (target >= nums[l] && target < nums[mid]) r = mid - 1;
      else l = mid + 1;
    } else { // Right sorted
      if (target > nums[mid] && target <= nums[r]) l = mid + 1;
      else r = mid - 1;
    }
  }
  return -1;
};</code></pre>
</div>

<div id="q15" class="question">15. Merge Intervals? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var merge = function(intervals) {
  intervals.sort((a, b) => a[0] - b[0]);
  const res = [intervals[0]];
  for (let i = 1; i < intervals.length; i++) {
    let last = res[res.length - 1];
    if (intervals[i][0] <= last[1]) {
      last[1] = Math.max(last[1], intervals[i][1]);
    } else {
      res.push(intervals[i]);
    }
  }
  return res;
};</code></pre>
</div>

<div id="q16" class="question">16. Longest Increasing Subsequence? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
<pre><code class="language-javascript">var lengthOfLIS = function(nums) {
  const dp = Array(nums.length).fill(1);
  for (let i = 1; i < nums.length; i++) {
    for (let j = 0; j < i; j++) {
      if (nums[i] > nums[j]) dp[i] = Math.max(dp[i], dp[j] + 1);
    }
  }
  return Math.max(...dp);
};</code></pre>
</div>

<div id="q17" class="question">17. Explain Union-Find? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
<pre><code class="language-javascript">class UnionFind {
  constructor(n) {
    this.parent = Array(n).fill(0).map((_, i) => i);
  }
  find(x) {
    if (this.parent[x] !== x) this.parent[x] = this.find(this.parent[x]);
    return this.parent[x];
  }
  union(x, y) {
    this.parent[this.find(x)] = this.find(y);
  }
}</code></pre>
</div>

<div id="q18" class="question">18. Median of Two Sorted Arrays? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Requires Binary Search on partition.</p>
<pre><code class="language-javascript">// Complex implementation involving partitioning A and B
// such that left parts == right parts size
// and max(leftA, leftB) <= min(rightA, rightB)</code></pre>
</div>

<div id="q19" class="question">19. Generate Parentheses? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var generateParenthesis = function(n) {
  const res = [];
  function backtrack(s, open, close) {
    if (s.length === n * 2) { res.push(s); return; }
    if (open < n) backtrack(s + "(", open + 1, close);
    if (close < open) backtrack(s + ")", open, close + 1);
  }
  backtrack("", 0, 0);
  return res;
};</code></pre>
</div>

<div id="q20" class="question">20. Word Search? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var exist = function(board, word) {
  for (let r = 0; r < board.length; r++)
    for (let c = 0; c < board[0].length; c++)
      if (dfs(r, c, 0)) return true;
  
  function dfs(r, c, i) {
    if (i === word.length) return true;
    if (r < 0 || c < 0 || r >= board.length || c >= board[0].length || board[r][c] !== word[i]) return false;
    let temp = board[r][c];
    board[r][c] = '#'; // visited
    let found = dfs(r+1,c,i+1) || dfs(r-1,c,i+1) || dfs(r,c+1,i+1) || dfs(r,c-1,i+1);
    board[r][c] = temp;
    return found;
  }
  return false;
};</code></pre>
</div>

<div id="q21" class="question">21. Reverse Linked List? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
<pre><code class="language-javascript">var reverseList = function(head) {
  let prev = null, curr = head;
  while (curr) {
    let next = curr.next;
    curr.next = prev;
    prev = curr;
    curr = next;
  }
  return prev;
};</code></pre>
</div>

<div id="q22" class="question">22. Valid Anagram? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
<pre><code class="language-javascript">var isAnagram = function(s, t) {
  if (s.length !== t.length) return false;
  const count = {};
  for (let c of s) count[c] = (count[c] || 0) + 1;
  for (let c of t) {
    if (!count[c]) return false;
    count[c]--;
  }
  return true;
};</code></pre>
</div>

<div id="q23" class="question">23. Group Anagrams? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var groupAnagrams = function(strs) {
  const map = {};
  for (let s of strs) {
    // Sort string to use as key
    const key = s.split('').sort().join('');
    if (!map[key]) map[key] = [];
    map[key].push(s);
  }
  return Object.values(map);
};</code></pre>
</div>

<div id="q24" class="question">24. Top K Frequent Elements? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var topKFrequent = function(nums, k) {
  const map = new Map();
  nums.forEach(n => map.set(n, (map.get(n) || 0) + 1));
  return [...map.entries()]
    .sort((a, b) => b[1] - a[1])
    .slice(0, k)
    .map(x => x[0]);
};</code></pre>
</div>

<div id="q25" class="question">25. Product of Array Except Self? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var productExceptSelf = function(nums) {
  const res = [];
  let prefix = 1;
  for (let i = 0; i < nums.length; i++) {
    res[i] = prefix;
    prefix *= nums[i];
  }
  let postfix = 1;
  for (let i = nums.length - 1; i >= 0; i--) {
    res[i] *= postfix;
    postfix *= nums[i];
  }
  return res;
};</code></pre>
</div>

<div id="q26" class="question">26. Valid Sudoku? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var isValidSudoku = function(board) {
  const rows = [], cols = [], boxes = [];
  for (let i = 0; i < 9; i++) {
    rows.push(new Set()); cols.push(new Set()); boxes.push(new Set());
  }
  for (let r = 0; r < 9; r++) {
    for (let c = 0; c < 9; c++) {
      let val = board[r][c];
      if (val === '.') continue;
      let boxIdx = Math.floor(r/3) * 3 + Math.floor(c/3);
      if (rows[r].has(val) || cols[c].has(val) || boxes[boxIdx].has(val)) return false;
      rows[r].add(val); cols[c].add(val); boxes[boxIdx].add(val);
    }
  }
  return true;
};</code></pre>
</div>

<div id="q27" class="question">27. Longest Consecutive Sequence? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var longestConsecutive = function(nums) {
  const set = new Set(nums);
  let max = 0;
  for (let n of set) {
    if (!set.has(n - 1)) { // Start of sequence
      let len = 0;
      while (set.has(n + len)) len++;
      max = Math.max(max, len);
    }
  }
  return max;
};</code></pre>
</div>

<div id="q28" class="question">28. Valid Palindrome? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
<pre><code class="language-javascript">var isPalindrome = function(s) {
  s = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
  let l = 0, r = s.length - 1;
  while (l < r) {
    if (s[l] !== s[r]) return false;
    l++; r--;
  }
  return true;
};</code></pre>
</div>

<div id="q29" class="question">29. 3Sum Problem? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var threeSum = function(nums) {
  nums.sort((a, b) => a - b);
  const res = [];
  for (let i = 0; i < nums.length - 2; i++) {
    if (i > 0 && nums[i] === nums[i-1]) continue;
    let l = i + 1, r = nums.length - 1;
    while (l < r) {
      let sum = nums[i] + nums[l] + nums[r];
      if (sum === 0) {
        res.push([nums[i], nums[l], nums[r]]);
        while (nums[l] === nums[l+1]) l++;
        while (nums[r] === nums[r-1]) r--;
        l++; r--;
      } else if (sum < 0) l++;
      else r--;
    }
  }
  return res;
};</code></pre>
</div>

<div id="q30" class="question">30. Container With Most Water? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var maxArea = function(height) {
  let l = 0, r = height.length - 1, max = 0;
  while (l < r) {
    let area = (r - l) * Math.min(height[l], height[r]);
    max = Math.max(max, area);
    if (height[l] < height[r]) l++;
    else r--;
  }
  return max;
};</code></pre>
</div>

<div id="q31" class="question">31. Best Time to Buy and Sell Stock? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
<pre><code class="language-javascript">var maxProfit = function(prices) {
  let minPrice = Infinity, maxP = 0;
  for (let p of prices) {
    if (p < minPrice) minPrice = p;
    else if (p - minPrice > maxP) maxP = p - minPrice;
  }
  return maxP;
};</code></pre>
</div>

<div id="q32" class="question">32. Longest Substring Without Repeating Characters? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var lengthOfLongestSubstring = function(s) {
  const set = new Set();
  let l = 0, max = 0;
  for (let r = 0; r < s.length; r++) {
    while (set.has(s[r])) {
      set.delete(s[l]);
      l++;
    }
    set.add(s[r]);
    max = Math.max(max, r - l + 1);
  }
  return max;
};</code></pre>
</div>

<div id="q33" class="question">33. Longest Repeating Character Replacement? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var characterReplacement = function(s, k) {
  const count = {};
  let res = 0, l = 0, maxF = 0;
  for (let r = 0; r < s.length; r++) {
    count[s[r]] = (count[s[r]] || 0) + 1;
    maxF = Math.max(maxF, count[s[r]]);
    // Window len - maxFreq > k means we need to shrink
    if ((r - l + 1) - maxF > k) {
      count[s[l]]--;
      l++;
    }
    res = Math.max(res, r - l + 1);
  }
  return res;
};</code></pre>
</div>

<div id="q34" class="question">34. Minimum Window Substring? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
<pre><code class="language-javascript">var minWindow = function(s, t) {
  const need = {}, have = {};
  for (let c of t) need[c] = (need[c] || 0) + 1;
  let matches = 0, needed = Object.keys(need).length;
  let l = 0, res = [-1, -1], minLen = Infinity;
  
  for (let r = 0; r < s.length; r++) {
    let c = s[r];
    have[c] = (have[c] || 0) + 1;
    if (need[c] && have[c] === need[c]) matches++;
    
    while (matches === needed) {
      if (r - l + 1 < minLen) {
        minLen = r - l + 1;
        res = [l, r];
      }
      have[s[l]]--;
      if (need[s[l]] && have[s[l]] < need[s[l]]) matches--;
      l++;
    }
  }
  return minLen === Infinity ? "" : s.substring(res[0], res[1] + 1);
};</code></pre>
</div>

<div id="q35" class="question">35. Valid Parentheses? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
<pre><code class="language-javascript">var isValid = function(s) {
  const stack = [], map = { ')': '(', ']': '[', '}': '{' };
  for (let c of s) {
    if (c in map) {
      if (stack.length && stack[stack.length - 1] === map[c]) stack.pop();
      else return false;
    } else stack.push(c);
  }
  return stack.length === 0;
};</code></pre>
</div>

<div id="q36" class="question">36. Min Stack Implementation? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">class MinStack {
  constructor() {
    this.stack = [];
    this.minStack = [];
  }
  push(val) {
    this.stack.push(val);
    if (!this.minStack.length || val <= this.minStack[this.minStack.length - 1]) {
      this.minStack.push(val);
    }
  }
  pop() {
    let val = this.stack.pop();
    if (val === this.minStack[this.minStack.length - 1]) this.minStack.pop();
  }
  top() { return this.stack[this.stack.length - 1]; }
  getMin() { return this.minStack[this.minStack.length - 1]; }
}</code></pre>
</div>

<div id="q37" class="question">37. Evaluate Reverse Polish Notation? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var evalRPN = function(tokens) {
  const stack = [];
  for (let t of tokens) {
    if (!isNaN(t)) stack.push(Number(t));
    else {
      let b = stack.pop(), a = stack.pop();
      if (t === '+') stack.push(a + b);
      else if (t === '-') stack.push(a - b);
      else if (t === '*') stack.push(a * b);
      else stack.push(Math.trunc(a / b));
    }
  }
  return stack[0];
};</code></pre>
</div>

<div id="q38" class="question">38. Daily Temperatures? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var dailyTemperatures = function(T) {
  const res = Array(T.length).fill(0);
  const stack = []; // [temp, index]
  for (let i = 0; i < T.length; i++) {
    while (stack.length && T[i] > stack[stack.length - 1][0]) {
      let [temp, idx] = stack.pop();
      res[idx] = i - idx;
    }
    stack.push([T[i], i]);
  }
  return res;
};</code></pre>
</div>

<div id="q39" class="question">39. Car Fleet? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var carFleet = function(target, position, speed) {
  const cars = position.map((p, i) => [p, speed[i]]).sort((a, b) => b[0] - a[0]);
  let fleets = 0, prevTime = 0;
  for (let [p, s] of cars) {
    let time = (target - p) / s;
    if (time > prevTime) {
      fleets++;
      prevTime = time;
    }
  }
  return fleets;
};</code></pre>
</div>

<div id="q40" class="question">40. Largest Rectangle in Histogram? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
<pre><code class="language-javascript">var largestRectangleArea = function(heights) {
  let maxArea = 0, stack = []; // [index, height]
  for (let i = 0; i < heights.length; i++) {
    let start = i;
    while (stack.length && stack[stack.length - 1][1] > heights[i]) {
      let [idx, h] = stack.pop();
      maxArea = Math.max(maxArea, h * (i - idx));
      start = idx;
    }
    stack.push([start, heights[i]]);
  }
  for (let [idx, h] of stack) {
    maxArea = Math.max(maxArea, h * (heights.length - idx));
  }
  return maxArea;
};</code></pre>
</div>

<div id="q41" class="question">41. Search a 2D Matrix? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var searchMatrix = function(matrix, target) {
  let rows = matrix.length, cols = matrix[0].length;
  let l = 0, r = rows * cols - 1;
  while (l <= r) {
    let mid = Math.floor((l + r) / 2);
    let val = matrix[Math.floor(mid / cols)][mid % cols];
    if (val === target) return true;
    if (val < target) l = mid + 1;
    else r = mid - 1;
  }
  return false;
};</code></pre>
</div>

<div id="q42" class="question">42. Koko Eating Bananas? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var minEatingSpeed = function(piles, h) {
  let l = 1, r = Math.max(...piles), res = r;
  while (l <= r) {
    let k = Math.floor((l + r) / 2);
    let hours = 0;
    for (let p of piles) hours += Math.ceil(p / k);
    if (hours <= h) {
      res = k;
      r = k - 1;
    } else l = k + 1;
  }
  return res;
};</code></pre>
</div>

<div id="q43" class="question">43. Find Minimum in Rotated Sorted Array? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var findMin = function(nums) {
  let l = 0, r = nums.length - 1;
  while (l < r) {
    let mid = Math.floor((l + r) / 2);
    if (nums[mid] > nums[r]) l = mid + 1;
    else r = mid;
  }
  return nums[l];
};</code></pre>
</div>

<div id="q44" class="question">44. Time Based Key-Value Store? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">class TimeMap {
  constructor() { this.store = {}; }
  set(key, value, timestamp) {
    if (!this.store[key]) this.store[key] = [];
    this.store[key].push([value, timestamp]);
  }
  get(key, timestamp) {
    let arr = this.store[key] || [];
    let l = 0, r = arr.length - 1, res = "";
    while (l <= r) {
      let mid = Math.floor((l + r) / 2);
      if (arr[mid][1] <= timestamp) {
        res = arr[mid][0];
        l = mid + 1;
      } else r = mid - 1;
    }
    return res;
  }
}</code></pre>
</div>

<div id="q45" class="question">45. Find the Duplicate Number? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Floyd's Tortoise and Hare (Cycle Detection).</p>
<pre><code class="language-javascript">var findDuplicate = function(nums) {
  let slow = nums[0], fast = nums[0];
  do {
    slow = nums[slow];
    fast = nums[nums[fast]];
  } while (slow !== fast);
  
  slow = nums[0];
  while (slow !== fast) {
    slow = nums[slow];
    fast = nums[fast];
  }
  return slow;
};</code></pre>
</div>

<div id="q46" class="question">46. Merge k Sorted Lists? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
<pre><code class="language-javascript">var mergeKLists = function(lists) {
  if (lists.length === 0) return null;
  while (lists.length > 1) {
    let a = lists.shift();
    let b = lists.shift();
    lists.push(merge(a, b));
  }
  return lists[0];
};
function merge(l1, l2) {
  if (!l1) return l2;
  if (!l2) return l1;
  if (l1.val < l2.val) { l1.next = merge(l1.next, l2); return l1; }
  else { l2.next = merge(l1, l2.next); return l2; }
}</code></pre>
</div>

<div id="q47" class="question">47. Reverse Nodes in k-Group? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
<pre><code class="language-javascript">var reverseKGroup = function(head, k) {
  let curr = head, count = 0;
  while (curr && count < k) { curr = curr.next; count++; }
  if (count === k) {
    curr = reverseKGroup(curr, k);
    while (count-- > 0) {
      let temp = head.next;
      head.next = curr;
      curr = head;
      head = temp;
    }
    head = curr;
  }
  return head;
};</code></pre>
</div>

<div id="q48" class="question">48. Subtree of Another Tree? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
<pre><code class="language-javascript">var isSubtree = function(root, subRoot) {
  if (!root) return false;
  if (isSame(root, subRoot)) return true;
  return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
};
function isSame(p, q) {
  if (!p && !q) return true;
  if (!p || !q || p.val !== q.val) return false;
  return isSame(p.left, q.left) && isSame(p.right, q.right);
}</code></pre>
</div>

<div id="q49" class="question">49. Lowest Common Ancestor of a BST? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var lowestCommonAncestor = function(root, p, q) {
  if (p.val < root.val && q.val < root.val) 
    return lowestCommonAncestor(root.left, p, q);
  if (p.val > root.val && q.val > root.val) 
    return lowestCommonAncestor(root.right, p, q);
  return root;
};</code></pre>
</div>

<div id="q50" class="question">50. Binary Tree Level Order Traversal? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var levelOrder = function(root) {
  if (!root) return [];
  const res = [], q = [root];
  while (q.length) {
    const level = [], len = q.length;
    for (let i = 0; i < len; i++) {
      let node = q.shift();
      level.push(node.val);
      if (node.left) q.push(node.left);
      if (node.right) q.push(node.right);
    }
    res.push(level);
  }
  return res;
};</code></pre>
</div>

<div id="q51" class="question">51. Validate Binary Search Tree? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var isValidBST = function(root, min = -Infinity, max = Infinity) {
  if (!root) return true;
  if (root.val <= min || root.val >= max) return false;
  return isValidBST(root.left, min, root.val) && isValidBST(root.right, root.val, max);
};</code></pre>
</div>

<div id="q52" class="question">52. Kth Smallest Element in a BST? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var kthSmallest = function(root, k) {
  const stack = [];
  while (root || stack.length) {
    while (root) {
      stack.push(root);
      root = root.left;
    }
    root = stack.pop();
    k--;
    if (k === 0) return root.val;
    root = root.right;
  }
};</code></pre>
</div>

<div id="q53" class="question">53. Construct Binary Tree from Preorder and Inorder? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var buildTree = function(preorder, inorder) {
  if (!preorder.length || !inorder.length) return null;
  let root = new TreeNode(preorder[0]);
  let mid = inorder.indexOf(preorder[0]);
  root.left = buildTree(preorder.slice(1, mid + 1), inorder.slice(0, mid));
  root.right = buildTree(preorder.slice(mid + 1), inorder.slice(mid + 1));
  return root;
};</code></pre>
</div>

<div id="q54" class="question">54. Binary Tree Maximum Path Sum? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
<pre><code class="language-javascript">var maxPathSum = function(root) {
  let max = -Infinity;
  function dfs(node) {
    if (!node) return 0;
    let left = Math.max(dfs(node.left), 0);
    let right = Math.max(dfs(node.right), 0);
    max = Math.max(max, node.val + left + right);
    return node.val + Math.max(left, right);
  }
  dfs(root);
  return max;
};</code></pre>
</div>

<div id="q55" class="question">55. Serialize and Deserialize Binary Tree? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
<pre><code class="language-javascript">var serialize = function(root) {
  if (!root) return "null";
  return root.val + "," + serialize(root.left) + "," + serialize(root.right);
};
var deserialize = function(data) {
  const list = data.split(',');
  function dfs() {
    if (list[0] === "null") { list.shift(); return null; }
    let node = new TreeNode(Number(list.shift()));
    node.left = dfs();
    node.right = dfs();
    return node;
  }
  return dfs();
};</code></pre>
</div>

<div id="q56" class="question">56. Implement Trie (Prefix Tree)? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">class Trie {
  constructor() { this.root = {}; }
  insert(word) {
    let node = this.root;
    for (let c of word) {
      if (!node[c]) node[c] = {};
      node = node[c];
    }
    node.isEnd = true;
  }
  search(word) {
    let node = this.root;
    for (let c of word) {
      if (!node[c]) return false;
      node = node[c];
    }
    return node.isEnd === true;
  }
}</code></pre>
</div>

<div id="q57" class="question">57. Design Add and Search Words Data Structure? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">class WordDictionary {
  constructor() { this.root = {}; }
  addWord(word) { /* Trie insert */ }
  search(word) {
    function dfs(j, node) {
      for (let i = j; i < word.length; i++) {
        let c = word[i];
        if (c === '.') {
          for (let key in node) {
            if (key !== 'isEnd' && dfs(i + 1, node[key])) return true;
          }
          return false;
        } else {
          if (!node[c]) return false;
          node = node[c];
        }
      }
      return node.isEnd === true;
    }
    return dfs(0, this.root);
  }
}</code></pre>
</div>

<div id="q58" class="question">58. Word Search II? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
<pre><code class="language-javascript">// Uses Trie + DFS on Grid
// 1. Build Trie from words
// 2. DFS on board: check if path exists in Trie
// Optimization: Remove word from Trie after finding to avoid duplicates</code></pre>
</div>

<div id="q59" class="question">59. Number of Islands? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var numIslands = function(grid) {
  let count = 0;
  for (let r = 0; r < grid.length; r++) {
    for (let c = 0; c < grid[0].length; c++) {
      if (grid[r][c] === '1') {
        count++;
        dfs(r, c);
      }
    }
  }
  function dfs(r, c) {
    if (r<0 || c<0 || r>=grid.length || c>=grid[0].length || grid[r][c] === '0') return;
    grid[r][c] = '0';
    dfs(r+1,c); dfs(r-1,c); dfs(r,c+1); dfs(r,c-1);
  }
  return count;
};</code></pre>
</div>

<div id="q60" class="question">60. Clone Graph? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var cloneGraph = function(node) {
  if (!node) return null;
  const map = new Map();
  function dfs(n) {
    if (map.has(n)) return map.get(n);
    const clone = new Node(n.val);
    map.set(n, clone);
    for (let neighbor of n.neighbors) {
      clone.neighbors.push(dfs(neighbor));
    }
    return clone;
  }
  return dfs(node);
};</code></pre>
</div>

<div id="q61" class="question">61. Max Area of Island? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var maxAreaOfIsland = function(grid) {
  let max = 0;
  for (let r = 0; r < grid.length; r++) {
    for (let c = 0; c < grid[0].length; c++) {
      if (grid[r][c] === 1) max = Math.max(max, dfs(r, c));
    }
  }
  function dfs(r, c) {
    if (r<0 || c<0 || r>=grid.length || c>=grid[0].length || grid[r][c] === 0) return 0;
    grid[r][c] = 0;
    return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1);
  }
  return max;
};</code></pre>
</div>

<div id="q62" class="question">62. Pacific Atlantic Water Flow? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">// DFS from Pacific edges and Atlantic edges
// Keep two visited sets. Intersection is the answer.
// Flow "up" from ocean to check reachable cells.</code></pre>
</div>

<div id="q63" class="question">63. Surrounded Regions? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">// Capture surrounded regions (O -> X)
// 1. DFS from borders to mark unsurrounded 'O's as temporary 'T'
// 2. Loop through board: 'O' -> 'X', 'T' -> 'O'</code></pre>
</div>

<div id="q64" class="question">64. Rotting Oranges? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var orangesRotting = function(grid) {
  const q = [];
  let fresh = 0, time = 0;
  // Init queue with rotten oranges, count fresh
  // BFS level by level. If fresh becomes rotten, add to queue, fresh--
  // If fresh > 0 return -1, else return time
};</code></pre>
</div>

<div id="q65" class="question">65. Walls and Gates? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">// Multi-source BFS from all gates (0)
// Update distance for empty rooms (INF)</code></pre>
</div>

<div id="q66" class="question">66. Course Schedule? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var canFinish = function(numCourses, prerequisites) {
  const graph = Array(numCourses).fill(0).map(() => []);
  const inDegree = Array(numCourses).fill(0);
  for (let [c, pre] of prerequisites) {
    graph[pre].push(c);
    inDegree[c]++;
  }
  const q = [];
  for (let i = 0; i < numCourses; i++) if (inDegree[i] === 0) q.push(i);
  let count = 0;
  while (q.length) {
    let curr = q.shift();
    count++;
    for (let next of graph[curr]) {
      inDegree[next]--;
      if (inDegree[next] === 0) q.push(next);
    }
  }
  return count === numCourses;
};</code></pre>
</div>

<div id="q67" class="question">67. Graph Valid Tree? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Tree = Connected + No Cycles + V-1 Edges.</p>
<pre><code class="language-javascript">// Use Union-Find
// Loop edges: if union(u, v) returns false (already connected), cycle detected -> false
// Finally check if numComponents === 1</code></pre>
</div>

<div id="q68" class="question">68. Number of Connected Components? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">// Union-Find
// Start with n components.
// For each edge, if union successful, components--.</code></pre>
</div>

<div id="q69" class="question">69. Redundant Connection? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">// Union-Find
// If find(u) === find(v) for an edge, that edge is redundant.</code></pre>
</div>

<div id="q70" class="question">70. Min Cost Climbing Stairs? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
<pre><code class="language-javascript">var minCostClimbingStairs = function(cost) {
  for (let i = 2; i < cost.length; i++) {
    cost[i] += Math.min(cost[i-1], cost[i-2]);
  }
  return Math.min(cost[cost.length - 1], cost[cost.length - 2]);
};</code></pre>
</div>

<div id="q71" class="question">71. House Robber? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var rob = function(nums) {
  let rob1 = 0, rob2 = 0;
  for (let n of nums) {
    let temp = Math.max(n + rob1, rob2);
    rob1 = rob2;
    rob2 = temp;
  }
  return rob2;
};</code></pre>
</div>

<div id="q72" class="question">72. House Robber II? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">// Houses are in a circle.
// Max(Rob(nums[0...n-2]), Rob(nums[1...n-1]))</code></pre>
</div>

<div id="q73" class="question">73. Palindromic Substrings? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var countSubstrings = function(s) {
  let count = 0;
  for (let i = 0; i < s.length; i++) {
    count += countPals(i, i); // odd
    count += countPals(i, i + 1); // even
  }
  function countPals(l, r) {
    let c = 0;
    while (l >= 0 && r < s.length && s[l] === s[r]) {
      c++; l--; r++;
    }
    return c;
  }
  return count;
};</code></pre>
</div>

<div id="q74" class="question">74. Decode Ways? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var numDecodings = function(s) {
  if (s[0] === '0') return 0;
  const dp = Array(s.length + 1).fill(0);
  dp[0] = 1; dp[1] = 1;
  for (let i = 2; i <= s.length; i++) {
    if (s[i-1] !== '0') dp[i] += dp[i-1];
    let twoDigit = Number(s.substring(i-2, i));
    if (twoDigit >= 10 && twoDigit <= 26) dp[i] += dp[i-2];
  }
  return dp[s.length];
};</code></pre>
</div>

<div id="q75" class="question">75. Coin Change? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var coinChange = function(coins, amount) {
  const dp = Array(amount + 1).fill(Infinity);
  dp[0] = 0;
  for (let c of coins) {
    for (let a = c; a <= amount; a++) {
      dp[a] = Math.min(dp[a], dp[a - c] + 1);
    }
  }
  return dp[amount] === Infinity ? -1 : dp[amount];
};</code></pre>
</div>

<div id="q76" class="question">76. Maximum Product Subarray? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var maxProduct = function(nums) {
  let res = Math.max(...nums);
  let curMin = 1, curMax = 1;
  for (let n of nums) {
    if (n === 0) { curMin = 1; curMax = 1; continue; }
    let temp = curMax * n;
    curMax = Math.max(n * curMax, n * curMin, n);
    curMin = Math.min(temp, n * curMin, n);
    res = Math.max(res, curMax);
  }
  return res;
};</code></pre>
</div>

<div id="q77" class="question">77. Word Break? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var wordBreak = function(s, wordDict) {
  const dp = Array(s.length + 1).fill(false);
  dp[s.length] = true;
  for (let i = s.length - 1; i >= 0; i--) {
    for (let w of wordDict) {
      if (i + w.length <= s.length && s.substring(i, i + w.length) === w) {
        dp[i] = dp[i + w.length];
        if (dp[i]) break;
      }
    }
  }
  return dp[0];
};</code></pre>
</div>

<div id="q78" class="question">78. Longest Common Subsequence? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var longestCommonSubsequence = function(text1, text2) {
  const dp = Array(text1.length + 1).fill(0).map(() => Array(text2.length + 1).fill(0));
  for (let i = 1; i <= text1.length; i++) {
    for (let j = 1; j <= text2.length; j++) {
      if (text1[i-1] === text2[j-1]) dp[i][j] = 1 + dp[i-1][j-1];
      else dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
    }
  }
  return dp[text1.length][text2.length];
};</code></pre>
</div>

<div id="q79" class="question">79. Jump Game? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var canJump = function(nums) {
  let goal = nums.length - 1;
  for (let i = nums.length - 2; i >= 0; i--) {
    if (i + nums[i] >= goal) goal = i;
  }
  return goal === 0;
};</code></pre>
</div>

<div id="q80" class="question">80. Unique Paths? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var uniquePaths = function(m, n) {
  const row = Array(n).fill(1);
  for (let i = 0; i < m - 1; i++) {
    for (let j = n - 2; j >= 0; j--) {
      row[j] = row[j] + row[j+1];
    }
  }
  return row[0];
};</code></pre>
</div>

<div id="q81" class="question">81. Partition Equal Subset Sum? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var canPartition = function(nums) {
  let sum = nums.reduce((a, b) => a + b);
  if (sum % 2 !== 0) return false;
  let target = sum / 2;
  let dp = new Set([0]);
  for (let n of nums) {
    let nextDp = new Set();
    for (let t of dp) {
      nextDp.add(t + n);
      nextDp.add(t);
    }
    dp = nextDp;
  }
  return dp.has(target);
};</code></pre>
</div>

<div id="q82" class="question">82. Insert Interval? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var insert = function(intervals, newInterval) {
  const res = [];
  for (let i = 0; i < intervals.length; i++) {
    if (newInterval[1] < intervals[i][0]) {
      res.push(newInterval);
      return [...res, ...intervals.slice(i)];
    } else if (newInterval[0] > intervals[i][1]) {
      res.push(intervals[i]);
    } else {
      newInterval = [Math.min(newInterval[0], intervals[i][0]), Math.max(newInterval[1], intervals[i][1])];
    }
  }
  res.push(newInterval);
  return res;
};</code></pre>
</div>

<div id="q83" class="question">83. Non-overlapping Intervals? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var eraseOverlapIntervals = function(intervals) {
  intervals.sort((a, b) => a[1] - b[1]);
  let count = 0, prevEnd = intervals[0][1];
  for (let i = 1; i < intervals.length; i++) {
    if (intervals[i][0] < prevEnd) count++;
    else prevEnd = intervals[i][1];
  }
  return count;
};</code></pre>
</div>

<div id="q84" class="question">84. Meeting Rooms? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
<pre><code class="language-javascript">var canAttendMeetings = function(intervals) {
  intervals.sort((a, b) => a[0] - b[0]);
  for (let i = 1; i < intervals.length; i++) {
    if (intervals[i][0] < intervals[i-1][1]) return false;
  }
  return true;
};</code></pre>
</div>

<div id="q85" class="question">85. Meeting Rooms II? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var minMeetingRooms = function(intervals) {
  let starts = intervals.map(i => i[0]).sort((a, b) => a - b);
  let ends = intervals.map(i => i[1]).sort((a, b) => a - b);
  let count = 0, max = 0, s = 0, e = 0;
  while (s < intervals.length) {
    if (starts[s] < ends[e]) { count++; s++; }
    else { count--; e++; }
    max = Math.max(max, count);
  }
  return max;
};</code></pre>
</div>

<div id="q86" class="question">86. Rotate Image? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var rotate = function(matrix) {
  matrix.reverse();
  for (let i = 0; i < matrix.length; i++) {
    for (let j = i + 1; j < matrix[i].length; j++) {
      [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
    }
  }
};</code></pre>
</div>

<div id="q87" class="question">87. Spiral Matrix? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var spiralOrder = function(matrix) {
  const res = [];
  let l = 0, r = matrix[0].length - 1, t = 0, b = matrix.length - 1;
  while (l <= r && t <= b) {
    for (let i = l; i <= r; i++) res.push(matrix[t][i]);
    t++;
    for (let i = t; i <= b; i++) res.push(matrix[i][r]);
    r--;
    if (t <= b) {
      for (let i = r; i >= l; i--) res.push(matrix[b][i]);
      b--;
    }
    if (l <= r) {
      for (let i = b; i >= t; i--) res.push(matrix[i][l]);
      l++;
    }
  }
  return res;
};</code></pre>
</div>

<div id="q88" class="question">88. Set Matrix Zeroes? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var setZeroes = function(matrix) {
  let col0 = 1, rows = matrix.length, cols = matrix[0].length;
  for (let i = 0; i < rows; i++) {
    if (matrix[i][0] === 0) col0 = 0;
    for (let j = 1; j < cols; j++)
      if (matrix[i][j] === 0) matrix[i][0] = matrix[0][j] = 0;
  }
  for (let i = rows - 1; i >= 0; i--) {
    for (let j = cols - 1; j >= 1; j--)
      if (matrix[i][0] === 0 || matrix[0][j] === 0) matrix[i][j] = 0;
    if (col0 === 0) matrix[i][0] = 0;
  }
};</code></pre>
</div>

<div id="q89" class="question">89. Happy Number? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
<pre><code class="language-javascript">var isHappy = function(n) {
  const seen = new Set();
  while (n !== 1 && !seen.has(n)) {
    seen.add(n);
    n = n.toString().split('').reduce((sum, num) => sum + Math.pow(num, 2), 0);
  }
  return n === 1;
};</code></pre>
</div>

<div id="q90" class="question">90. Plus One? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
<pre><code class="language-javascript">var plusOne = function(digits) {
  for (let i = digits.length - 1; i >= 0; i--) {
    if (digits[i] < 9) {
      digits[i]++;
      return digits;
    }
    digits[i] = 0;
  }
  return [1, ...digits];
};</code></pre>
</div>

<div id="q91" class="question">91. Pow(x, n)? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var myPow = function(x, n) {
  if (n === 0) return 1;
  if (n < 0) return 1 / myPow(x, -n);
  if (n % 2 === 0) return myPow(x * x, n / 2);
  return x * myPow(x * x, (n - 1) / 2);
};</code></pre>
</div>

<div id="q92" class="question">92. Multiply Strings? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var multiply = function(num1, num2) {
  if (num1 === '0' || num2 === '0') return '0';
  const res = Array(num1.length + num2.length).fill(0);
  for (let i = num1.length - 1; i >= 0; i--) {
    for (let j = num2.length - 1; j >= 0; j--) {
      let p1 = i + j, p2 = i + j + 1;
      let sum = (num1[i] * num2[j]) + res[p2];
      res[p2] = sum % 10;
      res[p1] += Math.floor(sum / 10);
    }
  }
  while (res[0] === 0) res.shift();
  return res.join('');
};</code></pre>
</div>

<div id="q93" class="question">93. Detect Squares? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">class DetectSquares {
  constructor() { this.points = []; this.counts = {}; }
  add(point) {
    this.points.push(point);
    let key = point.join(',');
    this.counts[key] = (this.counts[key] || 0) + 1;
  }
  count([x, y]) {
    let res = 0;
    for (let [px, py] of this.points) {
      if (Math.abs(px - x) !== Math.abs(py - y) || px === x) continue;
      res += (this.counts[`${x},${py}`] || 0) * (this.counts[`${px},${y}`] || 0);
    }
    return res;
  }
}</code></pre>
</div>

<div id="q94" class="question">94. Single Number? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>XOR all numbers. Duplicates cancel out.</p>
<pre><code class="language-javascript">var singleNumber = function(nums) {
  return nums.reduce((a, b) => a ^ b);
};</code></pre>
</div>

<div id="q95" class="question">95. Number of 1 Bits? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
<pre><code class="language-javascript">var hammingWeight = function(n) {
  let count = 0;
  while (n !== 0) {
    n = n & (n - 1); // drops lowest set bit
    count++;
  }
  return count;
};</code></pre>
</div>

<div id="q96" class="question">96. Counting Bits? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
<pre><code class="language-javascript">var countBits = function(n) {
  const dp = Array(n + 1).fill(0);
  for (let i = 1; i <= n; i++) {
    dp[i] = dp[i >> 1] + (i & 1);
  }
  return dp;
};</code></pre>
</div>

<div id="q97" class="question">97. Reverse Bits? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
<pre><code class="language-javascript">var reverseBits = function(n) {
  let res = 0;
  for (let i = 0; i < 32; i++) {
    res = (res << 1) | (n & 1);
    n >>= 1;
  }
  return res >>> 0;
};</code></pre>
</div>

<div id="q98" class="question">98. Missing Number? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
<pre><code class="language-javascript">var missingNumber = function(nums) {
  let res = nums.length;
  for (let i = 0; i < nums.length; i++) {
    res += (i - nums[i]);
  }
  return res;
};</code></pre>
</div>

<div id="q99" class="question">99. Sum of Two Integers (No + or -)? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">var getSum = function(a, b) {
  while (b !== 0) {
    let carry = (a & b) << 1;
    a = a ^ b;
    b = carry;
  }
  return a;
};</code></pre>
</div>

<div id="q100" class="question">100. Alien Dictionary? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Topological Sort.</p>
<pre><code class="language-javascript">// Build graph from comparing adjacent words
// Check for prefix errors (e.g. "abc" before "ab")
// Run Topological Sort (BFS/DFS)
// Return order or "" if cycle detected</code></pre>
</div>
