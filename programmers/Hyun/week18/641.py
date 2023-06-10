class MyCircularDeque:

    def __init__(self, k: int):  # 초기 사이즈 설정
        self.q = [None] * k
        self.front = self.rear = 0
        self.max_size = k

    def insertFront(self, value: int) -> bool:  # 앞에 아이템 넣고 성공 시 true 반환
        next_front_idx = (self.max_size + self.front - 1) % self.max_size
        if self.isFull():
            return False

        self.q[next_front_idx] = value
        self.front = next_front_idx
        return True

    def insertLast(self, value: int) -> bool:  # 뒤에 아이템 넣고 성공 시 true 반환
        if self.isFull():
            return False

        self.q[self.rear] = value
        self.rear = (self.rear + 1) % self.max_size
        return True

    def deleteFront(self) -> bool:  # 앞에서 아이템 빼고 성공 시 true 반환
        if self.isEmpty():
            return False

        self.q[self.front] = None
        self.front = (self.front + 1) % self.max_size
        return True

    def deleteLast(self) -> bool:  # 뒤에서 아이템 빼고 성공 시 true 반환
        next_rear_idx = (self.max_size + self.rear - 1) % self.max_size
        if self.isEmpty():
            return False

        self.q[next_rear_idx] = None
        self.rear = next_rear_idx
        return True

    def getFront(self) -> int:  # 첫 번째 아이템 반환 , 없을 시 -1
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def getRear(self) -> int:  # 맨 뒤 아이템 반환 , 없을 시 -1
        if self.isEmpty():
            return -1
        return self.q[self.rear - 1]

    def isEmpty(self) -> bool:
        return (self.front == self.rear and self.q[self.front] == None)

    def isFull(self) -> bool:
        return (self.front == self.rear and self.q[self.front] != None)

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
