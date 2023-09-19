class Solution:
    def buildGraph(self,numCourses,prerequisites):
        graph = [[] * numCourses for _ in range(numCourses)]
        for pre in prerequisites:
            from_,to_ = pre[0],pre[1]
            graph[to_].append(from_)
        return graph
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = self.buildGraph(numCourses,prerequisites)
        visited = [0] * numCourses
        onpath = [0] * numCourses
        res = []
        has_cycle = 0
        def traverse(graph,s):
            nonlocal has_cycle
            if onpath[s] != 0:
                has_cycle = 1
                return 
            if visited[s] != 0:
                return
            onpath[s] = 1
            visited[s] = 1
            for node in graph[s]:
                traverse(graph,node)
            res.append(s)
            onpath[s] = 0
        for i in range(numCourses):
            traverse(graph,i)
        if has_cycle == 1: 
            return []
        return res[::-1]

        