import heapq
import sys

INF = int(1e9)

input = sys.stdin.readline

def dijkstra(graph, distance):
    q = []
    distance[0] = distance[1] = 0
    heapq.heappush(q, (0, 1))
    while q:
        acc, curr = heapq.heappop(q)

        if distance[curr] < acc:
            continue

        for adj in graph[curr]:
            cost = acc + 1
            if cost < distance[adj]:
                distance[adj] = cost
                heapq.heappush(q, (cost, adj))

    max_dist = max(distance[1:])
    count = sum([1 for idx in range(1, N+1) if distance[idx] == max_dist])

    return distance.index(max_dist), max_dist, count

N, M = map(int, input().split())        # 노드의 수, 간선의 수
graph = [[] for _ in range(N+1)]
distance = [INF for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)


print(dijkstra(graph, distance))

'''
입력
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2

출력
(4, 2, 3)
'''