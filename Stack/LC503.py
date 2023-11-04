class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        newnums = nums + nums
        stk = [0]
        res = [-1] * len(nums)

        for i,num in enumerate(newnums):
            if num < newnums[stk[-1]]:
                stk.append(i)
                continue
            while stk and newnums[stk[-1]] < num:
                if res[stk[-1]%len(nums)] == -1:
                    res[stk[-1]%len(nums)] = num
                stk.pop()
            stk.append(i)
        return res
        