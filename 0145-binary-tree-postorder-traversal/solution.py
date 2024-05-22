# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postord(self, root, res):
        if not root:
            return
        self.postord(root.left,res)
        self.postord(root.right,res)
        res.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        self.postord(root,res)
        return res  
        
