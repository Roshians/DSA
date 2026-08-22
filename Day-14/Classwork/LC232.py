class MyQueue:

    def __init__(self):
        self.queue = []
        self.top = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        self.peek()
        return self.top.pop()
        
    def peek(self) -> int:
        if not self.top:
            while self.queue:
                self.top.append(self.queue.pop())
        return self.top[-1]
    def empty(self) -> bool:
        return not(self.queue) and not(self.top)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()