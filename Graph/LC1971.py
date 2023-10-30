class Solution:
    class UF:
        def __init__(self,n):
            self.father = [i for i in range(n)]
            self.rank = [1 for i in range(n)]
        def find(self,root):
            if self.father[root] != root:
                self.father[root] = self.find(self.father[root])
            return self.father[root]
        def union(self,u,v):
            if self.find(u) == self.find(v):
                return
            self.father[self.find(u)] = self.find(v)
            return
            # r1 = self.find(u)
            # r2 = self.find(v)
            # if r1 != r2:
            #     if self.rank[r1] < self.rank[r2]:
            #         self.father[r2] = r1
            #     elif self.rank[r2] < self.rank[r1]:
            #         self.father[r1] = r2
            #     else:
            #         self.rank[r1] += 1
            #         self.father[r2] = r1
                
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        uf = self.UF(n)
        for edge in edges:
            uf.union(edge[0],edge[1])
        return uf.find(source)==uf.find(destination)