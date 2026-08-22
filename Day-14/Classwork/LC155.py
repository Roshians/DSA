class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if len(self.minVal) == 0 or value <= self.minVal[-1]:
            self.minVal.append(value)

    def pop(self) -> None:
        rem = self.stack.pop()
        if rem == self.minVal[-1]:
            self.minVal.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVal[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()