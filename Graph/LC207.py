class Solution:
    def buildGraph(self,numCourses,prerequisites):
        graph = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            from_,to_ = pre[0],pre[1]
            graph[from_].append(to_)
        return graph
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.buildGraph(numCourses,prerequisites)
        visited = [0] * numCourses
        onpath = [0] * numCourses
        has_cycle = 0
        def traverse(graph,s):
            nonlocal has_cycle
            if onpath[s] != 0:
                has_cycle = 1
                return 
            if visited[s] != 0:
                #has_cycle = 1
                return 
            visited[s] = 1
            onpath[s] = 1
            for node in graph[s]:
                traverse(graph,node)
            onpath[s] = 0
        for i in range(numCourses):
            traverse(graph,i)
        return True if has_cycle == 0 else False
    

from collections import deque
class Solution:
    def canFinishBFS(self,numCourses,prerequisites):
        graph = [[]*numCourses for _ in range(numCourses)]
        indegree = [0]*numCourses

        for edge in prerequisites:
            graph[edge[1]].append(edge[0])
            indegree[edge[0]] += 1
        queue = deque()
        count = 0

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            root = queue.popleft()
            count += 1
            for edge in graph[root]:
                indegree[edge] -= 1
                if indegree[edge] == 0:
                    queue.append(edge)
        return count == numCourses