# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.helper(root,0)
    def helper(self, node,partial):
        if not node:
            return 0
        partial = 10*partial + node.val
        if not node.left and not node.right:
            return partial
        return self.helper(node.left,partial)  + self.helper(node.right,partial)            
        
