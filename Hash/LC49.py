class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for ch in strs:
            tmp = ''.join(sorted(ch))
            if tmp not in dic:
                dic[tmp]=[]
            dic[tmp].append(ch)
        return list(dic.values())