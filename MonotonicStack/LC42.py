class Solution:
    def trap(self, height: List[int]) -> int:
        stk = [0]
        size = 0
        #res = 0
        for i,h in enumerate(height):
            if i < 1:
                continue
            if h < height[stk[-1]]:
                stk.append(i)
            else:
                while stk and h > height[stk[-1]]:
                    mid = stk.pop()
                    if stk:
                        left = stk[-1]
                        tall = min(h,height[left]) - height[mid]
                        w = i - left - 1
                        size += tall * w
                stk.append(i)
                #res = max(size,res)
                #size = 0
        return size