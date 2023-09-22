# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list1=[]
        def preorder(root,list1):
            if not root:
                return 
            list1.append(root.val)
            preorder(root.left,list1)
            preorder(root.right,list1)
        preorder(root,list1)
        return list1
        
