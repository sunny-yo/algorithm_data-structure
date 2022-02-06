# https://www.acmicpc.net/problem/2110
# 369page
# N = 집의 개수, C = 공유기의 개수
# 출력 = 가장 인접한 두 공유기 사이의 최대 거리

# binary search - while
import sys

N, C = list(map(int, sys.stdin.readline().split()))
coor = []
for _ in range(N):
    coor.append(int(sys.stdin.readline()))
coor.sort()

lo = 1
hi = coor[-1] - coor[0]
min_gap = 0

while lo <= hi:
    curr = coor[0]
    count = 1
    mid = (lo + hi) // 2

    for i in range(1, len(coor)):
        if coor[i] >= curr + mid:
            curr = coor[i]
            count += 1

    if count >= C:
        min_gap = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(min_gap)


'''
# binary search - recursion
import sys

N, C = list(map(int, sys.stdin.readline().split()))
coor = []
for _ in range(N):
    coor.append(int(sys.stdin.readline()))
coor.sort()

lo = 1
hi = coor[-1] - coor[0]
min_gap = 0

def find_dist(lo, hi, min_gap):
    if lo > hi:
        return min_gap

    curr = coor[0]
    count = 1
    mid = (lo+hi) // 2

    for i in range(1, len(coor)):
        if coor[i] >= curr + mid:
            curr = coor[i]
            count += 1

    if count >= C:
        return find_dist(mid+1, hi, mid)
    else:
        return find_dist(lo, mid-1, min_gap)

answer = find_dist(lo, hi, 0)
print(answer)
'''

'''
입력 :
5 3
1
2
8
4
9
출력 : 3
'''