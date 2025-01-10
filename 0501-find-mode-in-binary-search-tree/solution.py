# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        cv= None
        cc=0
        mc =0
        modes=[]
        def handle_value(val):
            nonlocal cv,cc,mc,modes
            if val!=cv:
                cv = val
                cc=0
            cc+=1
            if cc>mc:
                mc=cc
                modes.clear()
                modes.append(val)
            elif cc==mc:
                modes.append(val)
        def inordertv(node):
            if not node:
                return
            inordertv(node.left)
            handle_value(node.val)
            inordertv(node.right)

        inordertv(root)
        return modes                        

        
