import re

class Solution:
    def mostCommonWord(self, paragraph, banned):
        result = ''
        count_dict = {}

        # 예외처리 : paragraph이 ''이거나, 한글자일 때
        if len(paragraph) < 2:
            return result

        words = re.sub(r'[^\w]', ' ', paragraph).lower().split()
        for word in words:
            if word not in banned:
                if word in count_dict:
                    count_dict[word] += 1
                else:
                    count_dict[word] = 1
        count_items = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
        return count_items[0][0]

s = Solution()
print(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))

# import collections
# import re
# from typing import List
#
#
# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
#             .lower().split()
#                  if word not in banned]
#
#         counts = collections.Counter(words)
#         # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
#         return counts.most_common(1)[0][0]