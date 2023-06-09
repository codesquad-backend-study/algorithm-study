class MyQueue:

    def __init__(self):
        self.stack = []
        self.tmp = []

    def push(self, x: int) -> None:
        for i in range(len(self.stack)):
            self.tmp.append(self.stack.pop())
        self.stack.append(x)
        for i in range(len(self.tmp)):
            self.stack.append(self.tmp.pop())

    def pop(self) -> int: # 꺼내고 삭제
        return self.stack.pop()

    def peek(self) -> int: # 꺼내기만
        return self.stack[-1]

    def empty(self) -> bool:
        return not self.stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()