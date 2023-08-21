def findAnagrams(self, s: str, p: str) -> List[int]:
    need = {}
    for item in p:
        if item in need:
            need[item] += 1
        else:
            need[item] = 1
    window = {}
    res = []
    left,right,start = 0,0,0
    cnt = 0

    while right < len(s):
        c = s[right]
        right += 1
        if c in need:
            if c in window:
                window[c]+=1
            else:
                window[c]=1
            if window[c] == need[c]:
                cnt +=1
        if right - left >= len(p):
            if cnt == len(need):
                res.append(left)
            d = s[left]
            left += 1
            if d in need:
                if d in window:
                    if window[d] == need[d]:
                        cnt -= 1
                    window[d] -= 1

    return res