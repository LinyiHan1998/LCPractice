def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    p1,p2 = headA,headB
    while p1 != p2:
        if p1 == None:
            p1 = headB
        else:
            p1 = p1.next
        if p2 == None:
            p2 = headA
        else:
            p2 = p2.next
    return p1