class Solution:
    def __init__(self):
        self.res = []
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path = []
        def traverse(graph,startidx,path):
            path.append(startidx)
            if startidx == len(graph)-1:
                self.res.append(path.copy())

            for idx in graph[startidx]:
                traverse(graph,idx,path)
            path.pop()
        traverse(graph,0,path)
        return self.res

        