import sys
def input(): return sys.stdin.readline().strip()

N, M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
K = int(input())

answer = 0
for i in range(N):
    cnt = arr[i].count('0')
    if not (K >= cnt and K % 2 == cnt % 2):
        continue
    
    count = 0
    for j in range(N):
        for k in range(M):
            if arr[i][k] != arr[j][k]:
                break
        else:
            count += 1
    answer = max(answer, count)
print(answer)