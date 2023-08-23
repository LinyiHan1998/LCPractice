def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    return self.builder(preorder,inorder)

def builder(self,preorder,inorder):
    if len(preorder)<=0 or len(inorder)<=0:
        return None
    rootval = preorder[0]
    idx = -1

    for i in range(len(inorder)):
        if inorder[i] == rootval:
            idx = i
            break
    root = TreeNode(rootval)
    root.left = self.builder(preorder[1:idx+1],inorder[0:idx])
    root.right = self.builder(preorder[idx+1:],inorder[idx+1:])
    return root