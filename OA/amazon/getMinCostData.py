from collections import Counter,defaultdict
def getMinCostData(word):
    if '?' not in word:
        return word
    letter_cnt = []
    for i in range(26):
        letter_cnt.append(0)
    need = 0
    for ch in word:
        if ch == '?':
            need += 1
            continue
        letter_cnt[ord(ch)-ord('a')] += 1
    print(letter_cnt)
    llen = 0
    cut = ''
    while llen < need:
        min_cnt = letter_cnt[0]
        nxtch = 'a'
        idx = 0
        for i in range(len(letter_cnt)):
            if letter_cnt[i] < min_cnt:
                min_cnt = letter_cnt[i]
                nxtch = chr(i+ord('a'))
                idx = i
        cut += nxtch
        letter_cnt[idx] += 1
        llen += 1
    cut = sorted(list(cut),reverse=True)
    word = list(word)
    for i in range(len(word)):
        if word[i] == '?':
            word[i] = cut.pop()
    return ''.join(word)


        

        

if __name__=='__main__':
    word = '??????????????????????????????'
    print(getMinCostData(word))