# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if root.val==0 or root.val==1:
            return root.val==1    
        lr = self.evaluateTree(root.left)
        rr = self.evaluateTree(root.right)

        if root.val ==2:
            return lr or rr
        elif root.val==3:
            return lr and rr
        return False               
        
