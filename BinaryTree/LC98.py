class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node,min_val,max_val):
            if node is None:
                return True
            if node.val < max_val and node.val>min_val:
                return helper(node.left,min_val,node.val) and helper(node.right,node.val,max_val)
        
        return helper(root,-inf,inf)