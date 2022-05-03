from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def quick_sort(lst, lo, hi):
            def partition(lo, hi):
                pivot = lst[hi]
                left = lo
                for right in range(lo, hi):
                    if lst[right] < pivot:
                        lst[left], lst[right] = lst[right], lst[left]
                        left += 1
                lst[left], lst[hi] = lst[hi], lst[left]
                return left

            if lo < hi:
                pivot = partition(lo, hi)
                quick_sort(lst, lo, pivot - 1)
                quick_sort(lst, pivot + 1, hi)

            return lst
        return quick_sort(nums, 0, len(nums) -1)

s = Solution()
print(s.sortColors([2, 0, 2, 1, 1, 0]))

'''
    def sortColors(self, nums: List[int]) -> None:
        def quick_sort(lst, lo, hi):
            def partition(lo, hi):
                pivot = lst[hi]
                left = lo
                for right in range(lo, hi):
                    if lst[right] < pivot:
                        lst[left], lst[right] = lst[right], lst[left]
                        left += 1
                lst[left], lst[hi] = lst[hi], lst[left]
                return left

            if lo < hi:
                pivot = partition(lo, hi)
                quick_sort(lst, lo, pivot - 1)
                quick_sort(lst, pivot + 1, hi)

            return lst
        return quick_sort(nums, 0, len(nums) -1)
'''
