# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathsAppender(self, root, path, paths):
        if root is None:
            return 0
        path.append(str(root.val))
        if root.left is None and root.right is None:
            paths.append('->'.join(path[:]))
        else:
            self.pathsAppender(root.left, path, paths)
            self.pathsAppender(root.right, path, paths)
        path.pop()
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        path = []
        self.pathsAppender(root, path, paths)
        return paths


        

        
