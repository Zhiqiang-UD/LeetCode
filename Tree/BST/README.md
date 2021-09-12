# Tree
Unlike Arrays, Linked Lists, Stack and queues, which are linear data structures, trees are hierarchical data structures.


## Definition of Tree:
Tree is a subset of graph. A graph *G* is a tree iff the following two conditions are met:
>1. G is fully connected. For every pair of nodes in G, there is a path between them
>2. G has no cycle. IOW, there is one unique path between every pair of nodes in G

## Different Types of Tree
### Binary Search Tree (BST)
The feature of BST can allow us to reduce searching space while searching for a value in the tree.  
#### Problems
* [285. Inorder Successor in BST](https://leetcode.com/problems/inorder-successor-in-bst/)
  * Get rid of left or right based on the comparison of root.val vs. p.val
  * The successor will always be the last one that is bigger than p