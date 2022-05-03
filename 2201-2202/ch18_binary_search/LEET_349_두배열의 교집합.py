# https://leetcode.com/problems/intersection-of-two-arrays/
import bisect
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2.sort()
        result = set()

        for num in nums1:
            idx = bisect.bisect_left(nums2, num)
            if idx < len(nums2) and nums2[idx] == num:
                result.add(num)
        return list(result)


s = Solution()
print(s.intersection(nums1=[1, 2, 2, 1], nums2=[2, 2]))
print(s.intersection(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
