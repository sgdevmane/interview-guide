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

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

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

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

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
