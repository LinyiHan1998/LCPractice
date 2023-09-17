#heap sort
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        #pq = heapq.heapify(pq)
        for n in nums:
            heapq.heappush(pq,n)
            if len(pq)>k:
               heappop(pq)
        
        return heappop(pq)