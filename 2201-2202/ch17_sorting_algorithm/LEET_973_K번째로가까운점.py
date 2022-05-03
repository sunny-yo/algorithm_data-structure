import heapq
from collections import deque
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            distance = point[0]*point[0] + point[1]*point[1]
            heapq.heappush(heap, (distance, point))

        return [heapq.heappop(heap)[1] for _ in range(k)]


s = Solution()
print(s.kClosest([[1, 3], [-2, 2]], 1))
print(s.kClosest([[3, 3], [5, -1], [-2, 4]], 2))

'''
# heapq 사용 (810ms)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            distance = point[0]*point[0] + point[1]*point[1]
            heapq.heappush(heap, (distance, point))

        return [heapq.heappop(heap)[1] for _ in range(k)]
'''

'''
# 내가 풀었을 것 같은 방법 (1116ms)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        result = []

        for point in points:
            distance.append((point[0] * point[0] + point[1] * point[1], point))

        distance.sort(reverse=True)

        for _ in range(k):
            result.append(distance.pop()[1])

        return result
'''