class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n = len(board),len(board[0])
        direction = [[-1,0],[1,0],[0,-1],[0,1]]
        def dfs(row,col):
            for d in direction:
                if 0<row + d[0]<m and 0<col+d[1]<n:
                    if board[row+d[0]][col+d[1]] == 'O':
                        board[row+d[0]][col+d[1]] = '#'
                        dfs(row+d[0],col+d[1])
        #1 row
        row = 0
        for i in range(n):
            if board[row][i] == 'O':
                board[row][i] = '#'
                dfs(row,i)
        #last row
        row = m-1
        for i in range(n):
            if board[row][i] == 'O':
                board[row][i] = '#'
                for d in direction:
                    dfs(row,i)
        #first col
        col = 0
        for i in range(m):
            if board[i][col] == 'O':
                board[i][col] = '#'
                dfs(i,col)
        #last col
        col = n-1
        for i in range(m):
            if board[i][col] == 'O':
                board[i][col] = '#'
                dfs(i,col)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
        