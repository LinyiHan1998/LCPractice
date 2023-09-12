
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
''' Q2
class Solution:
    def reverseBetween(self, head, left: int, right: int):
        pass


if __name__ == '__main__':
    arr = [1,2,3,4,5]
    dummy,head = ListNode(),ListNode()
    dummy = head
    for i in arr:
        cur = ListNode(i)
        head.next = cur
        head = head.next
    s = Solution()
    ret = s.reverseBetween(dummy.next,2,4)
    res = []
    while ret:
        res.append(ret.val)
        ret = ret.next
    print(res)
