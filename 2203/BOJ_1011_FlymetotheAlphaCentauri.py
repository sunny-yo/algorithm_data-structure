# https://www.acmicpc.net/problem/1011
# Fly me to the Alpha Centauri

import sys

input = sys.stdin.readline

T = int(input())
M = []
for _ in range(T):
    x, y = map(int, input().split())
    M.append([x, y])

result = []

for pair in M:
    a, b = pair[:]
    num = 1
    count = 0

    while a <= b:
        if b - a <= num:
            result.append(count + 1)
            break
        else:
            a += num
            b -= num
            count += 2

        if a >= b:
            result.append(count)
            break

        num += 1

for _ in result:
    print(_)