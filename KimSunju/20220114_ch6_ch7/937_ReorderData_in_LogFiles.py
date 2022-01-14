class Solution:
    def reorderLogFiles(self, logs):
        log_digit = []
        log_letter = []
        for log in logs:
            if log.split()[1].isdigit(): # 각 log를 split해서 index 1이 숫자이면
                log_digit.append(log) # 숫자배열에 넣고
            else: # 아니면
                log_letter.append(log) # 문자배열에 넣어라
        # 문자배열을 key값 : log를 split해서 index 1 부터 문자열로 sort를 하고,
        # 그 다음에 key값 : log를 split해서 index 0으로 sort를 해라
        log_letter.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return log_letter + log_digit

s = Solution()
print(s.reorderLogFiles(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))
