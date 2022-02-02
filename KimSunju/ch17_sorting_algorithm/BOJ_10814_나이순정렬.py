# https://www.acmicpc.net/problem/10814
import heapq
import sys

members = []
N = int(sys.stdin.readline())

for _ in range(N):
    age, name = sys.stdin.readline().split()
    heapq.heappush(members, (age, name))

for _ in range(N):
    (age, name) = heapq.heappop(members)
    print(int(age), name)

'''
# sort 사용
import sys

members = []
N = int(sys.stdin.readline())

for _ in range(N):
    age, name = sys.stdin.readline().split()
    members.append((int(age), name))

members.sort(key=lambda x: x[0])

for member in members:
    print(member[0], member[1])
'''
