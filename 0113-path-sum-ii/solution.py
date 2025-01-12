# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node,cp,cs):
            if not node:
                return
            cp.append(node.val)
            cs+=node.val
            if not node.left and not node.right and cs==targetSum:
                res.append(list(cp))
            else:
                dfs(node.left,cp,cs)
                dfs(node.right,cp,cs)
            cp.pop()
        res=[]
        dfs(root,[],0)
        return res                
        
