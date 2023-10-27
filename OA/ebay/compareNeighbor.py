def compare(arr):
    for i in range(1,len(arr)-1):
        if arr[i]<arr[i-1] and arr[i]<arr[i+1]:
            print(arr[i])
            return arr[i]
    return -1

if __name__ == '__main__':
    arr = [0,1,0,2,3]
    print(compare(arr))