# Data Structures Interview Questions

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
51. [What is a Spatial Index (R-Tree)?](#q51) <span class="advanced">Advanced</span>
52. [Gap Buffer (Text Editors)?](#q52) <span class="advanced">Advanced</span>
53. [Piece Table?](#q53) <span class="advanced">Advanced</span>
54. [What is a DAG (Directed Acyclic Graph)?](#q54) <span class="intermediate">Intermediate</span>
55. [Bipartite Graph?](#q55) <span class="intermediate">Intermediate</span>
56. [Complete Graph vs Connected Graph?](#q56) <span class="beginner">Beginner</span>
57. [What is an Euler Path?](#q57) <span class="advanced">Advanced</span>
58. [Hamiltonian Path?](#q58) <span class="advanced">Advanced</span>
59. [Minimum Spanning Tree (MST)?](#q59) <span class="intermediate">Intermediate</span>
60. [Adjacency List Implementation?](#q60) <span class="beginner">Beginner</span>
61. [Implementing a Stack with Array?](#q61) <span class="beginner">Beginner</span>
62. [Implementing a Stack with Linked List?](#q62) <span class="beginner">Beginner</span>
63. [Monotonic Stack?](#q63) <span class="intermediate">Intermediate</span>
64. [Monotonic Queue?](#q64) <span class="intermediate">Intermediate</span>
65. [Blocking Queue?](#q65) <span class="intermediate">Intermediate</span>
66. [ConcurrentHashMap (Java context)?](#q66) <span class="advanced">Advanced</span>
67. [What is a GeoHash?](#q67) <span class="advanced">Advanced</span>
68. [Merkle Tree (Blockchain)?](#q68) <span class="advanced">Advanced</span>
69. [LSM Tree (Log-Structured Merge)?](#q69) <span class="advanced">Advanced</span>
70. [Time Complexity of Common Operations?](#q70) <span class="beginner">Beginner</span>
71. [Space Complexity Analysis?](#q71) <span class="beginner">Beginner</span>
72. [Big O Notation Explained?](#q72) <span class="beginner">Beginner</span>
73. [Amortized Analysis?](#q73) <span class="advanced">Advanced</span>
74. [What is a Self-Organizing List?](#q74) <span class="advanced">Advanced</span>
75. [XOR Linked List?](#q75) <span class="advanced">Advanced</span>
76. [Unrolled Linked List?](#q76) <span class="advanced">Advanced</span>
77. [V-List?](#q77) <span class="advanced">Advanced</span>
78. [Difference between Max-Heap and Min-Heap?](#q78) <span class="beginner">Beginner</span>
79. [D-ary Heap?](#q79) <span class="advanced">Advanced</span>
80. [Binomial Heap?](#q80) <span class="advanced">Advanced</span>
81. [Pairing Heap?](#q81) <span class="advanced">Advanced</span>
82. [Leftist Tree?](#q82) <span class="advanced">Advanced</span>
83. [Skew Heap?](#q83) <span class="advanced">Advanced</span>
84. [Soft Heap?](#q84) <span class="advanced">Advanced</span>
85. [Interval Tree?](#q85) <span class="advanced">Advanced</span>
86. [Range Tree?](#q86) <span class="advanced">Advanced</span>
87. [Binary Space Partitioning (BSP)?](#q87) <span class="advanced">Advanced</span>
88. [Octree vs Quadtree?](#q88) <span class="intermediate">Intermediate</span>
89. [BK-Tree (Spell Check)?](#q89) <span class="advanced">Advanced</span>
90. [Radix Tree (Compact Trie)?](#q90) <span class="advanced">Advanced</span>
91. [Ternary Search Tree?](#q91) <span class="advanced">Advanced</span>
92. [Suffix Automaton?](#q92) <span class="advanced">Advanced</span>
93. [Cartesian Tree?](#q93) <span class="advanced">Advanced</span>
94. [MVP Tree (Metric VP)?](#q94) <span class="advanced">Advanced</span>
95. [Cover Tree?](#q95) <span class="advanced">Advanced</span>
96. [Bloom Filter vs Cuckoo Filter?](#q96) <span class="advanced">Advanced</span>
97. [Quotient Filter?](#q97) <span class="advanced">Advanced</span>
98. [What is a Persistent Data Structure?](#q98) <span class="advanced">Advanced</span>
99. [Retroactive Data Structures?](#q99) <span class="advanced">Advanced</span>
100. [Succinct Data Structures?](#q100) <span class="advanced">Advanced</span>

---

<div id="q1" class="question">1. Difference between Array and Linked List? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p><strong>Arrays:</strong> Contiguous memory, O(1) access, fixed size (mostly), O(n) insertion/deletion.</p>
  <p><strong>Linked Lists:</strong> Non-contiguous nodes, O(n) access, dynamic size, O(1) insertion/deletion (if pointer known).</p>
</div>

<div id="q2" class="question">2. Explain Stack and Queue? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <ul>
    <li><strong>Stack (LIFO):</strong> Last In First Out. Push/Pop from top. Used in recursion, undo.</li>
    <li><strong>Queue (FIFO):</strong> First In First Out. Enqueue rear, Dequeue front. Used in BFS, printer queues.</li>
  </ul>
</div>

<div id="q3" class="question">3. How does a Hash Map work? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Maps keys to values using a hash function to compute an index.</p>
  <p><strong>Collisions:</strong> Handled via Chaining (Linked List at bucket) or Open Addressing (Probing).</p>
</div>

<div id="q4" class="question">4. What is a Binary Search Tree (BST)? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Sorted binary tree: Left child < Parent < Right child. Allows O(log n) search/insert/delete if balanced.</p>
</div>

<div id="q5" class="question">5. Explain BFS vs DFS? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p><strong>BFS (Queue):</strong> Level by level. Shortest path in unweighted graph.</p>
  <p><strong>DFS (Stack/Recursion):</strong> Deep traversal. Path finding, topological sort.</p>
</div>

<div id="q6" class="question">6. What is a Heap (Min/Max)? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Complete binary tree satisfying heap property (Parent <= Child for Min-Heap). Root is min/max. O(1) peek, O(log n) push/pop.</p>
</div>

<div id="q7" class="question">7. Detect cycle in Linked List? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p><strong>Floyd's Tortoise and Hare:</strong> Slow pointer moves 1 step, Fast moves 2. If they meet, cycle exists.</p>
</div>

<div id="q8" class="question">8. What is a Trie? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Prefix tree for strings. Nodes represent characters. Efficient for autocomplete and prefix search O(L) where L is word length.</p>
</div>

<div id="q9" class="question">9. Graph Representations? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <ul>
    <li><strong>Adjacency Matrix:</strong> V*V 2D array. O(1) edge check. O(V^2) space.</li>
    <li><strong>Adjacency List:</strong> Array of lists. O(E) space. Efficient for sparse graphs.</li>
  </ul>
</div>

<div id="q10" class="question">10. Implement LRU Cache? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Use <strong>Hash Map</strong> + <strong>Doubly Linked List</strong>.</p>
  <ul>
    <li>Map: Key -> Node (O(1) access).</li>
    <li>List: Order of use. Move accessed node to head. Remove tail when full.</li>
  </ul>
</div>

<div id="q11" class="question">11. What is a Priority Queue? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Queue where elements are dequeued based on priority, not arrival time. Implemented using Heaps.</p>
</div>

<div id="q12" class="question">12. Tree vs Graph? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Tree: Acyclic, connected graph with N nodes and N-1 edges. One root. Hierarchical.</p>
  <p>Graph: Collection of vertices and edges. Can be cyclic/disconnected. Network.</p>
</div>

<div id="q13" class="question">13. Balanced Trees (AVL/Red-Black)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Self-balancing BSTs ensuring O(log n) height.</p>
  <ul>
    <li><strong>AVL:</strong> Strict balance (diff <= 1). More rotations. Faster lookups.</li>
    <li><strong>Red-Black:</strong> Looser balance. Fewer rotations. Faster insertions/deletions.</li>
  </ul>
</div>

<div id="q14" class="question">14. Middle of Linked List? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Two pointers: Fast moves 2x, Slow moves 1x. When Fast ends, Slow is at middle.</p>
</div>

<div id="q15" class="question">15. What is a Bloom Filter? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Probabilistic space-efficient structure to check set membership. Can return False Positive, but never False Negative.</p>
</div>

<div id="q16" class="question">16. B-Trees in Databases? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Multi-way search tree optimized for disk storage. Nodes have many children, reducing height and disk I/O.</p>
</div>

<div id="q17" class="question">17. Queue using Stacks? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Two stacks: Input and Output. Push to Input. Pop from Output (if empty, move all Input to Output). Amortized O(1).</p>
</div>

<div id="q18" class="question">18. Disjoint Set (Union-Find)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Tracks partitioned sets. Operations: Union(x, y) and Find(x). Used in Kruskal's MST and Cycle detection.</p>
</div>

<div id="q19" class="question">19. Cycle in Directed Graph? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>DFS with Recursion Stack. If node seen in current recursion stack -> Cycle.</p>
</div>

<div id="q20" class="question">20. What is a Segment Tree? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Tree for range queries (sum, min, max) on an array. O(log n) update and query.</p>
</div>

<div id="q21" class="question">21. What is a Skip List? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Probabilistic data structure alternative to balanced trees. Uses multiple layers of linked lists to allow skipping elements for O(log n) search.</p>
</div>

<div id="q22" class="question">22. Array vs ArrayList (Dynamic Array)? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p><strong>Array:</strong> Fixed size. <strong>ArrayList:</strong> Resizes automatically (usually doubles capacity when full, copying elements).</p>
</div>

<div id="q23" class="question">23. What is a Circular Queue? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Queue where last position connects back to first. Efficient use of fixed buffer space (Ring Buffer).</p>
</div>

<div id="q24" class="question">24. Doubly Linked List vs Singly? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p><strong>Singly:</strong> Next pointer only. Less memory.<br><strong>Doubly:</strong> Next and Prev pointers. Easier deletion/backward traversal. More memory.</p>
</div>

<div id="q25" class="question">25. What is a Deque (Double-ended Queue)? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Structure allowing insertion/deletion at both ends. Can function as both Stack and Queue.</p>
</div>

<div id="q26" class="question">26. Adjacency Matrix vs Adjacency List? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p><strong>Matrix:</strong> Good for dense graphs. Fast edge lookup O(1).<br><strong>List:</strong> Good for sparse graphs. Saves space. Fast iteration of neighbors.</p>
</div>

<div id="q27" class="question">27. What is a Suffix Tree? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Compressed trie of all suffixes of a text. Used for fast substring search, longest common substring. O(N) construction.</p>
</div>

<div id="q28" class="question">28. Fenwick Tree (Binary Indexed Tree)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Space-efficient array-based structure for prefix sums and point updates in O(log n). Easier to implement than Segment Tree.</p>
</div>

<div id="q29" class="question">29. What is a Quadtree? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Tree data structure where each node has exactly four children. Used to partition 2D space (Image processing, Collision detection).</p>
</div>

<div id="q30" class="question">30. KD-Tree (k-dimensional tree)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Space-partitioning tree for k-dimensional space. Used in Nearest Neighbor Search (e.g., 3D graphics, ML).</p>
</div>

<div id="q31" class="question">31. Hash Set vs Hash Map? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p><strong>Set:</strong> Stores unique keys only. <strong>Map:</strong> Stores Key-Value pairs.</p>
</div>

<div id="q32" class="question">32. What is Open Addressing? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Collision resolution strategy in Hash Tables. If bucket is full, find another slot within the array (Linear Probing, Quadratic Probing).</p>
</div>

<div id="q33" class="question">33. Separate Chaining vs Open Addressing? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p><strong>Chaining:</strong> List at each bucket. Degrades gracefully with high load factor.<br><strong>Open Addressing:</strong> No lists. Better cache performance but sensitive to clustering.</p>
</div>

<div id="q34" class="question">34. What is Consistent Hashing? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Distributed hashing scheme where adding/removing a slot (server) only affects K/N keys. Essential for distributed caches/DBs.</p>
</div>

<div id="q35" class="question">35. Count-Min Sketch? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Probabilistic frequency table. Uses multiple hash functions and an array. estimates frequency of events. Can overestimate, never underestimate.</p>
</div>

<div id="q36" class="question">36. What is a HyperLogLog? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Probabilistic algorithm for counting distinct elements (cardinality) in a set with very little memory.</p>
</div>

<div id="q37" class="question">37. Inorder, Preorder, Postorder Traversal? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p><strong>Inorder:</strong> Left, Root, Right (Sorted in BST).<br><strong>Preorder:</strong> Root, Left, Right (Copying tree).<br><strong>Postorder:</strong> Left, Right, Root (Deleting tree).</p>
</div>

<div id="q38" class="question">38. Threaded Binary Tree? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Binary Tree where null pointers point to inorder predecessor/successor, allowing traversal without stack/recursion.</p>
</div>

<div id="q39" class="question">39. Splay Tree? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Self-adjusting BST. Recently accessed elements are moved to the root. Good for locality of reference (caches).</p>
</div>

<div id="q40" class="question">40. Treap (Tree + Heap)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>BST with random priorities satisfying Heap property. Probabilistically balanced.</p>
</div>

<div id="q41" class="question">41. What is a Sparse Matrix? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Matrix populated primarily with zeros. Stored efficiently using lists of non-zero elements (Coordinate List, CSR).</p>
</div>

<div id="q42" class="question">42. Inverted Index (Search Engines)? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Map from content (words) to location (documents). "Word A" -> [Doc1, Doc5].</p>
</div>

<div id="q43" class="question">43. Difference between Set and List? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p><strong>Set:</strong> Unordered, Unique elements.<br><strong>List:</strong> Ordered, allows duplicates.</p>
</div>

<div id="q44" class="question">44. What is a Tuple? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Immutable ordered list of elements. Fixed size.</p>
</div>

<div id="q45" class="question">45. Immutable vs Mutable Data Structures? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p><strong>Immutable:</strong> Cannot change after creation (String in Java/Python). Thread-safe.<br><strong>Mutable:</strong> Can be modified in place.</p>
</div>

<div id="q46" class="question">46. What is a BitMap / BitSet? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Array of bits. Compact storage for boolean values or set membership of integers.</p>
</div>

<div id="q47" class="question">47. Rope Data Structure? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Tree-based structure for heavy string editing (concatenation/splitting). Better than arrays for large texts.</p>
</div>

<div id="q48" class="question">48. Van Emde Boas Tree? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Tree for integer keys from universe [0, U-1]. Operations in O(log log U).</p>
</div>

<div id="q49" class="question">49. Fibonacci Heap vs Binary Heap? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p><strong>Fibonacci:</strong> O(1) amortized decrease-key. Better for Dijkstra/Prim.<br><strong>Binary:</strong> O(log n) decrease-key. Simpler.</p>
</div>

<div id="q50" class="question">50. Difference between Tree and Trie? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Tree: General hierarchy. Trie: Specific tree for strings where position determines key.</p>
</div>

<div id="q51" class="question">51. What is a Spatial Index (R-Tree)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Tree structure for indexing multi-dimensional information (coordinates, rectangles). Used in Maps/GIS.</p>
</div>

<div id="q52" class="question">52. Gap Buffer (Text Editors)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Dynamic array with a "gap" at the cursor position. Insertions at cursor are O(1). Moving cursor is O(n).</p>
</div>

<div id="q53" class="question">53. Piece Table? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Data structure for text editors. Stores original file and "add buffer". The document is a sequence of spans pointing to these buffers. Fast undo/redo.</p>
</div>

<div id="q54" class="question">54. What is a DAG (Directed Acyclic Graph)? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Directed graph with no cycles. Basis for Topological Sort, Dynamic Programming dependencies, Git history.</p>
</div>

<div id="q55" class="question">55. Bipartite Graph? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Graph where vertices can be divided into two sets such that all edges connect a vertex in one set to one in the other. 2-colorable.</p>
</div>

<div id="q56" class="question">56. Complete Graph vs Connected Graph? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p><strong>Connected:</strong> Path exists between any two nodes.<br><strong>Complete:</strong> Edge exists between EVERY pair of nodes.</p>
</div>

<div id="q57" class="question">57. What is an Euler Path? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Path visiting every edge exactly once. Exists if 0 or 2 vertices have odd degree.</p>
</div>

<div id="q58" class="question">58. Hamiltonian Path? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Path visiting every vertex exactly once. NP-Complete problem.</p>
</div>

<div id="q59" class="question">59. Minimum Spanning Tree (MST)? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Subset of edges connecting all vertices with minimum total weight. Algorithms: Kruskal's, Prim's.</p>
</div>

<div id="q60" class="question">60. Adjacency List Implementation? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p><code>Map&lt;Node, List&lt;Node&gt;&gt;</code> or <code>Array&lt;List&lt;Integer&gt;&gt;</code>.</p>
</div>

<div id="q61" class="question">61. Implementing a Stack with Array? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Keep a <code>top</code> index. Push: <code>arr[++top] = val</code>. Pop: <code>return arr[top--]</code>.</p>
</div>

<div id="q62" class="question">62. Implementing a Stack with Linked List? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Push: Add to Head. Pop: Remove Head. O(1).</p>
</div>

<div id="q63" class="question">63. Monotonic Stack? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Stack that remains sorted (increasing/decreasing). Used for "Next Greater Element" problems.</p>
</div>

<div id="q64" class="question">64. Monotonic Queue? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Queue/Deque that remains sorted. Used for "Sliding Window Maximum".</p>
</div>

<div id="q65" class="question">65. Blocking Queue? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Queue that blocks Dequeue if empty and Enqueue if full. Thread-safe producer-consumer pattern.</p>
</div>

<div id="q66" class="question">66. ConcurrentHashMap (Java context)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Thread-safe hash map. Uses bucket-level locking (segment locking) or CAS (Compare-And-Swap) for high concurrency.</p>
</div>

<div id="q67" class="question">67. What is a GeoHash? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Geocoding system encoding lat/long into a short string. Nearby points have similar prefixes.</p>
</div>

<div id="q68" class="question">68. Merkle Tree (Blockchain)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Tree of hashes. Leafs are data hashes. Parents are hash of children. Efficient verification of data integrity.</p>
</div>

<div id="q69" class="question">69. LSM Tree (Log-Structured Merge)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>DB structure optimized for write-heavy workloads. Writes to in-memory MemTable, flushes to disk SSTables. Merged in background.</p>
</div>

<div id="q70" class="question">70. Time Complexity of Common Operations? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <ul>
    <li>Array Access: O(1)</li>
    <li>BST Search: O(log n)</li>
    <li>Hash Map Get: O(1)</li>
    <li>Sort: O(n log n)</li>
  </ul>
</div>

<div id="q71" class="question">71. Space Complexity Analysis? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Amount of working storage required. Auxiliary space + Input space. Recursion depth counts.</p>
</div>

<div id="q72" class="question">72. Big O Notation Explained? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Describes upper bound of growth rate. O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(2^n).</p>
</div>

<div id="q73" class="question">73. Amortized Analysis? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Average time per operation over a sequence of operations. Example: Dynamic Array resizing is O(n), but amortized O(1).</p>
</div>

<div id="q74" class="question">74. What is a Self-Organizing List? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>List that reorders elements based on access frequency (Move-to-Front heuristic).</p>
</div>

<div id="q75" class="question">75. XOR Linked List? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Memory-efficient Doubly Linked List using one field (prev XOR next) instead of two pointers.</p>
</div>

<div id="q76" class="question">76. Unrolled Linked List? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Linked List where each node stores an array of elements. Better cache locality.</p>
</div>

<div id="q77" class="question">77. V-List? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Variant of unrolled linked list with growing array sizes.</p>
</div>

<div id="q78" class="question">78. Difference between Max-Heap and Min-Heap? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p><strong>Max-Heap:</strong> Root is largest. <strong>Min-Heap:</strong> Root is smallest.</p>
</div>

<div id="q79" class="question">79. D-ary Heap? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Heap where nodes have D children instead of 2. Shallower tree, better cache performance, slower delete-min.</p>
</div>

<div id="q80" class="question">80. Binomial Heap? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Collection of Binomial Trees. Supports efficient merging O(log n).</p>
</div>

<div id="q81" class="question">81. Pairing Heap? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Simplified self-adjusting heap. Fast in practice for Priority Queues.</p>
</div>

<div id="q82" class="question">82. Leftist Tree? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Priority Queue optimized for merging. Bias towards left spine.</p>
</div>

<div id="q83" class="question">83. Skew Heap? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Self-adjusting version of Leftist Heap. No structural constraints stored.</p>
</div>

<div id="q84" class="question">84. Soft Heap? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Heap that allows "corruption" (increasing keys) to achieve faster operations. Used in optimal MST algorithms.</p>
</div>

<div id="q85" class="question">85. Interval Tree? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Tree to hold intervals. Allows finding all intervals overlapping a query point/interval.</p>
</div>

<div id="q86" class="question">86. Range Tree? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Data structure for points in d-dimensions to perform orthogonal range queries.</p>
</div>

<div id="q87" class="question">87. Binary Space Partitioning (BSP)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Recursively subdividing space into convex sets by hyperplanes. Used in 3D rendering (Doom engine).</p>
</div>

<div id="q88" class="question">88. Octree vs Quadtree? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p><strong>Quadtree:</strong> 2D space (4 children). <strong>Octree:</strong> 3D space (8 children).</p>
</div>

<div id="q89" class="question">89. BK-Tree (Spell Check)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Tree based on Levenshtein distance. Efficient for finding "near matches" in a dictionary.</p>
</div>

<div id="q90" class="question">90. Radix Tree (Compact Trie)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Trie where nodes with single child are merged. Reduces space.</p>
</div>

<div id="q91" class="question">91. Ternary Search Tree? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Trie node has 3 children (Low, Equal, High). More space efficient than standard Trie.</p>
</div>

<div id="q92" class="question">92. Suffix Automaton? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Smallest DFA accepting all suffixes of a string. Powerful string processing.</p>
</div>

<div id="q93" class="question">93. Cartesian Tree? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Tree derived from sequence. Heap property on values, Inorder property on indices.</p>
</div>

<div id="q94" class="question">94. MVP Tree (Metric VP)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Distance-based index for similarity search in metric spaces.</p>
</div>

<div id="q95" class="question">95. Cover Tree? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Data structure for Nearest Neighbor search in metric spaces.</p>
</div>

<div id="q96" class="question">96. Bloom Filter vs Cuckoo Filter? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p><strong>Cuckoo Filter:</strong> Supports deletion, higher space efficiency, better locality than Bloom.</p>
</div>

<div id="q97" class="question">97. Quotient Filter? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Probabilistic structure. Cache-friendly alternative to Bloom Filter. Supports merging.</p>
</div>

<div id="q98" class="question">98. What is a Persistent Data Structure? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Preserves previous versions when modified. <strong>Fully Persistent:</strong> Any version can be modified. <strong>Partially Persistent:</strong> Only latest can be modified.</p>
</div>

<div id="q99" class="question">99. Retroactive Data Structures? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Allows performing operations in the past.</p>
</div>

<div id="q100" class="question">100. Succinct Data Structures? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Uses space close to information-theoretic lower bound while supporting efficient operations.</p>
</div>
