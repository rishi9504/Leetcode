"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(root):
            if root:
                c=1
                for node in root.children:
                    c = max(c,1+dfs(node))
                return c
            return 0
        return dfs(root)                    
        
