class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def traverse(node):
            if node is None:
                return
            traverse(node.left)
            res.append(node.val)
            traverse(node.right)
        
        traverse(root)
        return res[k-1]