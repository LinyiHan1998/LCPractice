class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        #base case
        if root is None:return None
        #recursion
        #s1
        if root.val >= low and root.val <= high:
            root.left = self.trimBST(root.left,low,high)
            root.right = self.trimBST(root.right,low,high)
        #s2
        elif root.val < low:
            root = self.trimBST(root.right,low,high)
        #s3
        elif root.val > high:
            root = self.trimBST(root.left,low,high)

        return root