from collections import deque
import sys
def input(): return sys.stdin.readline().strip()

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

N, K = int(input()), int(input())
board = [[0] * N for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = 1
L = int(input())
moves = deque([input().split() for _ in range(L)])
for arr in moves:
    arr[0] = int(arr[0])

x, y, a = 0, 0, 1
board[y][x] = 2
time = 0
snake = deque([(x, y)])

while True:
    nx, ny = x + dx[a], y + dy[a]
    if not 0 <= nx < N or not 0 <= ny < N:
        break

    if board[ny][nx] == 2:
        break
    
    if board[ny][nx] == 1:
        board[ny][nx] = 0
    else:
        rx, ry = snake.popleft()
        board[ry][rx] = 0

    board[ny][nx] = 2
    snake.append((nx, ny))
    x, y, time = nx, ny, time + 1
    
    if len(moves) and moves[0][0] == time:
        _, ch = moves.popleft()
        if ch == 'L':
            a = (a + 3) % 4
        else:
            a = (a + 1) % 4

print(time + 1)