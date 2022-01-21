class Solution:
    def numIslands(self, grid) -> int:
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        rows, cols = len(grid), len(grid[0])
        count = 0

        # 스택 이용
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != '1':
                    continue

                stack = [(row, col)]

                while stack:
                    x, y = stack.pop()
                    grid[x][y] = '0'
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != '1':
                            continue
                        stack.append((nx, ny))
                count += 1

        # # 재귀
        # def dfs_recursive(r, c):
        #     if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
        #         return
        #
        #     grid[r][c] = '0'
        #     for i in range(4):
        #         dfs_recursive(r + dx[i], c + dy[i])
        #     return
        #
        # for r in range(rows):
        #     for c in range(cols):
        #         node = grid[r][c]
        #         if node != '1':
        #             continue
        #
        #         count += 1
        #         dfs_recursive(r, c)

        return count


s = Solution()
print(s.numIslands(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))

assert s.numIslands(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]) == 1
assert s.numIslands(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]) == 3
