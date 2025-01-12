# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(on,cn):
            if not on:
                return None
            if on==target:
                return cn
            lr = dfs(on.left,cn.left)
            if lr:
                return lr
            return dfs(on.right,cn.right)
        return dfs(original,cloned)                
        
