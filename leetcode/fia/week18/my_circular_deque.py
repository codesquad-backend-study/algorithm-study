class MyCircularDeque:

    def __init__(self, k: int):
        self.my_deque = [None] * k
        self.pointerA = 0
        self.pointerB = 0
        self.k = k

    def insertFront(self, value: int) -> bool:
        front = self.my_deque[(self.k + self.pointerA - 1) % self.k]
        if front is None:
            self.pointerA = (self.k + self.pointerA - 1) % self.k
            self.my_deque[self.pointerA] = value
            return True
        return False

    def insertLast(self, value: int) -> bool:
        last = self.my_deque[self.pointerB]
        if last is None:
            self.my_deque[self.pointerB] = value
            self.pointerB = (self.k + self.pointerB + 1) % self.k
            return True
        return False

    def deleteFront(self) -> bool:
        front = self.my_deque[self.pointerA]
        if front is not None:
            self.my_deque[self.pointerA] = None
            self.pointerA = (self.k + self.pointerA + 1) % self.k
            return True
        return False

    def deleteLast(self) -> bool:
        last = self.my_deque[(self.k + self.pointerB - 1) % self.k]
        if last is not None:
            self.pointerB = (self.k + self.pointerB - 1) % self.k
            self.my_deque[self.pointerB] = None
            return True
        return False

    def getFront(self) -> int:
        front = self.my_deque[self.pointerA]
        if front is not None:
            return self.my_deque[self.pointerA]
        return -1

    def getRear(self) -> int:
        rear_index = (self.k + self.pointerB - 1) % self.k
        if self.my_deque[rear_index] is not None:
            return self.my_deque[rear_index]
        return -1

    def isEmpty(self) -> bool:
        if self.pointerA == self.pointerB and self.my_deque[self.pointerA] is None:
            return True
        return False

    def isFull(self) -> bool:
        if self.pointerA == self.pointerB and self.my_deque[self.pointerA] is not None:
            return True
        return False

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
