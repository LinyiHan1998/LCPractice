def flip(s):
    res = ''
    for ch in s:
        if ch == '0':
            res += '1'
        else:
            res += '0'
    return res
def count(s,x):
    res = 0
    for i in range(x):
        if s[i] == '0':
            res += 1
    return res

if __name__=='__main__':
    bistr = '01010101111'
    print(count(bistr,3))
    print(flip(bistr))