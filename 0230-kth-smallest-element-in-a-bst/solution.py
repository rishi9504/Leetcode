# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(root) -> list:
            if not root:
                return []

            return dfs(root.right) + [root.val] + dfs(root.left)
        
        tl = dfs(root)
        return tl[-k]
