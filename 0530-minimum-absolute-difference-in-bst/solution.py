# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min_diff = float("inf")
        self.prev = float("-inf")
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.min_diff = min(self.min_diff, node.val-self.prev)
            self.prev = node.val
            inorder(node.right)
        inorder(root)
        return self.min_diff        
        
