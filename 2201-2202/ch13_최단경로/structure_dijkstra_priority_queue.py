import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

# 초기 세팅
# - 입력 받기
# - visited, distance 리스트 만들어두기
n, m = map(int, input().split())        # 노드 개수, 간선 개수
start = int(input())

graph = [[] for i in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())     # 출발노드, 도착노드, 비용(거리)
    graph[a].append((b, c))

distance = [INF] * (n + 1)      # 노드별 최소 비용(최단거리)을 기록하기 위한 리스트
# 초기 세팅 끝

def dijkstra_priority_q(graph, start):
    # priority queue, 시작노드 세팅
    q = []
    heapq.heappush(q, (0, start))       # q에 담을 때 : tuple(비용, 노드) -> 0번째 요소 기준으로 최소 힙 구조
    distance[start] = 0

    while q:
        # 비용이 가장 작은 노드를 꺼낸다
        acc, curr = heapq.heappop(q)

        # distance에 기록된 비용이 더 작으면 처리할 필요가 없기 때문에 다음 while문으로 넘어간다
        # 처리할 필요가 없다 = 이미 방문 처리가 된 노드이다
        if distance[curr] < acc:
            continue

        for adj, dist in graph[curr]:
            cost = acc + dist

            if cost < distance[adj]:
                distance[adj] = cost
                heapq.heappush(q, (cost, adj))

    return distance

print(dijkstra_priority_q(graph, start))

'''
입력
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''
'''
출력
[1000000000, 0, 2, 3, 1, 2, 4]
'''