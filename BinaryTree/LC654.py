def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
    if len(nums)<=0:
        return None
    maxnum = -1
    idx = -1
    for i,num in enumerate(nums):
        if num > maxnum:
            maxnum = num
            idx = i
    root = TreeNode(val=maxnum)
    root.left = self.constructMaximumBinaryTree(nums[:idx])
    root.right = self.constructMaximumBinaryTree(nums[idx+1:])
    return root