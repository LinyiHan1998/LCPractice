from collections import defaultdict
def maxSetSize(riceBags):
    riceSet = set(riceBags)
    res = 0
    for bag in riceBags:
        tmp = bag
        cnt = 1
        while tmp*tmp in riceSet:
            cnt += 1
            tmp = tmp*tmp
        res = max(cnt,res)

    return res
if __name__ == '__main__':
    riceBags = [3, 9, 4, 2, 16]
    print(maxSetSize(riceBags))