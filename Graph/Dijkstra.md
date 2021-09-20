# Dijkstra
Shortest path algorithm to find shortest distance from source to all nodes in a directed graph. 

It can be considered as a BFS algorithm for weighted graph. 

Keywords for this type of questions can be minimum/maximum of something in a graph all matrix. 

## Caveat
* All the edge weight must be non-negative
  * Add a new edge will never decrease the distance
  * Once minimum distance is found, it will never decrease
* Equivalent to find maximum distance if adding more edges would always decrease the distance
  * Use max-heap -> Pay attention to negative values
* The edges/weights might not be straightforward and you need to construct it by yourself, like in LC1631.
  * In a matrix, two adjacent elements have an edge between them. 

## Template
```python
def dijkstra(n, edges, src, target = None):
	# build graph
	# find all neighbors/weights of each node and store in list or dict
	G = []
	# use a minDist array to store minimum distance seen so far. Only push to pq if the current distance is smaller than the seen one. This will make sure the pq will not grow all the time
	minDist = [math.inf] * n 
	# change minDist for src to 0
	minDist[src] = 0

	# priority queue, with (dist, node) -> dist first
	pq = [(0, src)]
	while pq:
		dist, node = heappop(pq)
		if node == target:
			return dist
		# update node's neighbors
		for nb, weight in G[node]:
			newDist = dist + weight
			if newDist < minDist[nb]:
				# update minDist[nb] and push (newDist, nb) to pq
				minDist[nb] = newDist
				heappush(pq, (newDist, nb))
```

## Time complexity
$O(ElogE)$ in the above implementation. Same node can be added multiple times to the pq, since we are not updating values in the pq. The maximum node in the pq is equal to the number of edges. This can be optimized to $O(ElogV)$ with a more efficient implementation of the pq. 


## Leetcode Problems
* [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/)
* [1514. Paht with Maximum Prob](https://leetcode.com/problems/path-with-maximum-probability/)
  * Find maximum distance
* [1631. Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/)
  * Figure out edges and edge weight.