class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows>=len(s):
            return s
        res = ['']*numRows
        step = 1
        row = 0
        for i in range(len(s)):
            
            res[row]+=s[i]
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step
        return ''.join(res)

        