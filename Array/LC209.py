class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        s = 0
        res = float('inf')
        for i in range(len(nums)):
            s += nums[i]
            while s>=target:
                res = min(res,i-l+1)
                s -= nums[l]
                l += 1
            
        return res if res != float('inf') else 0

        