# https://www.acmicpc.net/problem/9663

def is_ok_on(nth_row):
    for row in range(nth_row):
        if board[row] == board[nth_row] or nth_row - row == abs(board[nth_row] - board[row]):
            return False
    return True


def dfs(row):
    global count
    if row >= N:
        count += 1
        return

    for col in range(N):
        board[row] = col
        if is_ok_on(row):
            dfs(row + 1)


N = int(input())
board = [-1] * N
count = 0

dfs(0)
print(count)
