# 1161. Maximum Level Sum of a Binary Tree
# Solved
# Medium

# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

# This code calculates the smallest level in a binary tree where the sum of node values is maximum. It uses a recursive approach to traverse the tree, accumulating node values by level in a dictionary (levels), and then returns the level with the maximum sum.

from collections import defaultdict

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        levels = defaultdict(int)
        def sum_vals(root, depth):
            if root:
                levels[depth] += root.val
                sum_vals(root.left,  depth+1)
                sum_vals(root.right, depth+1)
			
        sum_vals(root, 1)
        return max(levels, key=levels.get)