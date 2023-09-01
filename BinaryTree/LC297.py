# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:
    def __init__(self):
        self.SEP = ','
        self.EMPTY = '#'
        self.res = ''
    ####pre-order###
    def preTraverse(self,root):
        if root == None:
            self.res += self.EMPTY+self.SEP
            return
        self.res += str(root.val) +self.SEP
        self.preTraverse(root.left)
        self.preTraverse(root.right)

    def preTraverseDecode(self,nodes):
        if nodes == []:
            return None

        root_val = nodes.pop(0)
        if root_val == self.EMPTY:
            return None
        root = TreeNode(root_val)
        root.left = self.preTraverseDecode(nodes)
        root.right = self.preTraverseDecode(nodes)
        return root
    ###post-order###
    def postTraverse(self,root):
        if root == None:
            self.res += self.EMPTY+self.SEP
            return
        
        self.postTraverse(root.left)
        self.postTraverse(root.right)
        self.res += str(root.val) +self.SEP

    def postTraverseDecode(self,nodes):
        if nodes == []:return None
        root_val = nodes.pop()
        if root_val == self.EMPTY:
            return None
        root = TreeNode(int(root_val))
        root.right = self.postTraverseDecode(nodes)
        root.left = self.postTraverseDecode(nodes)
        return root

    ###sequence traversal###
    def iterativeTraverse(self,root):
        if root == None: return None
        queue=[root]
        while queue:
            sz = len(queue)
            for i in range(sz):
                cur = queue.pop(0)
                if cur is None:
                    self.res += self.EMPTY + self.SEP
                    continue
                self.res += str(cur.val) + self.SEP
                queue.append(cur.left)
                queue.append(cur.right)


    def iterativeTraverseDecode(self,nodes):
        if nodes == []: return None
        root = TreeNode(nodes.pop(0))
        queue = [root]
        while queue:
            sz = len(queue)
            for i in range(sz):
                parent = queue.pop(0)
                if parent is None: continue
                left = nodes.pop(0)
                right = nodes.pop(0)

                if left != self.EMPTY:
                    parent.left = TreeNode(left)
                    queue.append(parent.left)
                
                if right !=self.EMPTY:
                    parent.right = TreeNode(right)
                    queue.append(parent.right)

        return root

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        #self.preTraverse(root)
        #self.postTraverse(root)
        self.iterativeTraverse(root)
        return self.res
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        arr = data.split(self.SEP)
        arr.remove('')
        #if data == [] :return None
        
        #return self.preTraverseDecode(arr)
        #return self.postTraverseDecode(arr)
        return self.iterativeTraverseDecode(arr)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))