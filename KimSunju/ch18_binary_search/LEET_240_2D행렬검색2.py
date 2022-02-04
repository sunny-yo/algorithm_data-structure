# https://leetcode.com/problems/search-a-2d-matrix-ii/
import bisect
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for y in range(len(matrix)):
            idx = bisect.bisect_left(matrix[y], target)
            if idx < len(matrix[y]) and matrix[y][idx] == target:
                return True


s = Solution()
print(s.searchMatrix(
    matrix=[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
    target=5))
print(s.searchMatrix(
    matrix=[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
    target=20))
