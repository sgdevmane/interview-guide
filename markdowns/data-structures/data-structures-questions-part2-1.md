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
