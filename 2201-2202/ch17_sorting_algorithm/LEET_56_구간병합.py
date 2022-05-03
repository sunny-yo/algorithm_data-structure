# https://leetcode.com/problems/merge-intervals/

from typing import List


# 처음에만 입력 list에서 비교하고,
# result에 넣은 후부터는 result의 값과 비교 병합
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        intervals.sort()
        result = []
        i = j = 0

        while i < len(intervals):
            if i <= 0:
                if intervals[i][1] >= intervals[i + 1][0]:
                    if intervals[i][1] >= intervals[i + 1][1]:
                        result.append(intervals[i])
                        i += 2
                    else:
                        result.append([intervals[i][0], intervals[i + 1][1]])
                        i += 2
                else:
                    result.append(intervals[i])
                    i += 1
            else:
                if result[j][1] >= intervals[i][0]:
                    if result[j][1] >= intervals[i][1]:
                        i += 1
                    else:
                        result[j] = [result[j][0], intervals[i][1]]
                        i += 1
                else:
                    result.append(intervals[i])
                    i += 1
                    j += 1

        return result


s = Solution()
print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(s.merge([[1, 4], [1, 5]]))
print(s.merge([[1, 4], [5, 6]]))
print(s.merge([[2, 3], [2, 2], [3, 3], [1, 3], [5, 7], [2, 2], [4, 6]]))

'''
# 책 풀이
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key= lambda x: x[0])

        for interval in intervals:
            if result and interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result += interval,
        return result
'''

'''
# 병합하는 부분을 result를 재귀함수에 넣으면서 구현
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        answer = intervals

        def recursive(lst):
            nonlocal answer

            if len(lst) <= 1:
                return lst

            result = []
            i = 0

            while i < len(lst):
                if i + 1 >= len(lst):
                    result.append(lst[i])
                    i += 1
                else:
                    if lst[i][1] >= lst[i + 1][0]:
                        if lst[i][1] >= lst[i + 1][1]:
                            result.append(lst[i])
                            i += 2
                        else:
                            result.append([lst[i][0], lst[i + 1][1]])
                            i += 2
                    else:
                        result.append(lst[i])
                        i += 1

            if answer == result:
                return
            else:
                answer = result[:]
            recursive(result)

        recursive(intervals)
        return answer
'''
