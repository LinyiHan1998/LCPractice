def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    p = dummy

    while list1 and list2:
        if list1.val<list2.val:
            p.next=ListNode(list1.val)
            list1 = list1.next
        else:
            p.next = ListNode(list2.val)
            list2 = list2.next
        p = p.next
    if list1:
        p.next = list1
    if list2:
        p.next = list2
    return dummy.next