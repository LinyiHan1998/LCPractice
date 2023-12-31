class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtracking(left,right,s):
            if len(s) == n*2:
                res.append(s)
                return
            if left < n:
                backtracking(left+1,right,s+'(')
            if right<left:
                backtracking(left,right+1,s+')')
        backtracking(0,0,'')
        return res
        