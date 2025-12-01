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

---

<a id="q1"></a>
### Q1: Difference between Array and Linked List?

**Difficulty**: Beginner

**Strategy**:
**Arrays:** Contiguous memory, O(1) access, fixed size (mostly), O(n) insertion/deletion.


  **Linked Lists:** Non-contiguous nodes, O(n) access, dynamic size, O(1) insertion/deletion (if pointer known).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q2"></a>
### Q2: Explain Stack and Queue?

**Difficulty**: Beginner

**Strategy**:
- **Stack (LIFO):** Last In First Out. Push/Pop from top. Used in recursion, undo.

    - **Queue (FIFO):** First In First Out. Enqueue rear, Dequeue front. Used in BFS, printer queues.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q3"></a>
### Q3: How does a Hash Map work?

**Difficulty**: Intermediate

**Strategy**:
Maps keys to values using a hash function to compute an index.


  **Collisions:** Handled via Chaining (Linked List at bucket) or Open Addressing (Probing).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q4"></a>
### Q4: What is a Binary Search Tree (BST)?

**Difficulty**: Intermediate

**Strategy**:
Sorted binary tree: Left child < Parent < Right child. Allows O(log n) search/insert/delete if balanced.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q5"></a>
### Q5: Explain BFS vs DFS?

**Difficulty**: Intermediate

**Strategy**:
**BFS (Queue):** Level by level. Shortest path in unweighted graph.


  **DFS (Stack/Recursion):** Deep traversal. Path finding, topological sort.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q6"></a>
### Q6: What is a Heap (Min/Max)?

**Difficulty**: Intermediate

**Strategy**:
Complete binary tree satisfying heap property (Parent <= Child for Min-Heap). Root is min/max. O(1) peek, O(log n) push/pop.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q7"></a>
### Q7: Detect cycle in Linked List?

**Difficulty**: Intermediate

**Strategy**:
**Floyd's Tortoise and Hare:** Slow pointer moves 1 step, Fast moves 2. If they meet, cycle exists.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q8"></a>
### Q8: What is a Trie?

**Difficulty**: Advanced

**Strategy**:
Prefix tree for strings. Nodes represent characters. Efficient for autocomplete and prefix search O(L) where L is word length.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q9"></a>
### Q9: Graph Representations?

**Difficulty**: Intermediate

**Strategy**:
- **Adjacency Matrix:** V*V 2D array. O(1) edge check. O(V^2) space.

    - **Adjacency List:** Array of lists. O(E) space. Efficient for sparse graphs.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q10"></a>
### Q10: Implement LRU Cache?

**Difficulty**: Advanced

**Strategy**:
Use **Hash Map** + **Doubly Linked List**.


  
    - Map: Key -> Node (O(1) access).

    - List: Order of use. Move accessed node to head. Remove tail when full.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q11"></a>
### Q11: What is a Priority Queue?

**Difficulty**: Intermediate

**Strategy**:
Queue where elements are dequeued based on priority, not arrival time. Implemented using Heaps.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q12"></a>
### Q12: Tree vs Graph?

**Difficulty**: Beginner

**Strategy**:
Tree: Acyclic, connected graph with N nodes and N-1 edges. One root. Hierarchical.


  Graph: Collection of vertices and edges. Can be cyclic/disconnected. Network.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q13"></a>
### Q13: Balanced Trees (AVL/Red-Black)?

**Difficulty**: Advanced

**Strategy**:
Self-balancing BSTs ensuring O(log n) height.


  
    - **AVL:** Strict balance (diff <= 1). More rotations. Faster lookups.

    - **Red-Black:** Looser balance. Fewer rotations. Faster insertions/deletions.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q14"></a>
### Q14: Middle of Linked List?

**Difficulty**: Beginner

**Strategy**:
Two pointers: Fast moves 2x, Slow moves 1x. When Fast ends, Slow is at middle.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q15"></a>
### Q15: What is a Bloom Filter?

**Difficulty**: Advanced

**Strategy**:
Probabilistic space-efficient structure to check set membership. Can return False Positive, but never False Negative.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q16"></a>
### Q16: B-Trees in Databases?

**Difficulty**: Advanced

**Strategy**:
Multi-way search tree optimized for disk storage. Nodes have many children, reducing height and disk I/O.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q17"></a>
### Q17: Queue using Stacks?

**Difficulty**: Intermediate

