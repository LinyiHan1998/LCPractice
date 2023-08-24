def main(matrix):
    n = len(matrix)
    m = len(matrix[0])

    #1. n>=m then Matrix[(m+m%2-1)//2][n-m//2-m%2]
    #2.if mn is odd then matrix.back()
    #3.if mn is even then matrix.[n-1][m-1]
    
    if n >= m:
        return matrix[(m+m%2-1)//2][n-m//2-m%2]
    elif n*m%2 == 0:
        return matrix[n-2][m-3]
    else:
        return matrix[n-1][m-1]
    
if __name__ == "__main__":
    matrix = [
        [9,8,7,6],
	   [5,4,3,2],
       [1,10,11,12]]
    
    #29 8 37
    #15 41 3
    #31 10 14
    matrix2 = [
        [29,8,37],
        [15,41,3],
        [31,10,14]
    ]
    matrix3=[
        [1,2,3]
    ]

    res = main(matrix)
    print(res)
    res = main(matrix2)
    print(res)
    res = main(matrix3)
    print(res)