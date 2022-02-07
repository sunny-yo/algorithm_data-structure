import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = int(1e9)

        time_costs = [INF] * (n + 1)
        graph = [[] for _ in range(n + 1)]
        for time in times:
            source, target, time = time
            graph[source].append((time, target))

        start = k
        time_costs[k] = 0

        q = []
        heapq.heappush(q, (0, start))

        while q:
            acc, curr = heapq.heappop(q)

            if time_costs[curr] < acc:
                continue

            for time, adj in graph[curr]:
                cost = acc + time
                if cost < time_costs[adj]:
                    time_costs[adj] = cost
                    heapq.heappush(q, (cost, adj))

        if max(time_costs[1:]) >= INF:
            return -1
        else:
            return max(time_costs[1:])


s = Solution()
print(s.networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2))
print(s.networkDelayTime(times=[[1, 2, 1]], n=2, k=1))
