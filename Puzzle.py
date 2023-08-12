def Puzzle(str1):
    stk = []
    res = ''
    tmp = ''
    for s in str1:
        if stk and stk[-1] == s:
            stk.pop()
            tmp = s + tmp + s
            
            if len(tmp)>len(res):
                res = tmp
        else:
            stk.append(s)
        print(stk)
    return res

if __name__=='__main__':
    str1 = 'YABCCBAZ'
    print(Puzzle(str1))
