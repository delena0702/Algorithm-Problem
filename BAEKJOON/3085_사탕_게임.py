import sys
def input(): return sys.stdin.readline().strip()


N = int(input())
data = [list(input()) for _ in range(N)]


def count():
    global N
    retval = 0
    for i in range(N):
        x, y, x_now, y_now = 0, 0, 0, 0
        for j in range(N):
            x = x + 1 if data[i][j] == x_now else 1
            x_now = data[i][j]
            y = y + 1 if data[j][i] == y_now else 1
            y_now = data[j][i]
            retval = max(retval, x, y)
    return retval


answer = 0
for i in range(N):
    for j in range(N - 1):
        data[i][j], data[i][j+1] = data[i][j+1], data[i][j]
        answer = max(answer, count())
        data[i][j], data[i][j+1] = data[i][j+1], data[i][j]
        data[j][i], data[j+1][i] = data[j+1][i], data[j][i]
        answer = max(answer, count())
        data[j][i], data[j+1][i] = data[j+1][i], data[j][i]

print(answer)
