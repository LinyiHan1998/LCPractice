class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def traverse(node,val):
            if node is None: return
            if node.val > val:
                return traverse(node.left,val)
            elif node.val == val :
                return node
            elif node.val < val:
                return traverse(node.right,val)
        return traverse(root,val)