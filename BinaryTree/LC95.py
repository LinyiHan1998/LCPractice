class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def build(lo,hi):
            res = []
            if lo > hi:
                res.append(None)
                return res
            for i in range(lo,hi+1):

                left = build(lo,i-1)
                right = build(i+1,hi)
                for l in left:
                    for r in right:
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        res.append(node)
            return res
        return build(1,n)