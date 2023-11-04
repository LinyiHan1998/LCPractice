class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #print('-11'.isdigit())
        stk = []
        for ch in tokens:
            if ch.isdigit() or (ch[0] == '-' and len(ch)>1):
                stk.append(ch)
                continue
            a = int(stk.pop())
            b = int(stk.pop())
            if ch == '+':
                stk.append(int(a) + int(b))
            elif ch == '-':
                stk.append(int(b) - int(a))    
            elif ch =='/':
                stk.append(int(int(b)/int(a)))
                
            else:
                stk.append(int(a) * int(b))
            #print(stk)
        return int(stk[0])
        