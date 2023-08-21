def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    dummy.next = head
    slow,fast = dummy,dummy
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.next if fast else slow