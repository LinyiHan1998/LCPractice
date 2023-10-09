class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        class UnionFind:
            def __init__(self,n):
                self.count = n
                self.rank = [0] * n
                self.parent = [i for i in range(n)]
            def find(self,p):
                while p != self.parent[p]:
                    self.parent[p] = self.parent[self.parent[p]]
                    p = self.parent[p]
                return p
            def union(self,p,q):
                rootP,rootQ = self.find(p),self.find(q)
                if rootP == rootQ:
                    return
                if self.rank[rootP] < self.rank[rootQ]:
                    self.parent[rootP] = rootQ
                elif self.rank[rootQ] < self.rank[rootP]:
                    self.parent[rootQ] = rootP
                else:
                    self.parent[rootQ] = rootP
                    self.rank[rootP] += 1
                self.count -= 1
        uf = UnionFind(n)
        for e in edges:
            uf.union(e[0],e[1])
        return uf.count


                
        