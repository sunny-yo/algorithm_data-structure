class Solution:
    def combine(self, n, k):
        result = []

        def recursion(start, k, stack):
            if k == 0:
                result.append(stack[:])
                return

            for num in range(start, n+1):
                recursion(num+1, k-1, stack + [num])

        recursion(1, k, [])

        return result

s = Solution()
print(s.combine(5, 3))