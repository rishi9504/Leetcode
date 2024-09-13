# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        s = 0
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            root = q.get()
            s += 1
            if root.left is not None:
                q.put(root.left)
            if root.right is not None:
                q.put(root.right)
        return s
        
