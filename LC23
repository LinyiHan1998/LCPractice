def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    dummy = ListNode()
    p = dummy
    heap = []
    for i in range(len(lists)):
        if lists[i]:
            heap.append((lists[i].val,i))
    heapq.heapify(heap)
    while heap:
        cur,idx = heapq.heappop(heap)
        lists[idx] = lists[idx].next
        if lists[idx]:
            heapq.heappush(heap,(lists[idx].val,idx))
            
        p.next = ListNode(cur)
        p = p.next
    return dummy.next