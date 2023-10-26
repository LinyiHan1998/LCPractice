class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        res = 0
        dic = {}
        for i in range(len(fruits)):
            if fruits[i] in dic:
                dic[fruits[i]] += 1
                res = max(res,i-l+1)
                continue
            if len(dic)<2:
                dic[fruits[i]] = 1
                res = max(res,i-l+1)
                continue
            while fruits[l] != fruits[i] and len(dic)==2:
                dic[fruits[l]] -= 1
                if dic[fruits[l]] == 0:
                    del dic[fruits[l]]
                l += 1
            dic[fruits[i]] = 1
            res = max(res,i-l+1)
        return res
        