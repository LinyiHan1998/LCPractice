class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        res = 0
        m,n = len(grid),len(grid[0])
        offset = [[-1,0],[0,-1],[1,0],[0,1]]
        island_map = {}
        waters = set()
        def dfs(i,j,index):
            nonlocal area
            grid[i][j] = index
            area += 1
            for off_r,off_c in offset:
                if(i+off_r not in range(m) or
                j+off_c not in range(n) or
                grid[i+off_r][j+off_c] != 1):
                    continue
                dfs(i+off_r,j+off_c,index)
        index = 2
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    waters.add((r,c))
                elif grid[r][c] == 1:
                    area = 0
                    dfs(r,c,index)
                    island_map[index] = area
                    res = max(res,area)
                    index += 1
        for i,j in waters:
            connect = set()
            island_len = 1
            for off_r,off_c in offset:
                if(i+off_r not in range(m) or
                j+off_c not in range(n) or
                grid[i+off_r][j+off_c] not in island_map or
                grid[i+off_r][j+off_c] in connect):
                    continue
                connect.add(grid[i+off_r][j+off_c])
                island_len += island_map[grid[i+off_r][j+off_c]]
            res = max(res,island_len)
        return res
        