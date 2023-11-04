class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stk = [0]
        memo = [-1] * len(nums2)
        answer = [-1] * len(nums1)
        dic = defaultdict(int)
        for i,num in enumerate(nums2):
            dic[num] = i
            if num < nums2[stk[-1]]:
                stk.append(i)
            else:
                while stk and nums2[stk[-1]] < num and memo[stk[-1]] == -1:
                    memo[stk[-1]] = num
                    stk.pop()
                stk.append(i)
        for i,num in enumerate(nums1):
            answer[i] = memo[dic[num]]
        return answer

