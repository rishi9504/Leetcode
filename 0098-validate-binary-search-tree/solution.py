# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,mv,mxv):
            if not node:
                return True
            if not(mv<node.val<mxv):
                return False
            return dfs(node.left,mv,node.val) and dfs(node.right,node.val,mxv)
        return dfs(root,float('-inf'),float('inf'))            
        
