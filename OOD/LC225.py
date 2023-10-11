class MyStack:

    def __init__(self):
        self.queue = deque()
        self.top_elem = 0
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.top_elem = x

    def pop(self) -> int:
        size = len(self.queue)
        while size > 2:
            self.queue.append(self.queue.popleft())
            size -= 1
        self.top_elem = self.queue[0]
        self.queue.append(self.queue.popleft())
        return self.queue.popleft()
        

    def top(self) -> int:
        return self.top_elem
        

    def empty(self) -> bool:
        if len(self.queue) == 0:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()