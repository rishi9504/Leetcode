# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
           
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ml=0
        def dfs(node,is_left,l):
            if not node:
                return
            self.ml = max(self.ml,l)
            if is_left:
                dfs(node.left,False,l+1)
                dfs(node.right,True,1)
            else:
                dfs(node.right,True,l+1)
                dfs(node.left,False,1)
        dfs(root,True,0)
        dfs(root,False,0)
        return self.ml        

            
        
