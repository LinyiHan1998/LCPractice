class MyQueue:

    def __init__(self):
        self.sk = []
        self.sk_front = []
        

    def push(self, x: int) -> None:
        self.sk.append(x)
        

    def pop(self) -> int:
        self.peek()
        return self.sk_front.pop()
        

    def peek(self) -> int:
        if len(self.sk_front) == 0:
            while self.sk:
                self.sk_front.append(self.sk.pop())
        return self.sk_front[-1]

    def empty(self) -> bool:
        if len(self.sk)+len(self.sk_front) == 0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()