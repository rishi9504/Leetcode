# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ls=[]
        lc=[]
        def dfs(node,level):
            if not node:
                return
            # if being visited first time    
            if level == len(ls):
                ls.append(0)
                lc.append(0)
            ls[level] += node.val 
            lc[level]+=1
            dfs(node.left,level+1)
            dfs(node.right,level+1)
        dfs(root,0)
        return [ls[i]/lc[i] for i in range(len(ls))]           
        
