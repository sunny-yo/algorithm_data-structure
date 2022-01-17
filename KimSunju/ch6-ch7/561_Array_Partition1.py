class Solution:
    def arrayPairSum(self, nums):
        return sum(sorted(nums)[::2])

s = Solution()
print(s.arrayPairSum([1,4,3,2]))
