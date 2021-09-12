# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
    # self.pre stored the root of the processed branch
        self.pre = None
        
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        # we process right branch first
        self.flatten(root.right)
        # link the right root to left part
        self.flatten(root.left)
        # print(root.val)
        root.right = self.pre
        root.left = None
        self.pre = root
        
        
        
        
        
