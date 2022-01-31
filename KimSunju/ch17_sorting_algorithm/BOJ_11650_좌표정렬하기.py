# https://www.acmicpc.net/problem/11650

import sys

N = int(sys.stdin.readline())
xy_list = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    xy_list.append((x, y))

for i in sorted(xy_list):
    print(i[0], i[1])