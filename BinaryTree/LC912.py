#merge sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.sort(nums,0,len(nums)-1)
    
    def sort(self,nums,lo,hi):
        if lo == hi:
            return [nums[lo]]
        mid = lo + (hi-lo)//2
        left = self.sort(nums,lo,mid)
        right = self.sort(nums,mid+1,hi)
        return self.merge(left,right)

    def merge(self,left,right):
        res = []
        l,r=0,0
        while l<len(left) and r<len(right):
            if left[l]<right[r]:
                res.append(left[l])
                l+=1
            else:
                res.append(right[r])
                r+=1
        if l<len(left):
            res.extend(left[l:])
        elif r<len(right):
            res.extend(right[r:])
        
        return res
# quick sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.sort(nums,0,len(nums)-1)
        return nums
    
    def partition(self,nums,lo,hi):
        pivot = nums[lo]
        l,r = lo + 1,hi
        while  l <= r:
            while l < hi and nums[l] <= pivot:
                l += 1
            while r > lo and nums[r] > pivot:
                r -= 1
            if l >= r:
                break
            nums[l],nums[r] = nums[r],nums[l]
        nums[lo],nums[r] = nums[r],nums[lo]
        return r
        
    def sort(self,nums,lo,hi):
        if lo >= hi:
            return
        idx = self.partition(nums,lo,hi)
        self.sort(nums,lo,idx-1)
        self.sort(nums,idx+1,hi)
        return
    def shuffle(self,nums):
        pass
        