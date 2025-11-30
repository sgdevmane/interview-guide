# Data Structures Interview Questions

## Table of Contents

1. [Difference between Array and Linked List?](#q1-difference-between-array-and-linked-list) <span class="beginner">Beginner</span>
2. [Explain Stack and Queue data structures?](#q2-explain-stack-and-queue-data-structures) <span class="beginner">Beginner</span>
3. [How does a Hash Map work?](#q3-how-does-a-hash-map-work) <span class="intermediate">Intermediate</span>
4. [What is a Binary Search Tree (BST)?](#q4-what-is-a-binary-search-tree-bst) <span class="intermediate">Intermediate</span>
5. [Explain the difference between BFS and DFS?](#q5-explain-the-difference-between-bfs-and-dfs) <span class="intermediate">Intermediate</span>
6. [What is a Heap (Min-Heap vs Max-Heap)?](#q6-what-is-a-heap-min-heap-vs-max-heap) <span class="intermediate">Intermediate</span>
7. [How do you detect a cycle in a Linked List?](#q7-how-do-you-detect-a-cycle-in-a-linked-list) <span class="intermediate">Intermediate</span>
8. [What is a Trie (Prefix Tree)?](#q8-what-is-a-trie-prefix-tree) <span class="advanced">Advanced</span>
9. [Explain Graph representations (Adjacency Matrix vs List)?](#q9-explain-graph-representations-adjacency-matrix-vs-list) <span class="intermediate">Intermediate</span>
10. [How do you implement an LRU Cache?](#q10-how-do-you-implement-an-lru-cache) <span class="advanced">Advanced</span>
11. [What is a Priority Queue?](#q11-what-is-a-priority-queue) <span class="intermediate">Intermediate</span>
12. [Difference between Tree and Graph?](#q12-difference-between-tree-and-graph) <span class="beginner">Beginner</span>
13. [What is a Balanced Binary Tree (AVL/Red-Black)?](#q13-what-is-a-balanced-binary-tree-avl-red-black) <span class="advanced">Advanced</span>
14. [How do you find the middle element of a Linked List?](#q14-how-do-you-find-the-middle-element-of-a-linked-list) <span class="beginner">Beginner</span>
15. [What is a Bloom Filter?](#q15-what-is-a-bloom-filter) <span class="advanced">Advanced</span>
16. [Explain B-Trees and their use in Databases?](#q16-explain-b-trees-and-their-use-in-databases) <span class="advanced">Advanced</span>
17. [How to implement a Queue using Stacks?](#q17-how-to-implement-a-queue-using-stacks) <span class="intermediate">Intermediate</span>
18. [What is a Disjoint Set (Union-Find)?](#q18-what-is-a-disjoint-set-union-find) <span class="advanced">Advanced</span>
19. [Detecting a cycle in a directed graph?](#q19-detecting-a-cycle-in-a-directed-graph) <span class="advanced">Advanced</span>
20. [What is a Segment Tree?](#q20-what-is-a-segment-tree) <span class="advanced">Advanced</span>

---

<div id="q1-difference-between-array-and-linked-list" class="question">
  1. Difference between Array and Linked List?
  <span class="difficulty beginner">Beginner</span>
</div>

<div class="answer">
  <p><strong>Arrays</strong> and <strong>Linked Lists</strong> are fundamental linear data structures, but they differ significantly in how they store and access data.</p>
  <ul>
    <li><strong>Memory Layout:</strong> Arrays store elements in contiguous memory locations. Linked Lists store elements (nodes) in non-contiguous memory, linked by pointers.</li>
    <li><strong>Access Time:</strong> Arrays allow O(1) random access (accessing elements by index). Linked Lists require O(n) sequential access (traversing from the head).</li>
    <li><strong>Insertion/Deletion:</strong> Insertion/Deletion in Arrays is O(n) because elements must be shifted. In Linked Lists, it's O(1) if the pointer to the location is known (just updating pointers).</li>
    <li><strong>Size:</strong> Arrays usually have a fixed size (static arrays) or resizing is expensive (dynamic arrays). Linked Lists are dynamic and can grow/shrink easily.</li>
  </ul>
</div>

<div id="q2-explain-stack-and-queue-data-structures" class="question">
  2. Explain Stack and Queue data structures?
  <span class="difficulty beginner">Beginner</span>
</div>

<div class="answer">
  <p><strong>Stack (LIFO - Last In, First Out):</strong></p>
  <ul>
    <li>Think of a stack of plates. You add to the top and remove from the top.</li>
    <li><strong>Operations:</strong> <code>push()</code> (add), <code>pop()</code> (remove), <code>peek()</code> (view top).</li>
    <li><strong>Use cases:</strong> Function call stack (recursion), undo mechanisms, parsing expressions.</li>
  </ul>
  <p><strong>Queue (FIFO - First In, First Out):</strong></p>
  <ul>
    <li>Think of a line at a ticket counter. The first person in line is the first served.</li>
    <li><strong>Operations:</strong> <code>enqueue()</code> (add to rear), <code>dequeue()</code> (remove from front), <code>front()</code>.</li>
    <li><strong>Use cases:</strong> Job scheduling (printer queue), BFS traversal, handling requests in a server.</li>
  </ul>
</div>

<div id="q3-how-does-a-hash-map-work" class="question">
  3. How does a Hash Map work?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <p>A <strong>Hash Map</strong> (or Hash Table) stores key-value pairs and offers O(1) average time complexity for insertion, deletion, and lookup.</p>
  <ul>
    <li><strong>Hashing Function:</strong> Converts a key (string, number, object) into an integer index (hash code).</li>
    <li><strong>Bucket Array:</strong> The data is stored in an array. The index is calculated as <code>hash(key) % array_size</code>.</li>
    <li><strong>Collision Handling:</strong> Since two keys might hash to the same index (collision), strategies are used:
      <ul>
        <li><strong>Chaining:</strong> Each bucket points to a linked list (or tree) of entries.</li>
        <li><strong>Open Addressing:</strong> Finds the next available slot using probing (linear, quadratic, etc.).</li>
      </ul>
    </li>
  </ul>
  <pre><code class="language-javascript">// Simple conceptual implementation
class HashTable {
  constructor(size = 50) {
    this.buckets = new Array(size);
    this.size = size;
  }

hash(key) {
let total = 0;
for (let char of key) total += char.charCodeAt(0);
return total % this.size;
}

set(key, value) {
let index = this.hash(key);
if (!this.buckets[index]) this.buckets[index] = [];
this.buckets[index].push([key, value]);
}
}</code></pre>

</div>

<div id="q4-what-is-a-binary-search-tree-bst" class="question">
  4. What is a Binary Search Tree (BST)?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <p>A <strong>Binary Search Tree</strong> is a binary tree with a specific ordering property:</p>
  <ul>
    <li>The value of the <strong>left</strong> child is strictly less than the parent node.</li>
    <li>The value of the <strong>right</strong> child is strictly greater than the parent node.</li>
    <li>This property must hold true for every node in the tree.</li>
  </ul>
  <p><strong>Complexity:</strong> Search, Insert, and Delete operations are O(log n) on average (balanced tree), but can degrade to O(n) in the worst case (skewed tree, like a linked list).</p>
</div>

<div id="q5-explain-the-difference-between-bfs-and-dfs" class="question">
  5. Explain the difference between BFS and DFS?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <p><strong>BFS (Breadth-First Search):</strong></p>
  <ul>
    <li>Explores neighbors layer by layer (level by level).</li>
    <li>Uses a <strong>Queue</strong> data structure.</li>
    <li><strong>Best for:</strong> Finding the shortest path in an unweighted graph, level-order traversal.</li>
  </ul>
  <p><strong>DFS (Depth-First Search):</strong></p>
  <ul>
    <li>Explores as deep as possible along each branch before backtracking.</li>
    <li>Uses a <strong>Stack</strong> (or recursion).</li>
    <li><strong>Best for:</strong> Pathfinding maze puzzles, topological sorting, detecting cycles.</li>
  </ul>
</div>

<div id="q6-what-is-a-heap-min-heap-vs-max-heap" class="question">
  6. What is a Heap (Min-Heap vs Max-Heap)?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <p>A <strong>Heap</strong> is a specialized binary tree-based data structure that satisfies the heap property. It is a complete binary tree.</p>
  <ul>
    <li><strong>Max-Heap:</strong> The value of each node is greater than or equal to the values of its children. The root contains the maximum element.</li>
    <li><strong>Min-Heap:</strong> The value of each node is less than or equal to the values of its children. The root contains the minimum element.</li>
  </ul>
  <p><strong>Usage:</strong> Heaps are used to implement Priority Queues and the Heapsort algorithm. Accessing the min/max is O(1), while insertion/deletion is O(log n).</p>
</div>

<div id="q7-how-do-you-detect-a-cycle-in-a-linked-list" class="question">
  7. How do you detect a cycle in a Linked List?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <p>The most common efficient approach is <strong>Floyd's Cycle-Finding Algorithm</strong> (Tortoise and Hare).</p>
  <ul>
    <li>Use two pointers: <code>slow</code> (moves 1 step) and <code>fast</code> (moves 2 steps).</li>
    <li>If there is a cycle, the <code>fast</code> pointer will eventually enter the cycle and catch up to the <code>slow</code> pointer from behind.</li>
    <li>If <code>fast</code> reaches <code>null</code>, there is no cycle.</li>
  </ul>
  <pre><code class="language-javascript">function hasCycle(head) {
  let slow = head;
  let fast = head;
  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
    if (slow === fast) return true;
  }
  return false;
}</code></pre>
</div>

<div id="q8-what-is-a-trie-prefix-tree" class="question">
  8. What is a Trie (Prefix Tree)?
  <span class="difficulty advanced">Advanced</span>
</div>

<div class="answer">
  <p>A <strong>Trie</strong> is a tree-like data structure used to efficiently store and retrieve keys in a dataset of strings.</p>
  <ul>
    <li>Each node represents a character of a string.</li>
    <li>The root is empty, and paths from the root to a node represent prefixes.</li>
    <li><strong>Complexity:</strong> Searching for a word of length <code>m</code> takes O(m) time, which is very fast compared to Hash Tables for prefix-based searches.</li>
    <li><strong>Use Cases:</strong> Autocomplete, spell checking, IP routing (longest prefix match).</li>
  </ul>
</div>

<div id="q9-explain-graph-representations-adjacency-matrix-vs-list" class="question">
  9. Explain Graph representations (Adjacency Matrix vs List)?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <p>Graphs can be represented primarily in two ways:</p>
  <ul>
    <li><strong>Adjacency Matrix:</strong> A 2D array <code>V x V</code> where <code>matrix[i][j]</code> indicates an edge between vertex <code>i</code> and <code>j</code>.
      <ul>
        <li><strong>Pros:</strong> O(1) to check if an edge exists.</li>
        <li><strong>Cons:</strong> Consumes O(V²) space, sparse graphs waste space.</li>
      </ul>
    </li>
    <li><strong>Adjacency List:</strong> An array/map where each vertex stores a list of its neighbors.
      <ul>
        <li><strong>Pros:</strong> Saves space O(V + E), efficient for iteration over neighbors.</li>
        <li><strong>Cons:</strong> O(V) to check if a specific edge exists.</li>
      </ul>
    </li>
  </ul>
</div>

<div id="q10-how-do-you-implement-an-lru-cache" class="question">
  10. How do you implement an LRU Cache?
  <span class="difficulty advanced">Advanced</span>
</div>

<div class="answer">
  <p>An <strong>LRU (Least Recently Used) Cache</strong> discards the least recently used items first when the cache is full.</p>
  <p><strong>Implementation:</strong> Combine a <strong>Hash Map</strong> with a <strong>Doubly Linked List</strong>.</p>
  <ul>
    <li><strong>Hash Map:</strong> Stores <code>key -> node_pointer</code> for O(1) access.</li>
    <li><strong>Doubly Linked List:</strong> Maintains the order of usage.
      <ul>
        <li>Most recently used items are moved to the <strong>head</strong>.</li>
        <li>Least recently used items are at the <strong>tail</strong>.</li>
      </ul>
    </li>
    <li>When accessing an item: Move it to the head.</li>
    <li>When inserting a new item: Add to head. If full, remove from tail and delete from map.</li>
  </ul>
</div>

<div id="q11-what-is-a-priority-queue" class="question">
  11. What is a Priority Queue?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <p>A <strong>Priority Queue</strong> is an abstract data type where each element has a "priority". Elements with higher priority are served before elements with lower priority.</p>
  <ul>
    <li>Unlike a standard queue (FIFO), the order is determined by priority.</li>
    <li>Usually implemented using a <strong>Heap</strong> (Binary Heap).</li>
    <li><strong>Operations:</strong> <code>insert</code> (O(log n)), <code>pull/extract-max</code> (O(log n)), <code>peek</code> (O(1)).</li>
    <li><strong>Use Cases:</strong> Dijkstra's shortest path algorithm, task scheduling in OS, Huffman coding.</li>
  </ul>
</div>

<div id="q12-difference-between-tree-and-graph" class="question">
  12. Difference between Tree and Graph?
  <span class="difficulty beginner">Beginner</span>
</div>

<div class="answer">
  <ul>
    <li><strong>Hierarchy:</strong> A Tree is a hierarchical structure (parent-child relationship). A Graph is a network model (peer-to-peer).</li>
    <li><strong>Cycles:</strong> A Tree cannot have cycles. A Graph can be cyclic or acyclic.</li>
    <li><strong>Root:</strong> A Tree has a unique root node. A Graph has no concept of a root (though traversals start from a source).</li>
    <li><strong>Connectivity:</strong> A Tree is always connected. A Graph can be disconnected.</li>
    <li><strong>Edges:</strong> Trees have N-1 edges for N nodes. Graphs can have up to N(N-1)/2 edges.</li>
  </ul>
</div>

<div id="q13-what-is-a-balanced-binary-tree-avl-red-black" class="question">
  13. What is a Balanced Binary Tree (AVL/Red-Black)?
  <span class="difficulty advanced">Advanced</span>
</div>

<div class="answer">
  <p>A <strong>Balanced Binary Tree</strong> self-adjusts to keep its height minimal (logarithmic) after insertions and deletions to ensure O(log n) operations.</p>
  <ul>
    <li><strong>AVL Tree:</strong> Strictly balanced. The heights of two child subtrees of any node differ by at most one. Requires more rotations during insertion/deletion. Good for lookup-heavy workloads.</li>
    <li><strong>Red-Black Tree:</strong> Loosely balanced. Uses color bits (red/black) and rules to ensure the longest path is no more than twice the shortest. Requires fewer rotations. Good for insertion/deletion-heavy workloads (used in Java TreeMap, C++ std::map).</li>
  </ul>
</div>

<div id="q14-how-do-you-find-the-middle-element-of-a-linked-list" class="question">
  14. How do you find the middle element of a Linked List?
  <span class="difficulty beginner">Beginner</span>
</div>

<div class="answer">
  <p>Use the <strong>Two Pointer Technique</strong>:</p>
  <ul>
    <li>Initialize two pointers, <code>slow</code> and <code>fast</code>, at the head.</li>
    <li>Move <code>slow</code> one step at a time.</li>
    <li>Move <code>fast</code> two steps at a time.</li>
    <li>When <code>fast</code> reaches the end (null), <code>slow</code> will be at the middle.</li>
  </ul>
  <pre><code class="language-javascript">function findMiddle(head) {
  let slow = head;
  let fast = head;
  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
  }
  return slow; // Middle node
}</code></pre>
</div>

<div id="q15-what-is-a-bloom-filter" class="question">
  15. What is a Bloom Filter?
  <span class="difficulty advanced">Advanced</span>
</div>

<div class="answer">
  <p>A <strong>Bloom Filter</strong> is a probabilistic data structure used to test whether an element is a member of a set.</p>
  <ul>
    <li><strong>Properties:</strong> It is space-efficient but can produce <strong>false positives</strong> (it might say "yes" when the item isn't there). It never produces <strong>false negatives</strong> (if it says "no", the item is definitely not there).</li>
    <li><strong>How it works:</strong> Uses a bit array and multiple hash functions. Adding an element sets bits at hashed indices to 1. Checking involves verifying if all hashed indices are 1.</li>
    <li><strong>Use Cases:</strong> Database query caching (checking if row exists before disk read), checking for weak passwords, spell checkers.</li>
  </ul>
</div>

<div id="q16-explain-b-trees-and-their-use-in-databases" class="question">
  16. Explain B-Trees and their use in Databases?
  <span class="difficulty advanced">Advanced</span>
</div>

<div class="answer">
  <p>A <strong>B-Tree</strong> is a self-balancing tree data structure that maintains sorted data and allows searches, sequential access, insertions, and deletions in logarithmic time.</p>
  <ul>
    <li>Unlike binary trees, B-Tree nodes can have more than two children.</li>
    <li>Optimized for systems that read and write large blocks of data (like Disks/SSDs).</li>
    <li><strong>Databases (SQL):</strong> Indexes are typically implemented using B-Trees (or B+ Trees) because they minimize the number of disk I/O operations required to find a record (due to their high branching factor and low height).</li>
  </ul>
</div>

<div id="q17-how-to-implement-a-queue-using-stacks" class="question">
  17. How to implement a Queue using Stacks?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <p>You need two stacks: <code>inputStack</code> and <code>outputStack</code>.</p>
  <ul>
    <li><strong>Enqueue:</strong> Push the element onto <code>inputStack</code>.</li>
    <li><strong>Dequeue:</strong>
      <ol>
        <li>If <code>outputStack</code> is empty, pop all elements from <code>inputStack</code> and push them onto <code>outputStack</code> (this reverses the order).</li>
        <li>Pop from <code>outputStack</code>.</li>
      </ol>
    </li>
    <li>The amortized time complexity is O(1), though a single dequeue operation can be O(n).</li>
  </ul>
</div>

<div id="q18-what-is-a-disjoint-set-union-find" class="question">
  18. What is a Disjoint Set (Union-Find)?
  <span class="difficulty advanced">Advanced</span>
</div>

<div class="answer">
  <p>A <strong>Disjoint Set</strong> is a data structure that keeps track of a set of elements partitioned into a number of disjoint (non-overlapping) subsets.</p>
  <ul>
    <li><strong>Operations:</strong>
      <ul>
        <li><code>Find(x)</code>: Determine which subset element <code>x</code> belongs to.</li>
        <li><code>Union(x, y)</code>: Join two subsets into a single subset.</li>
      </ul>
    </li>
    <li><strong>Optimizations:</strong> Path Compression and Union by Rank/Size make operations nearly constant time O(α(n)).</li>
    <li><strong>Use Cases:</strong> Kruskal's algorithm for Minimum Spanning Tree, detecting cycles in undirected graphs, image processing (connected components).</li>
  </ul>
</div>

<div id="q19-detecting-a-cycle-in-a-directed-graph" class="question">
  19. Detecting a cycle in a directed graph?
  <span class="difficulty advanced">Advanced</span>
</div>

<div class="answer">
  <p>In a directed graph, a simple visited array isn't enough. You need to track the <strong>recursion stack</strong>.</p>
  <ul>
    <li>Use DFS. Keep track of nodes currently in the recursion stack (ancestors of the current node).</li>
    <li>If you encounter a node that is already in the current recursion stack, a cycle exists (back edge).</li>
    <li>Alternatively, use <strong>Kahn's Algorithm</strong> (Topological Sort). If the algorithm fails to include all vertices in the sorted output, the graph has a cycle.</li>
  </ul>
</div>

<div id="q20-what-is-a-segment-tree" class="question">
  20. What is a Segment Tree?
  <span class="difficulty advanced">Advanced</span>
</div>

<div class="answer">
  <p>A <strong>Segment Tree</strong> is a versatile data structure used to store information about intervals or segments. It allows querying which of the stored segments contain a given point.</p>
  <ul>
    <li><strong>Main Use:</strong> Range Query problems (e.g., sum of array from index i to j, min/max in range).</li>
    <li><strong>Complexity:</strong> Build: O(n), Query: O(log n), Update: O(log n).</li>
    <li>Ideally suited for scenarios where there are many range queries and updates on an array.</li>
  </ul>
</div>
