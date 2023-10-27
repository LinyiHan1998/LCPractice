class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        max_area = 0
        offset = [[-1,0],[0,-1],[1,0],[0,1]]
        m,n = len(grid),len(grid[0])
        visited = [['0']*n for _ in range(m)]

        def dfs(r,c):
            nonlocal area
            if grid[r][c] == 0 or visited[r][c] == '1':
                return
            visited[r][c] = '1'
            area += 1

            for off_r,off_c in offset:
                if (r+off_r<0 or
                r+off_r>=m or
                c+off_c<0 or
                c+off_c>= n):
                    continue
                dfs(r + off_r,c+off_c)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and visited[r][c]=='0':
                    area = 0
                    dfs(r,c)
                    max_area = max(area,max_area)
        return max_area
        