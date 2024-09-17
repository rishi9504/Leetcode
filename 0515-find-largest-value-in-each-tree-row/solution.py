# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        maxValue = []
        if root is None:
            return maxValue
        levelQ = []
        levelQ.append(root)
        while levelQ:
            s = len(levelQ)
            nodemax = float('-inf')
            while s>0:
                c = levelQ.pop(0)
                nodemax = max(c.val,nodemax)
                if c.left:
                    levelQ.append(c.left)
                if c.right:
                    levelQ.append(c.right)
                s-=1
            maxValue.append(nodemax)
        return maxValue                
        