**Strategy**:
Two stacks: Input and Output. Push to Input. Pop from Output (if empty, move all Input to Output). Amortized O(1).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q18"></a>
### Q18: Disjoint Set (Union-Find)?

**Difficulty**: Advanced

**Strategy**:
Tracks partitioned sets. Operations: Union(x, y) and Find(x). Used in Kruskal's MST and Cycle detection.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q19"></a>
### Q19: Cycle in Directed Graph?

**Difficulty**: Advanced

**Strategy**:
DFS with Recursion Stack. If node seen in current recursion stack -> Cycle.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q20"></a>
### Q20: What is a Segment Tree?

**Difficulty**: Advanced

**Strategy**:
Tree for range queries (sum, min, max) on an array. O(log n) update and query.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q21"></a>
### Q21: What is a Skip List?

**Difficulty**: Advanced

**Strategy**:
Probabilistic data structure alternative to balanced trees. Uses multiple layers of linked lists to allow skipping elements for O(log n) search.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q22"></a>
### Q22: Array vs ArrayList (Dynamic Array)?

**Difficulty**: Beginner

**Strategy**:
**Array:** Fixed size. **ArrayList:** Resizes automatically (usually doubles capacity when full, copying elements).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q23"></a>
### Q23: What is a Circular Queue?

**Difficulty**: Intermediate

**Strategy**:
Queue where last position connects back to first. Efficient use of fixed buffer space (Ring Buffer).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q24"></a>
### Q24: Doubly Linked List vs Singly?

**Difficulty**: Beginner

**Strategy**:
**Singly:** Next pointer only. Less memory.
**Doubly:** Next and Prev pointers. Easier deletion/backward traversal. More memory.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q25"></a>
### Q25: What is a Deque (Double-ended Queue)?

**Difficulty**: Intermediate

**Strategy**:
Structure allowing insertion/deletion at both ends. Can function as both Stack and Queue.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q26"></a>
### Q26: Adjacency Matrix vs Adjacency List?

**Difficulty**: Intermediate

**Strategy**:
**Matrix:** Good for dense graphs. Fast edge lookup O(1).
**List:** Good for sparse graphs. Saves space. Fast iteration of neighbors.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q27"></a>
### Q27: What is a Suffix Tree?

**Difficulty**: Advanced

**Strategy**:
Compressed trie of all suffixes of a text. Used for fast substring search, longest common substring. O(N) construction.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q28"></a>
### Q28: Fenwick Tree (Binary Indexed Tree)?

**Difficulty**: Advanced

**Strategy**:
Space-efficient array-based structure for prefix sums and point updates in O(log n). Easier to implement than Segment Tree.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q29"></a>
### Q29: What is a Quadtree?

**Difficulty**: Advanced

**Strategy**:
Tree data structure where each node has exactly four children. Used to partition 2D space (Image processing, Collision detection).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q30"></a>
### Q30: KD-Tree (k-dimensional tree)?

**Difficulty**: Advanced

**Strategy**:
Space-partitioning tree for k-dimensional space. Used in Nearest Neighbor Search (e.g., 3D graphics, ML).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q31"></a>
### Q31: Hash Set vs Hash Map?

**Difficulty**: Beginner

**Strategy**:
**Set:** Stores unique keys only. **Map:** Stores Key-Value pairs.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q32"></a>
### Q32: What is Open Addressing?

**Difficulty**: Advanced

**Strategy**:
Collision resolution strategy in Hash Tables. If bucket is full, find another slot within the array (Linear Probing, Quadratic Probing).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q33"></a>
### Q33: Separate Chaining vs Open Addressing?

**Difficulty**: Advanced

**Strategy**:
**Chaining:** List at each bucket. Degrades gracefully with high load factor.
**Open Addressing:** No lists. Better cache performance but sensitive to clustering.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q34"></a>
### Q34: What is Consistent Hashing?

**Difficulty**: Advanced

**Strategy**:
Distributed hashing scheme where adding/removing a slot (server) only affects K/N keys. Essential for distributed caches/DBs.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q35"></a>
### Q35: Count-Min Sketch?

**Difficulty**: Advanced

**Strategy**:
Probabilistic frequency table. Uses multiple hash functions and an array. estimates frequency of events. Can overestimate, never underestimate.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q36"></a>
### Q36: What is a HyperLogLog?

**Difficulty**: Advanced

