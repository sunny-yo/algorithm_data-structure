# 백준 시간 초과

N = int(input())
dic = {i: [] for i in range(1, N + 1)}
for _ in range(N - 1):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)


def dfs(node):
    visited.append(node)

    for next in dic[node]:
        if next in visited:
            continue
        tree_dic[next] = node
        dfs(next)


tree_dic = {}
visited = []
dfs(1)

for i in range(2, N + 1):
    print(tree_dic[i])