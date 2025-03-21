# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def dfs(node, num):
            if not node:
                return
            
            num = 2*num + node.val                        
            if not node.left and not node.right:
                self.sum_ += num
                return            
            dfs(node.left, num)                
            dfs(node.right, num)
            
        self.sum_ = 0
        dfs(root, 0)
        return self.sum_        
        
