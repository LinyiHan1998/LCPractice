class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        offset = [[-1,0],[0,-1],[1,0],[0,1]]
        visited = [[False]* n for _ in range(m)]
        def dfs(r,c):
            if visited[r][c]:
                return
            nonlocal perimeter
            visited[r][c] = True
            perimeter += 4
            for off_r,off_c in offset:
                if (r+off_r not in range(m) or
                c+off_c not in range(n)):
                    continue
                if grid[r+off_r][c+off_c]==1:
                    perimeter -= 1
                    dfs(r+off_r,c+off_c)
        perimeter = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r,c)
        return perimeter

