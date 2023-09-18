def maxGenePhone(arr1,memCon):
    memCon = sorted(memCon,key = lambda x:(x[0],x[1]))
    print(memCon)

if __name__=="__main__":
    memCon = [
        [0,1],[0,2],[1,4],[1,3]
    ]
    arr1 = []
    maxGenePhone(arr1,memCon)