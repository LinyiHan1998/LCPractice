class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        s = []
        for i in range(n-1,-1,-1):
            cnt = 0
            while s and temperatures[i] >= temperatures[s[-1]]:
                s.pop()
            res[i] = s[-1]-i if s else 0
            s.append(i)
        return res
        