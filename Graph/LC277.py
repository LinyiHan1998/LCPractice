# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        q = []
        for i in range(n):
            q.append(i)
        while len(q)>=2:
            cand = q.pop(0)
            other = q.pop(0)
            if knows(cand,other) or not knows(other,cand):
                q.append(other)
            else:
                q.append(cand)
        cand = q.pop(0)
        for i in range(n):
            if i == cand:
                continue
            if knows(cand,i) or not knows(i,cand):
                return -1
        return cand
        