from collections import defaultdict
def getTrucksForItems(trucks,items):
    for i in range(len(trucks)):
        trucks[i] = (trucks[i],i)
    for i in range(len(items)):
        items[i] = (items[i],i)
    trucks = sorted(trucks, key = lambda x:x[0])
    items = sorted(items, key = lambda x:x[0])
    print(trucks)
    print(items)
    res = [-1] * len(items)
    idx = 0
    for i in range(len(items)):
        while idx < len(trucks) and trucks[idx][0] <= items[i][0]:
            idx += 1
        if idx == len(trucks):
            break
        res[items[i][1]] = trucks[idx][1]
        idx += 1
    return res

if __name__ == '__main__':
    trucks = [4, 5, 7, 2]
    items = [1, 2, 5]
    # trucks = [5, 3, 8, 1]
    # items = [6, 10]
    # trucks = [1, 3, 5, 2, 3, 2]
    # items = [1, 2, 3]
    print(getTrucksForItems(trucks,items))