class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def dfs(path, sum):
            if sum == target:
                path = sorted(path)
                if path not in result:
                    result.append(path)
                return
            elif sum > target:
                return

            for num in candidates:
                dfs(path + [num], sum + num)

        dfs([], 0)
        return result

s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))
