class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = []
        self.maxSize = k

    def enQueue(self, value: int) -> bool:
        if len(self.queue) < self.maxSize:
            self.queue.append(value)
            return True
        else:
            return False
    def deQueue(self) -> bool:
        if self.queue:
            del self.queue[0]
            return True
        else:
            return False

    def Front(self) -> int:
        if self.queue:
            return self.queue[0]
        else:
            return -1

    def Rear(self) -> int:
        if self.queue:
            return self.queue[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return not self.queue

    def isFull(self) -> bool:
        return len(self.queue) == self.maxSize
