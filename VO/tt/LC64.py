'''
1->4->5
2->7->8
4->6->7
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])
        dp = [[0 for c in range(col)] for i in range(row)]
        dp[0][0] = grid[0][0]
        for r in range(1,row):
            dp[r][0] = dp[r-1][0] + grid[r][0]
        for c in range(1,col):
            dp[0][c] = dp[0][c-1] + grid[0][c]
        for r in range(1,row):
            for c in range(1,col):
                dp[r][c] = min(dp[r-1][c],dp[r][c-1]) + grid[r][c]
        return dp[row-1][col-1]