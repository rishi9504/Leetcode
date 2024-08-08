# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return
        res = []
        queue = deque()
        queue.append(root)
        pl = True
        while (len(queue)>0):
            level = len(queue)
            cl=deque()
            for _ in range(level):
                node = queue.popleft()
                if pl:
                    cl.append(node.val)
                else:
                    cl.appendleft(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            res.append(cl)
            pl=not pl
        return res         
