def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
    arr = [0]*length
    diff = [0]*length

    for up in updates:
        diff[up[0]] += up[2]
        if up[1]+1<length:
            diff[up[1]+1] -= up[2]
    
    arr[0] = diff[0]
    for i in range(1,length):
        arr[i] = diff[i] + arr[i-1]
    return arr
