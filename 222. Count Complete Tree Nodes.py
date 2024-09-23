# 222. Count Complete Tree Nodes
# Solved

# Given the root of a complete binary tree, return the number of the nodes in the tree.

# According to Wikipedia, every level, except possibly the last, 
# is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. 
# It can have between 1 and 2h nodes inclusive at the last level h.

# Design an algorithm that runs in less than O(n) time complexity.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#  counts the number of nodes in a binary tree. It uses a breadth-first search (BFS) algorithm to traverse the tree.

# The function starts by checking if the root of the tree is None, and if so, it returns 0.

# Then, it initializes a variable s to 0 and creates a queue q to store the nodes of the tree. The root node is added to the queue.

# Next, it enters a loop that continues until the queue is empty. In each iteration of the loop, it removes a node from the front of the queue, increments s by 1, and checks if the node has a left child. If it does, the left child is added to the queue. The same process is repeated for the right child.

# Finally, it returns the value of s, which represents the total number of nodes in the tree.

import queue
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        s = 0
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            root = q.get()
            s += 1
            if root.left is not None:
                q.put(root.left)
            if root.right is not None:
                q.put(root.right)
        return s
        