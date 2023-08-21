def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
    n = 0
    for t in trips:
        n = max(n,t[2])
    stops = [0] * n
    diff = [0] * n
    for t in trips:
        diff[t[1]] += t[0]
        if t[2] < n:
            diff[t[2]] -= t[0]
    stops[0] = diff[0]
    for i in range(1,n):
        stops[i] = stops[i-1] + diff[i]
    for s in stops:
        if s > capacity:
            return False
    return True