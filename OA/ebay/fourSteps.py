def steps(s):
    res = 0
    while True:
        #step1 find the idx of the leftmost non-zero element x where x != 0, if no such finishes
        idx,x = 0,0
        for i in range(len(s)):
            if s[i]!= 0:
                idx = i
                x = s[i]
                break
        if x == 0:
            return res
        #step2
        for i in range(idx,len(s)):
            if s[i] < x:
                break
            s[i] -= x
        #step3
        res += x
    return res
if __name__=='__main__':
    arr = [0,1,2,3,4,5,6,7]
    print(steps(arr))