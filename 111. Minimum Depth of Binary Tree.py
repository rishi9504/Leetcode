# 111. Minimum Depth of Binary Tree
# Solved
# Easy

# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down
#  to the nearest leaf node.

# Note: A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right





# This is a recursive function `rec` that calculates the minimum depth of a binary tree. It takes a node and a level (`lvl`) as input.

# Here's a succinct explanation:

# * If the node is `None`, return the current level (`lvl`).
# * If the node is a leaf node (both left and right children are `None`), return the current level plus one (`lvl+1`).
# * If the node has only one child, recursively call `rec` on that child with the next level (`lvl+1`).
# * If the node has both children, recursively call `rec` on both children with the next level (`lvl+1`) and return the minimum of the two results.

# The function is designed to find the shortest path from the root node to a leaf node in the binary tree.

class Solution:
    def rec(self,node,lvl):
        if node is None:
            return lvl
        if node.left is None and node.right is None:
            return lvl+1  
        if not node.left:
            return self.rec(node.right,lvl+1)  
        if not node.right:
            return self.rec(node.left,lvl+1)              
        # if node.left is None or node.right is None:
        #     return lvl + 1
        return min(self.rec(node.left,lvl+1),self.rec(node.right,lvl+1))

    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.rec(root,0)