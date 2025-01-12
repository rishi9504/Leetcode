# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        f=s=p = None
        def dfs(node):
            nonlocal f,s,p
            if not node:
                return
            dfs(node.left)
            if p and p.val>node.val:
                if not f:
                    f=p
                s=node
            p=node
            dfs(node.right)
        dfs(root)
        if f and s:
            f.val,s.val = s.val,f.val                
        
