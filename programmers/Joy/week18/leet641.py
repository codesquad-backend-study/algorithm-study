class MyCircularDeque:

    def __init__(self, k: int):
        self.circularDeque = []
        self.k = k

    def insertFront(self, value: int) -> bool:
        if len(self.circularDeque) >= self.k:
            return False
        tmp = [value]
        self.circularDeque = tmp + self.circularDeque
        return True

    def insertLast(self, value: int) -> bool:
        if len(self.circularDeque) >= self.k:
            return False
        self.circularDeque.append(value)
        return True

    def deleteFront(self) -> bool:
        if len(self.circularDeque) == 0:
            return False
        self.circularDeque = self.circularDeque[1:]
        return True

    def deleteLast(self) -> bool:
        if len(self.circularDeque) == 0:
            return False
        self.circularDeque.pop()
        return True

    def getFront(self) -> int:
        if len(self.circularDeque) == 0:
            return -1
        return self.circularDeque[0]

    def getRear(self) -> int:
        if len(self.circularDeque) == 0:
            return -1
        tmp =  self.circularDeque.pop()
        self.circularDeque.append(tmp)
        return tmp

    def isEmpty(self) -> bool:
        return not self.circularDeque


    def isFull(self) -> bool:
        return len(self.circularDeque) == self.k



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