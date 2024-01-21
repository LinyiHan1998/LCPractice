def getScoreDifference(points):
    points = sorted(points)
    res1,res2 = 0,0
    n = len(points)
    for i in range(n):
        if i % 2 != 0:
            res2 += points.pop()
        else:
            res1 += points.pop()
    return abs(res1 - res2)
if __name__=='__main__':
    #points = [4, 1, 2, 3]
    points = [4, 1, 1, 4]
    print(getScoreDifference(points))