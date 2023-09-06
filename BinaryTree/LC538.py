class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        s = [0]
        def traverse(node):
            if node is None:
                return
            traverse(node.right)
            s[0] += node.val
            node.val = s[0]
            traverse(node.left)
        traverse(root)
        return root