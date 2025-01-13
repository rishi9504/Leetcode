# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return
            if p.val<node.val and q.val<node.val:
                return dfs(node.left)
            if p.val>node.val and q.val>node.val:
                return dfs(node.right)
            return node
        return dfs(root)                
        
