class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:    return self.builder(preorder,postorder)
    
    def builder(self,preorder,postorder):
        if len(preorder)<=0 or len(postorder)<=0:
            return None
        if len(preorder)==1:
            return TreeNode(preorder[0])
        rootval,rootleftval = preorder[0],preorder[1]

        rootidx,leftidx = -1,-1

        for i in range(len(preorder)):
            if preorder[i] == rootval:
                rootidx = i
                break
        for i in range(len(postorder)):
            if postorder[i] == rootleftval:
                leftidx = i
                break
        root = TreeNode(rootval)
        root.left = self.builder(preorder[1:leftidx+2],postorder[:leftidx+1])
        root.right = self.builder(preorder[leftidx+2:],postorder[leftidx+1:-1])
        return root