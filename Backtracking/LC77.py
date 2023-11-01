class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtracking(idx,k,path):
            if len(path) == k:
                res.append(path.copy())
                return
            for i in range(idx+1,n+1):
                path.append(i)
                backtracking(i,k,path)
                path.pop()
        for i in range(1,n+1):
            path = [i]
            backtracking(i,k,path)
        return list(res)

        