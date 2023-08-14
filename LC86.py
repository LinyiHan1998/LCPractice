def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
    list1,list2 = ListNode(),ListNode()
    dummy,head2 = list1,list2
    while head:
        if head.val < x:
            list1.next = ListNode(head.val)
            list1 = list1.next
        else:
            list2.next = ListNode(head.val)
            list2 = list2.next
        head = head.next
    list1.next = head2.next
    return dummy.next