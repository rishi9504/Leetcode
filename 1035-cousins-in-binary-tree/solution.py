# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        xd=yd=-1
        xp=yp=None
        def dfs(node,p,d):
            nonlocal xd,yd,xp,yp
            if not node:
                return
            if node.val==x:
                xd,xp=d,p
            if node.val==y:
                yd,yp = d,p
            dfs(node.left,node,d+1)
            dfs(node.right,node,d+1)
        dfs(root,None,0)
        return xd==yd and xp!=yp        

        
