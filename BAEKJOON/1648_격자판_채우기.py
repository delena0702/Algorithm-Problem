import sys
def input(): return sys.stdin.readline().strip()


def search():
    if N % 2 == 1 and M % 2 == 1:
        return 0
    return _search(0, 0, 0) % 9901


dp = [[{} for _ in range(14)] for _ in range(14)]


def _search(x, y, data):
    if y == N and data == 0:
        return 1

    if dp[y][x].get(data, -1) != -1:
        return dp[y][x][data]

    ny, nx = divmod(y * M + x + 1, M)
    if data & (1 << x):
        return _search(nx, ny, data & ~(1 << x))

    retval = 0
    if nx and not (data & (1 << (x + 1))):
        retval += _search(nx, ny, data | (1 << (x + 1)))
    if y + 1 < N:
        retval += _search(nx, ny, data | (1 << x))
    dp[y][x][data] = retval % 9901
    return retval % 9901


(N, M) = map(int, input().split())
print(search())
