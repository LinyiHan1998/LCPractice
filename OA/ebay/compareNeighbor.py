def compare(arr):
    res = [arr[0]]
    if len(arr)<=2:
        return arr
    for i in range(1,len(arr)-1):
        if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
            res.append(arr[i])
    res.append(arr[-1])
    return res

if __name__ == '__main__':
    arr = [0,1,0,2,3]
    print(compare(arr))