class Solution:
    def operator(self,x,y,op):
        if op == '+':
            return x
        if op == '-':
            return -x
        if op == '*':
            return x*y
        return int(x/y)
    def calculate(self, s: str) -> int:
        stk = []
        curr = 0
        pre_op = '+'
        s += '#'

        for c in s:
            if c.isdigit():
                curr = curr*10+int(c)
            elif c == '(':
                stk.append(pre_op)
                pre_op = '+'
            else:
                if pre_op == '*' or pre_op == '/':
                    stk.append(self.operator(stk.pop(),curr,pre_op))
                else:
                    stk.append(self.operator(curr,0,pre_op))
                curr = 0
                pre_op = c
                if c == ')':
                    while type(stk[-1]) == int:
                        curr += stk.pop()
                    pre_op = stk.pop()
        return sum(stk)
        