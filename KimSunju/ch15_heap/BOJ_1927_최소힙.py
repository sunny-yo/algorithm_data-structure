'''
class BinaryMinHeap:
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items) - 1

    def _percolate_up(self):
        curr_idx = len(self)
        parent_idx = len(self) // 2

        while parent_idx > 0:
            if self.items[curr_idx] < self.items[parent_idx]:
                self.items[curr_idx], self.items[parent_idx] = self.items[parent_idx], self.items[curr_idx]

            curr_idx = parent_idx
            parent_idx = curr_idx // 2

    def _percolate_down(self, curr_idx):
        smallest_idx = curr_idx
        left_idx = curr_idx * 2
        right_idx = curr_idx * 2 + 1

        if left_idx <= len(self) and self.items[smallest_idx] > self.items[left_idx]:
            smallest_idx = left_idx
        if right_idx <= len(self) and self.items[smallest_idx] > self.items[right_idx]:
            smallest_idx = right_idx

        if smallest_idx != curr_idx:
            self.items[curr_idx], self.items[smallest_idx] = self.items[smallest_idx], self.items[curr_idx]
            self._percolate_down(smallest_idx)

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


import sys

N = int(sys.stdin.readline())
result = []
minheap = BinaryMinHeap()

for i in range(N):
    input_data = int(sys.stdin.readline())
    if input_data == 0:
        if len(minheap) <= 0:
            result.append(0)
        else:
            result.append(minheap.items[1])
            minheap.extract()
    else:
        minheap.insert(input_data)

for res in result:
    print(res)
'''

import sys
import heapq

N = int(sys.stdin.readline())
result = []
heap = []

for i in range(N):
    input_data = int(sys.stdin.readline())
    if input_data == 0:
        if len(heap) <= 0:
            result.append(0)
        else:
            result.append(heapq.heappop(heap))
    else:
        heapq.heappush(heap, input_data)

for res in result:
    print(res)
