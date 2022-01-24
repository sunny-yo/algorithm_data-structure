# https://www.acmicpc.net/problem/9095

def is_full(sum, T):
    if sum > T:
        return False
    elif sum <= T:
        return True

def dfs(sum, T):
    if sum == T:
        global count
        count += 1
        return

    for num in nums:
        if is_full(sum+num, T):
            dfs(sum+num, T)

T = []
N = int(input())
for _ in range(N):
    T.append(int(input()))
nums = [1, 2, 3]
result = []
count = 0

for i in T:
    count = 0
    dfs(0, i)
    result.append(count)

for _ in result:
    print(_)