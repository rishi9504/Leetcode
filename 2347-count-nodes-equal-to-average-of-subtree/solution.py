# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        c=0
        def dfs(node):
            nonlocal c
            if not node:
                return (0,0) # sum,count
            ls,lc = dfs(node.left)
            rs,rc = dfs(node.right)

            # compute the current subtree sum and count
            ss = ls +rs + node.val
            sc = lc+rc+1
            if node.val == ss//sc:
                c+=1
            return (ss,sc)
        dfs(root)
        return c            
        
