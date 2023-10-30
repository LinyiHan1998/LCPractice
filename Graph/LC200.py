import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        que = collections.deque()
        res = 0
        m,n = len(grid),len(grid[0])
        visited = [['0']*n for _ in range(m)]

        # que.push([0,0])
        # visited[0][0] = 1

        # dirction = [[0,-1],[0,1],[0,-1],[0,1]]
        # while que:
        #     i,j = que[0],que[1]
        def dfs(r,c):
            if grid[r][c] == '0' or visited[r][c] == '1':
                return
            visited[r][c] = '1'
            for offset_r,offset_c in offset:
                if (r+offset_r<0 or
                r+offset_r>=m or
                c+offset_c <0 or
                c+offset_c>=n):
                    continue
                dfs(r+offset_r,c+offset_c)
        def bfs(r,c):
            que.append([r,c])
            while que:
                pos = que.pop()
                row,col=pos[0],pos[1]
                for r_offset,c_offset in [[1,0],[-1,0],[0,1],[0,-1]]:
                    if row + r_offset< 0 or row + r_offset >= m or col + c_offset < 0 or col + c_offset >= n or grid[row + r_offset][col + c_offset] == '0' or visited[row + r_offset][col + c_offset] == '1':
                        continue
                    que.append([row + r_offset,col + c_offset])
                    visited[row + r_offset][col + c_offset] = '1'
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1' and visited[r][c]=='0':
                    res += 1
                    bfs(r,c)
        return res



        