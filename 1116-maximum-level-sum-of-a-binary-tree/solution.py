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
