from collections import deque
class solution:
    def __init__(self) -> None:
        self.ok = True
        self.color = []
        self.visited = []
    
    def isBipartite(self,graph):
        n = len(graph)
        self.visited = [False] * n
        self.color = [False] * n

        for v in range(n):
            if not self.visited[v]:
                self.BFS(graph,v)
                
        return self.ok

    def BFS(self,graph,start):
        if not self.ok:
            return
        
        queue = deque()
        queue.append(start)
        self.visited[start] = True

        while queue and self.ok:
            v = queue.popleft()
            for w in graph[v]:
                if self.visited[w]:
                    if self.color[w] == self.color[v]:
                        self.ok = False
                        return
                else:
                    self.visited[w] = True
                    self.color[w] = not self.color[v]
                    queue.append(w)

    # def isBipartite(self,graph):
    #     n = len(graph)
    #     self.color = [False] * n
    #     self.visited = [False] * n

    #     for v in range(n):
    #         if not self.visited[v]:
    #             self.traverse(graph,v)
    #             if self.ok == False:
    #                 break
    #     return self.ok
    # def traverse(self,graph,v):
    #     if self.ok == False:
    #         return
    #     self.visited[v] = True
    #     for w in graph[v]:
    #         if self.visited[w]:
    #             if self.color[w] == self.color[v]:
    #                 self.ok = False
    #                 return
    #         else:
    #             self.color[w] = not self.color[v]
    #             self.traverse(graph,w)

