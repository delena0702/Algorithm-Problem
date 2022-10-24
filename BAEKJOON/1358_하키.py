import sys
def input(): return sys.stdin.readline().strip()

W, H, X, Y, P = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(P)]
R = H // 2

answer = 0
for x, y in data:
    if x < X - R:
        continue
    if x <= X:
        if (X - x) ** 2 + (Y + R - y) ** 2 <= R ** 2:
            answer += 1
        continue
    if x <= X + W:
        if Y <= y <= Y + H:
            answer += 1
        continue
    if x <= X + W + R:
        if (X + W - x) ** 2 + (Y + R - y) ** 2 <= R ** 2:
            answer += 1
        continue
print(answer)