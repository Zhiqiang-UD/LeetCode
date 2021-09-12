## [272. Closest Binary Search Tree Value II](https://leetcode.com/problems/closest-binary-search-tree-value-ii/)
> BST -> Inorder traversal would give us the sorted list 
> 
> Covert this to find k closest values in a sorted array
>
>We just need k of the n, possible doing a partial sort with heap? Or keep a fixed size array and move the sliding window?

>Traversal is  O(n), This is the limit of time complexity.
### Solution 1
**Time: O(nlogn), Space: O(n)**

Algo:

* Inorder traversal to get a sorted array
* Sort based on abs(num - target) and take the first k
### Solution 2
**Time: O(nlogk), Space: O(n)**

Algo:

* Inorder traversal to get a sorted array
* Use a heap of size k and run n times
### Solution 3
**Time: O(n)**

**Space: O(n)**

Algo:

* Inorder traversal to get a sorted array
* Keep a sliding window of size k during traversal. Only pop from front when the size is k and the current node is closer to target than the front. Otherwise we can termite early