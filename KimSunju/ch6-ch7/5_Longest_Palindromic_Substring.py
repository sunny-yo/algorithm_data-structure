class Solution:
    def longestPalindrome(self, s):
        # 팰린드롬 len이 홀수일지 짝수일지 모르기 때문에
        #간격을 1로 두고 비교할건지, 2로 두고 비교할건지 두가지 경우를 고려해야 한다.

        # 필요한 함수를 먼저 구현
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left +1:right]

        # 예외처리
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        for i in range(len(s)-1):
            result = max(result, expand(i, i+1), expand(i, i+2), key = len)
        return result

s = Solution()
print(s.longestPalindrome("babadsdfbababa"))

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         # 팰린드롬 판별 및 투 포인터 확장
#         def expand(left: int, right: int) -> str: # 첫번째 index, 마지막 index를 인자로 갖는다
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#             # 첫번째 index는 0보다 크거나 같다 && 마지막idex는 문자열의 길이보다 작다 && 해당 index의 값이 같다
#             # 즉, 펠린드롬일 것 같으면
#                 left -= 1 # 왼쪽 pointer를 왼쪽으로 한칸 옮긴다
#                 right += 1 # 오른쪽 pointer를 오른쪽으로 한칸 옮긴다
#             # 그렇지 않을 경우 슬라이싱으로 문자열 s를 앞에 하나를 지운 나머지 문자열로 반환한다
#             return s[left + 1:right]
#
#         # 해당 사항이 없을때 빠르게 리턴
#         # 문자열의 길이가 하나이거나, 문자열 자체가 펠린드롬일 경우 바로 문자열을 그대로 return
#         if len(s) < 2 or s == s[::-1]:
#             return s
#
#         result = '' # 팰린드롬이 없을 경우 ''를 출력할 수 있도록
#         # 슬라이딩 윈도우 우측으로 이동
#         # i = 0~len(s)-1
#         for i in range(len(s) - 1):
#             # result, expand(i, i+1), expand(i, i+2)를 len으로 비교
#             # max(iterable, key) # iterable: 비교대상, key: 비교하는 기준
#             result = max(result,
#                          expand(i, i + 1),
#                          expand(i, i + 2),
#                          key=len)
#         return result