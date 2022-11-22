class MyQueue:

    def __init__(self):
        self.que = []

    def push(self, x: int) -> None:
        self.que = [x] + self.que

    def pop(self) -> int:
        x = self.que.pop()
        return x

    def peek(self) -> int:
        return self.que[-1]

    def empty(self) -> bool:
        return not self.que


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()