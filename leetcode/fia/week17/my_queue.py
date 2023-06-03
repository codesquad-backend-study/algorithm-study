class MyQueue:

    def __init__(self):
        self.stack = []
        self.temp = []

    def push(self, x: int) -> None:
        for _ in range(len(self.stack)):
            self.temp.append(self.stack.pop())
        self.temp.append(x)
        for _ in range(len(self.temp)):
            self.stack.append(self.temp.pop())

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[len(self.stack) - 1]

    def empty(self) -> bool:
        return not self.stack
