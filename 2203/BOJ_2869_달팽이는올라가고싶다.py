# https://www.acmicpc.net/problem/2869
# 달팽이는 올라가고 싶다

import sys
import math

input = sys.stdin.readline
A, B, V = map(int, input().split())

count = 1
rest = V - A
sub = A - B

result = math.ceil(rest / sub)
print(result + count)