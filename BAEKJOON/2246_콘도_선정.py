import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

answer = 0
for i in range(N):
    d, c = data[i]

    for j in range(N):
        if i == j:
            continue
        if data[j][0] < d and data[j][1] <= c:
            break
        if data[j][1] < c and data[j][0] <= d:
            break
    else:
        answer = answer + 1
print(answer)