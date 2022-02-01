from typing import List


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
# 처음에만 입력 list에서 비교하고,
# result에 넣은 후부터는 result의 값과 비교 병합

s = Solution()
print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(s.merge([[1, 4], [1, 5]]))
print(s.merge([[1, 4], [5, 6]]))
print(s.merge([[2, 3], [2, 2], [3, 3], [1, 3], [5, 7], [2, 2], [4, 6]]))

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

'''
# Wrong Answer
# Input [[1,4],[5,6]]
# Output [[5,6]]
# Expected [[1,4],[5,6]]

def merging(arr1, arr2):
            merged = []
            i = j = 0

            while i < len(arr1) and j < len(arr2):
                if arr1[i][0] < arr2[j][0]:
                    merged.append(arr1[i])
                    i += 1
                elif arr1[i][0] > arr2[j][0]:
                    merged.append(arr2[j])
                    j += 1
                else:
                    if arr1[i][1] < arr2[j][1]:
                        merged.append(arr1[i])
                        i += 1
                    else:
                        merged.append(arr2[j])
                        j += 1
            while i < len(arr1):
                merged.append(arr1[i])
                i += 1
            while j < len(arr2):
                merged.append(arr2[j])
                j += 1

            return merged

        def mergesort(lst):
            if len(lst) <= 1:
                return lst

            mid = len(lst) // 2
            L = lst[:mid]
            R = lst[mid:]

            return merging(mergesort(L), mergesort(R))

        k = 1
        result = []
        if len(intervals) <= 1:
            return intervals

        merged_intervals = mergesort(intervals)

        while k < len(merged_intervals):
            if merged_intervals[k-1][1] >= merged_intervals[k][0]:
                result.append([merged_intervals[k-1][0], merged_intervals[k][1]])
                k += 1
            else:
                result.append(merged_intervals[k])
                k += 1

        return result
'''
