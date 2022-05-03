# https://www.acmicpc.net/problem/10250
# ACM 호텔

import sys

input = sys.stdin.readline

result = []

T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())

    if N % H == 0:
        num = N // H
        floor = H
    else:
        num = N // H + 1
        floor = N % H

    result.append(floor * 100 + num)

for num in result:
    print(num)