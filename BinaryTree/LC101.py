# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSame(left,right):
            if left is None and right is not None:
                return False
            if right is None and left is not None:
                return False
            if right is None and left is None:
                return True
            if left.val != right.val:
                return False
            outside = isSame(left.left,right.right)
            inside = isSame(left.right,right.left)
            return (outside and inside)
        return isSame(root.left,root.right)
        