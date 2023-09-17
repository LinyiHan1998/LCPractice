# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        minval = min(p.val,q.val)
        maxval = max(p.val,q.val)
        def helper(node,val1,val2):
            if node.val > val2:
                return helper(node.left,val1,val2)
            elif node.val < val1:
                return helper(node.right,val1,val2)
            return node
        return helper(root,minval,maxval)
        