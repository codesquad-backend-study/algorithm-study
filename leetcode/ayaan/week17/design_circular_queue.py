class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = [None] * k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.queue[self.rear] is not None:
            return False
        else:
            self.queue[self.rear] = value
            self.rear = (self.rear + 1) % self.size
            return True

    def deQueue(self) -> bool:
        if self.queue[self.front] is None:
            return False
        else:
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
            return True

    def Front(self) -> int:
        return -1 if self.queue[self.front] is None else self.queue[self.front]

    def Rear(self) -> int:
        return -1 if self.queue[self.rear-1] is None else self.queue[self.rear-1]

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.queue[self.front] is None

    def isFull(self) -> bool:
        return self.front == self.rear and self.queue[self.front] is not None
