class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        directions = [[-1,0],[0,-1],[1,0],[0,1]]

        def dfs(r,c,index):
            nonlocal sz
            if grid[r][c]==0:
                return
            sz += 1
            #visited[r][c] = True
            grid[r][c] = index
            for x,y in directions:
                nr,nc = r+x,c+y
                if (nr < 0 or nr>=rows or
                nc<0 or nc>=cols or 
                grid[nr][nc] != 1):
                    continue
                dfs(nr,nc,index)

        water = set()
        index = 2
        island = {}
        max_island = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    water.add((row,col))
                elif grid[row][col] == 1:
                    sz = 0
                    dfs(row,col,index)
                    island[index] = sz
                    max_island = max(max_island,sz)
                    index += 1
        res = max_island
        
        for row,col in water:
            tmp = 1
            distinct =set()
            for x,y in directions:
                nr = row+x
                nc = col+y
                if (nr < 0 or nr>=rows or
                nc<0 or nc>=cols or 
                grid[nr][nc] == 0 or
                grid[nr][nc] in distinct):
                    continue
                tmp += island[grid[nr][nc]]
                distinct.add(grid[nr][nc] )
            res = max(res,tmp)
        return res


            
        