import collections

class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = [None] * k
        self.size = k
        self.front = 0
        self.rear = 0

    def insertFront(self, value: int) -> bool:
        index = (self.front + self.size - 1) % self.size
        if self.isFull():
            return False
        else:
            self.deque[index] = value
            self.front = index
            return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.deque[self.rear] = value
            self.rear = (self.rear + 1) % self.size
            return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.deque[self.front] = None
            self.front = (self.front + 1) % self.size
            return True

    def deleteLast(self) -> bool:
        index = (self.rear + self.size - 1) % self.size
        if self.isEmpty():
            return False
        else:
            self.deque[index] = None
            self.rear = index
            return True

    def getFront(self) -> int:
        return self.deque[self.front] if self.deque[self.front] is not None else -1
    def getRear(self) -> int:
        return self.deque[self.rear - 1] if self.deque[self.rear - 1] is not None else -1
    def isEmpty(self) -> bool:
        return self.rear == self.front and self.deque[self.rear] is None
    def isFull(self) -> bool:
        return self.rear == self.front and self.deque[self.rear] is not None

