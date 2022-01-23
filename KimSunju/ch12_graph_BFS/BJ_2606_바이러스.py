from collections import deque

dic_link = {}

N = int(input())
M = int(input())
for i in range(M):
    D, L = map(int, input().split())
    if D not in dic_link:
        dic_link[D] = [L]
    else:
        dic_link[D] = dic_link[D] + [L]

start_node = 1
virused = [1]
queue = deque([1])

while queue:
    node = queue.popleft()
    if node not in dic_link:
        continue
    for next_node in dic_link[node]:
        if next_node not in virused:
            queue.append(next_node)
            virused.append(next_node)

print(len(virused) - 1)


''' input
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''