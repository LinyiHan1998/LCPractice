class Solution:
    def leastBricks(self, wall) -> int:
        row,col = len(wall),0
        for w in wall:
            col = max(col,len(w)-1+sum(w))
        matrix = [[0]*col for _ in range(row)]
        for i in range(row):
            j = 0
            mat_col=0
            while j < len(wall[i]):
                k = wall[i][j]
                while k > 0:
                    matrix[i][mat_col] = 1
                    mat_col += 1
                    k -= 1
                if mat_col < col:
                    matrix[i][mat_col] = 0
                j += 1
        print(col)
        print(matrix)
        s = row
        for j in range(col):
            tmp = 0
            for i in range(row):
                tmp += matrix[i][j]
            if tmp < s:
                s = tmp
        return s

if __name__=='__main__':
    s = Solution()
    wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
    print(s.leastBricks(wall))