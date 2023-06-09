from collections import deque

class MyStack:

    def __init__(self):
        self.deque = deque()
        
    def push(self, x: int) -> None:
        self.deque.append(x)

    def pop(self) -> int:
        answer = deque()
        for _ in range(len(self.deque) - 1):
            temp = self.deque.popleft()
            answer.append(temp)
        result = self.deque.popleft()
        self.deque = answer
        return result

        
    def top(self) -> int:
        copy = self.deque.copy()
        for _ in range(len(self.deque) - 1):
            copy.popleft()
        return copy.popleft()


    def empty(self) -> bool:
        return not self.deque
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
