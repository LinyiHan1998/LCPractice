# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.maxSum = 0
        def dfs(node): #isvalid,min_val,max_val,curr_sum
            if node is None:
                return (True,float('inf'),float('-inf'),0)
            isvalid_left,min_val_left,max_val_left,curr_sum_left = dfs(node.left)
            isvalid_right,min_val_right,max_val_right,curr_sum_right = dfs(node.right)

            if isvalid_left and isvalid_right and max_val_left < node.val and node.val < min_val_right:
                curr_sum = curr_sum_left+curr_sum_right+node.val
                self.maxSum = max(self.maxSum,curr_sum)
                return (True,min(min_val_left,node.val),max(max_val_right,node.val),curr_sum)
            return (False,float('inf'),float('-inf'),0)
        dfs(root)
        return self.maxSum


        