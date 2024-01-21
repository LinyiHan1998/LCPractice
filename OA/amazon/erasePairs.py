from collections import Counter
def erasePairs(s):
    counter = Counter(s)
    res = ''
    record = set()
    for ch in s:
        if counter[ch] % 2 == 1 and ch not in record:
            record.add(ch)
            res += ch
    # for k,v in counter.items():
    #     if v % 2 != 0:
    #         res += k
    return res
if __name__=="__main__":
    S = "CBCAAXA"
    print(erasePairs(S))
    