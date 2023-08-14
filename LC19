def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode()
    dummy.next = head
    left,right = dummy, dummy
    for i in range(n+1):
        right = right.next
    while right:
        left = left.next
        right = right.next
    
    left.next = left.next.next
        
    return dummy.next