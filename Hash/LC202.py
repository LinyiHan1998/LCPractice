class Solution:
    def isHappy(self, n: int) -> bool:
        occurred = set()
        while n!= 1:
            
            tmp = 0
            while n:
                tmp += (n%10)**2
                n //= 10
            n = tmp
            if n in occurred:
                return False
            occurred.add(n)
        return True
        