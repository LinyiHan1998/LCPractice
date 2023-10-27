def flip(s):#带上函数名字抄，外面还要补个string处理
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
def solution(bistr,requests):
    res = []
    for request in requests:
        if 'count' in request:
            i = 6
            x = ''
            while request[i]!='>':
                x += request[i]
                i += 1
            res.append(count(bistr,int(x)))
        else:
            res.append(flip(bistr))
    return res

if __name__=='__main__':
    bistr = '01010101111'
    requests = ['count<3>','flip']
    print(count(bistr,3))
    print(flip(bistr))
    print(solution(bistr,requests))