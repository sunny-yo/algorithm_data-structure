import sys

sys.stdin = open("input.txt", "r")
num = int(sys.stdin.readline())

map = []

for i in range(num):
    row = list(sys.stdin.readline().split()[0])
    map.append(row)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
rows = len(map)
cols = len(map[0])
house = []
count = 0

def recursion(r, c):
    if r < 0 or r >= rows or c < 0 or c >= cols or map[r][c] != '1':
        return

    map[r][c] = '0'
    global count
    count += 1

    for i in range(4):
        recursion(r + dx[i], c + dy[i])

for r in range(rows):
    for c in range(cols):
        if map[r][c] == 0:
            continue

        if count > 0:
            house.append(count)
        count = 0
        recursion(r, c)

house.sort()
print(len(house))
for i in range(len(house)):
    print(house[i])
