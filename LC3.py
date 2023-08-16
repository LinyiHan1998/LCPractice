def lengthOfLongestSubstring(self, s: str) -> int:
    left = right = 0
    res = 0
    window = Counter()
    while right<len(s):
        c = s[right]
        right += 1
        window[c]+=1
        
        while window[c]>1:
            window[s[left]] -= 1
            left += 1
        res = max(res,right - left)
            
    return res