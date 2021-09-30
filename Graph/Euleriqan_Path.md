# Eulerian Path & Cycle
## Definition
>A path/cycle that visits all the nodes in the graph exactly once.

## Condition 
1. Eulerian cycle: 
   	* Undirected graph: connected and all nodes have even degrees.
   	* Directed graph: connected and all nodes have equal in and out degrees
2. Eulerian path:
	* Undirected: has eulerian cycle or only one pair of nodes has even degrees (entrance and exit)
	* Directed: has eulerian cycle or iff one pair of nodes, one node has one more in degree (exit) and the other has one more out degree (entrance).
  
  ## Print out eulerian path/cycle: Hierholzer's algorithm
 ```python
# represent graph G as edge list
  st = []
  def visit(node):
	# traverse all its neighbors
	while G[node]:
		  visit(G[node].pop())
	# This node has no exit, it must be the exit
	st.append(node)
# remember to reverse the stack
return st[::-1]
```
## Leetcode reference
1. [753	Cracking the Safe](https://leetcode.com/problems/cracking-the-safe/)
   1. Visit all the nodes once
   2. Two nodes are connected if last (n-1) of the previous node plus a new digit would form the next node
2. [332. Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/)










