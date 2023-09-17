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
    
#quick selection
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums)-k
        lo,hi = 0, len(nums)-1

        while lo <= hi:
            p = self.partition(nums,lo,hi)
            if p < k:
                lo = p+1
            elif p > k:
                hi = p-1
            else:
                return nums[p]
        return -1
    def partition(self,nums,lo,hi):
        pivot = nums[lo]
        l,r = lo+1,hi
        while l <= r:
            while l < hi and nums[l] <= pivot:
                l += 1
            while r > lo and nums[r] > pivot:
                r -= 1
            if r <= l:
                break
            nums[r],nums[l] = nums[l],nums[r]
        nums[lo],nums[r] = nums[r],nums[lo]
        return r
    def shuffle(self,nums):
        for i in range(n):
            r = i + random.randint(n-i-1)
            nums[i],nums[r] = nums[r],nums[i]
