class Solution:
    def __init__(self):
        self.maxdistance = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.maxdistance
    def traverse(self,root):
        if root is None:
            return 0
        left_dep = self.traverse(root.left)
        right_dep = self.traverse(root.right)

        self.maxdistance = max(self.maxdistance,left_dep+right_dep)
        return max(left_dep,right_dep) + 1