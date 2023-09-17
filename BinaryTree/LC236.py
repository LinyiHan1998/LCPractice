# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node,p,q):
            
            if node == p or node == q:
                return node
            if node is None:
                return False
            left = helper(node.left,p,q)
            right = helper(node.right,p,q)

            if left and right:
                return node
            return left if left else right
            
        
        return helper(root,p,q)

        