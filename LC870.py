def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
    n = len(nums1)
    pq = [(-val,i) for i, val in enumerate(nums2)]
    heapq.heapify(pq)
    nums1.sort()

    left,right = 0,n-1
    res = [0]*n
    while pq:
        val,i = heapq.heappop(pq)
        maxVal = -val
        if maxVal < nums1[right]:
            res[i] = nums1[right]
            right -= 1
        else:
            res[i] = nums1[left]
            left += 1
    return res
