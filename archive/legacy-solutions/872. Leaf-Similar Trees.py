# 872. Leaf-Similar Trees
# Solved
# Easy

# Consider all the leaves of a binary tree, from left to right order, 
# the values of those leaves form a leaf value sequence.



# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

# Two binary trees are considered leaf-similar if their leaf value sequence is the same.

# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# This code checks if two binary trees (`root1` and `root2`) are leaf-similar by comparing their leaf value sequences. It uses a Depth-First Search (DFS) approach to traverse both trees and collect the values of their leaf nodes. The function returns `True` if the leaf value sequences are the same, and `False` otherwise. (`Leaf-Similar Trees.py:Solution.leafSimilar`)

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # dfs mentioned in blind 75

        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            return dfs(node.left) + dfs(node.right)
        return dfs(root1) == dfs(root2)            
        