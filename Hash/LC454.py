class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        dic = defaultdict(int)
        for i in range(n):
            for j in range(n):
                dic[0 - nums1[i] - nums2[j]] += 1
        cnt = 0
        for i in range(n):
            for j in range(n):
                if nums3[i]+nums4[j] in dic:
                    cnt += dic[nums3[i]+nums4[j]]
        return cnt
        