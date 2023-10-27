class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        while cur and cur.next and cur.next.next:
                p1,p2,tmp = cur.next,cur.next.next,cur.next.next.next
                cur.next = p2
                p2.next = p1
                p1.next = tmp
                cur = p1
        return dummy.next