**Strategy**:
Probabilistic algorithm for counting distinct elements (cardinality) in a set with very little memory.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q37"></a>
### Q37: Inorder, Preorder, Postorder Traversal?

**Difficulty**: Beginner

**Strategy**:
**Inorder:** Left, Root, Right (Sorted in BST).
**Preorder:** Root, Left, Right (Copying tree).
**Postorder:** Left, Right, Root (Deleting tree).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q38"></a>
### Q38: Threaded Binary Tree?

**Difficulty**: Advanced

**Strategy**:
Binary Tree where null pointers point to inorder predecessor/successor, allowing traversal without stack/recursion.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q39"></a>
### Q39: Splay Tree?

**Difficulty**: Advanced

**Strategy**:
Self-adjusting BST. Recently accessed elements are moved to the root. Good for locality of reference (caches).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q40"></a>
### Q40: Treap (Tree + Heap)?

**Difficulty**: Advanced

**Strategy**:
BST with random priorities satisfying Heap property. Probabilistically balanced.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q41"></a>
### Q41: What is a Sparse Matrix?

**Difficulty**: Intermediate

**Strategy**:
Matrix populated primarily with zeros. Stored efficiently using lists of non-zero elements (Coordinate List, CSR).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q42"></a>
### Q42: Inverted Index (Search Engines)?

**Difficulty**: Intermediate

**Strategy**:
Map from content (words) to location (documents). "Word A" -> [Doc1, Doc5].

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q43"></a>
### Q43: Difference between Set and List?

**Difficulty**: Beginner

**Strategy**:
**Set:** Unordered, Unique elements.
**List:** Ordered, allows duplicates.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q44"></a>
### Q44: What is a Tuple?

**Difficulty**: Beginner

**Strategy**:
Immutable ordered list of elements. Fixed size.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q45"></a>
### Q45: Immutable vs Mutable Data Structures?

**Difficulty**: Intermediate

**Strategy**:
**Immutable:** Cannot change after creation (String in Java/Python). Thread-safe.
**Mutable:** Can be modified in place.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q46"></a>
### Q46: What is a BitMap / BitSet?

**Difficulty**: Intermediate

**Strategy**:
Array of bits. Compact storage for boolean values or set membership of integers.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q47"></a>
### Q47: Rope Data Structure?

**Difficulty**: Advanced

**Strategy**:
Tree-based structure for heavy string editing (concatenation/splitting). Better than arrays for large texts.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q48"></a>
### Q48: Van Emde Boas Tree?

**Difficulty**: Advanced

**Strategy**:
Tree for integer keys from universe [0, U-1]. Operations in O(log log U).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q49"></a>
### Q49: Fibonacci Heap vs Binary Heap?

**Difficulty**: Advanced

**Strategy**:
**Fibonacci:** O(1) amortized decrease-key. Better for Dijkstra/Prim.
**Binary:** O(log n) decrease-key. Simpler.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q50"></a>
### Q50: Difference between Tree and Trie?

**Difficulty**: Intermediate

**Strategy**:
Tree: General hierarchy. Trie: Specific tree for strings where position determines key.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q51"></a>
### Q51: What is a Spatial Index (R-Tree)?

**Difficulty**: Advanced

**Strategy**:
Tree structure for indexing multi-dimensional information (coordinates, rectangles). Used in Maps/GIS.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q52"></a>
### Q52: Gap Buffer (Text Editors)?

**Difficulty**: Advanced

**Strategy**:
Dynamic array with a "gap" at the cursor position. Insertions at cursor are O(1). Moving cursor is O(n).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q53"></a>
### Q53: Piece Table?

**Difficulty**: Advanced

**Strategy**:
Data structure for text editors. Stores original file and "add buffer". The document is a sequence of spans pointing to these buffers. Fast undo/redo.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q54"></a>
### Q54: What is a DAG (Directed Acyclic Graph)?

**Difficulty**: Intermediate

**Strategy**:
Directed graph with no cycles. Basis for Topological Sort, Dynamic Programming dependencies, Git history.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q55"></a>
### Q55: Bipartite Graph?

**Difficulty**: Intermediate

**Strategy**:
Graph where vertices can be divided into two sets such that all edges connect a vertex in one set to one in the other. 2-colorable.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q56"></a>
### Q56: Complete Graph vs Connected Graph?

**Difficulty**: Beginner

