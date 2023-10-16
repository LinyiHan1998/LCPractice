# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        p=dummy
        prev = 0
        while l1 and l2:
            tmp = l1.val + l2.val + prev
            p.next = ListNode(tmp%10)
            prev = tmp//10
            p=p.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            tmp = l1.val + prev
            p.next = ListNode(tmp%10)
            prev = tmp//10
            p=p.next
            l1 = l1.next
        while l2:
            tmp = l2.val + prev
            p.next = ListNode(tmp%10)
            prev = tmp//10
            p=p.next
            l2 = l2.next
        if prev !=0:
            p.next = ListNode(prev)
        return dummy.next