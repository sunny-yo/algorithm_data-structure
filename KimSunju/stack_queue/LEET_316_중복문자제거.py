# class Solution:
#     def removeDuplicateLetters(self, s: str) -> str:
#         # 집합으로 정렬
#         for char in sorted(set(s)):
#             suffix = s[s.index(char):]
#             # 전체 집합과 접미사 집합이 일치할때 분리 진행
#             if set(s) == set(suffix):
#                 return char + self.removeDuplicateLetters(suffix.replace(char, ''))
#         return ''

import collections

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index = {c:i for i, c in enumerate(s)}
        result = []

        for i, c in enumerate(s):
            if c not in result and i < last_index[]

        return ''.join(result)

s = Solution()
print(s.removeDuplicateLetters("cbacdcbc"))