**Strategy**:
**Connected:** Path exists between any two nodes.
**Complete:** Edge exists between EVERY pair of nodes.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q57"></a>
### Q57: What is an Euler Path?

**Difficulty**: Advanced

**Strategy**:
Path visiting every edge exactly once. Exists if 0 or 2 vertices have odd degree.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q58"></a>
### Q58: Hamiltonian Path?

**Difficulty**: Advanced

**Strategy**:
Path visiting every vertex exactly once. NP-Complete problem.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q59"></a>
### Q59: Minimum Spanning Tree (MST)?

**Difficulty**: Intermediate

**Strategy**:
Subset of edges connecting all vertices with minimum total weight. Algorithms: Kruskal's, Prim's.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q60"></a>
### Q60: Adjacency List Implementation?

**Difficulty**: Beginner

**Strategy**:
<code>Map&lt;Node, List&lt;Node&gt;&gt;</code> or <code>Array&lt;List&lt;Integer&gt;&gt;</code>.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q61"></a>
### Q61: Implementing a Stack with Array?

**Difficulty**: Beginner

**Strategy**:
Keep a <code>top</code> index. Push: <code>arr[++top] = val</code>. Pop: <code>return arr[top--]</code>.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q62"></a>
### Q62: Implementing a Stack with Linked List?

**Difficulty**: Beginner

**Strategy**:
Push: Add to Head. Pop: Remove Head. O(1).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q63"></a>
### Q63: Monotonic Stack?

**Difficulty**: Intermediate

**Strategy**:
Stack that remains sorted (increasing/decreasing). Used for "Next Greater Element" problems.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q64"></a>
### Q64: Monotonic Queue?

**Difficulty**: Intermediate

**Strategy**:
Queue/Deque that remains sorted. Used for "Sliding Window Maximum".

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q65"></a>
### Q65: Blocking Queue?

**Difficulty**: Intermediate

**Strategy**:
Queue that blocks Dequeue if empty and Enqueue if full. Thread-safe producer-consumer pattern.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q66"></a>
### Q66: ConcurrentHashMap (Java context)?

**Difficulty**: Advanced

**Strategy**:
Thread-safe hash map. Uses bucket-level locking (segment locking) or CAS (Compare-And-Swap) for high concurrency.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q67"></a>
### Q67: What is a GeoHash?

**Difficulty**: Advanced

**Strategy**:
Geocoding system encoding lat/long into a short string. Nearby points have similar prefixes.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q68"></a>
### Q68: Merkle Tree (Blockchain)?

**Difficulty**: Advanced

**Strategy**:
Tree of hashes. Leafs are data hashes. Parents are hash of children. Efficient verification of data integrity.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q69"></a>
### Q69: LSM Tree (Log-Structured Merge)?

**Difficulty**: Advanced

**Strategy**:
DB structure optimized for write-heavy workloads. Writes to in-memory MemTable, flushes to disk SSTables. Merged in background.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q70"></a>
### Q70: Time Complexity of Common Operations?

**Difficulty**: Beginner

**Strategy**:
- Array Access: O(1)

    - BST Search: O(log n)

    - Hash Map Get: O(1)

    - Sort: O(n log n)

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q71"></a>
### Q71: Space Complexity Analysis?

**Difficulty**: Beginner

**Strategy**:
Amount of working storage required. Auxiliary space + Input space. Recursion depth counts.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q72"></a>
### Q72: Big O Notation Explained?

**Difficulty**: Beginner

**Strategy**:
Describes upper bound of growth rate. O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(2^n).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q73"></a>
### Q73: Amortized Analysis?

**Difficulty**: Advanced

**Strategy**:
Average time per operation over a sequence of operations. Example: Dynamic Array resizing is O(n), but amortized O(1).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q74"></a>
### Q74: What is a Self-Organizing List?

**Difficulty**: Advanced

**Strategy**:
List that reorders elements based on access frequency (Move-to-Front heuristic).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q75"></a>
### Q75: XOR Linked List?

**Difficulty**: Advanced

**Strategy**:
Memory-efficient Doubly Linked List using one field (prev XOR next) instead of two pointers.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q76"></a>
### Q76: Unrolled Linked List?

**Difficulty**: Advanced

**Strategy**:
Linked List where each node stores an array of elements. Better cache locality.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q77"></a>
### Q77: V-List?

**Difficulty**: Advanced

