class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(idx,path,visited):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if visited[i]:
                    continue
                path.append(nums[i])
                visited[i] = True
                backtrack(i,path,visited)
                visited[i] = False
                path.pop()
        backtrack(0,[],[False]*len(nums))
        return res
            