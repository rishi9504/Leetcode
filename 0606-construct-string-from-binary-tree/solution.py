# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            if node is None:
                return ''
            if node.right:
                return str(node.val) + '(' + dfs(node.left) + ')('+ dfs(node.right)+')'
            if node.left:
                return str(node.val)+'('+dfs(node.left)+')'
            return str(node.val)
        return dfs(root)               
        
