import heapq
from typing import List

from KimSunju.ch15_heap.structures import BinaryMaxHeap


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = BinaryMaxHeap()
        for num in nums:
            maxheap.insert(num)

        return [maxheap.extract() for _ in range(k)][-1]
        # return [maxheap.extract() for _ in range(k)][k - 1]


# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         return heapq.nlargest(k, nums)[-1]


s = Solution()
print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))

assert s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 1) == 6
assert s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 2) == 5
assert s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 3) == 5
assert s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
assert s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 5) == 3
assert s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 6) == 3
assert s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 7) == 2
assert s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 8) == 2
assert s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 9) == 1
