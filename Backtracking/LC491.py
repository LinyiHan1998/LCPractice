class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        res = []
        def backtrack(idx,path):
            if len(path)>=2:
                #mem.add(set(path.copy()))
                res.append(path.copy())
            uset = set()
            for i in range(idx,len(nums)):
                if (path and nums[i]<path[-1]) or nums[i] in uset:
                    continue
                uset.add(nums[i])
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()
        backtrack(0,[])
        return res