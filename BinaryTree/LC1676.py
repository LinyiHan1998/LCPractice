# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        arr = []
        for node in nodes:
            arr.append(node.val)
        #arr = set(arr)

        def helper(node):
            if node is None: 
                return
            if node.val in arr:
                return node
            left = helper(node.left)
            right = helper(node.right)

            if left and right:
                return node
            return left if left else right

        return helper(root)
        