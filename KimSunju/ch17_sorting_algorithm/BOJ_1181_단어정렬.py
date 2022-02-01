# https://www.acmicpc.net/problem/1181


# 병합정렬 사용
def merge(arr1, arr2):
    result = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if len(arr1[i]) < len(arr2[j]):
            result.append(arr1[i])
            i += 1
        elif len(arr1[i]) > len(arr2[j]):
            result.append(arr2[j])
            j += 1
        else:
            if arr1[i] > arr2[j]:
                result.append(arr2[j])
                j += 1
            else:
                result.append(arr1[i])
                i += 1

    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result


def mergesort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    L = lst[:mid]
    R = lst[mid:]
    return merge(mergesort(L), mergesort(R))


import sys

N = int(sys.stdin.readline())
input_data = set()

for _ in range(N):
    input_data.add(sys.stdin.readline().rstrip())

answer = mergesort(list(input_data))

for _ in answer:
    print(_)

'''
# sorted, lambda 이용해서 정렬
import sys

N = int(sys.stdin.readline())
input_data = set()

for _ in range(N):
    input_data.add(sys.stdin.readline().rstrip())

result = sorted(sorted(list(input_data)), key= lambda x: len(x))

for _ in result:
    print(_)
'''
