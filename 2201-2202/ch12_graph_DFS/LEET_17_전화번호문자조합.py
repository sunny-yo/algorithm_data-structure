class Solution:
    def letterCombinations(self, digits):
        digit_dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        i = 0

        def recursion(i, path):
            if len(path) == len(digits):
                result.append(path)
                return

            for char in digit_dic[digits[i]]:
                recursion(i + 1, path + char)

        if len(digits) == 0:
            return []

        recursion(i, '')
        return result

        # digit_dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        # digit_list = list(map(lambda x: list(digit_dic[x]), digits)) [[a, b, c], [d, e, f]]
        # result = []
        # path = []
        # i = 0
        #
        # def recursion(i):
        #     if len(path) == len(digits):
        #         result.append(path[:])
        #         return
        #
        #     for char in digit_list[i]:
        #         path.append(char)
        #         recursion(i+1)
        #         path.pop()
        #
        # if len(digits) == 0:
        #     return []
        #
        # recursion(i)
        # return list(map(lambda x: ''.join(x), result))


s = Solution()
print(s.letterCombinations("23"))
