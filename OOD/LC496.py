class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def greater(nums):
            n = len(nums)
            res = [0] * n
            s = []
            
            for i in range(n-1,-1,-1):
                while s and nums[i]>=s[-1]:
                    s.pop()
                res[i] = s[-1] if s else -1
                s.append(nums[i])
            return res
        
        greaterNums = greater(nums2)
        dictNums = {}
        for i in range(len(nums2)):
            dictNums[nums2[i]] = greaterNums[i]
        ret = []
        for i in range(len(nums1)):
            ret.append(dictNums[nums1[i]])
        return ret

        