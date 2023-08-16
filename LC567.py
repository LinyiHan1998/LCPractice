def checkInclusion(self, s2: str, s1: str) -> bool:
    need,window = {},{}
    for s in s2:
        if s in need:
            need[s]+=1
        else:
            need[s] = 1
    left = 0
    right = 0
    cnt = 0
    while right < len(s1):
        a = s1[right]
        right += 1
        if a in need:
            if a in window:
                window[a]+=1
            else:
                window[a] = 1
            if window[a] == need[a]:
                cnt += 1
        
        while right-left >= len(s2):
            if cnt == len(need):
                return True
            c = s1[left]
            left += 1
            if c in need:
                if c in window:
                    if window[c] == need[c]:
                        cnt -= 1
                    window[c] -= 1

    return False