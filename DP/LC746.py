class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        dp = [float('inf')] * len(cost)
        dp[0],dp[1] = 0,0
        for i in range(2,len(cost)):
            dp[i] = min(dp[i-2]+cost[i-2],dp[i-1]+cost[i-1])
        return dp[-1]