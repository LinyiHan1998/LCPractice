class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        class UF:
            def __init__(self,n):
                self.count = n
                self.parent = [i for i in range(n)]
            def find(self,p):
                if p != self.parent[p]:
                    self.parent[p] = self.find(self.parent[p])
                return self.parent[p]
            def union(self,p,q):
                rootp,rootq = self.find(p),self.find(q)
                if rootp == rootq: return
                self.parent[rootp] = rootq
                self.count -= 1
        uf = UF(n)
        for e in edges:
            if uf.find(e[0]) == uf.find(e[1]):
                return False
            uf.union(e[0],e[1])
        return uf.count == 1
        