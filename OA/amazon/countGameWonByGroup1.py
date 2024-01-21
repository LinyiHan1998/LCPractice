def countGameWonByGroup1(group1,group2):
    res = 0
    n = len(group1)
    for i in range(n):
        for j in range(i+1,n):
            if (group1[i] > group2[i] and group1[j] >= group2[j]) or (group1[i] >= group2[i] and group1[j] > group2[j]):
                res += 1
    return res%(10**9 +7)
if __name__=='__main__':
    group1 = [1, 2, 3]
    group2 = [1, 2, 3]
    print(countGameWonByGroup1(group1,group2))