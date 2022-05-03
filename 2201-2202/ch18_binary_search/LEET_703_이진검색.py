# https://leetcode.com/problems/binary-search/
import bisect


class Solution:
    def search(self, nums, target):
        idx = bisect.bisect_left(nums, target)

        if idx < len(nums) and nums[idx] == target:
            return idx
        else:
            return -1

s = Solution()
print(s.search([-1,0,3,5,9,12], 9))
print(s.search([-1,0,3,5,9,12], 2))

'''
# 구현
    def search(self, nums, target):
        def binary_search(start, end):
            if start > end:
                return -1

            mid = (start + end) // 2

            if nums[mid] < target:
                return binary_search(mid + 1, end)
            elif nums[mid] > target:
                return binary_search(start, mid-1)
            else:
                return mid

        return binary_search(0, len(nums) - 1)
'''

'''
# bisect
    def search(self, nums, target):
        idx = bisect.bisect_left(nums, target)

        if idx < len(nums) and nums[idx] == target:
            return idx
        else:
            return -1
'''