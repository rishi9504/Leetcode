"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(node):
            if node==None or node.left==None:
                return
            node.left.next = node.right
            if node.next!=None:
                node.right.next = node.next.left
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return root            



        