**Strategy**:
Variant of unrolled linked list with growing array sizes.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q78"></a>
### Q78: Difference between Max-Heap and Min-Heap?

**Difficulty**: Beginner

**Strategy**:
**Max-Heap:** Root is largest. **Min-Heap:** Root is smallest.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q79"></a>
### Q79: D-ary Heap?

**Difficulty**: Advanced

**Strategy**:
Heap where nodes have D children instead of 2. Shallower tree, better cache performance, slower delete-min.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q80"></a>
### Q80: Binomial Heap?

**Difficulty**: Advanced

**Strategy**:
Collection of Binomial Trees. Supports efficient merging O(log n).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q81"></a>
### Q81: Pairing Heap?

**Difficulty**: Advanced

**Strategy**:
Simplified self-adjusting heap. Fast in practice for Priority Queues.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q82"></a>
### Q82: Leftist Tree?

**Difficulty**: Advanced

**Strategy**:
Priority Queue optimized for merging. Bias towards left spine.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q83"></a>
### Q83: Skew Heap?

**Difficulty**: Advanced

**Strategy**:
Self-adjusting version of Leftist Heap. No structural constraints stored.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q84"></a>
### Q84: Soft Heap?

**Difficulty**: Advanced

**Strategy**:
Heap that allows "corruption" (increasing keys) to achieve faster operations. Used in optimal MST algorithms.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q85"></a>
### Q85: Interval Tree?

**Difficulty**: Advanced

**Strategy**:
Tree to hold intervals. Allows finding all intervals overlapping a query point/interval.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q86"></a>
### Q86: Range Tree?

**Difficulty**: Advanced

**Strategy**:
Data structure for points in d-dimensions to perform orthogonal range queries.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q87"></a>
### Q87: Binary Space Partitioning (BSP)?

**Difficulty**: Advanced

**Strategy**:
Recursively subdividing space into convex sets by hyperplanes. Used in 3D rendering (Doom engine).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q88"></a>
### Q88: Octree vs Quadtree?

**Difficulty**: Intermediate

**Strategy**:
**Quadtree:** 2D space (4 children). **Octree:** 3D space (8 children).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q89"></a>
### Q89: BK-Tree (Spell Check)?

**Difficulty**: Advanced

**Strategy**:
Tree based on Levenshtein distance. Efficient for finding "near matches" in a dictionary.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q90"></a>
### Q90: Radix Tree (Compact Trie)?

**Difficulty**: Advanced

**Strategy**:
Trie where nodes with single child are merged. Reduces space.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q91"></a>
### Q91: Ternary Search Tree?

**Difficulty**: Advanced

**Strategy**:
Trie node has 3 children (Low, Equal, High). More space efficient than standard Trie.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q92"></a>
### Q92: Suffix Automaton?

**Difficulty**: Advanced

**Strategy**:
Smallest DFA accepting all suffixes of a string. Powerful string processing.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q93"></a>
### Q93: Cartesian Tree?

**Difficulty**: Advanced

**Strategy**:
Tree derived from sequence. Heap property on values, Inorder property on indices.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q94"></a>
### Q94: MVP Tree (Metric VP)?

**Difficulty**: Advanced

**Strategy**:
Distance-based index for similarity search in metric spaces.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q95"></a>
### Q95: Cover Tree?

**Difficulty**: Advanced

**Strategy**:
Data structure for Nearest Neighbor search in metric spaces.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q96"></a>
### Q96: Bloom Filter vs Cuckoo Filter?

**Difficulty**: Advanced

**Strategy**:
**Cuckoo Filter:** Supports deletion, higher space efficiency, better locality than Bloom.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q97"></a>
### Q97: Quotient Filter?

**Difficulty**: Advanced

**Strategy**:
Probabilistic structure. Cache-friendly alternative to Bloom Filter. Supports merging.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q98"></a>
### Q98: What is a Persistent Data Structure?

**Difficulty**: Advanced

**Strategy**:
Preserves previous versions when modified. **Fully Persistent:** Any version can be modified. **Partially Persistent:** Only latest can be modified.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q99"></a>
### Q99: Retroactive Data Structures?

**Difficulty**: Advanced

**Strategy**:
Allows performing operations in the past.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q100"></a>
### Q100: Succinct Data Structures?

**Difficulty**: Advanced

**Strategy**:
Uses space close to information-theoretic lower bound while supporting efficient operations.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---
