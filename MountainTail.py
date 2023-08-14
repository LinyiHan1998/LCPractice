class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        ans = [None for _ in range(len(arrival))]
        prev = None  # previous action, either 0 (enter), 1 (exit) or None
        enterq = deque()
        exitq = deque()
        time = arrival[0]
        i = 0
        while i < len(arrival) or enterq or exitq:
            while i < len(arrival) and arrival[i] <= time:
                if state[i] == 0:
                    enterq.append(i)
                else:
                    exitq.append(i)
                i += 1
            if enterq and (prev == 0 or not exitq):
                person = enterq.popleft()
                ans[person] = time
                prev = 0
                time += 1
            elif exitq:
                person = exitq.popleft()
                ans[person] = time
                prev = 1
                time += 1
            else:
                if i < len(arrival):
                    time = arrival[i]
                prev = None
        return ans