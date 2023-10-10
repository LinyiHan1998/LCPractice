class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
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
                if rootp == rootq:
                    return
                self.parent[rootp] = rootq
                self.count -= 1
        uf = UF(n)
        res = 0
        connections = sorted(connections,key=lambda x: x[2])
        for conn in connections:
            x = conn[0]-1
            y = conn[1]-1
            if uf.find(x) == uf.find(y):
                continue
            uf.union(x,y)
            res += conn[2]
        return res if uf.count == 1 else -1
        