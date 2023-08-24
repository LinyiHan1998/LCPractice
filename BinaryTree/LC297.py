class Codec:
    def traverse(self,root,res):
        if root is None:
            res.append(str(None))
            return 
        res.append(str(root.val))
        self.traverse(root.left,res)
        self.traverse(root.right,res)

    def deseralize_helper(self,d):
        if d == []:return None
        root_val = d.pop(0)
        if root_val == 'None':return None
        root = TreeNode(root_val)
        root.left = self.deseralize_helper(d)
        root.right = self.deseralize_helper(d)
        return root
        
    def serialize(self, root):
        res = []
        self.traverse(root,res)
        return str(res)
    

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        d = ' '.join(eval(data)).split()
        return self.deseralize_helper(d)