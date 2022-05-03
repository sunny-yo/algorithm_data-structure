# https://programmers.co.kr/learn/courses/30/lessons/42586

from collections import deque

def solution(progresses, speeds):
    answer = []
    speeds = deque(speeds)

    while len(progresses) > 0:
        count = 0
        # while progresses[0] + speeds[0] * days < 100:
        #     days += 1
        days = (100 - progresses[0]) // speeds[0]
        days = days if (100 - progresses[0]) % speeds[0] == 0 else days + 1
        plus = list(map(lambda speed: speed * days, speeds))
        progresses = deque([x + y for x, y in zip(progresses, plus)])
        while progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            count += 1
            if not progresses:
                break
        answer.append(count)
    return answer

print(solution([93, 25, 25, 45, 90, 1, 5], [3, 8, 7, 8, 4, 15, 7]))
print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
print(solution([2, 2, 1, 2], [1, 1, 1, 1]))
