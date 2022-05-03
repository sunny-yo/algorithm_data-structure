# https://programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge_list = deque([0] * bridge_length)
    sec = 0
    sum_weight = 0
    for truck in truck_weights:
        # while sum(list(bridge_list)[1:]) + truck > weight:
        # while sum(bridge_list) - bridge_list[0] + truck > weight:
        while sum_weight - bridge_list[0] + truck > weight:
            bridge_list.append(0)
            sum_weight = sum_weight - bridge_list.popleft()
            sec += 1
        bridge_list.append(truck)
        sum_weight = sum_weight + truck - bridge_list.popleft()
        sec += 1

    while sum(bridge_list) > 0:
        bridge_list.append(0)
        sum_weight = sum_weight - bridge_list.popleft()
        sec += 1

    return sec


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
