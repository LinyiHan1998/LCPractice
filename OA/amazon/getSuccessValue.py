def getSuccessValue(num_viewers,queries):
    num_viewers = sorted(num_viewers,reverse=True)
    ans = [num_viewers[0]]
    for i in range(1,len(num_viewers)):
        ans.append(ans[-1] + num_viewers[i])
    res = []
    for q in queries:
        res.append(ans[q-1])
    return res
if __name__=='__main__':
    # num_viewers = [2, 5, 6, 3, 5]
    # queries = [2, 3, 5]
    # num_viewers = [7, 3, 5, 2]
    # queries = [1, 4]
    num_viewers = [7, 5, 6]
    queries = [1, 2, 3]
    print(getSuccessValue(num_viewers,queries))