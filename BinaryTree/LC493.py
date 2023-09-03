class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        sz = len(nums)
        arr = [[v,i] for i,v in enumerate(nums)]
        res = 0
        def merge_sort(arr,lo,hi):
            if hi - lo <= 1:
                return
            mid = lo + (hi-lo)//2
            merge_sort(arr,lo,mid)
            merge_sort(arr,mid,hi)
            merge(arr,lo,mid,hi)
        def merge(arr,lo,mid,hi):
            nonlocal res
            end = mid
            for i in range(lo,mid):
                while end < hi and arr[i][0] > 2*arr[end][0]:
                    end += 1
                res += end-mid
            i,j = lo,mid
            temp = []
            while i < mid and j < hi:
                if arr[i] < arr[j]:
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
        merge_sort(arr,0,sz)
        return res

