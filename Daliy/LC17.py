class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res = []
        def traverse(tmp,index):
            if index == len(digits):
                return tmp
            for ch in letters[digits[index]]:
                tmp += ch
                a = traverse(tmp,index+1)
                if a:
                    res.append(a)
                tmp = tmp[0:-1]
        traverse('',0)
        return res
        