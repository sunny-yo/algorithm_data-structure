class LinkedNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):     # 처음에는 empty
        self.size = 1000
        self.table = {}

    # key: value를 해시맵에 inserts, 이미 있다면 해당값을 update
    def put(self, key: int, value: int) -> None:
        index = key % self.size

        # 테이블의 해당 index가 비어있으면 값을 넣어주고 리턴
        if index not in self.table:
            self.table[index] = LinkedNode(key, value)
            return

        # 테이블의 해당 index에 노드가 있으면
        p = self.table[index]       # 포인터 지정
        while p:
            # 포인터에 노드가 있을 때
            # 노드의 key와 입력하고자하는 key가 같으면
            # 해당 value를 새로 들어온 value로 업데이트하고 리턴
            if p.key == key:
                p.value = value
                return

            # key가 달라서 다음 노드를 탐색해야할 때 next가 없으면 while문을 break
            if p.next is None:
                break

            # key가 다르고 next에 연결된 노드가 있으면 포인터를 다음 노드로 이동
            p = p.next
        # p.next가 None이어서 while문을 빠져나왔을 때
        # p.next에 입력한 key와 value가 들어있는 LinkedNode를 연결
        p.next = LinkedNode(key, value)

    # key 값으로 get, 없으면 -1 반환
    def get(self, key: int) -> int:
        index = key % self.size

        # table에서 해당 index를 찾을 수 없을 경우 -1 리턴
        if index not in self.table:
            return -1

        # table에 해당 index가 있을 경우 key를 비교
        p = self.table[index]       # 포인터 지정
        # next 노드가 없을 때까지 포인터를 next로 이동하면서 key 비교
        while p:
            if p.key == key:
                return p.value
            p = p.next

        # 해당 index의 linkedNode를 다 돌아도 없으면 -1 리턴
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size

        # table에 해당 index가 없으면 리턴
        if index not in self.table:
            return

        # 해당 index가 있을 때 table[index]로 들어가서 key 비교 탐색
        p = self.table[index]       # 포인터 지정

        # key가 같고 추가로 연결된 노드가 없으면 해당 index를 table에서 삭제
        # key가 같고 추가로 연결된 노드가 있으면 해당 index에 다음 노드를 연결
        if p.key == key:
            if p.next is None:
                self.table.pop(index)
            else:
                self.table[index] = p.next
            return
        # key가 같지 않을 때
        prev = p        # 삭제했을 때 연결하기 위한 포인터 지정
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next
