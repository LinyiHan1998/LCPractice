class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        s_dict = defaultdict(int)
        for ch in s:
            s_dict[ch]+=1
        for ch in t:
            if ch not in s_dict:
                return False
            s_dict[ch] -= 1
            if s_dict[ch] < 0:
                return False
        return True