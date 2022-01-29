import sys

N = int(sys.stdin.readline())
pn = []

for _ in range(N):
    T = int(sys.stdin.readline())
    pn_list = []
    for _ in range(T):
        pn_list.append(sys.stdin.readline().rstrip())
    pn_list.sort()
    pn.append(pn_list)

for pn_list in pn:
    state = True
    for i in range(len(pn_list) - 1):
        if pn_list[i] == pn_list[i + 1][:len(pn_list[i])]:
            state = False
            break
    if state:
        print('YES')
    else:
        print('NO')

# for pn_list in pn:
#     for i in range(len(pn_list) - 1):
#         for j in range(i + 1, len(pn_list)):
#             if len(pn_list[i]) <= len(pn_list[j]):
#                 if pn_list[i] == pn_list[j][:len(pn_list[i])]:
#                     result.append('NO')
#                     break
#             else:
#                 if pn_list[i][:len(pn_list[j])] == pn_list[j]:
#                     result.append('NO')
#                     break
# result.append('YES')
