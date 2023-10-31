class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(idx,target,s,path):
            if s == target:
                res.append(path.copy())
            for i in range(idx,len(candidates)):
                if target < s + candidates[i]:
                    break
                if i> idx and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                s += candidates[i]
                backtrack(i+1,target,s,path)
                path.pop()
                s -= candidates[i]
        backtrack(0,target,0,[])
        return res
        