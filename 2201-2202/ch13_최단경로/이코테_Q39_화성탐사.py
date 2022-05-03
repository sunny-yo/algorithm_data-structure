import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)
answer = []


def dijkstra(space, energy, N):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 시작 노드 세팅
    q = []
    energy[0][0] = space[0][0]
    heapq.heappush(q, (energy[0][0], 0, 0))  # (energy, curr_y, curr_x)

    while q:
        acc, y, x = heapq.heappop(q)

        if energy[y][x] < acc:
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                cost = energy[y][x] + space[ny][nx]
                if cost < energy[ny][nx]:
                    energy[ny][nx] = cost
                    heapq.heappush(q, (cost, ny, nx))

    return energy[N - 1][N - 1]


# 입력 처리
T = int(input())  # 테스트케이스 개수

for _ in range(T):
    N = int(input())
    space = []
    energy = [[INF] * N for _ in range(N)]
    for _ in range(N):
        space.append(list(map(int, input().split())))
    # 입력 처리 끝
    print(dijkstra(space, energy, N))

'''
입력
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1 
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
'''
