class Solution:
    def __init__(self):
        self.dic = {}
        self.res = []
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.traverse(root)
        return self.res
    
    def traverse(self,root):
        if root is None:
            return '#'
        left = self.traverse(root.left)
        right = self.traverse(root.right)

        myself = left+','+right+','+str(root.val)
        if myself in self.dic:
            self.dic[myself] += 1
            if self.dic[myself] == 2:
                self.res.append(root)
        else:
            self.dic[myself] = 1
        return myself