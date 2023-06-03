class MyQueue:

    def __init__(self):
        self.que = []
        self.temp = []
        
    def push(self, x: int) -> None:
        self.que.append(x)
        
    def pop(self) -> int:
        for _ in range(len(self.que) - 1):
            number = self.que.pop()
            self.temp.append(number)
        answer =  self.que.pop()
        for _ in range(len(self.temp)):
            number = self.temp.pop()
            self.que.append(number)
        return answer

    def peek(self) -> int:
        for _ in range(len(self.que) - 1):
            number = self.que.pop()
            self.temp.append(number)
        answer =  self.que.pop()
        self.que.append(answer)
        for _ in range(len(self.temp)):
            number = self.temp.pop()
            self.que.append(number)
        return answer

    def empty(self) -> bool:
        return not self.que
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
