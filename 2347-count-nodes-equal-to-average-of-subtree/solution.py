# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0  # To keep track of nodes satisfying the condition

        def dfs(node):
            if not node:
                return (0, 0)  # (sum, count)
            
            # Postorder traversal: process left and right children first
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            
            # Subtree sum and count
            subtree_sum = left_sum + right_sum + node.val
            subtree_count = left_count + right_count + 1
            
            # Check if node value equals the average of its subtree
            if node.val == subtree_sum // subtree_count:
                self.count += 1
            
            return (subtree_sum, subtree_count)
        
        dfs(root)
        return self.count

        
