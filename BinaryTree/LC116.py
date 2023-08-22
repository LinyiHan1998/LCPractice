class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
           return None
        self.traverse(root.left,root.right)
        return root
    def traverse(self,node1,node2):
        if node1 is None or node2 is None:
            return
        node1.next = node2
        self.traverse(node1.left,node1.right)
        self.traverse(node2.left,node2.right)
        self.traverse(node1.right,node2.left)