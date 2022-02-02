import heapq
import sys

N = int(sys.stdin.readline())
nums = []

for _ in range(N):
    heapq.heappush(nums, int(sys.stdin.readline()))

for _ in range(N):
    print(heapq.heappop(nums))

'''
# sorted 사용
import sys

N = int(sys.stdin.readline())
nums = []

for _ in range(N):
    nums.append(int(sys.stdin.readline()))

for i in sorted(nums):
    print(i)
'''