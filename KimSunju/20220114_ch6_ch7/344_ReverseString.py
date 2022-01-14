class Solution:
    def reverseString(self, s):
        s.reverse()
        return s

s = Solution()
print(s.reverseString(["h","e","l","l","o"]))

# from typing import List
#
#
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         left, right = 0, len(s) - 1 # left = 0, right = len(s)
#         while left < right: # left가 right보다 작으면
#             s[left], s[right] = s[right], s[left] # 두개를 바꾼다
#             left += 1 # left는 +1
#             right -= 1 # right는 -1