# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack = []
        while root:
            if root.right:
                stack.append(root.right)
            if root.left:
                root.right = root.left
                root.left = None
            elif stack:
                root.right = stack.pop()
            root = root.right
