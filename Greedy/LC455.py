class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cnt = 0
        left,right = 0,0
        while left<len(g) and right<len(s):
            if g[left] >s[right]:
                right += 1
            else:
                left += 1
                right += 1
                cnt += 1
        return cnt

        