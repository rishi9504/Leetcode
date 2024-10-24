# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node: TreeNode, current_sum: int, path_count: dict) -> int:
        

            if not node:
                # If the node is None, return 0
                return 0

            current_sum += node.val
            # Calculate the current sum

            count = path_count.get(current_sum - targetSum, 0)
            # Get the number of paths that sum to the target sum

            path_count[current_sum] = path_count.get(current_sum, 0) + 1
            # Increment the count of the current sum

            count += dfs(node.left, current_sum, path_count)
            # Recursively call the function on the left subtree

            count += dfs(node.right, current_sum, path_count)
            # Recursively call the function on the right subtree

            path_count[current_sum] -= 1
            # Decrement the count of the current sum

            return count

        return dfs(root, 0, {0: 1})
        
