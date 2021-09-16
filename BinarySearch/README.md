## Introduction
Binary Search (BS) operates on a contiguous sequence with a specified left and right index. This is called Search Space. BS will reduce the Search Space by one half on each iteration, thus achieve $logn$ performance. 

## General Procedure
1. Pre-processing - Sort if collection is unsorted or identify the hidden yet sorted part of the problem.
2. BS - Using a loop to divide search space in half after each comparison. 
3. Post-processing - Determine viable candidate in the remaining space.

## Template
```python
def binarySearch(nums, target):
	# find if target is in nums
	left, right = 0, len(nums)
	# exit condition: left == right
	while left < right:
		mid = left + (right - left) // 2
		if nums[mid] < target:
			left = mid + 1
		else:
			right = mid
	# post-processing
	return left != len(nums) and nums[left] == target
	
def bisect_left(nums, target):
	# find insert index for target, while all i < index in nums nums[i] < target
	left, right = 0, len(nums)
	while left < right:
		mid = left + (right - left) // 2
		if nums[mid] < target:
			left = mid + 1
		else:
			right = mid
	return left # could == len(nums), insert at the end

def bisect_right(nums, target):
	# find insert index for target, while for all i >= index, nums[i] > target
	left, right = 0, len(nums)
	while left < right:
		mid = left + (right - left) // 2
		if nums[mid] <= target:
			left = mid + 1
		else:
			right = mid
	return left # could == len(nums), insert at the end	
```

### Key Attributes
* Search space is [left, right), so we need to make sure left < right, otherwise there is no element left.
* Exit condition is left == right, use it to do post-processing.

### Pitfalls
[LeetCode Binary Search 101](https://leetcode.com/problems/binary-search/discuss/423162/Binary-Search-101-The-Ultimate-Binary-Search-Handbook)
1. Calculate `mid`
   1. Always use `(lo + hi) >> 1` to avoid overflow
   2. When the search space has even elements, we can pick lower or upper `mid`.
      1. `mid = lo + (hi - lo) // 2` lower//left mid
      2. `mid = lo + (hi - lo + 1) // 2` upper//right mid
2. How do we shrink boundary?
   1. Use a simple pair of `if ... else`.
   2. In `if` condition, use a logic that can exclude `mid` : `hi = mid - 1` or `lo = mid + 1`.
3. Avoid infinity loop
   1. Pick the correct `mid` and shrink logic.
      1. Lower mid with `lo = mid + 1` and upper mid with `hi = mid - 1`.
   2. Always think of the case when there are 2 elements left.

## Leetcode Problems
[658. Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/)