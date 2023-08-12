import collections
def getResult(arrival, street):
    n = len(arrival)
    mainStreet = collections.deque()
    firstAve = collections.deque()

    for i in range(n):
        t = arrival[i]
        s = street[i]
        if s == 0:
            mainStreet.append([t,i])
        else:
            firstAve.append([t,i])
    result = [0 for i in range(n)]
    time = 0

    while mainStreet and firstAve:
        main = mainStreet.popleft()
        mainTime = main[0]
        mainIndex = main[1]

        first = firstAve.popleft()
        firstTime = first[0]
        firstIndex = first[1]

        if mainTime < firstTime:
            firstAve.appendleft([firstTime,firstIndex])
            time = max(time,mainTime)
            result[mainIndex] = time
            time += 1
            time = passStreet(mainStreet,time,result)
        else: 
            mainStreet.appendleft([mainTime,mainIndex])
            time = max(time,firstTime)
            result[firstIndex] = time
            time += 1
            time = passStreet(firstAve,time,result)
    if mainStreet:
        passToEmpty(mainStreet,time,result)
    if firstAve:
        passToEmpty(firstAve,time,result)
    
    return result

def passStreet(street,time,result):
    while street:
        S = street.popleft()
        Time = S[0]
        Index = S[1]

        if Time <= time:
            result[Index] = time
            time = time + 1
        else:
            street.appendleft([Time,Index])
            return time
    return time

def passToEmpty(street,time,result):
    while street:
        S = street.popleft()
        Time = S[0]
        Index = S[1]
        time = max(Time,time)
        result[Index] = time
        time += 1
    return

if __name__=='__main__':
    arrival = [0,0,1,4]
    street = [0,1,1,0]
    print(getResult(arrival,street))


