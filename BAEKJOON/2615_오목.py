import sys
N = 19
dx = [1, 1, 1, 0]
dy = [-1, 0, 1, 1]
def input(): return sys.stdin.readline().strip()


def inBoard(x, y):
    if x < 0:
        return False
    if x >= N:
        return False
    if y < 0:
        return False
    if y >= N:
        return False
    return True


data = [list(map(int, input().split())) for _ in range(N)]

answer = None
for i in range(N * N):
    (x, y) = divmod(i, N)
    if data[y][x] == 0:
        continue

    for direct in range(4):
        cnt = 1
        while True:
            nx, ny = x + cnt*dx[direct], y + cnt*dy[direct]

            if not inBoard(nx, ny):
                break
            if data[y][x] != data[ny][nx]:
                break

            cnt += 1

        if cnt == 5:
            if not inBoard(x - dx[direct], y - dy[direct]) or\
                    data[y - dy[direct]][x - dx[direct]] != data[y][x]:
                answer = (data[y][x], y + 1, x + 1)
                break

    if answer:
        break

if answer:
    print(f"{answer[0]}\n{answer[1]} {answer[2]}")
else:
    print(0)
