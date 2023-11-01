class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backtracking(idx,k,path):
            if len(path) == k:
                if sum(path) == n:
                    res.append(path.copy())
                return
            for i in range(idx+1,10):
                path.append(i)
                backtracking(i,k,path)
                path.pop()
        for i in range(1,10):
            path = [i]
            backtracking(i,k,path)
        return res

        