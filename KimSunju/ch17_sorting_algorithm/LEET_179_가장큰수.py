from typing import List


class Solution:
    def to_swap(self, n1: int, n2: int):
        if str(n1) + str(n2) < str(n2) + str(n1):
            return True
        else:
            return False

    def largestNumber(self, nums: List[int]) -> str:
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j - 1], nums[j]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
            i += 1

        return str(int(''.join(map(str, nums))))


s = Solution()
print(s.largestNumber([10, 2]))
print(s.largestNumber([3, 30, 34, 5, 9]))

# 3 30 34 5 9 -> 9 5 3 34 30
# 답 : 9 5 34 3 30
# str_nums = sorted((map(str, sorted(nums, reverse=True))), key=lambda x: (x[0], -len(x)), reverse=True)
# return ''.join(str_nums)