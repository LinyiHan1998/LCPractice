def KMPcompare(s,t):
    #s is pattern
    combine = s + t
    j = 0
    nextarr = [0]
    for i in range(1,len(combine)):
        while j>0 and combine[j] != combine[i]:
            j = nextarr[j-1]
        if combine[j] == combine[i]:
            j += 1
        nextarr.append(j)
    print(nextarr)
    for cmp in nextarr[len(s):]:
        if cmp == 0:
            return False
    return True

if __name__ == '__main__':
    s = 'aabaab'
    t = 'aabaabaab'
    print(KMPcompare(s,t))
    s = 'aabaab'
    t = 'aabaabaaf'
    print(KMPcompare(s,t))
