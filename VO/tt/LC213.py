'''
1. circle
if steal first, have to skip last,range(0,n-1)
if steal last, have to skip first, range(1,n)

2. calculate the greatest earn
i: represents house idx
dp[i]: when robber gets to house i, robber's greatest earn
when i = 0
dp[0] = nums[0]
when i = 1
dp[1] = max(nums[0],nums[1])
when i = 2
dp[2] = max(dp[1],dp[0]+nums[2])
general
dp[i] = max(dp[i-1],dp[i-2]+nums[i])
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0 : return 0
        if len(nums) == 1 : return nums[0]
        
        def helper(nums):
            n = len(nums)
            if n < 3: return max(nums)
            dp = [0] * n
            dp[0] = nums[0]
            dp[1] = max(nums[0],nums[1])
            for i in range(2,n):
                dp[i] = max(dp[i-1],dp[i-2]+nums[i])
            return dp[n-1]
        return max(helper(nums[:-1]),helper(nums[1:]))
        
            

            

        