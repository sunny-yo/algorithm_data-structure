class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # s_dic = {}
        # i_dic = {}
        # result = 0
        #
        # for i, char in enumerate(s):
        #     if char in s_dic:
        #         if result < len(i_dic):
        #             result = len(i_dic)
        #         index = s_dic[char]
        #         while index >= 0:
        #             if index in i_dic:
        #                 if i_dic[index] in s_dic:
        #                     s_dic.pop(i_dic[index])
        #                 i_dic.pop(index)
        #                 index -= 1
        #             else:
        #                 break
        #     i_dic[i] = char
        #     s_dic[char] = i
        #
        # if result < len(i_dic):
        #     result = len(i_dic)
        # return result

        s_dic = {}
        res_list = []
        result = 0

        for i, char in enumerate(s):
            if char in res_list:
                index = s_dic[char]
                res_list = list(s[index+1:i])
            s_dic[char] = i
            res_list.append(char)
            if result < len(res_list):
                result = len(res_list)

        return result

s = Solution()
print(s.lengthOfLongestSubstring(" asgsd asdfwes"))