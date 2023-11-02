"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def subDepth(node):
            if node is None:
                return 0
            length = 0
            for child in node.children:
                length = max(length,subDepth(child))
            return length + 1
        return subDepth(root)
        