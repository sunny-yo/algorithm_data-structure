import sys

sys.stdin = open("input.txt", "r")
num = int(sys.stdin.readline())
num_link = int(sys.stdin.readline())

num_list = list(range(1, num + 1))
dic = {}
result = []

for i in range(num_link):
    x, y = sys.stdin.readline().split()
    if x not in dic:
        dic[x] = [y]
    else:
        dic[x] = dic[x] + [y]

def virus(node, virused):
    if node not in dic:
        global result
        result = virused[:]
        return
    for next in dic[node]:
        if next not in virused:
            virused.append(next)
            virus(next, virused)
        continue

virus('1', ['1'])
print(len(result) - 1)
