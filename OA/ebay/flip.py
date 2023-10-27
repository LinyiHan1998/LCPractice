
def solution(bistr,requests):
    res = []
    b1 = bistr
    b2 = "".join([str(1-int(c)) for c in bistr])

    if bistr[0] == '0':
        c1,c2 = [0],[1]
    else:
        c1,c2 = [1],[0]
    
    for i in range(1,len(bistr)):
        if bistr[i]=='1':
            c1.append(c1[-1]+1)
            c2.append(c2[-1])
        else:
            c1.append(c1[-1])
            c2.append(c2[-1]+1)

    for request in requests:
        s = request.split(":")
        if len(s)==1:
            bistr = b1 if bistr == b2 else b2
        if len(s) == 2:
            if bistr == b1:
                res.append(c1[int(s[1])])
            else:
                res.append(c2[int(s[1])])
    return res

if __name__=='__main__':
    bistr = '01010101111'
    requests = ['count:3','flip']
    # print(count(bistr,3))
    # print(flip(bistr))
    print(solution(bistr,requests))