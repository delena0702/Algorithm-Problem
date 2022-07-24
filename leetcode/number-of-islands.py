class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        N, M = len(grid), len(grid[0])
        dx, dy = (0, 0, 1, -1), (1, -1, 0, 0)

        answer = 0
        for ind in range(N*M):
            (y, x) = divmod(ind, M)

            if grid[y][x] != "1":
                continue
            answer += 1

            stack = [ind]
            grid[y][x] = "0"
            while stack:
                here = stack.pop()
                (y, x) = divmod(here, M)

                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if nx < 0 or nx >= M or ny < 0 or ny >= N:
                        continue
                    if grid[ny][nx] != "1":
                        continue
                    grid[ny][nx] = "0"
                    stack.append(ny*M+nx)
        return answer
