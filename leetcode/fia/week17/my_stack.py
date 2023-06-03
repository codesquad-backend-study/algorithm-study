import collections


class MyStack:
    deque = None

    def __init__(self):
        self.deque = collections.deque()

    def push(self, x: int) -> None:
        self.deque.append(x)

    def pop(self) -> int:
        return self.deque.pop()

    def top(self) -> int:
        temp = self.deque.pop()
        self.deque.append(temp)
        return temp

    def empty(self) -> bool:
        return len(self.deque) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
