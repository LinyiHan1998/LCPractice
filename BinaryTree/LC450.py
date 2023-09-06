class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def getmin(node):
            if node.left is None:
                return node
            return getmin(node.left)
        if root == None: return
        if root.val == key:
            if root.left == None:
                return root.right
            if root.right == None:
                return root.left
            min_node = getmin(root.right)
            root.right = self.deleteNode(root.right,min_node.val)
            min_node.left = root.left
            min_node.right = root.right
            root = min_node


        elif root.val > key:
            root.left = self.deleteNode(root.left,key)
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
        return root