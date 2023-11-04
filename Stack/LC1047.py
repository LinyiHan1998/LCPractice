class Solution:
    def removeDuplicates(self, s: str) -> str:
        stk = []
        for ch in s:
            if stk and ch == stk[-1]:
                stk.pop()
                continue
            stk.append(ch)
        return ''.join(stk)
        