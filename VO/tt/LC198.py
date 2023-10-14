'''
i : 1 to n represent each house
dp[i]:when the robber gets to house i, robeer's current greatest earn

i = 1
dp[1] = nums[0]
i = 2
d[2] = max(nums[1],nums[0])

i = 3
dp[3] = max(dp[1]+nums[2],dp[2])

dp[i] = max(dp[i-2]+nums[i-1],dp[i-1])
memo = dp[i-2],dp[i-1]
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        #base case
        if len(nums) < 3: return max(nums)
        n = len(nums)
        #dp
        dp = [0] * (n+1)
        dp[1] = nums[0]
        dp[2] = max(nums[0],nums[1])
        #memo = [nums[0],max(nums[0],nums[1])]

        for i in range(3,len(nums)+1):
            dp[i] = max(dp[i-2]+nums[i-1],dp[i-1])
        return dp[n]
            