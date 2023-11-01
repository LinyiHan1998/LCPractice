# import heapq
# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         graph = defaultdict(list)
#         def buildgraph(tickets):
#             for departure,terminal in tickets:
#                 graph[departure].append(terminal)
#             for airport in graph:
#                 graph[airport].sort()
#         buildgraph(tickets)
#         #print(graph)
#         path = ['JFK']
#         def backtrack(depart,path,cnt):
#             if cnt == len(tickets):
#                 return True
#             for i,terminal in enumerate(graph[depart]):
#                 #terminal = heapq.heappop(graph[depart])
#                 path.append(terminal)
#                 graph[depart].pop(i)
#                 flag = backtrack(terminal,path,cnt+1)
#                 if flag:
#                     return True
#                 path.pop()
#                 graph[depart].insert(i,terminal)
#         backtrack('JFK',path,0)
#         return path
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets):
        targets = defaultdict(list)  # 创建默认字典，用于存储机场映射关系
        for ticket in tickets:
            targets[ticket[0]].append(ticket[1])  # 将机票输入到字典中
        
        for key in targets:
            targets[key].sort(reverse=True)  # 对到达机场列表进行字母逆序排序
        
        result = []
        self.backtracking("JFK", targets, result)  # 调用回溯函数开始搜索路径
        return result[::-1]  # 返回逆序的行程路径
    
    def backtracking(self, airport, targets, result):
        while targets[airport]:  # 当机场还有可到达的机场时
            next_airport = targets[airport].pop()  # 弹出下一个机场
            self.backtracking(next_airport, targets, result)  # 递归调用回溯函数进行深度优先搜索
        result.append(airport)  # 将当前机场添加到行程路径中