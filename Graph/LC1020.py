class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        res = 0
        m,n = len(grid),len(grid[0])
        visited = [[False]*n for _ in range(m)]
        que = deque()

        offset = [[1,0],[0,1],[-1,0],[0,-1]]

        def bfs(r,c,area,flag):
            que.append([r,c])
            visited[r][c] = True
            area += 1
            while que:
                pos = que.popleft()
                row,col = pos[0],pos[1]

                for off_r,off_c in offset:
                    if (row+off_r not in range(m) or
                    col + off_c not in range(n)):
                        flag = 1
                        continue
                    if grid[row+off_r][col+off_c] == 0 or visited[row+off_r][col+off_c] == True:
                        continue
                    que.append([row+off_r,col+off_c])
                    visited[row+off_r][col+off_c] = True
                    area += 1
            return (area,flag)
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and visited[r][c] == False:
                    area,flag = bfs(r,c,0,0)
                    if flag == 0:
                        res += area
        return res


        