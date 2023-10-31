class Solution:
    def isValid(self,s):
        if not s.isdigit():
            return False
        if len(s) < 1:
            return False
        if s[0] == '0' and len(s)>1:
            return False
        if int(s)>255:
            return False
        return True
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def backtrack(idx,path,cnt):
            if idx == len(s) and cnt==4:
                res.append(path[:-1])
                return
            for i in range(idx,min(len(s),idx+3)):
                tmp = s[idx:i+1]
                if self.isValid(tmp):
                    backtrack(i+1,path + tmp + '.',cnt+1)
        backtrack(0,'',0)
        return res

        