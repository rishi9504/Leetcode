# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return
        res = []
        queue = deque()
        queue.append(root)
        while (len(queue)>0):
            level = len(queue)
            cl=[]
            for _ in range(level):
                node = queue.popleft()
                cl.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            res.append(cl)
        return res[::-1]                    
