class Queue:
    def __init__(self):
        """큐를 초기화합니다."""
        self.items = []
        self.front = -1  # 큐의 시작 인덱스
        self.rear = -1   # 큐의 끝 인덱스

    def is_empty(self):
        """큐가 비어 있는지 확인합니다."""
        return self.front == -1 and self.rear == -1

    def push(self, item):
        """큐의 뒤쪽에 항목을 추가합니다."""
        if self.is_empty():
            # 큐가 비어 있으면 front와 rear를 0으로 설정
            self.front = 0
        self.rear += 1
        self.items.append(item)

    def pop(self):
        """큐의 앞쪽에서 항목을 제거하고 반환합니다."""
        if self.is_empty():
            raise IndexError("pop from empty queue")
        item = self.items[self.front]
        if self.front == self.rear:
            # 큐에 하나의 항목만 있는 경우 초기 상태로 복원
            self.front = -1
            self.rear = -1
        else:
            self.front += 1
        return item

    def peek(self):
        """큐의 앞쪽 항목을 반환하지만 제거하지는 않습니다."""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[self.front]

    def size(self):
        """큐에 있는 항목의 개수를 반환합니다."""
        if self.is_empty():
            return 0
        return self.rear - self.front + 1