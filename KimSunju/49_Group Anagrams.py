class Solution:
    def groupAnagrams(self, strs):
        a_dict = {}
        for str in strs:
            a = ''.join(sorted(str)) # 각 단어를 정렬
            if a in a_dict: # a_dict의 키값으로 정렬한 단어가 있으면
                a_dict[a] = a_dict[a] + [str] # 기존에 있는 list에 단어를 추가
            else: # 없으면
                a_dict[a] = [str] # 새로운 key와 value로 추가
        return list(a_dict.values()) # a_dict의 values들을 리스트로 만들어서 return


s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

#
# import collections
# from typing import List
#
#
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         anagrams = collections.defaultdict(list)
#
#         for word in strs:
#             # 정렬하여 딕셔너리에 추가
#             anagrams[''.join(sorted(word))].append(word)
#         return list(anagrams.values())