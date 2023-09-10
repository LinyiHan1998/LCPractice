def helper(a):
    s = 0
    has0 = False
    for x in a:
        if x == 0:
            has0 = True
            s += 1
        else:
            s += x
    return (has0, s)

def solution(a, b):
    ahas0, sa = helper(a)
    bhas0, sb = helper(b)
    if sa == sb:
        return sa
    if sa < sb:
        return sb if ahas0 else -1
    else:
        return sa if bhas0 else -1
    
print(solution([1, 0, 2], [1, 3, 0, 0]))
print(solution([0, 0, 0], [1, 1]))

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums is None: return
        res,s =nums[0],nums[0]
        for i in nums[1:]:
            s += i
            s = max(s,i)
            res = max(s,res)
        return res