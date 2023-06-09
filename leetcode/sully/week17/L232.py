import collections


class MyQueue:

    def __init__(self):
        self.dq = collections.deque()

    def push(self, x: int) -> None:
        self.dq.appendleft(x)

        for _ in range(len(self.dq)):
            pop = self.dq.pop()
            self.dq.appendleft(pop)

    def pop(self) -> int:
        return self.dq.pop()

    def peek(self) -> int:
        return self.dq[-1]

    def empty(self) -> bool:
        return len(self.dq) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
