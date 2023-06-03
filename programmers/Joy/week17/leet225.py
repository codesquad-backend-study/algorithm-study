from collections import deque

class MyStack:

    def __init__(self):
        self.que = deque()

    def push(self, x: int) -> None:
        self.que.append(x)

    def pop(self) -> int:
        for i in range(len(self.que)-1):
            tmp = self.que.popleft()
            self.que.append(tmp)
        return self.que.popleft()

    def top(self) -> int:
        return self.que[-1]

    def empty(self) -> bool:
        return len(self.que) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()