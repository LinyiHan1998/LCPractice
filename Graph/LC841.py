# class Solution:
#     def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
#         n = len(rooms)
#         visited = [False] * n
#         def dfs(idx):
#             nonlocal size
#             if visited[idx]:
#                 return
#             visited[idx] = True
#             size += 1
#             for room in rooms[idx]:
#                 dfs(room)
#         size = 0
#         dfs(0)
#         return size == n
            
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False]*n
        que = deque()
        que.append(0)
        sz = 1
        visited[0] = True
        while que:
            idx = que.popleft()
            for room in rooms[idx]:
                if visited[room]:
                    continue
                sz += 1
                visited[room] = True
                que.append(room)
        print(sz)
        return sz == n