class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sz = len(nums)
        arr = [[v,i] for i,v in enumerate(nums)]
        res = [0]*sz
        def merge_sort(arr,lo,hi):
            if hi - lo <= 1: return
            mid = lo + (hi-lo)//2
            merge_sort(arr,lo,mid)
            merge_sort(arr,mid,hi)
            merge(arr,lo,mid,hi)
        def merge(arr,lo,mid,hi):
            i,j=lo,mid
            temp = []
            while i<mid and j < hi:
                if arr[i][0] <= arr[j][0]:
                    res[arr[i][1]] += j - mid
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1
            while i<mid:
                res[arr[i][1]] += j - mid
                temp.append(arr[i])
                i += 1
            while j < hi:
                temp.append(arr[j])
                j += 1
            for i in range(lo,hi):
                arr[i] = temp[i-lo]
        merge_sort(arr,0,sz)
        return res 
        