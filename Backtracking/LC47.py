class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False]*len(nums)
        def backtrack(idx,path,visited):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            uset = set()
            for i in range(len(nums)):
                if visited[i] or nums[i] in uset:
                    continue
                uset.add(nums[i])
                path.append(nums[i])
                visited[i] = True
                backtrack(i,path,visited)
                visited[i] = False
                path.pop()
        backtrack(0,[],visited)
        return res