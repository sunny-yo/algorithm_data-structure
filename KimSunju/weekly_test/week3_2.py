# https://programmers.co.kr/learn/courses/30/lessons/42626
# 힙(Heap) > 더 맵게
import heapq


def solution(scoville, K):
    answer = 0

    def mix(num1, num2):
        return num1 + num2*2

    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) <= 1:
            answer = -1
            break
        mixed = mix(heapq.heappop(scoville), heapq.heappop(scoville))
        heapq.heappush(scoville, mixed)
        answer += 1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
