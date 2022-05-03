# https://www.acmicpc.net/problem/2805

# while문으로 했을 때 아직 시간 초과 문제를 해결하지 못함
import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

# 절단기 최소높이 : 0, 최대높이 : 나무 중 최대높이
lo = 0
hi = max(trees)

while lo <= hi:
    sum = 0
    mid = (lo + hi) // 2

    for tree in trees:
        if tree > mid:
            sum += tree - mid

    if sum < M:
        hi = mid - 1
    else:
        lo = mid + 1

print(hi)

'''
import sys
N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
trees.sort()

def find_meter(lo, hi):
    sum = 0
    mid = (lo + hi) // 2
    if mid == lo:
        return mid

    for length in trees:
        if length <= mid:
            continue
        else:
            sum += length - mid

    if sum == M:
        return mid
    elif sum > M:
        return find_meter(mid, hi)
    elif sum < M:
        return find_meter(lo, mid)


lo = 0
hi = trees[N-1]

answer = find_meter(lo, hi)
print(answer)
'''
