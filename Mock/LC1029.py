class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = sorted( costs,key = lambda x : x[0]-x[1])
        sz = len(costs)
        n = sz//2
        cost = sum(c[0] for c in costs[:n]) + sum(c[1] for c in costs[n:])
        return cost
        