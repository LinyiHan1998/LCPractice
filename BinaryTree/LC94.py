# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = []
        res = []
        cur = root
        if root is None:
            return res

        while cur or st:
            if cur:
                st.append(cur)
                cur = cur.left
            else:
                cur = st.pop()
                res.append(cur.val)
                cur = cur.right

        return res
        