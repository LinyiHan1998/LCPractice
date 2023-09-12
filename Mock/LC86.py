'''
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head, x: int):
        pass

if __name__ == '__main__':
    arr = [1,4,3,2,5,2]
    dummy,head = ListNode(),ListNode()
    dummy = head
    for i in arr:
        cur = ListNode(i)
        head.next = cur
        head = head.next
    s = Solution()
    ret = s.partition(dummy.next,3)
    res = []
    while ret:
        res.append(ret.val)
        ret = ret.next
    print(res)