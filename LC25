def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head:
        return None
    a, b = head,head
    for i in range(k):
        if not b:
            return head
        b = b.next
    new_head = self.reverse(a,b)
    a.next = self.reverseKGroup(b,k)
    return new_head
def reverse(self,head,tail):
    pre,cur,nxt = None,head,head
    while cur != tail:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    return pre