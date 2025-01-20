# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        leftmost_positions = {}
        max_width = 0

        def dfs(node, depth, position):
            nonlocal max_width
            if not node:
                return
            
            # If this is the first node we visit at this depth, set its position as the leftmost
            if depth not in leftmost_positions:
                leftmost_positions[depth] = position
            
            # Calculate the width for the current depth
            current_width = position - leftmost_positions[depth] + 1
            max_width = max(max_width, current_width)
            
            # Recursively visit left and right children with updated positions
            dfs(node.left, depth + 1, 2 * position)
            dfs(node.right, depth + 1, 2 * position + 1)

        # Start DFS from the root at depth 0 and position 0
        dfs(root, 0, 0)
        return max_width
        
