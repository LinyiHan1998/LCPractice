# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if not node.left and not node.right:
                return [1]
            left = dfs(node.left) if node.left else []
            right = dfs(node.right) if node.right else []
            for i in left:
                for k in right:
                    if i + k<=distance:
                        res += 1
            return [i+1 for i in left + right]
        dfs(root)
        return res
        