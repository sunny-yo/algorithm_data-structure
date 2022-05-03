# 368page
# 고정점 : 수열의 원소 중 그 값이 인덱스와 동일한 원소

# 강의 시작 전 풀이 시작
import sys

def binary_search(lst, start, end):
    if start == end and lst[start] != start:
        return -1

    mid = (start + end) // 2

    if lst[mid] == mid:
        return mid
    elif lst[mid] > mid:
        return binary_search(lst, start, mid-1)
    else:
        return binary_search(lst, mid+1, end)

N = int(sys.stdin.readline())
input_data = list(map(int, sys.stdin.readline().split()))
print(binary_search(input_data, 0, N-1))
# 강의 시작 전 풀이 끝

'''
입력: 
5
-15 -6 1 3 7
출력 : 3
'''
'''
입력 : 
7
-15 -4 2 8 9 13 15
출력 : 2
'''
'''
입력 : 
7
-15 -4 3 8 9 13 15
출력 : -1
'''