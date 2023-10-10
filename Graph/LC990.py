class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        class UF:
            def __init__(self):
                self.count = 26
                self.parent = [i for i in range(26)]
            def find(self,ch):
                if ch != self.parent[ch]:
                    self.parent[ch] = self.find(self.parent[ch])
                return self.parent[ch]
            def union(self,ch1,ch2):
                root1,root2 = self.find(ch1),self.find(ch2)
                if root1 == root2:
                    return
                self.parent[root1] = root2
                self.count -= 1
        uf = UF()
        for eq in equations:
            if eq[1] == '=':
                uf.union(ord(eq[0])-ord('a'),ord(eq[3])-ord('a'))
        for eq in equations:
            if eq[1] == '!':
                if uf.find(ord(eq[0])-ord('a')) == uf.find(ord(eq[3])-ord('a')):
                    return False
        return True
        