#class Solution:
#     def backspaceCompare(self, s: str, t: str) -> bool:
#         def helper(s):
#             stk = []
#             for ch in s:
#                 if ch != '#':
#                     stk.append(ch)
#                 elif stk:
#                     stk.pop()
#             return stk
#         return helper(s) == helper(t)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(s):
            backspace = 0
            res = ''
            for ch in reversed(s):
                if ch == '#':
                    backspace += 1
                elif backspace:
                    backspace -= 1
                else:
                    res += ch
            return res
        return helper(s) == helper(t)
        