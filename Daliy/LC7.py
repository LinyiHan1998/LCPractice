class Solution:
    def reverse(self, x: int) -> int:
        tmp = ''
        if x < 0:
            tmp = '-'+str(-1*x)[::-1]
        else:
            tmp = str(x)[::-1]
        res = int(tmp)

        return res if res<=(2**31-1) and res>=-1* 2**31 else 0

        