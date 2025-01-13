"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        my_map = {}
        
        def rec(node):
            if my_map.get(node.val):
                return my_map[node.val]
            
            my_map[node.val] = Node(node.val)
            for neighbor in node.neighbors:
                my_map[node.val].neighbors.append(rec(neighbor))
            return my_map[node.val]
            
        if not node: return None
        return rec(node)  
        
