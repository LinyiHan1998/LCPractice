# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        l,r = root,root
        hl,hr=0,0
        while l :
            l=l.left
            hl += 1
        while r:
            r = r.right
            hr += 1
        if hr == hl:
            return pow(2,hl) - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
        