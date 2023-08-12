import collections
class Solution:
    def timeTaken(self, arrivals: list[int], states: list[int]) -> list[int]:
        n = len(arrivals)
        answer = [0] * n

        time, direction = 0, 1
        queues = [collections.deque(), collections.deque()]

        def exhaust_until(end_time: int=2*10**5) -> None:
            nonlocal time, direction
            while end_time > time and any(queues):
                if not queues[direction]:
                    direction ^= 1
                answer[queues[direction].popleft()] = time
                time += 1

        for index, (arrival, state) in enumerate(zip(arrivals, states)):
            exhaust_until(arrival)
            if arrival > time:
                time, direction = arrival, 1
            queues[state].append(index)

        exhaust_until()
        return answer
