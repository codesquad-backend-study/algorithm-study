import collections


class MyStack:

    def __init__(self):
        self.deque = collections.deque()

    def push(self, x: int) -> None:
        self.deque.append(x)

    def pop(self) -> int:
        return self.deque.pop()

    def top(self) -> int:
        return self.deque[-1]

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
