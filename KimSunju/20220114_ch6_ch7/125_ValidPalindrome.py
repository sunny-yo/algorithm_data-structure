import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower() # 소문자로 바꿔준다
        s = re.sub('[^a-z0-9]','',s) # s를 가져와서 a-z0-9에 해당하지 않으면 ''으로 replace
        return s == s[::-1]


s = Solution()
print(s.isPalindrome("test"))

# 1-1
# def isPalindrome(self, s: str) -> bool:
#     strs = []
#     for char in s: # s의 문자들을 하나하나 for문으로 돌린다
#         if char.isalnum(): # if 문자가 영어, 숫자이면
#             strs.append(char.lower()) # 소문자로 변경해서 strs 배열에 append한다
#
#     # 팰린드롬 여부 판별
#     while len(strs) > 1:  # strs의 길이가 1보다 크면
#         if strs.pop(0) != strs.pop(): # strs의 앞, 뒤에서 pop해서 문자를 비교해서 다르면
#             return False  # False를 반환한다
#
#     return True

# import collections
# from typing import Deque
#
# 1-2
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         # 자료형 데크로 선언
#         strs: Deque = collections.deque()
#
#         for char in s:
#             if char.isalnum():
#                 strs.append(char.lower())
#
#         while len(strs) > 1:
#             if strs.popleft() != strs.pop(): # 데크는 스택과 큐의 기능을 가진 객체, 문이 앞뒤로 있다
                                               # popleft() 해서 O(1)
#                 return False
#
#         return True