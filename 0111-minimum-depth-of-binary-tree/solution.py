# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
