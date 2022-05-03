class BinaryMaxHeap:
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items) - 1

    def _percolate_up(self):
        curr_idx = len(self)
        parent_idx = len(self) // 2

        while parent_idx  > 0:
            if self.items[curr_idx] > self.items[parent_idx]:
                self.items[curr_idx], self.items[parent_idx] = self.items[parent_idx], self.items[curr_idx]

            curr_idx = parent_idx
            parent_idx = curr_idx // 2

    def _percolate_down(self, curr_idx):
        biggest_idx = curr_idx
        left_idx = curr_idx * 2
        right_idx = curr_idx * 2 + 1

        if left_idx <= len(self) and self.items[biggest_idx] < self.items[left_idx]:
            biggest_idx = left_idx
        if right_idx <= len(self) and self.items[biggest_idx] < self.items[right_idx]:
            biggest_idx = right_idx

        if biggest_idx != curr_idx:
            self.items[curr_idx], self.items[biggest_idx] = self.items[biggest_idx], self.items[curr_idx]
            self._percolate_down(biggest_idx)

    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    def extract(self):
        if len(self) < 1:
            return None

        root = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self._percolate_down(1)

        return root