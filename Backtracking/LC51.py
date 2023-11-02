class Solution:
    
    def isValid(self,row,col,board,n):
        #check col
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        #check 45
        i,j=row-1,col-1
        while i>=0 and j>=0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        #check 135
        i,j=row-1,col+1
        while i>=0 and j<n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        # def is_valid(board, row, col):
        #     # same col
        #     for i in range(row):
        #         if board[i][col] == "Q":
        #             return False
        #     # left top 
        #     for i, j in zip(reversed(range(row)), reversed(range(col))):
        #         if board[i][j] == "Q":
        #             return False
        #     # right top
        #     for i, j in zip(reversed(range(row)), range(col + 1, n)):
        #         if board[i][j] == "Q":
        #             return False

        #     return True
        def backtrack(row):
            if row == n:
                res.append([''.join(solution) for solution in board])
                return
            for c in range(n):
                if self.isValid(row,c,board,n):
                # if is_valid(board,row,c):
                    board[row][c] = 'Q'
                    backtrack(row+1)
                    board[row][c] = '.'
        backtrack(0)
        return res