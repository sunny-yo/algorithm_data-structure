class Solution:
    def twoSum(self, nums, target):
        num_dict = {}
        for i, num in enumerate(nums):
            num_dict[num] = i
        for i, num in enumerate(nums):
            if target - num in num_dict and num_dict[target - num]:
                return [i, num_dict[target - num]]

s = Solution()
print(s.twoSum([1,3,4,2], 6))

# 1
# from typing import List
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)): # i=0 ~ i=len(nums)-1까지 for문
#             for j in range(i + 1, len(nums)): # j=i+1 ~ j=len(nums)-1까지 for문
#                 if nums[i] + nums[j] == target: # nums[i]+nums[j] == target이 될 때
#                     return [i, j] # [i, j] 값 반환

# 2
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i, n in enumerate(nums): # {(0, nums[0]), (1, nums[1]), (2, nums[2]), ...}
#             complement = target - n   # target - nums[i]
#
#             if complement in nums[i + 1:]: # nums[i + 1:]에 complement 가 있으면
#                 #
#                 return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]