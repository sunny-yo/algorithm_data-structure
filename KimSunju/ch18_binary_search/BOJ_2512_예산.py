# https://www.acmicpc.net/problem/2512

import sys

def find_hi(lo, hi):
    mid = (lo + hi) // 2
    if lo == mid:
        return mid

    sum = 0

    for budg in budgets:
        sum += budg if budg <= mid else mid

    if sum == total_budget:
        return mid
    elif sum < total_budget:
        return find_hi(mid, hi)
    elif sum > total_budget:
        return find_hi(lo, mid)


N = int(sys.stdin.readline())
budgets = list(map(int, sys.stdin.readline().split()))
total_budget = int(sys.stdin.readline())
budgets.sort()

lo = 1
hi = budgets[N-1]
answer = 0

if sum(budgets) <= total_budget:
    answer = hi
else:
    answer = find_hi(lo, hi)

print(answer)



