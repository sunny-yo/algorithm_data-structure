from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [-1]*n
        answer = []

        def is_ok_on(nth_row):
            for row in range(nth_row):
                if board[row] == board[nth_row] or nth_row-row == abs(board[nth_row]-board[row]):
                    return False
            return True

        def dfs(row):
            if row >= n:
                result = []
                grid = [['.']*n for _ in range(n)]
                for idx, value in enumerate(board):
                    grid[idx][value] = 'Q'
                for row in grid:
                    result.append(''.join(row))
                nonlocal answer
                answer.append(result)
                return

            for col in range(n):
                board[row] = col
                if is_ok_on(row):
                    dfs(row + 1)

        dfs(0)
        return answer

s = Solution()
print(s.solveNQueens(4))