# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def traverse(s):
            if s:
                return '#' + str(s.val)+',' + traverse(s.left)+',' + traverse(s.right)
            return 'null'

        string_s = traverse(root)
        string_t = traverse(subRoot)
        print(string_s)
        print(string_t)
        if string_t in string_s:
            return True
        return False
        