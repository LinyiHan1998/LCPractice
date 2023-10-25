def solution(queryType, query):
    hashmap = {}
    key = 0
    value = 0

    def insert(pair):
        nonlocal key,value
        if pair:
            hashmap[pair[0]-key] = pair[1]-value
    def get(k):
        nonlocal key,value
        if k - key in hashmap:
            return hashmap[k-key] + value
        else:
            return -1
    def addTovalue(v):
        nonlocal value
        value += v
    def addTokey(k):
        nonlocal key
        key += k
    res = []
    for t,q in zip(queryType,query):
        if t == 'insert':
            insert(q)
        elif t =='get':
            res.append(get(q[0]))
        elif t == 'addToValue':
            addTovalue(q[0])
        else:
            addTokey(q[0])
    return sum(res)
        
            

