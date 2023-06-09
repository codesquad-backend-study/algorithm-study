import collections


class MyStack:

    def __init__(self):
        self.deque = collections.deque()

    def push(self, x: int) -> None:
        self.deque.append(x)

        for _ in range(len(self.deque) - 1):
            popleft = self.deque.popleft()
            self.deque.append(popleft)

    def pop(self) -> int:
        return self.deque.popleft()

    def top(self) -> int:
        return self.deque[0]

    def empty(self) -> bool:
        if not self.deque:
            return True

        return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
