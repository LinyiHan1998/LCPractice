class Solution:
    class UF:
        def __init__(self,n):
            self.parent = [i for i in range(n)]
        def find(self,x):
            if x != self.parent[x]:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        def union(self,child,parent):
            if self.find(child) != self.find(parent):
                self.parent[self.find(child)] = self.find(parent)

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = self.UF(len(edges))
        res = [0,0]
        for u,v in edges:

            if uf.find(u-1) == uf.find(v-1):
                res = [u,v]
            else:
                uf.union(u-1,v-1)
        return res
        