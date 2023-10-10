class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
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
                if rootp == rootq:return
                self.parent[rootp] = rootq
                self.count -= 1
        cnt = len(points)
        edges = []
        for i in range(cnt):
            xi,yi = points[i][0],points[i][1]
            for j in range(i+1,cnt):
                xj,yj = points[j][0],points[j][1]
                edges.append([i,j,abs(xi-xj)+abs(yi-yj)])
        edges.sort(key=lambda x:x[2])

        uf = UF(cnt)
        res = 0
        for e in edges:
            if uf.count == 1:break
            x,y = e[0],e[1]
            if uf.find(x) == uf.find(y):
                continue
            uf.union(x,y)
            res += e[2]
        return res if uf.count==1 else -1


                

                