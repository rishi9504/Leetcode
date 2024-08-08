# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# from collections import defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return
#         # queue = []
#         # cl = 0
#         # queue.append((root,cl))
#         # res = defaultdict(list)
#         # while(len(queue) > 0):
#         #     node,lvl = queue.pop(0)
#         #     res[lvl].append(node.val)
#         #     if node.left is not None:
#         #         queue.append((node.left,cl+1))
#         #     if node.right is not None:
#         #         queue.append((node.right,cl+1))
            
#         #     cl+=1
#         # return list(res.values()) 

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
        return res            


# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         list1=[]
#         q=deque()
#         q.append(root)
#         while q:
#             level=[]
#             for i in range(len(q)):
#                 poping=q.popleft()
#                 if poping:
#                     level.append(poping.val)
#                     q.append(poping.left)
#                     q.append(poping.right)
#             if level:
#                 list1.append(level)
#         return list1
    #please upvote me it would encourage me alot



