# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        cnt = 0
        que = deque()

        que.append(root)
        while que:
            sz = len(que)
            cnt += 1
            for i in range(sz):
                node = que.popleft()
                if (not node.left and not node.right):
                    return cnt
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return cnt