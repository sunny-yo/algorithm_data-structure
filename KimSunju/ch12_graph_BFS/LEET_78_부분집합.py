from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(path, index):
            result.append(path)
            if len(path) == len(nums):
                return

            for i in range(index, len(nums)):
                dfs(path + [nums[i]], i + 1)

        dfs([], 0)
        return result


s = Solution()
print(s.subsets([1, 2, 3]))
