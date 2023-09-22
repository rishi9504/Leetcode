# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Base condition
        if root is None:
            return True
 
        # Compute height of left subtree
        lh = self.isBalanced(root.left)
    
        # If left subtree is not balanced,
        # return 0
        if lh == 0:
            return 0
    
        # Do same thing for the right subtree
        rh = self.isBalanced(root.right)
        if rh == 0:
            return 0
    
        # Allowed values for (lh - rh) are 1, -1, 0
        if (abs(lh - rh) > 1):
            return 0
    
        # If we reach here means tree is
        # height-balanced tree, return height
        # in this case
        else:
            return max(lh, rh) + 1
            
