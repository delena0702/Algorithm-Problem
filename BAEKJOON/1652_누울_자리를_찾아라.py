import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
arr = [input() for _ in range(N)]

answer = [0, 0]
for i in range(N):
    cnt = 0
    for j in range(N + 1):
        if j < N and arr[i][j] == '.':
            cnt += 1
        else:
            if cnt >= 2:
                answer[0] += 1
            cnt = 0
    
    cnt = 0
    for j in range(N + 1):
        if j < N and arr[j][i] == '.':
            cnt += 1
        else:
            if cnt >= 2:
                answer[1] += 1
            cnt = 0

print(*answer)