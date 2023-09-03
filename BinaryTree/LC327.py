class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        sz = len(nums)
        res = 0
        pre_sum = [0]*(sz+1)
        for i in range(1,sz+1):
            pre_sum[i] = nums[i-1]+pre_sum[i-1]
        def merge_sort(arr,lo,hi):
            if hi-lo<=1:
                return
            mid = lo + (hi-lo)//2
            merge_sort(arr,lo,mid)
            merge_sort(arr,mid,hi)
            merge(arr,lo,mid,hi)
        
        def merge(arr,lo,mid,hi):
            nonlocal res
            l,r = mid,mid
            for i in range(lo,mid):
                while l < hi and arr[l] - arr[i] <lower:
                    l += 1
                while r < hi and arr[r] - arr[i] <= upper:
                    r += 1
                res += r-l
            i,j = lo,mid
            temp = []
            while i<mid and j<hi:
                if arr[i]<arr[j]:
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1
            while i<mid:
                temp.append(arr[i])
                i += 1
            while j < hi:
                temp.append(arr[j])
                j += 1
            for i in range(lo,hi):
                arr[i] = temp[i-lo]
        merge_sort(pre_sum,0,sz+1)
        return res
        