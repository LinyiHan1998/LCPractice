def minimalCost(price):
    n = len(price)
    diff = 0
    for i in range(n-1):
        diff += (abs(price[i]-price[i+1]))
    res = diff
    for i in range(n):
        tmp = diff
        if i < n-1:
            tmp -= abs(price[i]-price[i+1])
        if i >= 1:
            tmp -= abs(price[i]-price[i-1])
        p = price[i]
        p //= 2
        if i < n-1:
            tmp += abs(p-price[i+1])
        if i >= 1:
            tmp += abs(p-price[i-1])
        res = min(res,tmp)
    return res
if __name__=='__main__':
    arr = [1,4,1]
    print(minimalCost(arr))