# class Solution:
#     def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
#         if root is None:
#            return None
#         self.traverse(root.left,root.right)
#         return root
#     def traverse(self,node1,node2):
#         if node1 is None or node2 is None:
#             return
#         node1.next = node2
#         self.traverse(node1.left,node1.right)
#         self.traverse(node2.left,node2.right)
#         self.traverse(node1.right,node2.left)
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        que = deque()
        que.append(root)

        while que:
            sz = len(que)
            #cur = que.popleft()
            for i in range(sz):
                node = que.popleft()
                if i < sz-1:
                    node.next = que[0]
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return root
        