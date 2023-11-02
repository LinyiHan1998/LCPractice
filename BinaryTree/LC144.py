class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def traverse(cur):
            if cur == None:
                return
            res.append(cur.val)
            traverse(cur.left)
            traverse(cur.right)
        traverse(root)
        return res