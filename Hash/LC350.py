class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        need = defaultdict(int)
        for num in nums1:
            need[num] += 1
        res = []
        for num in nums2:
            if num in need and need[num]>0:
                need[num] -= 1
                res.append(num)
        return res