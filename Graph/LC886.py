class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        visited = [False] * (n+1)
        color = [False] * (n+1)
        table = [[] for _ in range(n+1)]
        for dis in dislikes:
            v, w =dis[0],dis[1]
            table[dis[0]].append(dis[1])
            table[dis[1]].append(dis[0])
        res = True
        def BFS(table,start):
            nonlocal res
            visited[start] = True
            q = deque()
            q.append(start)

            while q:
                root = q.pop()
                for node in table[root]:
                    if visited[node] == False:
                        color[node] = not color[root]
                        visited[node] = True
                        q.append(node)
                    else:
                        if color[node] == color[root]:
                            res = False
                            return res
        for i in range(n):
            if visited[i] == False:
                BFS(table,i)
        return res
        # def DFS(idx):
        #     nonlocal res
        #     visited[idx] = True
        #     for node in table[idx]:
        #         if visited[node] == False:
        #             color[node] = not color[idx]
        #             DFS(node)
        #         else:
        #             if color[node] == color[idx]:
        #                 res = False
        #                 return res
        # for i in range(1,n+1):
        #     DFS(i)
        # return res

