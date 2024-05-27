# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if q is None and p is None:
            return True
        if q is None or p is None:
        
            print(p,q)
            # if q!=p:
            #     return False
            return False
        if p.val!=q.val:
            return False
        pt = self.isSameTree(p.left,q.left)
        qt = self.isSameTree(p.right,q.right)
        # print(f'{pt=},{qt=}', p an)
        return pt and qt
