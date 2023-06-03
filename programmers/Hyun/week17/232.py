class MyQueue:

    def __init__(self):
        self.main = []
        self.tmp = []

    def push(self, x: int) -> None:
        self.tmp.append(x)

    def pop(self) -> int:

        if not self.main:
            while self.tmp:
                self.main.append(self.tmp.pop())

        return self.main.pop()

    def peek(self) -> int:
        if not self.main:
            while self.tmp:
                self.main.append(self.tmp.pop())

        return self.main[-1]

    def empty(self) -> bool:
        return (not self.main and not self.tmp)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
