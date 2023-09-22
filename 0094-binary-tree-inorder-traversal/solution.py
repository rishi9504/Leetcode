# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list1=[]
        def inorder(root,list1):
            if not root:
                return 
            
            inorder(root.left,list1)
            list1.append(root.val)
            inorder(root.right,list1)
        inorder(root,list1)
        return list1
        
