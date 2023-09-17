# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        findp,findq = False,False
        def helper(node,p,q):
            nonlocal findp,findq
            if node is None:
                return
            left = helper(node.left,p,q)
            right = helper(node.right,p,q)

            if left and right:
                return node

            if node.val == p:
                findp = True
                return node
            elif node.val ==q:
                findq = True
                return node
            return left if left else right
            
        res = helper(root,p.val,q.val)
        if not (findp and findq):
            return None
        return res
        