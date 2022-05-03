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

visited = [False] * (n + 1)     # 방문노드 리스트
distance = [INF] * (n + 1)      # 노드별 최소 비용(최단거리)을 기록하기 위한 리스트
# 초기 세팅 끝

def get_smallest_node():
    min_value = INF     # 최소 비용 담을 변수 min_value
    idx = 0     # 최소 비용인 노드의 index를 담을 변수

    for i in range(1, n):     # 각 노드의 distance 확인 (시작노드 제외한 n-1개 노드 확인)
       if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            idx = i

    return idx


def dijkstra_naive(graph, start):
    # 시작노드 세팅
    visited[start] = True
    distance[start] = 0

    # 시작노드랑 연결된 노드부터 처리
    for adj, dist in graph[start]:      # 간접노드, 거리
        distance[adj] = dist

    # 시작노드를 제외한 노드에서 가장 거리가 짧은 노드를 찾아서 방문 처리, 연결된 노드 확인 및 처리
    for _ in range(n-1):
        curr = get_smallest_node()
        visited[curr] = True

        for adj, dist in graph[curr]:
            cost = distance[curr] + dist
            if cost < distance[adj]:
                distance[adj] = cost

    return distance

print(dijkstra_naive(graph, start))

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