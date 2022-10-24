import sys
def input(): return sys.stdin.readline().strip()

N, M = map(int, input().split())
arr = [[0] * 101 for _ in range(101)]
for i in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1, x2 + 1):
        for k in range(y1, y2 + 1):
            arr[k][j] += 1

answer = 0
for i in range(1, 101):
    for j in range(1, 101):
        if arr[i][j] > M:
            answer += 1
print(answer)