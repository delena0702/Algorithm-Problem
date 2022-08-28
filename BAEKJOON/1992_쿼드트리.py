import sys
sys.stdin = open("1.txt")
def input(): return sys.stdin.readline().strip()

def dfs(x, y, g):
    cnt = psum[y + g - 1][x + g - 1] + psum[y - 1][x - 1]\
        - psum[y + g - 1][x - 1] - psum[y - 1][x + g - 1]
    if cnt == g ** 2:
        return "1"
    if cnt == 0:
        return "0"

    retval = ""
    retval = retval + dfs(x, y, g // 2)
    retval = retval + dfs(x + g // 2, y, g // 2)
    retval = retval + dfs(x, y + g // 2, g // 2)
    retval = retval + dfs(x + g // 2, y + g // 2, g // 2)
    return f"({retval})"

N = int(input())
data = [list(map(int, input())) for _ in range(N)]
psum = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(N):
    for j in range(N):
        psum[i][j] = psum[i - 1][j] + psum[i][j - 1]\
            - psum[i - 1][j - 1] + data[i][j]

print(dfs(0, 0, N))
