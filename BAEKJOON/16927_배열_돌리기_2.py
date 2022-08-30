import sys
def input(): return sys.stdin.readline().strip()

(N, M, R) = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

for i in range(min(M, N) // 2):
    size = 2*(M + N - 4*i - 2)
    arr = [0] * size

    x, y = 0, 0
    for j in range(2):
        for k in range(size):
            rx, ry = i + x, i + y

            if j:
                data[ry][rx] = arr[(k + size - (R % size)) % size]
            else:
                arr[k] = data[ry][rx]

            if x == 0 and y == 0:
                y += 1
            elif y == 0:
                x -= 1
            elif x == M - 2 * i - 1:
                y -= 1
            elif y == N - 2 * i - 1:
                x += 1
            else:
                y += 1

for a in data:
    print(*a)