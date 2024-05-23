# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     self.invert(root)
    #     return root
    
    # def invert(self,node):
    #     if node is None:
    #         return
    #     node.left,node.right = node.right,node.left
    #     self.invert(node.left)
    #     self.invert(node.right)

        if not root:
            return
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root  

        
