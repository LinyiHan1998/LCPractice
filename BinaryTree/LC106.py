class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.build(inorder,postorder)
    
    def build(self,inorder,postorder):
        if len(inorder)<=0 or len(postorder)<=0:
            return None
        rootval = postorder[-1]
        idx = -1
        for i in range(len(inorder)):
            if inorder[i] == rootval:
                idx = i
                break
        root = TreeNode(rootval)
        root.left = self.build(inorder[:idx],postorder[:idx])
        root.right = self.build(inorder[idx+1:],postorder[idx:-1])
        return root