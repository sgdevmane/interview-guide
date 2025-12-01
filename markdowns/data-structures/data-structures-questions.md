<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Data Structures Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [Difference between Array and Linked List?](#q1) <span class="beginner">Beginner</span>
2. [Explain Stack and Queue?](#q2) <span class="beginner">Beginner</span>
3. [How does a Hash Map work?](#q3) <span class="intermediate">Intermediate</span>
4. [What is a Binary Search Tree (BST)?](#q4) <span class="intermediate">Intermediate</span>
5. [Explain BFS vs DFS?](#q5) <span class="intermediate">Intermediate</span>
6. [What is a Heap (Min/Max)?](#q6) <span class="intermediate">Intermediate</span>
7. [Detect cycle in Linked List?](#q7) <span class="intermediate">Intermediate</span>
8. [What is a Trie?](#q8) <span class="advanced">Advanced</span>
9. [Graph Representations?](#q9) <span class="intermediate">Intermediate</span>
10. [Implement LRU Cache?](#q10) <span class="advanced">Advanced</span>
11. [What is a Priority Queue?](#q11) <span class="intermediate">Intermediate</span>
12. [Tree vs Graph?](#q12) <span class="beginner">Beginner</span>
13. [Balanced Trees (AVL/Red-Black)?](#q13) <span class="advanced">Advanced</span>
14. [Middle of Linked List?](#q14) <span class="beginner">Beginner</span>
15. [What is a Bloom Filter?](#q15) <span class="advanced">Advanced</span>
16. [B-Trees in Databases?](#q16) <span class="advanced">Advanced</span>
17. [Queue using Stacks?](#q17) <span class="intermediate">Intermediate</span>
18. [Disjoint Set (Union-Find)?](#q18) <span class="advanced">Advanced</span>
19. [Cycle in Directed Graph?](#q19) <span class="advanced">Advanced</span>
20. [What is a Segment Tree?](#q20) <span class="advanced">Advanced</span>
21. [What is a Skip List?](#q21) <span class="advanced">Advanced</span>
22. [Array vs ArrayList (Dynamic Array)?](#q22) <span class="beginner">Beginner</span>
23. [What is a Circular Queue?](#q23) <span class="intermediate">Intermediate</span>
24. [Doubly Linked List vs Singly?](#q24) <span class="beginner">Beginner</span>
25. [What is a Deque (Double-ended Queue)?](#q25) <span class="intermediate">Intermediate</span>
26. [Adjacency Matrix vs Adjacency List?](#q26) <span class="intermediate">Intermediate</span>
27. [What is a Suffix Tree?](#q27) <span class="advanced">Advanced</span>
28. [Fenwick Tree (Binary Indexed Tree)?](#q28) <span class="advanced">Advanced</span>
29. [What is a Quadtree?](#q29) <span class="advanced">Advanced</span>
30. [KD-Tree (k-dimensional tree)?](#q30) <span class="advanced">Advanced</span>
31. [Hash Set vs Hash Map?](#q31) <span class="beginner">Beginner</span>
32. [What is Open Addressing?](#q32) <span class="advanced">Advanced</span>
33. [Separate Chaining vs Open Addressing?](#q33) <span class="advanced">Advanced</span>
34. [What is Consistent Hashing?](#q34) <span class="advanced">Advanced</span>
35. [Count-Min Sketch?](#q35) <span class="advanced">Advanced</span>
36. [What is a HyperLogLog?](#q36) <span class="advanced">Advanced</span>
37. [Inorder, Preorder, Postorder Traversal?](#q37) <span class="beginner">Beginner</span>
38. [Threaded Binary Tree?](#q38) <span class="advanced">Advanced</span>
39. [Splay Tree?](#q39) <span class="advanced">Advanced</span>
40. [Treap (Tree + Heap)?](#q40) <span class="advanced">Advanced</span>
41. [What is a Sparse Matrix?](#q41) <span class="intermediate">Intermediate</span>
42. [Inverted Index (Search Engines)?](#q42) <span class="intermediate">Intermediate</span>
43. [Difference between Set and List?](#q43) <span class="beginner">Beginner</span>
44. [What is a Tuple?](#q44) <span class="beginner">Beginner</span>
45. [Immutable vs Mutable Data Structures?](#q45) <span class="intermediate">Intermediate</span>
46. [What is a BitMap / BitSet?](#q46) <span class="intermediate">Intermediate</span>
47. [Rope Data Structure?](#q47) <span class="advanced">Advanced</span>
48. [Van Emde Boas Tree?](#q48) <span class="advanced">Advanced</span>
49. [Fibonacci Heap vs Binary Heap?](#q49) <span class="advanced">Advanced</span>
50. [Difference between Tree and Trie?](#q50) <span class="intermediate">Intermediate</span>
51. [What is a Splay Tree?](#q51) <span class="advanced">Advanced</span>
52. [What is a Treap?](#q52) <span class="advanced">Advanced</span>
53. [What is a Radix Tree (Patricia Trie)?](#q53) <span class="advanced">Advanced</span>
54. [What is a Fibonacci Heap?](#q54) <span class="expert">Expert</span>
55. [What is an Interval Tree?](#q55) <span class="advanced">Advanced</span>
56. [What is an R-Tree?](#q56) <span class="expert">Expert</span>
57. [What is an LSM Tree (Log-Structured Merge-Tree)?](#q57) <span class="expert">Expert</span>
58. [What is a Merkle Tree?](#q58) <span class="advanced">Advanced</span>
59. [What is an Inverted Index?](#q59) <span class="intermediate">Intermediate</span>
60. [What is a Sparse Matrix?](#q60) <span class="intermediate">Intermediate</span>
61. [What is a Ring Buffer (Circular Buffer)?](#q61) <span class="intermediate">Intermediate</span>
62. [What is a Rope Data Structure?](#q62) <span class="advanced">Advanced</span>
63. [What is Cuckoo Hashing?](#q63) <span class="expert">Expert</span>
64. [What is a Gap Buffer?](#q64) <span class="advanced">Advanced</span>
65. [What is a Piece Table?](#q65) <span class="expert">Expert</span>
66. [What is an XOR Linked List?](#q66) <span class="advanced">Advanced</span>
67. [What is a Geohash?](#q67) <span class="intermediate">Intermediate</span>
68. [What is a Bitset (Bitmap)?](#q68) <span class="intermediate">Intermediate</span>
69. [What is a Suffix Array?](#q69) <span class="advanced">Advanced</span>
70. [What is a Binary Heap vs Binomial Heap?](#q70) <span class="advanced">Advanced</span>
71. [What is a K-d Tree?](#q71) <span class="advanced">Advanced</span>
72. [What is a Quadtree?](#q72) <span class="advanced">Advanced</span>
73. [What is Huffman Coding?](#q73) <span class="intermediate">Intermediate</span>
74. [What is Run-Length Encoding (RLE)?](#q74) <span class="beginner">Beginner</span>
75. [What is Burrows-Wheeler Transform (BWT)?](#q75) <span class="expert">Expert</span>
76. [What is a Unrolled Linked List?](#q76) <span class="advanced">Advanced</span>
77. [What is a Skip List?](#q77) <span class="advanced">Advanced</span>
78. [What is a Self-Organizing List?](#q78) <span class="intermediate">Intermediate</span>
79. [What is a V-List?](#q79) <span class="expert">Expert</span>
80. [What is a Dancing Links (DLX) structure?](#q80) <span class="expert">Expert</span>
81. [What is a Cartesian Tree?](#q81) <span class="advanced">Advanced</span>
82. [What is a Ternary Search Tree?](#q82) <span class="advanced">Advanced</span>
83. [What is a BK-Tree (Burkhard-Keller Tree)?](#q83) <span class="advanced">Advanced</span>
84. [What is a Van Emde Boas Tree?](#q84) <span class="expert">Expert</span>
85. [What is a Disjoint Set (Union-Find)?](#q85) <span class="intermediate">Intermediate</span>
86. [What is a Fenwick Tree (BIT)?](#q86) <span class="advanced">Advanced</span>
87. [What is a Segment Tree?](#q87) <span class="advanced">Advanced</span>
88. [What is a Priority Queue?](#q88) <span class="beginner">Beginner</span>
89. [What is a Deque?](#q89) <span class="beginner">Beginner</span>
90. [What is a Bloom Filter?](#q90) <span class="advanced">Advanced</span>
91. [What is HyperLogLog?](#q91) <span class="advanced">Advanced</span>
92. [What is Count-Min Sketch?](#q92) <span class="advanced">Advanced</span>
93. [What is Consistent Hashing?](#q93) <span class="advanced">Advanced</span>
94. [What is Spatial Hashing?](#q94) <span class="intermediate">Intermediate</span>
95. [What is Perfect Hashing?](#q95) <span class="expert">Expert</span>
96. [What is Hopscotch Hashing?](#q96) <span class="expert">Expert</span>
97. [What is a Z-Order Curve?](#q97) <span class="advanced">Advanced</span>
98. [What is a B-Tree?](#q98) <span class="advanced">Advanced</span>
99. [What is a B+ Tree?](#q99) <span class="advanced">Advanced</span>
100. [What is a Hilbert Curve?](#q100) <span class="expert">Expert</span>

---

---

---

<a id="q1"></a>

### Q1: Difference between Array and Linked List?

**Difficulty**: Beginner

**Strategy**:
Arrays and Linked Lists differ fundamentally in memory allocation and access patterns.

- **Array**: Stores elements in contiguous memory locations. This allows `O(1)` random access via index but requires contiguous space. Insertions/deletions are `O(n)` because elements must shift.
- **Linked List**: Stores elements as nodes scattered in memory, linked by pointers. Access is `O(n)` (sequential), but insertions/deletions are `O(1)` if the pointer to the location is known (no shifting required).

**Complexity**:
| Operation | Array | Linked List |
|-----------|-------|-------------|
| Access | O(1) | O(n) |
| Insert | O(n) | O(1)_ |
| Delete | O(n) | O(1)_ |
_\*Assuming we are at the node position._

**Code Example**:

```javascript
// Array
const arr = [10, 20, 30];
console.log(arr[1]); // O(1) Access

// Linked List Node
class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

const head = new Node(10);
head.next = new Node(20); // Linked via pointers
console.log(head.next.val); // Traversal needed
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q2"></a>

### Q2: Explain Stack and Queue?

**Difficulty**: Beginner

**Strategy**:
Both are linear data structures with different access rules.

- **Stack (LIFO)**: Last In, First Out. Like a stack of plates. Operations: `push()` (add top), `pop()` (remove top). Used in recursion, undo mechanisms, syntax parsing.
- **Queue (FIFO)**: First In, First Out. Like a line at a store. Operations: `enqueue()` (add rear), `dequeue()` (remove front). Used in task scheduling, BFS, printer jobs.

**Code Example**:

```javascript
// Stack
const stack = [];
stack.push(1);
stack.push(2);
console.log(stack.pop()); // 2 (Last In First Out)

// Queue
const queue = [];
queue.push(1);
queue.push(2);
console.log(queue.shift()); // 1 (First In First Out)
// Note: Array.shift() is O(n), real queues use linked lists for O(1).
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q3"></a>

### Q3: How does a Hash Map work?

**Difficulty**: Intermediate

**Strategy**:
A Hash Map stores key-value pairs. It uses a **hash function** to convert the key into an index (bucket) in an array.

1.  **Hash Function**: Computes index `idx = hash(key) % size`.
2.  **Collision Handling**: If two keys hash to the same index:
    - **Chaining**: Store a Linked List (or Tree) at that index.
    - **Open Addressing**: Probe for the next empty slot.

**Complexity**:

- **Average**: `O(1)` for search, insert, delete.
- **Worst Case**: `O(n)` (many collisions, degrading to linked list).

**Code Example**:

```javascript
class SimpleHashMap {
  constructor() {
    this.map = {};
  }
  put(key, value) {
    // Simple hash simulation using object property
    this.map[key] = value;
  }
  get(key) {
    return this.map[key];
  }
}
// Real implementation involves handling array indices and collisions manually.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q4"></a>

### Q4: What is a Binary Search Tree (BST)?

**Difficulty**: Intermediate

**Strategy**:
A BST is a binary tree where for every node:

- Left subtree values < Node value.
- Right subtree values > Node value.
  This property enables binary search behavior.

**Complexity**:

- Search/Insert/Delete: `O(log n)` (Balanced), `O(n)` (Skewed/Unbalanced).

**Code Example**:

```javascript
class TreeNode {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

function searchBST(root, val) {
  if (!root || root.val === val) return root;
  if (val < root.val) return searchBST(root.left, val);
  return searchBST(root.right, val);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q5"></a>

### Q5: Explain BFS vs DFS?

**Difficulty**: Intermediate

**Strategy**:
Two main algorithms to traverse graphs/trees.

- **BFS (Breadth-First Search)**: Explores neighbor nodes first before moving to next level neighbors. Uses a **Queue**. Best for finding shortest path in unweighted graphs.
- **DFS (Depth-First Search)**: Explores as deep as possible along each branch before backtracking. Uses a **Stack** (or Recursion). Best for path existence, topological sort, cycle detection.

**Code Example**:

```javascript
// BFS
function bfs(startNode) {
  const queue = [startNode];
  const visited = new Set();
  while (queue.length) {
    const node = queue.shift();
    console.log(node.val);
    for (let neighbor of node.neighbors) {
      if (!visited.has(neighbor)) {
        visited.add(neighbor);
        queue.push(neighbor);
      }
    }
  }
}

// DFS (Recursive)
function dfs(node, visited = new Set()) {
  if (!node || visited.has(node)) return;
  console.log(node.val);
  visited.add(node);
  for (let neighbor of node.neighbors) dfs(neighbor, visited);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q6"></a>

### Q6: What is a Heap (Min/Max)?

**Difficulty**: Intermediate

**Strategy**:
A Heap is a specialized binary tree-based structure (usually implemented as an array) that satisfies the heap property:

- **Max-Heap**: Parent node is always $\ge$ children. Root is the maximum.
- **Min-Heap**: Parent node is always $\le$ children. Root is the minimum.
  It is a **complete binary tree**.
  Commonly used for Priority Queues.

**Complexity**:

- Access Max/Min: `O(1)`
- Insert/Extract: `O(log n)`

**Code Example**:

```javascript
// Array representation of Heap:
// Parent(i) -> floor((i-1)/2)
// Left(i) -> 2*i + 1
// Right(i) -> 2*i + 2
const minHeap = [1, 3, 5, 10, 8]; // 1 is root (min)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q7"></a>

### Q7: Detect cycle in Linked List?

**Difficulty**: Intermediate

**Strategy**:
Use **Floyd’s Cycle-Finding Algorithm** (Tortoise and Hare).

1.  Initialize two pointers, `slow` and `fast`, at the head.
2.  Move `slow` by 1 step and `fast` by 2 steps.
3.  If `fast` meets `slow`, there is a cycle.
4.  If `fast` reaches `null`, there is no cycle.

**Complexity**:

- Time: `O(n)`
- Space: `O(1)`

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

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q8"></a>

### Q8: What is a Trie?

**Difficulty**: Advanced

**Strategy**:
A Trie (Prefix Tree) is a tree-based structure used for efficient retrieval of keys in a dataset of strings. Each node represents a character.

- Useful for **autocomplete**, spell checking, and IP routing.
- Root is empty.
- Paths from root to node define the string.

**Complexity**:

- Insert/Search: `O(L)` where `L` is string length.
- Space: `O(AL)` where `A` is alphabet size.

**Code Example**:

```javascript
class TrieNode {
  constructor() {
    this.children = {};
    this.isEndOfWord = false;
  }
}

class Trie {
  constructor() {
    this.root = new TrieNode();
  }

  insert(word) {
    let node = this.root;
    for (let char of word) {
      if (!node.children[char]) node.children[char] = new TrieNode();
      node = node.children[char];
    }
    node.isEndOfWord = true;
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q9"></a>

### Q9: Graph Representations?

**Difficulty**: Intermediate

**Strategy**:
Graphs can be represented mainly in two ways:

1.  **Adjacency Matrix**: 2D array `matrix[i][j] = 1` if edge exists.
    - Pros: O(1) check edge.
    - Cons: O(V^2) space. Good for dense graphs.
2.  **Adjacency List**: Array of lists/maps. `adj[i]` contains neighbors of `i`.
    - Pros: O(V+E) space. Good for sparse graphs.

**Code Example**:

```javascript
// Adjacency Matrix (for nodes 0,1,2)
const matrix = [
  [0, 1, 0], // Node 0 -> 1
  [1, 0, 1], // Node 1 -> 0, 2
  [0, 1, 0], // Node 2 -> 1
];

// Adjacency List
const list = {
  0: [1],
  1: [0, 2],
  2: [1],
};
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q10"></a>

### Q10: Implement LRU Cache?

**Difficulty**: Advanced

**Strategy**:
LRU (Least Recently Used) Cache evicts the least recently accessed item when full.

- Use **Hash Map** + **Doubly Linked List**.
- **Map**: Key -> Node (O(1) access).
- **List**: Maintains order.
  - Head: Most recently used.
  - Tail: Least recently used.
- **Access**: Move node to Head.
- **Evict**: Remove Tail.

**Code Example**:

```javascript
class Node {
  constructor(key, val) {
    this.key = key;
    this.val = val;
    this.prev = null;
    this.next = null;
  }
}

class LRUCache {
  constructor(capacity) {
    this.cap = capacity;
    this.map = new Map();
    this.head = new Node(0, 0); // Dummy head
    this.tail = new Node(0, 0); // Dummy tail
    this.head.next = this.tail;
    this.tail.prev = this.head;
  }

  get(key) {
    if (this.map.has(key)) {
      const node = this.map.get(key);
      this.remove(node);
      this.insert(node);
      return node.val;
    }
    return -1;
  }

  put(key, value) {
    if (this.map.has(key)) this.remove(this.map.get(key));
    if (this.map.size === this.cap) this.remove(this.tail.prev);
    this.insert(new Node(key, value));
  }

  remove(node) {
    this.map.delete(node.key);
    node.prev.next = node.next;
    node.next.prev = node.prev;
  }

  insert(node) {
    this.map.set(node.key, node);
    const headNext = this.head.next;
    this.head.next = node;
    node.prev = this.head;
    node.next = headNext;
    headNext.prev = node;
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q11"></a>

### Q11: What is a Priority Queue?

**Difficulty**: Intermediate

**Strategy**:
A Priority Queue is an abstract data type where each element has a "priority". Elements with higher priority are served before elements with lower priority.

- Usually implemented with a **Heap**.
- **Operations**: `enqueue` (insert), `dequeue` (extract max/min).

**Code Example**:

```javascript
// Conceptual usage (using an array and sorting for simplicity, O(n log n))
// Real implementation uses Heap for O(log n)
const pq = [];
pq.push({ task: "Low", p: 1 });
pq.push({ task: "High", p: 10 });
pq.sort((a, b) => b.p - a.p); // Sort by priority
console.log(pq.shift()); // {task: 'High', p: 10}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q12"></a>

### Q12: Tree vs Graph?

**Difficulty**: Beginner

**Strategy**:

- **Tree**: A restricted graph.
  - Connected, no cycles.
  - N nodes have exactly N-1 edges.
  - Hierarchical structure (Root -> Children).
  - One path between any two nodes.
- **Graph**: General collection of nodes (vertices) and edges.
  - Can have cycles.
  - Can be disconnected.
  - Can be directed/undirected.
  - Network structure.

**Code Example**:

```javascript
// Tree: Root with children
const tree = { val: 1, children: [{ val: 2 }, { val: 3 }] };

// Graph: Nodes with neighbors (potentially cyclic)
const nodeA = { val: "A", neighbors: [] };
const nodeB = { val: "B", neighbors: [] };
nodeA.neighbors.push(nodeB);
nodeB.neighbors.push(nodeA); // Cycle A <-> B
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q13"></a>

### Q13: Balanced Trees (AVL/Red-Black)?

**Difficulty**: Advanced

**Strategy**:
Self-balancing BSTs ensure the tree height remains `O(log n)` after insertions/deletions to prevent degradation to `O(n)`.

- **AVL Tree**: Strictly balanced. Difference in height of left/right subtrees is at most 1. Good for lookups.
- **Red-Black Tree**: Loosely balanced using color properties. Good for insertions/deletions (fewer rotations). Used in Java `TreeMap`, C++ `std::map`.

**Code Example**:

```javascript
// Concept: Rotations
// Left Rotation example:
//     A          B
//      \        /
//       B  ->  A
//      /        \
//     C          C
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q14"></a>

### Q14: Middle of Linked List?

**Difficulty**: Beginner

**Strategy**:
Use the **Two Pointer** approach (Tortoise and Hare).

1.  `slow` moves 1 step.
2.  `fast` moves 2 steps.
3.  When `fast` reaches the end, `slow` will be at the middle.

**Code Example**:

```javascript
function findMiddle(head) {
  let slow = head,
    fast = head;
  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
  }
  return slow; // Middle node
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q15"></a>

### Q15: What is a Bloom Filter?

**Difficulty**: Advanced

**Strategy**:
A probabilistic data structure that tests if an element is in a set.

- **False Positives**: Possible (Says "Maybe in set").
- **False Negatives**: Impossible (Says "Definitely not in set" is 100% true).
- Uses a bit array and multiple hash functions.
- Space efficient. Used in database caches, spell checkers.

**Code Example**:

```javascript
// Concept
// 1. Initialize bit array of 0s.
// 2. Hash(item) -> index1, index2, index3...
// 3. Set bits at indices to 1.
// 4. Check: If all bits are 1, maybe present. If any is 0, definitely not.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q16"></a>

### Q16: B-Trees in Databases?

**Difficulty**: Advanced

**Strategy**:
A B-Tree is a self-balancing tree data structure that maintains sorted data and allows searches, sequential access, insertions, and deletions in logarithmic time.

- Optimized for systems that read/write large blocks of data (Disks/Databases).
- Nodes have many children (high branching factor), reducing tree height and disk I/O.
- **B+ Tree** (variant): Data only in leaves, internal nodes only keys. Leaves linked for range scans.

**Code Example**:

```text
// Structure of a Node: [Key1, Key2]
// Children: [Ptr1, Ptr2, Ptr3]
// Keys in children are between keys in parent.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q17"></a>

### Q17: Queue using Stacks?

**Difficulty**: Intermediate

**Strategy**:
Use two stacks: `inputStack` and `outputStack`.

- **Enqueue**: Push to `inputStack`.
- **Dequeue**:
  1.  If `outputStack` is empty, pop all from `inputStack` and push to `outputStack` (reverses order).
  2.  Pop from `outputStack`.

**Complexity**:

- Amortized O(1) for dequeue.

**Code Example**:

```javascript
class QueueUsingStacks {
  constructor() {
    this.inStack = [];
    this.outStack = [];
  }
  enqueue(val) {
    this.inStack.push(val);
  }
  dequeue() {
    if (this.outStack.length === 0) {
      while (this.inStack.length) this.outStack.push(this.inStack.pop());
    }
    return this.outStack.pop();
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q18"></a>

### Q18: Disjoint Set (Union-Find)?

**Difficulty**: Advanced

**Strategy**:
Data structure to track elements partitioned into disjoint subsets.

- **Find**: Determine which subset an element belongs to.
- **Union**: Join two subsets.
- Optimizations: **Path Compression** (flatten tree during find) and **Union by Rank** (attach small tree to large tree).
- Used in Kruskal’s MST, cycle detection in undirected graphs.

**Code Example**:

```javascript
class UnionFind {
  constructor(n) {
    this.parent = Array(n)
      .fill(0)
      .map((_, i) => i);
  }
  find(i) {
    if (this.parent[i] !== i) {
      this.parent[i] = this.find(this.parent[i]); // Path compression
    }
    return this.parent[i];
  }
  union(i, j) {
    const rootI = this.find(i);
    const rootJ = this.find(j);
    if (rootI !== rootJ) this.parent[rootI] = rootJ;
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q19"></a>

### Q19: Cycle in Directed Graph?

**Difficulty**: Advanced

**Strategy**:
Use **DFS**. Keep track of nodes in current recursion stack.

- `visited`: Node fully processed.
- `recursionStack`: Node currently being visited (ancestors).
- If we encounter a node in `recursionStack`, cycle detected.

**Code Example**:

```javascript
function hasCycle(graph, nodes) {
  const visited = new Set();
  const recStack = new Set();

  function dfs(node) {
    if (recStack.has(node)) return true;
    if (visited.has(node)) return false;

    visited.add(node);
    recStack.add(node);

    for (let neighbor of graph[node]) {
      if (dfs(neighbor)) return true;
    }

    recStack.delete(node);
    return false;
  }

  for (let node of nodes) {
    if (dfs(node)) return true;
  }
  return false;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q20"></a>

### Q20: What is a Segment Tree?

**Difficulty**: Advanced

**Strategy**:
A tree used for storing information about intervals or segments.

- Allows querying which of the stored segments contain a given point.
- Efficiently answers range queries (e.g., sum, min, max in range `[L, R]`) in `O(log n)`.
- Updates in `O(log n)`.

**Code Example**:

```javascript
// Range Sum Query
// Tree array stores sums.
// Root covers [0, n-1], Left [0, mid], Right [mid+1, n-1]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q21"></a>

### Q21: What is a Skip List?

**Difficulty**: Advanced

**Strategy**:
A probabilistic data structure based on parallel linked lists.

- Allows fast search within an ordered sequence of elements.
- Layers of linked lists: Bottom layer has all nodes. Higher layers skip nodes.
- **Search/Insert/Delete**: `O(log n)` average.
- Alternative to balanced trees.

**Code Example**:

```text
Level 3: 1 -----------------> 10
Level 2: 1 -----> 5 --------> 10
Level 1: 1 -> 3 -> 5 -> 7 -> 9 -> 10
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q22"></a>

### Q22: Array vs ArrayList (Dynamic Array)?

**Difficulty**: Beginner

**Strategy**:

- **Array**: Fixed size. Cannot grow once initialized.
- **ArrayList (Java) / Vector (C++) / Array (JS/Python)**: Dynamic size.
  - Resizes automatically. When full, creates new larger array (usually 2x), copies elements.
  - Amortized insertion time `O(1)`.

**Code Example**:

```javascript
// JS Arrays are dynamic by default
const list = [];
for (let i = 0; i < 100; i++) list.push(i); // Automatically resizes
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q23"></a>

### Q23: What is a Circular Queue?

**Difficulty**: Intermediate

**Strategy**:
A queue where the last position is connected back to the first position (Ring Buffer).

- Efficient use of fixed buffer space.
- Avoids shifting elements when dequeueing.
- Used in traffic lights, CPU scheduling, streaming buffering.

**Code Example**:

```javascript
// Index calculation
// next_pos = (current_pos + 1) % capacity
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q24"></a>

### Q24: Doubly Linked List vs Singly?

**Difficulty**: Beginner

**Strategy**:

- **Singly Linked List**: Node has `next` pointer.
  - Less memory.
  - Forward traversal only.
- **Doubly Linked List**: Node has `next` and `prev` pointers.
  - More memory (extra pointer).
  - Bidirectional traversal.
  - Easier deletion (O(1) if node is given, as we have access to `prev`).

**Code Example**:

```javascript
class DNode {
  constructor(val) {
    this.val = val;
    this.next = null;
    this.prev = null;
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q25"></a>

### Q25: What is a Deque (Double-ended Queue)?

**Difficulty**: Intermediate

**Strategy**:
A generalized queue that allows insertion and deletion at both ends (Front and Rear).

- Combines Stack and Queue features.
- Operations: `pushFront`, `pushBack`, `popFront`, `popBack`.
- Used in Sliding Window Maximum problems.

**Code Example**:

```javascript
const deque = [];
deque.unshift(1); // Add Front
deque.push(2); // Add Back
deque.shift(); // Remove Front
deque.pop(); // Remove Back
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q26"></a>

### Q26: Adjacency Matrix vs Adjacency List?

**Difficulty**: Intermediate

**Strategy**:
Comparing graph representations:

- **Adjacency Matrix**: `V x V` matrix.
  - **Space**: `O(V^2)`.
  - **Check Edge**: `O(1)`.
  - **Iterate Neighbors**: `O(V)`.
  - Best for dense graphs.
- **Adjacency List**: Array of Lists.
  - **Space**: `O(V + E)`.
  - **Check Edge**: `O(degree(V))`.
  - **Iterate Neighbors**: `O(degree(V))`.
  - Best for sparse graphs (most real-world graphs).

**Code Example**:

```javascript
// Matrix: Good for quick lookups
if (matrix[u][v] === 1) return true;

// List: Good for memory
for (let neighbor of list[u]) process(neighbor);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q27"></a>

### Q27: What is a Suffix Tree?

**Difficulty**: Advanced

**Strategy**:
A compressed Trie containing all suffixes of a given text.

- Used for fast pattern matching, finding longest repeated substring, longest common substring.
- **Construction**: `O(n)` using Ukkonen’s algorithm.
- **Search**: `O(m)` where `m` is pattern length.

**Code Example**:

```text
Text: "BANANA"
Suffixes: BANANA, ANANA, NANA, ANA, NA, A
Tree stores these suffixes efficiently sharing common prefixes.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q28"></a>

### Q28: Fenwick Tree (Binary Indexed Tree)?

**Difficulty**: Advanced

**Strategy**:
A data structure that provides efficient methods for calculation and manipulation of the prefix sums of a table of values.

- **Update**: `O(log n)`.
- **Prefix Sum**: `O(log n)`.
- Easier to implement than Segment Tree but less flexible (mostly for cumulative frequency).

**Code Example**:

```javascript
// Get sum from 0 to i
function query(i) {
  let sum = 0;
  for (; i > 0; i -= i & -i) sum += tree[i];
  return sum;
}
// Add val to index i
function update(i, val) {
  for (; i < n; i += i & -i) tree[i] += val;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q29"></a>

### Q29: What is a Quadtree?

**Difficulty**: Advanced

**Strategy**:
A tree data structure in which each internal node has exactly four children.

- Used to partition a two-dimensional space by recursively subdividing it into four quadrants.
- Common in **Image Processing**, **Spatial Indexing**, **Collision Detection** (Games).

**Code Example**:

```javascript
class QuadNode {
  constructor(boundary) {
    this.boundary = boundary; // Rect(x, y, w, h)
    this.points = [];
    this.nw = null; // North West
    this.ne = null; // North East
    this.sw = null; // South West
    this.se = null; // South East
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q30"></a>

### Q30: KD-Tree (k-dimensional tree)?

**Difficulty**: Advanced

**Strategy**:
A space-partitioning data structure for organizing points in a `k`-dimensional space.

- Similar to BST but cycles through dimensions (e.g., x-split, then y-split, then z-split).
- Used for **Nearest Neighbor Search** and Range Search.
- Complexity: Average `O(log n)` insert/search.

**Code Example**:

```text
Level 0 (Root): Split by X-coordinate
Level 1: Split by Y-coordinate
Level 2: Split by X-coordinate
...
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q31"></a>

### Q31: Hash Set vs Hash Map?

**Difficulty**: Beginner

**Strategy**:

- **Hash Map**: Stores **Key-Value** pairs. Keys are unique. Used for lookups.
- **Hash Set**: Stores only **Values** (or Keys without values). Values are unique. Used for membership tests.
- Internally, a Set is often implemented as a Map with dummy values.

**Code Example**:

```javascript
const set = new Set([1, 2, 2, 3]); // {1, 2, 3}
const map = new Map();
map.set("a", 1);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q32"></a>

### Q32: What is Open Addressing?

**Difficulty**: Advanced

**Strategy**:
A method for handling collisions in Hash Tables. All elements are stored in the hash table array itself.

- If a collision occurs, search for another open slot.
- **Linear Probing**: Check `i+1, i+2...`
- **Quadratic Probing**: Check `i+1^2, i+2^2...`
- **Double Hashing**: Use a second hash function.

**Code Example**:

```javascript
// Linear Probing
let index = hash(key);
while (table[index] !== null) {
  index = (index + 1) % size;
}
table[index] = value;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q33"></a>

### Q33: Separate Chaining vs Open Addressing?

**Difficulty**: Advanced

**Strategy**:

- **Separate Chaining**:
  - Bucket contains a list.
  - Tolerates high Load Factor (> 1).
  - More memory overhead (pointers).
- **Open Addressing**:
  - Everything in array.
  - Load Factor must be < 1 (usually resize at 0.7).
  - Better Cache locality (Linear probing).

**Code Example**:

```text
Chaining: [A] -> [B] -> null
Open: [A, B, null, C]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q34"></a>

### Q34: What is Consistent Hashing?

**Difficulty**: Advanced

**Strategy**:
A hashing technique used in distributed systems to minimize reorganization when nodes are added/removed.

- Maps keys and nodes to a **Hash Ring** (0 to 2^32).
- Key is assigned to the first node found clockwise.
- **Virtual Nodes**: Used to balance load.
- Used in DynamoDB, Cassandra, Load Balancers.

**Code Example**:

```text
Ring: [NodeA] ... [Key1] ... [NodeB]
Key1 maps to NodeB.
If NodeB removed, Key1 maps to next node (NodeC).
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q35"></a>

### Q35: Count-Min Sketch?

**Difficulty**: Advanced

**Strategy**:
A probabilistic data structure for estimating frequency of events in a stream.

- Uses a 2D array of counters and multiple hash functions.
- **Update**: Increment counters at hashed indices.
- **Query**: Return minimum of counters at hashed indices.
- Overestimates frequency (never underestimates). Space efficient.

**Code Example**:

```javascript
// Add(x):
// row1[h1(x)]++
// row2[h2(x)]++
// ...
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q36"></a>

### Q36: What is a HyperLogLog?

**Difficulty**: Advanced

**Strategy**:
A probabilistic algorithm for the **Count-Distinct** problem (Cardinality estimation).

- Estimates number of unique elements in a large dataset.
- Uses `O(log log n)` space.
- Relies on observing the position of the leftmost '1' bit in hashed values.

**Code Example**:

```text
Stream: User IDs
Result: "Approx 1.2M unique users" (with 2KB memory)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q37"></a>

### Q37: Inorder, Preorder, Postorder Traversal?

**Difficulty**: Beginner

**Strategy**:
DFS traversal orders for Binary Trees:

- **Inorder (Left-Root-Right)**: Sorted order for BST.
- **Preorder (Root-Left-Right)**: Useful for copying tree / serialization.
- **Postorder (Left-Right-Root)**: Useful for deleting tree / evaluating math expressions.

**Code Example**:

```javascript
function inorder(node) {
  if (!node) return;
  inorder(node.left);
  console.log(node.val);
  inorder(node.right);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q38"></a>

### Q38: Threaded Binary Tree?

**Difficulty**: Advanced

**Strategy**:
A binary tree where null pointers are replaced by "threads" to other nodes (predecessor/successor).

- Allows **Stack-less** traversal.
- Efficient finding of inorder successor.
- Memory optimization (uses null space).

**Code Example**:

```text
Node.right is null? Point it to Inorder Successor.
Flag: isThreaded = true.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q39"></a>

### Q39: Splay Tree?

**Difficulty**: Advanced

**Strategy**:
A self-balancing BST with the property that recently accessed elements are quick to access again.

- **Splay Operation**: Moves the accessed node to the **Root** via rotations.
- Good for caches / locality of reference.
- Amortized `O(log n)`.

**Code Example**:

```text
Search(x) -> Found x -> Rotate x to top.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q40"></a>

### Q40: Treap (Tree + Heap)?

**Difficulty**: Advanced

**Strategy**:
A Cartesian Tree where every node has a **Key** (BST property) and a **Priority** (Heap property).

- Priorities are usually assigned randomly.
- Ensures tree stays balanced with high probability.
- Operations: Split and Merge.

**Code Example**:

```javascript
// Node: { key: 5, priority: 87, left, right }
// Keys sorted left-right.
// Priorities sorted parent-child (Max Heap).
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q41"></a>

### Q41: What is a Sparse Matrix?

**Difficulty**: Intermediate

**Strategy**:
A matrix where most elements are zero.

- Storing as 2D array is wasteful.
- **Storage Formats**:
  - **Coordinate List (COO)**: List of `(row, col, value)` tuples.
  - **CSR (Compressed Sparse Row)**: 3 arrays (Values, Column Indices, Row Pointers). Efficient for arithmetic.

**Code Example**:

```javascript
// COO
const sparse = [
  { r: 0, c: 1, val: 5 },
  { r: 2, c: 0, val: 9 },
];
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q42"></a>

### Q42: Inverted Index (Search Engines)?

**Difficulty**: Intermediate

**Strategy**:
A mapping from content (words) to its location in database/documents.

- Core component of Full Text Search (Elasticsearch, Lucene).
- **Structure**: Word -> List of Document IDs.

**Code Example**:

```javascript
const index = {
  apple: [1, 3, 5], // Appears in Doc 1, 3, 5
  banana: [2, 3],
};
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q43"></a>

### Q43: Difference between Set and List?

**Difficulty**: Beginner

**Strategy**:

- **List**: Ordered collection. Allows duplicates. Accessed by index.
- **Set**: Unordered collection. Unique elements. No index access (usually).

**Code Example**:

```javascript
// List
const list = [1, 2, 2];
// Set
const set = new Set([1, 2, 2]); // {1, 2}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q44"></a>

### Q44: What is a Tuple?

**Difficulty**: Beginner

**Strategy**:
A data structure representing an ordered list of elements.

- Usually **Immutable** (cannot be changed after creation).
- Can contain mixed types.
- Used as keys in maps (if hashable) or returning multiple values from functions.

**Code Example**:

```python
# Python Tuple
point = (10, 20)
# point[0] = 5 # Error!
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q45"></a>

### Q45: Immutable vs Mutable Data Structures?

**Difficulty**: Intermediate

**Strategy**:

- **Mutable**: Can be modified in-place.
  - Pros: Efficiency (no copying).
  - Cons: Thread safety issues, side effects.
- **Immutable**: Cannot be modified. Any change creates a new copy.
  - Pros: Thread safe, predictable state (Redux/React).
  - Cons: Memory/CPU overhead for copies (mitigated by Structural Sharing).

**Code Example**:

```javascript
// Mutable
let obj = { a: 1 };
obj.a = 2;

// Immutable (Spread)
const newObj = { ...obj, a: 3 };
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q46"></a>

### Q46: What is a BitMap / BitSet?

**Difficulty**: Intermediate

**Strategy**:
An array of bits (0 or 1) used to compactly store boolean values.

- Space efficient (1 bit vs 1 byte/word).
- Fast bitwise operations (AND, OR, XOR).
- Used in Bloom Filters, Database Indexing.

**Code Example**:

```javascript
// Represent set {0, 2, 5}
// 100101 (Binary) -> 37 (Integer)
const hasZero = (37 & (1 << 0)) !== 0; // True
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q47"></a>

### Q47: Rope Data Structure?

**Difficulty**: Advanced

**Strategy**:
A tree-based data structure for storing strings.

- Used for efficiently storing and manipulating very long strings (e.g., in Text Editors).
- Concatenation is `O(1)` (create new root).
- Access is `O(log n)`.
- Better than standard string (array of chars) for heavy editing.

**Code Example**:

```text
     (Root: Len 10)
    /            \
(Leaf: "Hello")  (Leaf: "World")
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q48"></a>

### Q48: Van Emde Boas Tree?

**Difficulty**: Advanced

**Strategy**:
A tree data structure for an associative array with integer keys from `0` to `U-1`.

- Operations (Insert, Delete, Find, Successor) run in `O(log log U)`.
- Exploits bit manipulation and universe size.
- Faster than normal BST `O(log n)` when `U` is reasonable.

**Code Example**:

```text
// Recursive structure dividing universe size by square root.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q49"></a>

### Q49: Fibonacci Heap vs Binary Heap?

**Difficulty**: Advanced

**Strategy**:

- **Binary Heap**: Standard heap. `O(log n)` for insert/decrease-key.
- **Fibonacci Heap**: More complex.
  - **Insert**: `O(1)` amortized.
  - **Decrease Key**: `O(1)` amortized.
  - **Extract Min**: `O(log n)`.
  - Crucial for **Dijkstra’s** and **Prim’s** algorithms speedup.

**Code Example**:

```text
// Collection of trees. Trees are merged lazily.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q50"></a>

### Q50: Difference between Tree and Trie?

**Difficulty**: Intermediate

**Strategy**:

- **Tree**: General hierarchy. Keys stored in nodes. Search compares keys. `O(log n)` (BST).
- **Trie**: Specific for strings. Edges represent characters. Keys (strings) are defined by the path. `O(L)` where `L` is string length. Independent of number of keys `N`.

**Code Example**:

```text
Tree: Node(5) -> Node(2), Node(8)
Trie: Root -('c')-> Node -('a')-> Node -('t')-> Node(isWord)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

<a id="q51"></a>

### Q51: What is a Splay Tree?

**Difficulty**: Advanced

**Strategy:**
A self-adjusting binary search tree where recently accessed elements are moved to the root ("splayed"). This provides fast access to frequently used elements. Amortized time complexity for operations is O(log n).

**Code Example:**

```javascript
// Access(x) -> Splay(x) -> x becomes root
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q52"></a>

### Q52: What is a Treap?

**Difficulty**: Advanced

**Strategy:**
A randomized binary search tree that maintains two values per node: a 'key' (BST property) and a 'priority' (Heap property). It provides O(log n) expected time for operations by using rotations to satisfy heap property after insertion/deletion.

**Code Example:**

```javascript
// Node { key, priority, left, right }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q53"></a>

### Q53: What is a Radix Tree (Patricia Trie)?

**Difficulty**: Advanced

**Strategy:**
A space-optimized Trie where each node that is the only child is merged with its parent. It reduces the depth of the tree by compressing common prefixes.

**Code Example:**

```text
"test", "team" -> "te" -> "st", "am"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q54"></a>

### Q54: What is a Fibonacci Heap?

**Difficulty**: Expert

**Strategy:**
A heap data structure consisting of a forest of trees. It has better amortized running time than Binomial heaps. `Decrease-Key` is O(1) amortized, making it ideal for Dijkstra's and Prim's algorithms.

**Code Example:**

```text
Used internally in advanced graph algorithms.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q55"></a>

### Q55: What is an Interval Tree?

**Difficulty**: Advanced

**Strategy:**
A tree data structure to hold intervals. It allows efficiently finding all intervals that overlap with any given interval or point. Augmented BST where each node stores the max endpoint in its subtree.

**Code Example:**

```javascript
// Search for overlap: check root, go left/right based on max
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---


<a id="q56"></a>

### Q56: What is an R-Tree?

**Difficulty**: Expert

**Strategy:**
A tree data structure used for spatial access methods, i.e., for indexing multi-dimensional information such as geographical coordinates, rectangles, or polygons. Used in databases like PostGIS.

**Code Example:**

```text
Groups nearby objects into Minimum Bounding Rectangles (MBRs).
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q57"></a>

### Q57: What is an LSM Tree (Log-Structured Merge-Tree)?

**Difficulty**: Expert

**Strategy:**
A data structure used in write-heavy databases (Cassandra, RocksDB). Writes go to an in-memory MemTable (sorted). When full, flushed to disk as SSTable (immutable). Compaction merges SSTables in background.

**Code Example:**

```text
Write -> MemTable -> Flush -> SSTable (Level 0) -> Merge -> Level 1
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q58"></a>

### Q58: What is a Merkle Tree?

**Difficulty**: Advanced

**Strategy:**
A hash tree where every leaf node is a hash of a data block, and every non-leaf node is a hash of its children. Used in Blockchains (Bitcoin, Git) to verify data integrity efficiently.

**Code Example:**

```text
Root Hash covers all data. Changing one block changes root.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q59"></a>

### Q59: What is an Inverted Index?

**Difficulty**: Intermediate

**Strategy:**
An index data structure storing a mapping from content, such as words or numbers, to its locations in a document or a set of documents. The core of search engines (Elasticsearch).

**Code Example:**

```json
{
  "apple": [1, 5, 8], // Doc IDs
  "banana": [2, 3]
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q60"></a>

### Q60: What is a Sparse Matrix?

**Difficulty**: Intermediate

**Strategy:**
A matrix in which most of the elements are zero. Stored efficiently using lists (COO, CSR formats) containing only non-zero values and their indices, saving memory.

**Code Example:**

```javascript
// CSR: Values[], ColumnIndices[], RowPtr[]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q61"></a>

### Q61: What is a Ring Buffer (Circular Buffer)?

**Difficulty**: Intermediate

**Strategy:**
A fixed-size buffer that acts as if it were connected end-to-end. Useful for streaming data, audio processing, and queues where old data is overwritten by new data.

**Code Example:**

```javascript
// writeIndex = (writeIndex + 1) % capacity
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q62"></a>

### Q62: What is a Rope Data Structure?

**Difficulty**: Advanced

**Strategy:**
A tree-based data structure used to store and manipulate very long strings efficiently. Concatenation is O(1), while it's O(n) for standard strings/arrays. Used in text editors.

**Code Example:**

```text
Node(Left: "Hello ", Right: "World")
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q63"></a>

### Q63: What is Cuckoo Hashing?

**Difficulty**: Expert

**Strategy:**
A hashing scheme resolving collisions using multiple hash functions and tables. If a bucket is full, the existing key is "kicked out" to its alternative location, potentially causing a chain of displacements. Lookup is O(1) worst-case.

**Code Example:**

```text
Key x -> Hash1(x) or Hash2(x)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q64"></a>

### Q64: What is a Gap Buffer?

**Difficulty**: Advanced

**Strategy:**
A dynamic array implementation used in text editors. It has a "gap" (empty space) at the cursor position, allowing O(1) insertions and deletions at the cursor by shifting the gap.

**Code Example:**

```text
[H, e, l, l, o, _, _, _, W, o, r, l, d]
Cursor at index 5.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q65"></a>

### Q65: What is a Piece Table?

**Difficulty**: Expert

**Strategy:**
A data structure for text editors managing an original file buffer and an add buffer. The document is a list of "pieces" pointing to spans in these buffers. Supports efficient undo/redo.

**Code Example:**

```text
Piece 1: Original[0-5] ("Hello")
Piece 2: Add[0-1] (" ")
Piece 3: Original[6-10] ("World")
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---


<a id="q66"></a>

### Q66: What is an XOR Linked List?

**Difficulty**: Advanced

**Strategy:**
A memory-efficient doubly linked list. Instead of storing `prev` and `next` pointers, each node stores `prev XOR next`. Traversal requires knowing the address of the previous node.

**Code Example:**

```text
Node.npx = Address(prev) ^ Address(next)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q67"></a>

### Q67: What is a Geohash?

**Difficulty**: Intermediate

**Strategy:**
A geocoding system that encodes a geographic location into a short string of letters and digits. Longer strings are more precise. Nearby points often have similar prefixes.

**Code Example:**

```text
"u4pruydqqvj" -> Lat/Lon
```

<div align="right"><a href="#table-of-contents">Back to Top ��</a></div>

---

<a id="q68"></a>

### Q68: What is a Bitset (Bitmap)?

**Difficulty**: Intermediate

**Strategy:**
A compact array of bits (booleans). Efficient for storing sets of integers or flags. Operations (union, intersection) can be done using bitwise logic in parallel.

**Code Example:**

```javascript
// Checking if user ID 5 is active: (bitmap >> 5) & 1
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q69"></a>

### Q69: What is a Suffix Array?

**Difficulty**: Advanced

**Strategy:**
A sorted array of all suffixes of a string. Used with LCP (Longest Common Prefix) array for efficient string pattern matching, finding longest repeated substring, etc. Space efficient compared to Suffix Tree.

**Code Example:**

```text
"banana" -> suffixes: "a", "ana", "anana", "banana", "na", "nana"
Sorted: 5, 3, 1, 0, 4, 2
```

<div align="right"><a href="#table-of-contents">Back to Top ��</a></div>

---

<a id="q70"></a>

### Q70: What is a Binary Heap vs Binomial Heap?

**Difficulty**: Advanced

**Strategy:**
Binary Heap is a complete binary tree. Binomial Heap is a collection of Binomial Trees. Binomial Heaps support faster merging of two heaps (O(log n)) compared to Binary Heap (O(n)).

**Code Example:**

```text
Merge: Link trees of same order.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q71"></a>

### Q71: What is a K-d Tree?

**Difficulty**: Advanced

**Strategy:**
A space-partitioning data structure for organizing points in a k-dimensional space. Useful for nearest neighbor search and range searches (e.g., finding points within a radius).

**Code Example:**

```text
Split planes cycle: x-axis, y-axis, z-axis...
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q72"></a>

### Q72: What is a Quadtree?

**Difficulty**: Advanced

**Strategy:**
A tree where each internal node has exactly four children. Used to partition a two-dimensional space by recursively subdividing it into four quadrants. Common in image processing and game collision detection.

**Code Example:**

```text
Root -> NW, NE, SW, SE
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q73"></a>

### Q73: What is Huffman Coding?

**Difficulty**: Intermediate

**Strategy:**
A lossless data compression algorithm. It builds a binary tree where frequently used characters have shorter paths (codes) from the root.

**Code Example:**

```text
'e': 0, 'a': 10, 'z': 110
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q74"></a>

### Q74: What is Run-Length Encoding (RLE)?

**Difficulty**: Beginner

**Strategy:**
A simple compression form where sequences of same data value are stored as a single data value and count.

**Code Example:**

```text
"AAABBBCC" -> "3A3B2C"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q75"></a>

### Q75: What is Burrows-Wheeler Transform (BWT)?

**Difficulty**: Expert

**Strategy:**
Rearranges a character string into runs of similar characters. Used in compression (bzip2). It makes the string more compressible by RLE.

**Code Example:**

```text
Transforms string to grouping of chars: "banana" -> "nnbaaa"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---


<a id="q76"></a>

### Q76: What is a Unrolled Linked List?

**Difficulty**: Advanced

**Strategy:**
A linked list where each node stores an array of elements instead of just one. Increases cache locality and reduces memory overhead for pointers.

**Code Example:**

```text
Node -> [1, 2, 3, 4] -> Node -> [5, 6]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q77"></a>

### Q77: What is a Skip List?

**Difficulty**: Advanced

**Strategy:**
A probabilistic data structure that allows O(log n) search complexity within an ordered sequence of elements. It uses multiple layers of linked lists, skipping over elements.

**Code Example:**

```text
L2: 1 --------> 10
L1: 1 -> 5 ---> 10
L0: 1 -> 3 -> 5 -> 7 -> 10
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q78"></a>

### Q78: What is a Self-Organizing List?

**Difficulty**: Intermediate

**Strategy:**
A list that reorders its elements based on access frequency. Heuristics: Move-to-Front (move accessed item to head) or Transpose (swap with predecessor).

**Code Example:**

```text
Access 5 in [1, 2, 5] -> [5, 1, 2] (Move-to-Front)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q79"></a>

### Q79: What is a V-List?

**Difficulty**: Expert

**Strategy:**
A hybrid of array and linked list. It is a list of arrays where each array is typically double the size of the previous one. Allows O(1) average indexing with the flexibility of a list.

**Code Example:**

```text
[1] -> [2, 3] -> [4, 5, 6, 7]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q80"></a>

### Q80: What is a Dancing Links (DLX) structure?

**Difficulty**: Expert

**Strategy:**
A technique using circular doubly linked lists to implement Algorithm X for exact cover problems (like Sudoku, N-Queens). Efficiently removes and restores rows/columns during backtracking.

**Code Example:**

```text
Used in Knuth's Algorithm X.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q81"></a>

### Q81: What is a Cartesian Tree?

**Difficulty**: Advanced

**Strategy:**
A binary tree derived from a sequence of numbers. It is heap-ordered (parent <= children) and an inorder traversal yields the original sequence. Used for Range Minimum Query (RMQ).

**Code Example:**

```text
Smallest element is root. Left/Right subtrees are Cartesian trees of left/right subarrays.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q82"></a>

### Q82: What is a Ternary Search Tree?

**Difficulty**: Advanced

**Strategy:**
A type of Trie where nodes are arranged in a manner similar to a BST. Each node has 3 children: low, equal, high. More space-efficient than standard Trie for sparse datasets.

**Code Example:**

```text
Node for char 'a'. Left: < 'a', Middle: = 'a', Right: > 'a'
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q83"></a>

### Q83: What is a BK-Tree (Burkhard-Keller Tree)?

**Difficulty**: Advanced

**Strategy:**
A tree data structure adapted to discrete metric spaces. Used for approximate string matching (spell checking) based on Levenshtein distance.

**Code Example:**

```text
Edge weights represent edit distance.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q84"></a>

### Q84: What is a Van Emde Boas Tree?

**Difficulty**: Expert

**Strategy:**
A tree data structure which implements an associative array with m-bit integer keys. It performs all operations in O(log m) time, which is O(log log U) where U is the universe size.

**Code Example:**

```text
Recursive structure dividing universe size by sqrt(U).
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q85"></a>

### Q85: What is a Disjoint Set (Union-Find)?

**Difficulty**: Intermediate

**Strategy:**
A data structure that keeps track of a set of elements partitioned into a number of disjoint (non-overlapping) subsets. Operations: `Union` and `Find`. Uses Path Compression and Union by Rank for near O(1) time.

**Code Example:**

```javascript
parent[rootA] = rootB; // Union
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---


<a id="q86"></a>

### Q86: What is a Fenwick Tree (BIT)?

**Difficulty**: Advanced

**Strategy:**
Binary Indexed Tree. Provides methods to calculate prefix sums and update elements in O(log n). Easier to implement than Segment Tree but less flexible (only prefix operations).

**Code Example:**

```javascript
update(i, delta) { while(i <= n) tree[i] += delta; i += i & -i; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q87"></a>

### Q87: What is a Segment Tree?

**Difficulty**: Advanced

**Strategy:**
A tree used for storing information about intervals or segments. It allows querying which of the stored segments contain a given point. Powerful for range queries (sum, min, max) and range updates.

**Code Example:**

```text
Root covers [0, n-1]. Children [0, mid] and [mid+1, n-1].
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q88"></a>

### Q88: What is a Priority Queue?

**Difficulty**: Beginner

**Strategy:**
An abstract data type where each element has a priority. Elements with higher priority are served before elements with lower priority. Usually implemented with a Heap.

**Code Example:**

```text
Insert: O(log n). Pull: O(log n).
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q89"></a>

### Q89: What is a Deque?

**Difficulty**: Beginner

**Strategy:**
Double-Ended Queue. Allows insertion and deletion of elements from both the front and the back.

**Code Example:**

```javascript
// pushFront, pushBack, popFront, popBack
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q90"></a>

### Q90: What is a Bloom Filter?

**Difficulty**: Advanced

**Strategy:**
A probabilistic data structure used to test whether an element is a member of a set. False positives are possible, but false negatives are not. Space efficient.

**Code Example:**

```text
Hash k times. Check if all k bits are set.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q91"></a>

### Q91: What is HyperLogLog?

**Difficulty**: Advanced

**Strategy:**
A probabilistic algorithm for the cardinality estimation problem (counting distinct elements). Uses very little memory to count huge datasets with acceptable error rate.

**Code Example:**

```text
Count unique IP addresses in a stream.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q92"></a>

### Q92: What is Count-Min Sketch?

**Difficulty**: Advanced

**Strategy:**
A probabilistic data structure that serves as a frequency table of events in a stream of data. Uses multiple hash functions and arrays to estimate frequency.

**Code Example:**

```text
"Heavy Hitters" problem.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q93"></a>

### Q93: What is Consistent Hashing?

**Difficulty**: Advanced

**Strategy:**
A hashing technique where only K/n keys need to be remapped on average when a slot (node) is added or removed. Keys and nodes are mapped to a ring.

**Code Example:**

```text
Used in Distributed Caches (DynamoDB, Cassandra).
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q94"></a>

### Q94: What is Spatial Hashing?

**Difficulty**: Intermediate

**Strategy:**
A process of mapping a 3D or 2D space into a 1D hash table. Used in game development for broad-phase collision detection (grouping nearby objects).

**Code Example:**

```text
Grid cell (x, y) -> Hash(x, y) -> Bucket
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q95"></a>

### Q95: What is Perfect Hashing?

**Difficulty**: Expert

**Strategy:**
A hash function that maps distinct elements to a set of integers with no collisions. Static perfect hashing is used when the set of keys is known in advance.

**Code Example:**

```text
Lookup tables for keywords in compilers.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q96"></a>

### Q96: What is Hopscotch Hashing?

**Difficulty**: Expert

**Strategy:**
A scheme for resolving hash collisions that combines elements of cuckoo hashing and linear probing. It guarantees that an item is found within a fixed neighborhood of its original hash bucket.

**Code Example:**

```text
Optimized for cache locality.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q97"></a>

### Q97: What is a Z-Order Curve?

**Difficulty**: Advanced

**Strategy:**
A space-filling curve that maps multidimensional data to one dimension while preserving locality. Used in databases for spatial indexing (interleaving bits).

**Code Example:**

```text
(x, y) -> Morton Code
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q98"></a>

### Q98: What is a B-Tree?

**Difficulty**: Advanced

**Strategy:**
A self-balancing tree data structure that maintains sorted data and allows searches, sequential access, insertions, and deletions in logarithmic time. Optimized for disk storage (databases, file systems).

**Code Example:**

```text
Nodes contain multiple keys and children.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q99"></a>

### Q99: What is a B+ Tree?

**Difficulty**: Advanced

**Strategy:**
A variant of B-Tree where all data is stored in leaf nodes, and leaf nodes are linked. This makes range queries and sequential access much faster. Standard for DB indexes.

**Code Example:**

```text
Internal nodes: only keys. Leaf nodes: keys + data + next ptr.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q100"></a>

### Q100: What is a Hilbert Curve?

**Difficulty**: Expert

**Strategy:**
A continuous fractal space-filling curve. It preserves locality better than Z-Order curve. Used in spatial databases to map 2D to 1D for indexing.

**Code Example:**

```text
Spatial Indexing.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

