def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    m = len(matrix)
    n = len(matrix[0])
    top = 0
    btm=m-1
    left=0
    right=n-1
    res = []
    i=j=0
    while len(res)<m*n:
        if top <= btm:
            for j in range(left,right+1):
                res.append(matrix[top][j])

            top += 1
        if left <= right:
            for i in range(top,btm+1):
                res.append(matrix[i][right])

            right -= 1
        if top <= btm:
            for j in range(right,left-1,-1):
                res.append(matrix[btm][j])
        
            btm -= 1
        if left <= right:
            for i in range(btm,top-1,-1):
                res.append(matrix[i][left])
            left += 1
    return res






