def getMinDistance(center,destination):
    center = sorted(center)
    destination = sorted(destination)
    res = 0
    for i in range(len(center)):
        res += abs(center[i] - destination[i])
    return res
if __name__ == '__main__':
    center = [50, 60, 70]
    destination = [5, 2, 4]
    print(getMinDistance(center,destination))