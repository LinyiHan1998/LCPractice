class Solution:
    def isPalindrome(self,s):
        left,right = 0,len(s)-1
        while left < right:
            if s[left]!= s[right]:
                return False
            left += 1
            right -= 1
        return True
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(idx,path):
            if idx == len(s):
                res.append(path.copy())
                return
            for i in range(idx,len(s)):
                if self.isPalindrome(s[idx:i+1]):
                    path.append(s[idx:i+1])
                    backtrack(i+1,path)
                    path.pop()
        backtrack(0,[])
        return res
        