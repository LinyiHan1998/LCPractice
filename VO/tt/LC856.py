class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = []
        for ch in s:
            if stk is None or ch =='(':
                stk.append(ch)
            elif stk[-1] == '(':
                stk.pop()
                stk.append(1)
            else:
                num = 0
                while stk and str(stk[-1]).isdigit():
                    num += stk.pop()
                stk.pop()
                stk.append(2*num)
        return sum(stk)
        