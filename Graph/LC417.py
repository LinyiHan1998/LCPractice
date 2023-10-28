class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights),len(heights[0])
        offset = [[-1,0],[0,-1],[1,0],[0,1]]

        def dfs(r,c,visited):
            if visited[r][c]:
                return
            visited[r][c] = True
            for off_r,off_c in offset:
                if (r+off_r not in range(m) or
                c+off_c not in range(n) or
                heights[r+off_r][c+off_c]<heights[r][c] or
                visited[r+off_r][c+off_c]):
                    continue
                dfs(r+off_r,c+off_c,visited)
        
        pacific = [[False]*n for _ in range(m)]
        atlantic = [[False]*n for _ in range(m)]

        for c in range(n):
            dfs(0,c,pacific)
            dfs(m-1,c,atlantic)
        for r in range(m):
            dfs(r,0,pacific)
            dfs(r,n-1,atlantic)
        
        res = []
        for r in range(m):
            for c in range(n):
                if pacific[r][c] and atlantic[r][c]:
                    res.append([r,c])
            
        return res
            
        