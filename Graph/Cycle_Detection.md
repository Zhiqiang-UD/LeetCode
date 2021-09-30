# Cycle Detection
## Methods
1. Undirected: Union-Find
2. Directed: Topological Sort / DFS

## Template
```python
def findCycleDFS(G, n):
	# Directed graph G with n nodes
	visited = [0] * n # 0 un-visited, 1, being visited, 2 complete
	# returns true if no cycle
	# check if there is any backward edge
	def dfs(node):
		if visited[node]: return visited[node] == 2
		# mark node on this path as being visited
		visited[node] = 1
		for nb in G[node]:
			if not dfs(nb):
				return False
		# mark this node complete
		visited[node] = 2
	# check if there is cycle from each node	
	for i in range(n):
		if not dfs(i):
			return False
	return True
```

## Time Complexity
O(V + E)

## Leetcode reference
1. [1203. Sort Items by Groups Respecting Dependencies](https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/)
2. [444. Sequence Reconstruction](https://leetcode.com/problems/sequence-reconstruction/)
3. [802. Find Eventual Safe States](https://leetcode.com/problems/find-eventual-safe-states/)
   1. No cycle is equivalent to end in terminal node
   2. Reverse edges and do topological sort from terminal nodes. Then all visited nodes are also safe nodes.