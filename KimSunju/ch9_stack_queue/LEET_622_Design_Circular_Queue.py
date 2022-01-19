class MyCircularQueue:      # 큐 : 선입선출 FIFO
    def __init__(self, k: int):
        self.queue = [None] * k     # k = 3일 때, [1, 2, 3]
        self.max_size = k
        self.size = 0               # 원형 큐의 size : size=0(empty), size=k(full)
        self.front = 0              # front가 되는 index (포인터)
        self.rear = 0               # rear가 되는 index (포인터)

    # 원형큐에 값을 추가 성공하면 true 반환
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False      # 포화상태일 때 추가할 곳이 없으므로 False
        self.queue[self.rear] = value         # queue라는 리스트의 rear번째 인덱스의 값 = value
        self.size += 1
        self.rear = (self.rear + 1) % self.max_size     # rear=2 -> rear=(2+1)%3=0
        return True

    # 원형큐에서 값을 삭제 성공하면 true 반환
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False     # 비어있을 때 삭제할 값이 없으므로 False
        self.queue[self.front] = None           # queue: FIFO, 값을 삭제
        self.size -= 1
        self.front = (self.front + 1) % self.max_size
        return True

    # 큐에서 맨 앞의 값을 가져오고, 비어있으면 -1을 반환
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    # 큐에서 맨 뒤의 값을 가져오고, 비어있으면 -1을 반환
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        # rear 포인터(index)는 값이 있는 곳이 아니라
        # 값을 추가해야하는 다음 index를 가리키고 있기 때문에
        # -1을 해준다
        return self.queue[self.rear-1]

    # 원형큐가 비어있는지 확인하여 true 반환
    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False

    # 원형큐가 포화상태인지 확인하여 true 반환
    def isFull(self) -> bool:
        if self.size == self.max_size:
            return True
        return False


