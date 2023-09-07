class Solution:
    def __init__(self):
        self.memo = []
    def numTrees(self, n: int) -> int:
        self.memo = [[0] * (n+1) for _ in range(n+1)]
        def count(lo,hi):
            if lo > hi : return 1
            if self.memo[lo][hi] != 0:
                return self.memo[lo][hi]
            res = 0
            for i in range(lo,hi+1):
                left = count(lo,i-1)
                right = count(i+1,hi)
                res += left * right
            self.memo[lo][hi] = res
            return res
        return count(1,n)