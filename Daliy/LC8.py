class Solution:
    def myAtoi(self, s: str) -> int:
        Max = 2**31 -1
        Min = -1 * 2**31
        res = '0'
        flag = 1
        start = 0
        for ch in s:
            if start == 1 and not ch.isdigit():
                break
            if ch == ' ':
                continue
            
            if ch == '-':
                start = 1
                if flag != 1:
                    break
                flag = -1
                continue
            elif ch == "+":
                start = 1
                if flag != 1:
                    break
                flag = 0
                continue
            if ch.isdigit():
                start = 1
                res += ch
            else:
                break
        if flag == 0:
            flag = 1
        res = flag*int(res)
        if res > Max:
            res = Max
        elif res < Min:
            res = Min
        return res
        