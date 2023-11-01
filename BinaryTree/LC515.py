# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        que = deque()
        res = []

        que.append(root)
        while que:
            sz = len(que)
            num = - float('inf')
            for i in range(sz):
                node = que.popleft()
                num = max(node.val,num)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(num)
        return res