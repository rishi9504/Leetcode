# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # two pointer approach using dfs
        def dfs(node,seen):
            if not node:
                return False
            if k-node.val in seen:
                return True
            seen.add(node.val)
            return dfs(node.left,seen) or dfs(node.right,seen)
        return dfs(root,set())        

        
