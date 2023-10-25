def minimunCost(data,k):
    def helper(data,mid,k):
        s = 0
        n = len(data)
        s += sum(data[n-mid-2:])
        for i in range(mid,n-mid,2):
            s += data[i]
        return s>=k

    data.sort()
    n=len(data)
    if sum(data[(n-1)//2:])<k:
        return -1
    l,r=0,n//2
    while l<r:
        mid = (l+r)//2
        if helper(data,mid,k):
            r = mid
        else:
            l = mid+1
    return l