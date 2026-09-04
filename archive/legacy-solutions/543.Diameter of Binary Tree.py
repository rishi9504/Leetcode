# 543. Diameter of Binary Tree
# Solved
# Easy

# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
#  This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

class Solution:
    def __init__(self):
	    self.diameter = 0  # stores the maximum diameter calculated
	
    def depth(self, node: Optional[TreeNode]) -> int:
        """
        This function needs to do the following:
            1. Calculate the maximum depth of the left and right sides of the given node
            2. Determine the diameter at the given node and check if its the maximum
        """
        # Calculate maximum depth
        left = self.depth(node.left) if node.left else 0
        right = self.depth(node.right) if node.right else 0
        # Calculate diameter
        self.diameter = max(self.diameter, left + right)
        # Make sure the parent node(s) get the correct depth from this node
        return 1 + max(left, right)
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.depth(root)
        return self.diameter