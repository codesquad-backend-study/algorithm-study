class MyCircularQueue:

    def __init__(self, k: int):
        self.front = self.rear = 0
        self.q = [None] * k
        self.max_len = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.q[self.rear] = value
        self.rear = (self.rear + 1) % self.max_len
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.q[self.front] = None
        self.front = (self.front + 1) % self.max_len
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.q[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.q[self.rear - 1]

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.q[self.front] is None

    def isFull(self) -> bool:
        return self.front == self.rear and self.q[self.front] is not None

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
