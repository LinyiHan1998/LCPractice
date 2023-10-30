class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)>len(magazine):
            return False
        source = defaultdict(int)
        for ch in magazine:
            source[ch] += 1
        for ch in ransomNote:
            if ch not in source:
                return False
            source[ch] -= 1
            if source[ch]<0:
                return False
        return True