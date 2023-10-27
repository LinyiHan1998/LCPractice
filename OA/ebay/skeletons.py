def solution(word,skeletons):
    n = len(word)
    res = []

    for s in skeletons:
        letters = set(s)
        i = 0
        while i<n:
            if s[i]=='-' and word[i] not in letters:
                break
            i += 1
        if i == n:
            res.append(s)
    return res