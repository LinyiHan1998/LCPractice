class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        arr = []
        for key,value in dic.items():
            heapq.heappush(arr,(value,key))
            if len(arr)>k:
                heapq.heappop(arr)
        
        return [key for value,key in arr]
        