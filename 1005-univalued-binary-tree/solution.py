class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if root.right:
            if root.val != root.right.val:
                return False
        if root.left:
            if root.val != root.left.val:
                return False
        return self.isUnivalTree(root.right) and self.isUnivalTree(root.left)
