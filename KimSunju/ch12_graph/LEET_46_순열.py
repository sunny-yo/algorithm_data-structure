class Solution:
    def permute(self, nums):
        result = []     # 숫자 조합 result
        path = []       # 지나간 길

        def recursion(unused):
            if len(unused) == 0:        # 가지 않은 정점 list
                result.append(path[:])
                return

            for num in unused:
                next_unused = unused[:]
                next_unused.remove(num)

                path.append(num)
                recursion(next_unused)
                path.pop()

        recursion(nums)
        return result


s = Solution()
print(s.permute([1,2,3]))

# def permute(self, nums):
#     result = []
#
#     def recursion(unused, path):
#         if len(unused) == 0:
#             result.append(path[:])
#             return
#
#         for num in unused:
#             next_unused = unused[:]
#             next_unused.remove(num)
#
#             recursion(next_unused, path + [num])
#
#     recursion(nums, [])
#     return result