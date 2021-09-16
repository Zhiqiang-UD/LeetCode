# Union Find
Union-find data structure, also called disjoint-set-union (DSU) data structure, is a data structure that stores a collection of disjoint (non-overlapping) sets. It provides operations for **adding new sets, merging sets, and finding a representative member of a set.**

Union-find data structure can be implemented with linked-list, array or **disjoint-set forrest**, which is essentially one type of tree structure. The disjoin-set forrest is most commonly used as its amortized time cost for find is nearly constant. To perform a sequence of *m* add, union or find operations with n nodes takes *O(m$\alpha (n)$), where $\alpha (n)$ is extremely slow-growing inverse Ackermann function (can be considered as less than 5 in practice for extremely large n).

# Code Template
```python
# two main functions: find(), union()
# parent and rank often implemented with maps
parent = {}
rank = {}
def find(x):
	# initialization. Can be done in advance
	if x not in parent:
		parent[x] = x
	if x != parent[x]:
		# path compression
		parent[x] = find(parent[x])
	return parent[x]
def union(x, y):
	# without union by rank -> log(n)
	parent[find(x)] = find(y)
	# with union by rank
	rx = find(x)
	ry = find(y)
	if rx == ry:
		return False # no need to union
	elif rank[rx] < rank[ry]:
		parent[rx] = ry
	elif rank[rx] > rank[ry]:
		parent[ry] = rx
	else:
		# equal rank, increment rank of the new parent
		parent[rx] = ry
		rank[ry] += 1
	return True # union operation done
""" If size of each set is required, can add a size map, initialize to 1 for all in find() and update size in union(). In getSize(), find root and return sizeMap[root].
"""
```

## Common Usage
1. Detect cycles in a tree graph
2. Find number of connected components (i.e. number of islands)

## General Procedure to Solve Union-Find Problems
1. Find out it's a disjoin-set problem. 
   1. Graph connectivity
   2. Number of groups
2. Figure out how and when to do union.
   1. Most time we just union the points/elements in the system.
   2. Like  [947. Most Stones Removed with Same Row or Column](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/) we need to union the row and column index.
   3. Update rank or size during the union operation.


## Leetcode Problems
1. [803. Bricks Falling When Hit](https://leetcode.com/problems/bricks-falling-when-hit/)
2. [Union-Find Tag](https://leetcode.com/tag/union-find/)
3. [947. Most Stones Removed with Same Row or Column](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/)
   1. Union row and col index for each point
   2. Convert colIdx to colIdx + 10001, so its unique.
