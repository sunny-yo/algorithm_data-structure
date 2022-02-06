# https://www.acmicpc.net/problem/1654

# 재귀
import sys


def counting(meter):
    count = 0
    for line in lines:
        count += line // meter
    return count


def find_len(lo, hi):
    if lo > hi:
        return hi
    mid = (lo + hi) // 2

    count = counting(mid)

    if count >= N:
        return find_len(mid + 1, hi)
    elif count < N:
        return find_len(lo, mid - 1)


K, N = map(int, sys.stdin.readline().split())
lines = []
for _ in range(K):
    lines.append(int(sys.stdin.readline()))

low = 1
high = max(lines)

print(find_len(low, high))

'''
# while
import sys
K, N = map(int, sys.stdin.readline().split())
lines = []
for _ in range(K):
    lines.append(int(sys.stdin.readline()))
lines.sort()

lo = 1
hi = lines[-1]

while(lo <= hi):
    mid = (lo + hi) // 2
    count = 0

    for line in lines:
        count += line // mid

    if count >= N:
        lo = mid + 1
    elif count < N:
        hi = mid-1

print(hi)'''
