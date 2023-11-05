

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stk = []
        for i,ch in enumerate(s):
            if ch == '(':
                stk.append(i)
            elif ch == ')':
                if stk:
                    stk.pop()
                else:
                    s[i] = ''
        while stk:
            s[stk.pop()] = ''
        return ''.join(s)
        

        