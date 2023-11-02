# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []
        que = deque()
        que.append(root)
        res = []
        while que:
            sz = len(que)
            s = 0
            for i in range(sz):
                node = que.popleft()
                s += node.val
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(s/sz)
        return res