from collections import Counter
def isTwin(arr):
    counter = Counter(arr)
    for c in counter:
        if counter[c] == 1:
            return c
    return -1
if __name__ == '__main__':
    arr = [1,1,2,2,3,3,4,4]
    print(isTwin(arr))
