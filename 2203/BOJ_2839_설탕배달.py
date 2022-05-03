# https://www.acmicpc.net/problem/2839
# 설탕 배달

import sys

input = sys.stdin.readline

N = int(input())

a = N // 5
result = 0

while a >= 0:
    b = (N - a * 5) // 3

    if a * 5 + b * 3 == N:
        result = a + b
        break
    else:
        a -= 1


if result > 0:
    print(result)
else:
    print(-1)