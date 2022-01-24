# https://www.acmicpc.net/problem/1759

def is_ok(path):
    global count
    count = 0
    for alp in path:
        if alp in v:
            count += 1
        else:
            continue
    if count < 1 or L - count < 2:
        return False
    return True


def dfs(path, index, n):
    if n <= 0:
        if is_ok(path):
            result.append(''.join(path[:]))
            return
        return

    for i in range(index, C - n + 1):
        dfs(path + [char[i]], i + 1, n - 1)


L, C = map(int, input().split())
char = list(sorted(input().split(' ')))
v = ['a', 'e', 'i', 'o', 'u']
result = []
count = 0

dfs([], 0, L)

for res in result:
    print(res)
