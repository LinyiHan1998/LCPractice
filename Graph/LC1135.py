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



import heapq
class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        class Prim:
            def __init__(self,graph):
                self.graph = graph
                self.pq = []
                self.inMST = [False]*len(graph)
                self.weightSum = 0

                self.inMST[0] = True
                self.cut(0)

                while self.pq:
                    _,edge = heapq.heappop(self.pq)
                    to = edge[1]
                    weight = edge[2]
                    if self.inMST[to]:
                        continue
                    self.weightSum += weight
                    self.inMST[to] = True
                    self.cut(to)
            def cut(self,s):
                for edge in self.graph[s]:
                    to = edge[1]
                    if self.inMST[to]:
                        continue
                    heapq.heappush(self.pq,(edge[2],edge))
            def allconnected(self):
                for i in range(len(self.inMST)):
                    if self.inMST[i] == False:
                        return False
                return True
        def BuildGraph(n,connections):
            graph = [[] for _ in range(n)]
            for conn in connections:
                u = conn[0]-1
                v = conn[1]-1
                weight = conn[2]
                graph[u].append([u,v,weight])
                graph[v].append([v,u,weight])
            return graph
        graph = BuildGraph(n,connections)
        prim = Prim(graph)

        if prim.allconnected():
            return prim.weightSum
        return -1

        