<div align="center">
  <a href="#" target="_blank">
    <img src="../../assets/icons/interview_guide_logo.png" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Algorithms Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [Explain QuickSort algorithm?](#q1) <span class="intermediate">Intermediate</span>
2. [Explain MergeSort algorithm?](#q2) <span class="intermediate">Intermediate</span>
3. [What is Binary Search?](#q3) <span class="beginner">Beginner</span>
4. [Solve Two Sum problem?](#q4) <span class="beginner">Beginner</span>
5. [Explain Sliding Window technique?](#q5) <span class="intermediate">Intermediate</span>
6. [Check for Valid Anagram?](#q6) <span class="beginner">Beginner</span>
7. [Explain Two Pointers technique?](#q7) <span class="beginner">Beginner</span>
8. [Find Maximum Subarray Sum (Kadane's Algorithm)?](#q8) <span class="intermediate">Intermediate</span>
9. [Reverse a Linked List?](#q9) <span class="beginner">Beginner</span>
10. [Detect Cycle in Linked List (Floyd's Cycle Detection)?](#q10) <span class="intermediate">Intermediate</span>
11. [Merge Two Sorted Lists?](#q11) <span class="beginner">Beginner</span>
12. [Explain Breadth-First Search (BFS)?](#q12) <span class="intermediate">Intermediate</span>
13. [Explain Depth-First Search (DFS)?](#q13) <span class="intermediate">Intermediate</span>
14. [Number of Islands (Graph)?](#q14) <span class="intermediate">Intermediate</span>
15. [Explain Dijkstra's Algorithm?](#q15) <span class="advanced">Advanced</span>
16. [Explain Topological Sort?](#q16) <span class="advanced">Advanced</span>
17. [Climbing Stairs (DP)?](#q17) <span class="beginner">Beginner</span>
18. [Coin Change (DP)?](#q18) <span class="intermediate">Intermediate</span>
19. [Longest Increasing Subsequence (LIS)?](#q19) <span class="advanced">Advanced</span>
20. [0/1 Knapsack Problem?](#q20) <span class="advanced">Advanced</span>
21. [Valid Parentheses (Stack)?](#q21) <span class="beginner">Beginner</span>
22. [Implement Queue using Stacks?](#q22) <span class="beginner">Beginner</span>
23. [Explain Heap Sort?](#q23) <span class="intermediate">Intermediate</span>
24. [Kth Largest Element in an Array?](#q24) <span class="intermediate">Intermediate</span>
25. [Explain Trie (Prefix Tree)?](#q25) <span class="advanced">Advanced</span>
26. [Invert Binary Tree?](#q26) <span class="beginner">Beginner</span>
27. [Validate Binary Search Tree?](#q27) <span class="intermediate">Intermediate</span>
28. [Level Order Traversal (Tree)?](#q28) <span class="intermediate">Intermediate</span>
29. [Lowest Common Ancestor of BST?](#q29) <span class="intermediate">Intermediate</span>
30. [Search in Rotated Sorted Array?](#q30) <span class="intermediate">Intermediate</span>
31. [Find Minimum in Rotated Sorted Array?](#q31) <span class="intermediate">Intermediate</span>
32. [Container With Most Water?](#q32) <span class="intermediate">Intermediate</span>
33. [3Sum Problem?](#q33) <span class="intermediate">Intermediate</span>
34. [Group Anagrams?](#q34) <span class="intermediate">Intermediate</span>
35. [Longest Substring Without Repeating Characters?](#q35) <span class="intermediate">Intermediate</span>
36. [Longest Repeating Character Replacement?](#q36) <span class="intermediate">Intermediate</span>
37. [Minimum Window Substring?](#q37) <span class="advanced">Advanced</span>
38. [Valid Palindrome?](#q38) <span class="beginner">Beginner</span>
39. [Longest Palindromic Substring?](#q39) <span class="intermediate">Intermediate</span>
40. [Palindromic Substrings?](#q40) <span class="intermediate">Intermediate</span>
41. [Encode and Decode Strings?](#q41) <span class="intermediate">Intermediate</span>
42. [Top K Frequent Elements?](#q42) <span class="intermediate">Intermediate</span>
43. [Product of Array Except Self?](#q43) <span class="intermediate">Intermediate</span>
44. [Valid Sudoku?](#q44) <span class="intermediate">Intermediate</span>
45. [Longest Consecutive Sequence?](#q45) <span class="intermediate">Intermediate</span>
46. [Best Time to Buy and Sell Stock?](#q46) <span class="beginner">Beginner</span>
47. [Best Time to Buy and Sell Stock II?](#q47) <span class="intermediate">Intermediate</span>
48. [Jump Game?](#q48) <span class="intermediate">Intermediate</span>
49. [Jump Game II?](#q49) <span class="intermediate">Intermediate</span>
50. [Insert Interval?](#q50) <span class="intermediate">Intermediate</span>
51. [Merge Intervals?](#q51) <span class="intermediate">Intermediate</span>
52. [Non-overlapping Intervals?](#q52) <span class="intermediate">Intermediate</span>
53. [Meeting Rooms?](#q53) <span class="beginner">Beginner</span>
54. [Meeting Rooms II?](#q54) <span class="intermediate">Intermediate</span>
55. [Rotate Image (Matrix)?](#q55) <span class="intermediate">Intermediate</span>
56. [Spiral Matrix?](#q56) <span class="intermediate">Intermediate</span>
57. [Set Matrix Zeroes?](#q57) <span class="intermediate">Intermediate</span>
58. [Search a 2D Matrix?](#q58) <span class="intermediate">Intermediate</span>
59. [Word Search (Backtracking)?](#q59) <span class="intermediate">Intermediate</span>
60. [Median of Two Sorted Arrays?](#q60) <span class="hard">Hard</span>
61. [Trapping Rain Water?](#q61) <span class="hard">Hard</span>
62. [Largest Rectangle in Histogram?](#q62) <span class="hard">Hard</span>
63. [Binary Tree Maximum Path Sum?](#q63) <span class="hard">Hard</span>
64. [Serialize and Deserialize Binary Tree?](#q64) <span class="hard">Hard</span>
65. [Construct Binary Tree from Preorder and Inorder?](#q65) <span class="intermediate">Intermediate</span>
66. [Word Ladder (BFS)?](#q66) <span class="hard">Hard</span>
67. [Course Schedule (Topological Sort)?](#q67) <span class="intermediate">Intermediate</span>
68. [Number of Connected Components?](#q68) <span class="intermediate">Intermediate</span>
69. [Alien Dictionary?](#q69) <span class="hard">Hard</span>
70. [House Robber?](#q70) <span class="intermediate">Intermediate</span>
71. [House Robber II (Circular)?](#q71) <span class="intermediate">Intermediate</span>
72. [Decode Ways?](#q72) <span class="intermediate">Intermediate</span>
73. [Unique Paths?](#q73) <span class="intermediate">Intermediate</span>
74. [Longest Common Subsequence?](#q74) <span class="intermediate">Intermediate</span>
75. [Word Break?](#q75) <span class="intermediate">Intermediate</span>
76. [Combination Sum?](#q76) <span class="intermediate">Intermediate</span>
77. [Subsets?](#q77) <span class="intermediate">Intermediate</span>
78. [Permutations?](#q78) <span class="intermediate">Intermediate</span>
79. [N-Queens?](#q79) <span class="hard">Hard</span>
80. [Implement LRU Cache?](#q80) <span class="intermediate">Intermediate</span>
81. [Implement LFU Cache?](#q81) <span class="hard">Hard</span>
82. [Find Median from Data Stream?](#q82) <span class="hard">Hard</span>
83. [Sliding Window Maximum?](#q83) <span class="hard">Hard</span>
84. [Basic Calculator II?](#q84) <span class="intermediate">Intermediate</span>
85. [Task Scheduler?](#q85) <span class="intermediate">Intermediate</span>
86. [K Closest Points to Origin?](#q86) <span class="intermediate">Intermediate</span>
87. [Daily Temperatures?](#q87) <span class="intermediate">Intermediate</span>
88. [Car Fleet?](#q88) <span class="intermediate">Intermediate</span>
89. [Min Cost to Connect All Points?](#q89) <span class="intermediate">Intermediate</span>
90. [Network Delay Time?](#q90) <span class="intermediate">Intermediate</span>
91. [Cheapest Flights Within K Stops?](#q91) <span class="intermediate">Intermediate</span>
92. [Reconstruct Itinerary?](#q92) <span class="hard">Hard</span>
93. [Partition Equal Subset Sum?](#q93) <span class="intermediate">Intermediate</span>
94. [Target Sum?](#q94) <span class="intermediate">Intermediate</span>
95. [Interleaving String?](#q95) <span class="intermediate">Intermediate</span>
96. [Edit Distance?](#q96) <span class="hard">Hard</span>
97. [Burst Balloons?](#q97) <span class="hard">Hard</span>
98. [Regular Expression Matching?](#q98) <span class="hard">Hard</span>
99. [Palindrome Partitioning?](#q99) <span class="intermediate">Intermediate</span>
100. [Word Search II?](#q100) <span class="hard">Hard</span>

---

<a id="q1"></a>
### Q1: Explain QuickSort algorithm?

**Difficulty**: Intermediate

**Strategy**:
**
QuickSort is a divide-and-conquer algorithm. It picks a 'pivot' element and partitions the array around the pivot (smaller elements to left, larger to right). It then recursively sorts the sub-arrays. Average time complexity is O(n log n).

**Code Example**:
```javascript
function quickSort(arr) {
  if (arr.length <= 1) return arr;
  const pivot = arr[arr.length - 1];
  const left = [],
    right = [];
  for (let i = 0; i < arr.length - 1; i++) {
    arr[i] < pivot ? left.push(arr[i]) : right.push(arr[i]);
  }
  return [...quickSort(left), pivot, ...quickSort(right)];
}
```

---

<a id="q2"></a>
### Q2: Explain MergeSort algorithm?

**Difficulty**: Intermediate

**Strategy**:
**
MergeSort divides the array into two halves, recursively sorts them, and then merges the sorted halves. It guarantees O(n log n) time complexity but requires O(n) extra space.

**Code Example**:
```javascript
function mergeSort(arr) {
  if (arr.length <= 1) return arr;
  const mid = Math.floor(arr.length / 2);
  const left = mergeSort(arr.slice(0, mid));
  const right = mergeSort(arr.slice(mid));
  return merge(left, right);
}

function merge(left, right) {
  let res = [],
    l = 0,
    r = 0;
  while (l < left.length && r < right.length) {
    if (left[l] < right[r]) res.push(left[l++]);
    else res.push(right[r++]);
  }
  return [...res, ...left.slice(l), ...right.slice(r)];
}
```

---

<a id="q3"></a>
### Q3: What is Binary Search?

**Difficulty**: Beginner

**Strategy**:
**
Binary Search finds a target value within a **sorted** array. It compares the target value to the middle element of the array. If they are unequal, the half in which the target cannot lie is eliminated. Complexity: O(log n).

**Code Example**:
```javascript
function binarySearch(arr, target) {
  let l = 0,
    r = arr.length - 1;
  while (l <= r) {
    const mid = Math.floor((l + r) / 2);
    if (arr[mid] === target) return mid;
    if (arr[mid] < target) l = mid + 1;
    else r = mid - 1;
  }
  return -1;
}
```

---

<a id="q4"></a>
### Q4: Solve Two Sum problem?

**Difficulty**: Beginner

**Strategy**:
**
Given an array of integers and a target, return indices of the two numbers such that they add up to target. Use a Hash Map to store the complement (`target - num`) and its index. Time: O(n).

**Code Example**:
```javascript
function twoSum(nums, target) {
  const map = new Map();
  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];
    if (map.has(complement)) return [map.get(complement), i];
    map.set(nums[i], i);
  }
}
```

---

<a id="q5"></a>
### Q5: Explain Sliding Window technique?

**Difficulty**: Intermediate

**Strategy**:
**
Used for array/string problems involving subarrays or substrings. Maintain a window (start, end indices) and adjust it to satisfy constraints, optimizing from O(n^2) to O(n).

**Code Example**:
```javascript
// Max Sum Subarray of size K
function maxSum(arr, k) {
  let maxSum = 0,
    windowSum = 0;
  for (let i = 0; i < k; i++) windowSum += arr[i];
  maxSum = windowSum;
  for (let i = k; i < arr.length; i++) {
    windowSum += arr[i] - arr[i - k];
    maxSum = Math.max(maxSum, windowSum);
  }
  return maxSum;
}
```

---

<a id="q6"></a>
### Q6: Check for Valid Anagram?

**Difficulty**: Beginner

**Strategy**:
**
Two strings are anagrams if they contain the same characters with the same frequencies. Use a frequency map (or array for 26 lowercase letters) to count and compare.

**Code Example**:
```javascript
function isAnagram(s, t) {
  if (s.length !== t.length) return false;
  const map = {};
  for (let char of s) map[char] = (map[char] || 0) + 1;
  for (let char of t) {
    if (!map[char]) return false;
    map[char]--;
  }
  return true;
}
```

---

<a id="q7"></a>
### Q7: Explain Two Pointers technique?

**Difficulty**: Beginner

**Strategy**:
**
Use two pointers (usually `left` and `right`) to iterate through a data structure (often sorted array) to solve problems like finding pairs or reversing.

**Code Example**:
```javascript
// Valid Palindrome
function isPalindrome(s) {
  let l = 0,
    r = s.length - 1;
  while (l < r) {
    if (s[l] !== s[r]) return false;
    l++;
    r--;
  }
  return true;
}
```

---

<a id="q8"></a>
### Q8: Find Maximum Subarray Sum (Kadane's Algorithm)?

**Difficulty**: Intermediate

**Strategy**:
**
Iterate through the array, keeping track of the maximum sum ending at the current position (`currentSum`) and the global maximum (`maxSum`). If `currentSum` becomes negative, reset it to 0.

**Code Example**:
```javascript
function maxSubArray(nums) {
  let maxSum = nums[0],
    currentSum = 0;
  for (let num of nums) {
    if (currentSum < 0) currentSum = 0;
    currentSum += num;
    maxSum = Math.max(maxSum, currentSum);
  }
  return maxSum;
}
```

---

<a id="q9"></a>
### Q9: Reverse a Linked List?

**Difficulty**: Beginner

**Strategy**:
**
Iterate through the list, changing the `next` pointer of each node to point to the `previous` node. Requires 3 pointers: `prev`, `curr`, `next`.

**Code Example**:
```javascript
function reverseList(head) {
  let prev = null,
    curr = head;
  while (curr) {
    let next = curr.next;
    curr.next = prev;
    prev = curr;
    curr = next;
  }
  return prev;
}
```

---

<a id="q10"></a>
### Q10: Detect Cycle in Linked List (Floyd's Cycle Detection)?

**Difficulty**: Intermediate

**Strategy**:
**
Use two pointers, `slow` (moves 1 step) and `fast` (moves 2 steps). If there is a cycle, they will eventually meet. If `fast` reaches null, there is no cycle.

**Code Example**:
```javascript
function hasCycle(head) {
  let slow = head,
    fast = head;
  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
    if (slow === fast) return true;
  }
  return false;
}
```

---

<a id="q11"></a>
### Q11: Merge Two Sorted Lists?

**Difficulty**: Beginner

**Strategy**:
**
Use a dummy node. Compare heads of both lists, attach the smaller one to `current.next`, and move the pointer. Attach remaining nodes at the end.

**Code Example**:
```javascript
function mergeTwoLists(l1, l2) {
  const dummy = new ListNode(0);
  let curr = dummy;
  while (l1 && l2) {
    if (l1.val < l2.val) {
      curr.next = l1;
      l1 = l1.next;
    } else {
      curr.next = l2;
      l2 = l2.next;
    }
    curr = curr.next;
  }
  curr.next = l1 || l2;
  return dummy.next;
}
```

---

<a id="q12"></a>
### Q12: Explain Breadth-First Search (BFS)?

**Difficulty**: Intermediate

**Strategy**:
**
BFS explores a graph layer by layer. Use a **Queue**. Add starting node, then while queue is not empty, dequeue, process, and enqueue unvisited neighbors. Good for shortest path in unweighted graphs.

**Code Example**:
```javascript
function bfs(graph, start) {
  const queue = [start];
  const visited = new Set([start]);
  while (queue.length) {
    const node = queue.shift();
    console.log(node);
    for (let neighbor of graph[node]) {
      if (!visited.has(neighbor)) {
        visited.add(neighbor);
        queue.push(neighbor);
      }
    }
  }
}
```

---

<a id="q13"></a>
### Q13: Explain Depth-First Search (DFS)?

**Difficulty**: Intermediate

**Strategy**:
**
DFS explores as far as possible along each branch before backtracking. Use a **Stack** (or recursion). Good for topological sort, maze solving.

**Code Example**:
```javascript
function dfs(graph, node, visited = new Set()) {
  console.log(node);
  visited.add(node);
  for (let neighbor of graph[node]) {
    if (!visited.has(neighbor)) {
      dfs(graph, neighbor, visited);
    }
  }
}
```

---

<a id="q14"></a>
### Q14: Number of Islands (Graph)?

**Difficulty**: Intermediate

**Strategy**:
**
Iterate through the grid. When a '1' (land) is found, increment count and trigger DFS/BFS to mark all connected '1's as '0' (water) so they aren't counted again.

**Code Example**:
```javascript
function numIslands(grid) {
  let count = 0;
  for (let r = 0; r < grid.length; r++) {
    for (let c = 0; c < grid[0].length; c++) {
      if (grid[r][c] === "1") {
        count++;
        dfs(grid, r, c);
      }
    }
  }
  return count;
}
// dfs function helper omitted for brevity
```

---

<a id="q15"></a>
### Q15: Explain Dijkstra's Algorithm?

**Difficulty**: Advanced

**Strategy**:
**
Finds shortest paths from a source to all other nodes in a weighted graph. Use a **Priority Queue** (Min-Heap). Greedily select the node with the smallest known distance and update neighbors.

**Code Example**:
```javascript
// Conceptual
function dijkstra(graph, start) {
  const dist = {}; // Init with Infinity
  const pq = new MinHeap();
  pq.push(0, start);

  while (!pq.isEmpty()) {
    const [d, u] = pq.pop();
    if (d > dist[u]) continue;
    for (let [v, weight] of graph[u]) {
      if (dist[u] + weight < dist[v]) {
        dist[v] = dist[u] + weight;
        pq.push(dist[v], v);
      }
    }
  }
}
```

---

<a id="q16"></a>
### Q16: Explain Topological Sort?

**Difficulty**: Advanced

**Strategy**:
**
Ordering of vertices in a DAG (Directed Acyclic Graph) where for every edge u->v, u comes before v. Uses DFS (post-order + reverse) or Kahn's Algorithm (in-degree).

**Code Example**:
```javascript
// Kahn's Algorithm
function topologicalSort(numCourses, prereqs) {
  const inDegree = new Array(numCourses).fill(0);
  const graph = [...Array(numCourses)].map(() => []);
  prereqs.forEach(([c, p]) => {
    graph[p].push(c);
    inDegree[c]++;
  });

  const queue = [];
  inDegree.forEach((d, i) => {
    if (d === 0) queue.push(i);
  });

  const res = [];
  while (queue.length) {
    const u = queue.shift();
    res.push(u);
    for (let v of graph[u]) {
      inDegree[v]--;
      if (inDegree[v] === 0) queue.push(v);
    }
  }
  return res.length === numCourses ? res : [];
}
```

---

<a id="q17"></a>
### Q17: Climbing Stairs (DP)?

**Difficulty**: Beginner

**Strategy**:
**
Ways to reach step `n` = Ways to reach `n-1` + Ways to reach `n-2`. This is the Fibonacci sequence.

**Code Example**:
```javascript
function climbStairs(n) {
  if (n <= 2) return n;
  let a = 1,
    b = 2;
  for (let i = 3; i <= n; i++) {
    let temp = a + b;
    a = b;
    b = temp;
  }
  return b;
}
```

---

<a id="q18"></a>
### Q18: Coin Change (DP)?

**Difficulty**: Intermediate

**Strategy**:
**
Find fewest coins to make amount. `dp[i]` = min coins for amount `i`. `dp[i] = min(dp[i], dp[i - coin] + 1)`.

**Code Example**:
```javascript
function coinChange(coins, amount) {
  const dp = new Array(amount + 1).fill(Infinity);
  dp[0] = 0;
  for (let coin of coins) {
    for (let i = coin; i <= amount; i++) {
      dp[i] = Math.min(dp[i], dp[i - coin] + 1);
    }
  }
  return dp[amount] === Infinity ? -1 : dp[amount];
}
```

---

<a id="q19"></a>
### Q19: Longest Increasing Subsequence (LIS)?

**Difficulty**: Advanced

**Strategy**:
**
`dp[i]` = length of LIS ending at index `i`. Check all `j < i`, if `nums[i] > nums[j]`, update `dp[i]`. Time: O(n^2). Can be optimized to O(n log n) using Binary Search.

**Code Example**:
```javascript
function lengthOfLIS(nums) {
  const dp = new Array(nums.length).fill(1);
  let max = 1;
  for (let i = 1; i < nums.length; i++) {
    for (let j = 0; j < i; j++) {
      if (nums[i] > nums[j]) dp[i] = Math.max(dp[i], dp[j] + 1);
    }
    max = Math.max(max, dp[i]);
  }
  return max;
}
```

---

<a id="q20"></a>
### Q20: 0/1 Knapsack Problem?

**Difficulty**: Advanced

**Strategy**:
**
Given weights and values, maximize value within capacity. `dp[i][w]` = max value using first `i` items with capacity `w`.
Recurrence: `max(dp[i-1][w], val[i] + dp[i-1][w-wt[i]])`.

**Code Example**:
```javascript
// Space Optimized (1D array)
function knapsack(weights, values, capacity) {
  const dp = new Array(capacity + 1).fill(0);
  for (let i = 0; i < weights.length; i++) {
    for (let w = capacity; w >= weights[i]; w--) {
      dp[w] = Math.max(dp[w], values[i] + dp[w - weights[i]]);
    }
  }
  return dp[capacity];
}
```

---

<a id="q21"></a>
### Q21: Valid Parentheses (Stack)?

**Difficulty**: Beginner

**Strategy**:
**
Use a Stack. Push opening brackets. When closing bracket appears, check if matches stack top. If stack empty or mismatch, invalid. At end, stack must be empty.

**Code Example**:
```javascript
function isValid(s) {
  const stack = [];
  const map = { "(": ")", "{": "}", "[": "]" };
  for (let char of s) {
    if (map[char]) stack.push(map[char]);
    else if (stack.pop() !== char) return false;
  }
  return stack.length === 0;
}
```

---

<a id="q22"></a>
### Q22: Implement Queue using Stacks?

**Difficulty**: Beginner

**Strategy**:
**
Use two stacks: `input` and `output`. Push to `input`. Pop/Peek from `output`. If `output` empty, move all elements from `input` to `output` (reverses order).

**Code Example**:
```javascript
class MyQueue {
  constructor() {
    this.in = [];
    this.out = [];
  }
  push(x) {
    this.in.push(x);
  }
  pop() {
    if (!this.out.length) while (this.in.length) this.out.push(this.in.pop());
    return this.out.pop();
  }
}
```

---

<a id="q23"></a>
### Q23: Explain Heap Sort?

**Difficulty**: Intermediate

**Strategy**:
**

1. Build Max-Heap from array.
2. Swap root (max) with last element.
3. Reduce heap size and heapify root.
4. Repeat. Time: O(n log n). Space: O(1).

**Code Example**:
```javascript
// Conceptual
function heapSort(arr) {
  buildMaxHeap(arr);
  for (let i = arr.length - 1; i > 0; i--) {
    swap(arr, 0, i);
    heapify(arr, 0, i);
  }
  return arr;
}
```

---

<a id="q24"></a>
### Q24: Kth Largest Element in an Array?

**Difficulty**: Intermediate

**Strategy**:
**
Can sort (O(n log n)) or use Min-Heap of size K (O(n log k)). For O(n) average, use QuickSelect (partitioning like QuickSort).

**Code Example**:
```javascript
// Using QuickSelect logic
function findKthLargest(nums, k) {
  // Implementation of QuickSelect...
}
```

---

<a id="q25"></a>
### Q25: Explain Trie (Prefix Tree)?

**Difficulty**: Advanced

**Strategy**:
**
Tree structure for strings. Each node represents a character. Good for autocomplete, spell checker. Operations (Insert, Search, StartsWith) are O(L) where L is word length.

**Code Example**:
```javascript
class TrieNode {
  constructor() {
    this.children = {};
    this.isEnd = false;
  }
}

class Trie {
  constructor() {
    this.root = new TrieNode();
  }
  insert(word) {
    let node = this.root;
    for (let c of word) {
      if (!node.children[c]) node.children[c] = new TrieNode();
      node = node.children[c];
    }
    node.isEnd = true;
  }
}
```

---

<a id="q26"></a>
### Q26: Invert Binary Tree?

**Difficulty**: Beginner

**Strategy**:
**
Recursive approach: Swap left and right children, then recursively invert left subtree and right subtree.

**Code Example**:
```javascript
function invertTree(root) {
  if (!root) return null;
  [root.left, root.right] = [root.right, root.left];
  invertTree(root.left);
  invertTree(root.right);
  return root;
}
```

---

<a id="q27"></a>
### Q27: Validate Binary Search Tree?

**Difficulty**: Intermediate

**Strategy**:
**
Recursively validate that `left.val < root.val < right.val`. Pass down `min` and `max` constraints. `validate(node, min, max)`.

**Code Example**:
```javascript
function isValidBST(root, min = -Infinity, max = Infinity) {
  if (!root) return true;
  if (root.val <= min || root.val >= max) return false;
  return (
    isValidBST(root.left, min, root.val) &&
    isValidBST(root.right, root.val, max)
  );
}
```

---

<a id="q28"></a>
### Q28: Level Order Traversal (Tree)?

**Difficulty**: Intermediate

**Strategy**:
**
Use BFS with a Queue. Process nodes level by level. Keep track of queue length at start of loop to process one level at a time.

**Code Example**:
```javascript
function levelOrder(root) {
  if (!root) return [];
  const res = [],
    queue = [root];
  while (queue.length) {
    const level = [],
      len = queue.length;
    for (let i = 0; i < len; i++) {
      const node = queue.shift();
      level.push(node.val);
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
    res.push(level);
  }
  return res;
}
```

---

<a id="q29"></a>
### Q29: Lowest Common Ancestor of BST?

**Difficulty**: Intermediate

**Strategy**:
**
For BST: If both p and q are smaller than root, go left. If both larger, go right. Otherwise, root is the split point (LCA).

**Code Example**:
```javascript
function lowestCommonAncestor(root, p, q) {
  if (p.val < root.val && q.val < root.val)
    return lowestCommonAncestor(root.left, p, q);
  if (p.val > root.val && q.val > root.val)
    return lowestCommonAncestor(root.right, p, q);
  return root;
}
```

---

<a id="q30"></a>
### Q30: Search in Rotated Sorted Array?

**Difficulty**: Intermediate

**Strategy**:
**
Modified Binary Search. Determine which half is sorted. If target is in the sorted half range, search there; else search the other half.

**Code Example**:
```javascript
// Logic:
// if nums[l] <= nums[mid]: Left half sorted
//   if nums[l] <= target < nums[mid]: search left
//   else: search right
// else: Right half sorted
```

---

<a id="q31"></a>
### Q31: Find Minimum in Rotated Sorted Array?

**Difficulty**: Intermediate

**Strategy**:
**
Binary Search. If `nums[mid] > nums[right]`, min is in right half (`l = mid + 1`). Else, min is at mid or left (`r = mid`).

**Code Example**:
```javascript
function findMin(nums) {
  let l = 0,
    r = nums.length - 1;
  while (l < r) {
    const mid = Math.floor((l + r) / 2);
    if (nums[mid] > nums[r]) l = mid + 1;
    else r = mid;
  }
  return nums[l];
}
```

---

<a id="q32"></a>
### Q32: Container With Most Water?

**Difficulty**: Intermediate

**Strategy**:
**
Two Pointers (start, end). Area = `min(height[l], height[r]) * (r - l)`. Move the pointer with the smaller height inward to potentially find a taller line.

**Code Example**:
```javascript
function maxArea(height) {
  let l = 0,
    r = height.length - 1,
    max = 0;
  while (l < r) {
    max = Math.max(max, Math.min(height[l], height[r]) * (r - l));
    if (height[l] < height[r]) l++;
    else r--;
  }
  return max;
}
```

---

<a id="q33"></a>
### Q33: 3Sum Problem?

**Difficulty**: Intermediate

**Strategy**:
**
Sort array. Iterate `i`. Use Two Pointers (`l`, `r`) on the rest to find `nums[l] + nums[r] = -nums[i]`. Skip duplicates to avoid repeating triplets.

**Code Example**:
```javascript
// Sort, loop i, l=i+1, r=end
// if sum < 0: l++
// if sum > 0: r--
// if sum == 0: add, l++, r--, skip dupes
```

---

<a id="q34"></a>
### Q34: Group Anagrams?

**Difficulty**: Intermediate

**Strategy**:
**
Use a Map. Key = sorted string (or char count signature), Value = array of strings. Iterate input, compute key, push to map. Return map values.

**Code Example**:
```javascript
function groupAnagrams(strs) {
  const map = {};
  for (let s of strs) {
    const key = s.split("").sort().join("");
    if (!map[key]) map[key] = [];
    map[key].push(s);
  }
  return Object.values(map);
}
```

---

<a id="q35"></a>
### Q35: Longest Substring Without Repeating Characters?

**Difficulty**: Intermediate

**Strategy**:
**
Sliding Window with Set/Map. Expand `right` pointer. If char exists in window, contract `left` pointer until unique. Update max length.

**Code Example**:
```javascript
function lengthOfLongestSubstring(s) {
  const set = new Set();
  let l = 0,
    max = 0;
  for (let r = 0; r < s.length; r++) {
    while (set.has(s[r])) set.delete(s[l++]);
    set.add(s[r]);
    max = Math.max(max, set.size);
  }
  return max;
}
```

---

<a id="q36"></a>
### Q36: Longest Repeating Character Replacement?

**Difficulty**: Intermediate

**Strategy**:
**
Sliding Window. Keep track of char counts in window and `maxCount` of a single char. If `windowLen - maxCount > k`, shrink window.

**Code Example**:
```javascript
// Window size - max freq char count <= k -> Valid
```

---

<a id="q37"></a>
### Q37: Minimum Window Substring?

**Difficulty**: Advanced

**Strategy**:
**
Sliding Window. Expand `r` until window has all chars of `t`. Then shrink `l` to minimize window while maintaining validity. Track min length.

**Code Example**:
```javascript
// Use two maps (needed, window)
// validCount variable
```

---

<a id="q38"></a>
### Q38: Valid Palindrome?

**Difficulty**: Beginner

**Strategy**:
**
Filter non-alphanumeric chars, convert to lowercase. Use two pointers starting from ends moving inwards.

**Code Example**:
```javascript
// s.replace(/[^a-z0-9]/gi, '').toLowerCase()
```

---

<a id="q39"></a>
### Q39: Longest Palindromic Substring?

**Difficulty**: Intermediate

**Strategy**:
**
Expand Around Center. For each index `i`, expand for odd length (`i, i`) and even length (`i, i+1`). Keep track of max length found.

**Code Example**:
```javascript
// expand(l, r): while s[l] == s[r], l--, r++
```

---

<a id="q40"></a>
### Q40: Palindromic Substrings?

**Difficulty**: Intermediate

**Strategy**:
**
Similar to Longest Palindromic Substring. Count how many valid palindromes are found while expanding around center.

**Code Example**:
```javascript
// count++ inside the expansion loop
```

---

<a id="q41"></a>
### Q41: Encode and Decode Strings?

**Difficulty**: Intermediate

**Strategy**:
**
Prefix each string with its length and a delimiter (e.g., "4#Code5#Tests"). Decoding reads length, consumes delimiter, extracts substring.

**Code Example**:
```javascript
// "Hello" -> "5#Hello"
```

---

<a id="q42"></a>
### Q42: Top K Frequent Elements?

**Difficulty**: Intermediate

**Strategy**:
**
Count frequencies. Use Min-Heap of size K (keep top K largest). Or use Bucket Sort (freq array) for O(n).

**Code Example**:
```javascript
// Bucket sort approach is O(n)
```

---

<a id="q43"></a>
### Q43: Product of Array Except Self?

**Difficulty**: Intermediate

**Strategy**:
**
Two passes. First pass (left to right): calculate prefix products. Second pass (right to left): multiply by suffix products. O(n) time, O(1) extra space (excluding output).

**Code Example**:
```javascript
// res[i] = prefix * suffix
```

---

<a id="q44"></a>
### Q44: Valid Sudoku?

**Difficulty**: Intermediate

**Strategy**:
**
Validate rows, columns, and 3x3 sub-boxes. Use Sets or boolean arrays to check for duplicates in each scope.

**Code Example**:
```javascript
// rows[9], cols[9], boxes[9] sets
```

---

<a id="q45"></a>
### Q45: Longest Consecutive Sequence?

**Difficulty**: Intermediate

**Strategy**:
**
Put all nums in a Set. Iterate nums. If `num-1` is not in set (start of sequence), check `num+1, num+2...` in set. Maximize length. O(n).

**Code Example**:
```javascript
// if (!set.has(n-1)) { while set.has(n+len) len++ }
```

---

<a id="q46"></a>
### Q46: Best Time to Buy and Sell Stock?

**Difficulty**: Beginner

**Strategy**:
**
One pass. Track `minPrice` so far. Max profit is `currentPrice - minPrice`. Update max profit.

**Code Example**:
```javascript
// min = Infinity, maxP = 0
// min = min(min, price)
// maxP = max(maxP, price - min)
```

---

<a id="q47"></a>
### Q47: Best Time to Buy and Sell Stock II?

**Difficulty**: Intermediate

**Strategy**:
**
Accumulate all positive price differences (greedy). If `price[i] > price[i-1]`, add difference to profit.

**Code Example**:
```javascript
// if (prices[i] > prices[i-1]) profit += prices[i] - prices[i-1]
```

---

<a id="q48"></a>
### Q48: Jump Game?

**Difficulty**: Intermediate

**Strategy**:
**
Greedy. Track `maxReach`. Iterate. If `i > maxReach`, unreachable. Else `maxReach = max(maxReach, i + nums[i])`. If `maxReach >= lastIndex`, return true.

**Code Example**:
```javascript
// maxReach >= length - 1
```

---

<a id="q49"></a>
### Q49: Jump Game II?

**Difficulty**: Intermediate

**Strategy**:
**
BFS/Greedy. `jumps++` when we reach end of current jump range (`currentEnd`). Update `currentEnd` to `farthest` reachable.

**Code Example**:
```javascript
// jumps, currentEnd, farthest
```

---

<a id="q50"></a>
### Q50: Insert Interval?

**Difficulty**: Intermediate

**Strategy**:
**

1. Add intervals ending before newInterval.
2. Merge overlapping intervals with newInterval (`start = min`, `end = max`).
3. Add remaining intervals.

**Code Example**:
```javascript
// Linear scan O(n)
```

---

<a id="q51"></a>
### Q51: Merge Intervals?

**Difficulty**: Intermediate

**Strategy**:
**
Sort intervals by start time. Iterate through sorted intervals. If current interval overlaps with the last added interval in result (`current.start <= last.end`), merge them (`last.end = max(last.end, current.end)`). Else, add current.

**Code Example**:
```javascript
// Sort -> Iterate -> Merge
```

---

<a id="q52"></a>
### Q52: Non-overlapping Intervals?

**Difficulty**: Intermediate

**Strategy**:
**
Greedy. Sort by **end time**. Select first interval. Iterate. If next interval starts after current ends, select it and update end. Else, count as removal (overlap).

**Code Example**:
```javascript
// Sort by end -> Count non-overlapping -> Result = Total - Non-overlapping
```

---

<a id="q53"></a>
### Q53: Meeting Rooms?

**Difficulty**: Beginner

**Strategy**:
**
Sort intervals by start time. Check if any `interval[i].end > interval[i+1].start`. If so, return false.

**Code Example**:
```javascript
// Sort -> Check adjacent overlap
```

---

<a id="q54"></a>
### Q54: Meeting Rooms II?

**Difficulty**: Intermediate

**Strategy**:
**
1. Min-Heap stores end times of active meetings. If `newMeeting.start >= minHeap.top`, pop (room freed). Push `newMeeting.end`. Heap size is min rooms.
2. Or Chronological Ordering: Sort starts and ends separately. Two pointers.

**Code Example**:
```javascript
// Two pointers approach: starts[], ends[]
```

---

<a id="q55"></a>
### Q55: Rotate Image (Matrix)?

**Difficulty**: Intermediate

**Strategy**:
**
1. Transpose matrix (swap `matrix[i][j]` with `matrix[j][i]`).
2. Reverse each row.
Result is 90-degree clockwise rotation.

**Code Example**:
```javascript
// Transpose -> Reverse Rows
```

---

<a id="q56"></a>
### Q56: Spiral Matrix?

**Difficulty**: Intermediate

**Strategy**:
**
Simulation. Maintain boundaries: `top`, `bottom`, `left`, `right`. Loop while `top <= bottom` and `left <= right`. Traverse Right -> Down -> Left -> Up. Update boundaries after each pass.

**Code Example**:
```javascript
// While loop with 4 for-loops inside
```

---

<a id="q57"></a>
### Q57: Set Matrix Zeroes?

**Difficulty**: Intermediate

**Strategy**:
**
Use first row and first column as markers. Iterate matrix, if `matrix[i][j] == 0`, set `matrix[i][0] = 0` and `matrix[0][j] = 0`. Then use markers to set cells to 0. Handle first row/col separately. Space: O(1).

**Code Example**:
```javascript
// Use markers in-place
```

---

<a id="q58"></a>
### Q58: Search a 2D Matrix?

**Difficulty**: Intermediate

**Strategy**:
**
Treat 2D matrix (m x n) as a sorted 1D array of length `m * n`. Perform Binary Search. Mapping: `row = index / n`, `col = index % n`.

**Code Example**:
```javascript
// Binary Search on range [0, m*n - 1]
```

---

<a id="q59"></a>
### Q59: Word Search (Backtracking)?

**Difficulty**: Intermediate

**Strategy**:
**
DFS on grid. For each cell matching first char, explore neighbors (up, down, left, right) recursively. Mark visited cells (e.g., '#') to avoid cycles, then backtrack (restore char).

**Code Example**:
```javascript
// DFS(r, c, index)
```

---

<a id="q60"></a>
### Q60: Median of Two Sorted Arrays?

**Difficulty**: Hard

**Strategy**:
**
Binary Search on partition of smaller array. Find partition such that `max(leftPart) <= min(rightPart)`. Time: O(log(min(n, m))).

**Code Example**:
```javascript
// Binary Search partition
```

---

<a id="q61"></a>
### Q61: Trapping Rain Water?

**Difficulty**: Hard

**Strategy**:
**
Two Pointers. `l`, `r`, `maxL`, `maxR`. If `height[l] < height[r]`, fill water based on `maxL - height[l]`, move `l`. Else fill based on `maxR`, move `r`. Time: O(n).

**Code Example**:
```javascript
// Two pointers moving inward
```

---

<a id="q62"></a>
### Q62: Largest Rectangle in Histogram?

**Difficulty**: Hard

**Strategy**:
**
Monotonic Stack (increasing). When `current < stack.top`, pop. Popped height is `h`, width is `current_i - stack.new_top - 1`.

**Code Example**:
```javascript
// Stack stores indices
```

---

<a id="q63"></a>
### Q63: Binary Tree Maximum Path Sum?

**Difficulty**: Hard

**Strategy**:
**
DFS. For each node, max path starting at node is `node.val + max(left, right)`. Update global max with `node.val + left + right` (path going through node).

**Code Example**:
```javascript
// Post-order traversal
```

---

<a id="q64"></a>
### Q64: Serialize and Deserialize Binary Tree?

**Difficulty**: Hard

**Strategy**:
**
Preorder traversal (DFS). Serialize: "1,2,X,X,3,X,X" (X is null). Deserialize: Use queue/iterator, reconstruct recursively.

**Code Example**:
```javascript
// DFS or BFS
```

---

<a id="q65"></a>
### Q65: Construct Binary Tree from Preorder and Inorder?

**Difficulty**: Intermediate

**Strategy**:
**
Preorder first element is root. Find root in Inorder. Left of root in Inorder is left subtree, right is right subtree. Recursively build.

**Code Example**:
```javascript
// Recursive with pointers/indices
```

---

<a id="q66"></a>
### Q66: Word Ladder (BFS)?

**Difficulty**: Hard

**Strategy**:
**
BFS for shortest path. Start word to End word. Neighbors are words differing by 1 char. Use a Set for word list for O(1) lookup.

**Code Example**:
```javascript
// BFS with Queue and Visited Set
```

---

<a id="q67"></a>
### Q67: Course Schedule (Topological Sort)?

**Difficulty**: Intermediate

**Strategy**:
**
Detect cycle in directed graph. Use DFS (recursion stack) or BFS (Kahn's algo with in-degrees). If cycle exists, impossible.

**Code Example**:
```javascript
// Cycle detection
```

---

<a id="q68"></a>
### Q68: Number of Connected Components?

**Difficulty**: Intermediate

**Strategy**:
**
Union-Find or DFS/BFS. Count number of times a new traversal starts. Or `n - numberOfUnions`.

**Code Example**:
```javascript
// Union-Find is efficient
```

---

<a id="q69"></a>
### Q69: Alien Dictionary?

**Difficulty**: Hard

**Strategy**:
**
Build graph from sorted words (compare adjacent words to find edge `char1 -> char2`). Perform Topological Sort.

**Code Example**:
```javascript
// Build Graph -> Topo Sort
```

---

<a id="q70"></a>
### Q70: House Robber?

**Difficulty**: Intermediate

**Strategy**:
**
DP. `rob(i) = max(rob(i-2) + nums[i], rob(i-1))`.

**Code Example**:
```javascript
// dp[i] = Math.max(dp[i-1], dp[i-2] + nums[i])
```

---

<a id="q71"></a>
### Q71: House Robber II (Circular)?

**Difficulty**: Intermediate

**Strategy**:
**
Break circle. Max of `rob(nums[0...n-2])` and `rob(nums[1...n-1])`.

**Code Example**:
```javascript
// Run House Robber I twice
```

---

<a id="q72"></a>
### Q72: Decode Ways?

**Difficulty**: Intermediate

**Strategy**:
**
DP. `dp[i]` ways to decode string of length `i`. If `s[i]` valid, `dp[i] += dp[i-1]`. If `s[i-1]s[i]` valid (10-26), `dp[i] += dp[i-2]`.

**Code Example**:
```javascript
// Similar to Climbing Stairs
```

---

<a id="q73"></a>
### Q73: Unique Paths?

**Difficulty**: Intermediate

**Strategy**:
**
DP. `dp[i][j] = dp[i-1][j] + dp[i][j-1]`. Or Math: Combinations `(m+n-2) C (m-1)`.

**Code Example**:
```javascript
// 2D DP or 1D optimized
```

---

<a id="q74"></a>
### Q74: Longest Common Subsequence?

**Difficulty**: Intermediate

**Strategy**:
**
2D DP. If `s1[i] == s2[j]`, `dp[i][j] = 1 + dp[i-1][j-1]`. Else `max(dp[i-1][j], dp[i][j-1])`.

**Code Example**:
```javascript
// Standard LCS
```

---

<a id="q75"></a>
### Q75: Word Break?

**Difficulty**: Intermediate

**Strategy**:
**
DP. `dp[i]` is true if `s[0...i]` can be segmented. `dp[i] = true` if `dp[j]` is true and `s[j...i]` in dictionary.

**Code Example**:
```javascript
// Check all valid substrings
```

---

<a id="q76"></a>
### Q76: Combination Sum?

**Difficulty**: Intermediate

**Strategy**:
**
Backtracking. Allow reusing same element. Sort candidates. Recurse with `target - num`. If target 0, add path.

**Code Example**:
```javascript
// Backtrack
```

---

<a id="q77"></a>
### Q77: Subsets?

**Difficulty**: Intermediate

**Strategy**:
**
Backtracking. At each step, either include `nums[i]` or not. Or iterate length 0 to n and backtrack.

**Code Example**:
```javascript
// Power Set
```

---

<a id="q78"></a>
### Q78: Permutations?

**Difficulty**: Intermediate

**Strategy**:
**
Backtracking. Swap elements or use `visited` array. `n!` complexity.

**Code Example**:
```javascript
// Backtrack with visited check
```

---

<a id="q79"></a>
### Q79: N-Queens?

**Difficulty**: Hard

**Strategy**:
**
Backtracking. Place queen row by row. Maintain sets for columns, diagonals, and anti-diagonals to check validity in O(1).

**Code Example**:
```javascript
// cols, diag1, diag2 sets
```

---

<a id="q80"></a>
### Q80: Implement LRU Cache?

**Difficulty**: Intermediate

**Strategy**:
**
Hash Map + Doubly Linked List. Map stores `key -> node`. Node has `val, prev, next`. On access, move node to head. On capacity full, remove tail.

**Code Example**:
```javascript
// Map + DLL
```

---

<a id="q81"></a>
### Q81: Implement LFU Cache?

**Difficulty**: Hard

**Strategy**:
**
Two Maps: `key -> val/freq` and `freq -> List of keys`. Also track `minFreq`. On access, update freq, move key to new freq list.

**Code Example**:
```javascript
// Complex Map logic
```

---

<a id="q82"></a>
### Q82: Find Median from Data Stream?

**Difficulty**: Hard

**Strategy**:
**
Two Heaps. Max-Heap for lower half, Min-Heap for upper half. Balance sizes. Median is top of heap(s).

**Code Example**:
```javascript
// Two Heaps
```

---

<a id="q83"></a>
### Q83: Sliding Window Maximum?

**Difficulty**: Hard

**Strategy**:
**
Monotonic Queue (Decreasing). Store indices. Remove out of window from front. Maintain decreasing order from back. Front is max.

**Code Example**:
```javascript
// Deque
```

---

<a id="q84"></a>
### Q84: Basic Calculator II?

**Difficulty**: Intermediate

**Strategy**:
**
Stack. Process `*` and `/` immediately (pop, calc, push). Push numbers for `+` and `-`. Sum stack at end.

**Code Example**:
```javascript
// Stack based parsing
```

---

<a id="q85"></a>
### Q85: Task Scheduler?

**Difficulty**: Intermediate

**Strategy**:
**
Greedy. Arrange most frequent tasks first with cooling intervals. Math formula: `(maxFreq - 1) * (n + 1) + countOfMaxFreq`.

**Code Example**:
```javascript
// Frequency calculation
```

---

<a id="q86"></a>
### Q86: K Closest Points to Origin?

**Difficulty**: Intermediate

**Strategy**:
**
Max-Heap of size K. Store points. If new point closer than heap top, pop and push. Or QuickSelect.

**Code Example**:
```javascript
// Heap or QuickSelect
```

---

<a id="q87"></a>
### Q87: Daily Temperatures?

**Difficulty**: Intermediate

**Strategy**:
**
Monotonic Stack (Decreasing). Store indices. If `curr > stack.top`, pop and record diff `curr_i - popped_i`.

**Code Example**:
```javascript
// Stack
```

---

<a id="q88"></a>
### Q88: Car Fleet?

**Difficulty**: Intermediate

**Strategy**:
**
Sort by position (descending). Calculate time to target. If `time[i] <= time[i-1]`, it becomes a fleet (slows down). Stack approach.

**Code Example**:
```javascript
// Sort + Stack/Linear Pass
```

---

<a id="q89"></a>
### Q89: Min Cost to Connect All Points?

**Difficulty**: Intermediate

**Strategy**:
**
Minimum Spanning Tree (Prim's or Kruskal's). Prim's is usually better for dense graph (points).

**Code Example**:
```javascript
// Prim's Algo
```

---

<a id="q90"></a>
### Q90: Network Delay Time?

**Difficulty**: Intermediate

**Strategy**:
**
Dijkstra's Algorithm. Find max of shortest paths to all nodes. If any node unreachable, return -1.

**Code Example**:
```javascript
// Dijkstra
```

---

<a id="q91"></a>
### Q91: Cheapest Flights Within K Stops?

**Difficulty**: Intermediate

**Strategy**:
**
Bellman-Ford or BFS (Level-wise). Run K+1 iterations of relaxing edges.

**Code Example**:
```javascript
// Bellman-Ford optimized
```

---

<a id="q92"></a>
### Q92: Reconstruct Itinerary?

**Difficulty**: Hard

**Strategy**:
**
Hierholzer's Algorithm for Eulerian Path. DFS. Visit edges, delete them, add node to result *after* visiting neighbors (post-order), then reverse.

**Code Example**:
```javascript
// Hierholzer's
```

---

<a id="q93"></a>
### Q93: Partition Equal Subset Sum?

**Difficulty**: Intermediate

**Strategy**:
**
0/1 Knapsack. Target = `sum / 2`. Can we get `sum / 2` using subset?

**Code Example**:
```javascript
// DP subset sum
```

---

<a id="q94"></a>
### Q94: Target Sum?

**Difficulty**: Intermediate

**Strategy**:
**
DP or DFS with Memoization. `dp(index, currentSum)`.

**Code Example**:
```javascript
// Memoization
```

---

<a id="q95"></a>
### Q95: Interleaving String?

**Difficulty**: Intermediate

**Strategy**:
**
2D DP. `dp[i][j]` is true if `s3[0...i+j]` is interleave of `s1[0...i]` and `s2[0...j]`.

**Code Example**:
```javascript
// 2D DP
```

---

<a id="q96"></a>
### Q96: Edit Distance?

**Difficulty**: Hard

**Strategy**:
**
2D DP. `dp[i][j]` min ops to convert `word1[0...i]` to `word2[0...j]`. Ops: Insert, Delete, Replace.

**Code Example**:
```javascript
// Levenshtein Distance
```

---

<a id="q97"></a>
### Q97: Burst Balloons?

**Difficulty**: Hard

**Strategy**:
**
DP (Matrix Chain Multiplication pattern). `dp[i][j]` max coins for range `(i, j)`. Iterate split point `k`.

**Code Example**:
```javascript
// Divide and Conquer DP
```

---

<a id="q98"></a>
### Q98: Regular Expression Matching?

**Difficulty**: Hard

**Strategy**:
**
DP. Handle `.` and `*`. `*` can count as 0 or more of previous. `dp[i][j]` match `s[0...i]` and `p[0...j]`.

**Code Example**:
```javascript
// Complex DP
```

---

<a id="q99"></a>
### Q99: Palindrome Partitioning?

**Difficulty**: Intermediate

**Strategy**:
**
Backtracking. Iterate `end` index. If `s[start...end]` is palindrome, add to path and recurse for `s[end+1...]`.

**Code Example**:
```javascript
// Backtracking + Palindrome Check
```

---

<a id="q100"></a>
### Q100: Word Search II?

**Difficulty**: Hard

**Strategy**:
**
Backtracking (DFS) + Trie. Build Trie from words. Iterate board. DFS checking if path exists in Trie.

**Code Example**:
```javascript
// Trie + DFS
```

---
