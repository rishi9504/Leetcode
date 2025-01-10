# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        uv=set()
        def dfs(node):
            if not node:
                return
            uv.add(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        if len(uv)<2:
            return -1
        mv = root.val
        sm = float('inf')
        for value in uv:
            if mv<value<sm:
                sm=value
        return sm if sm<float('inf') else -1                    
        
