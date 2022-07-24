import sys
def input(): return sys.stdin.readline().strip()


(N, M) = map(int, input().split())
data = []
for i in range(N):
    data.append(input())

answer = 321
for ind in range((N-7)*(M-7)):
    y, x = divmod(ind, M-7)
    cnt = 0
    for i in range(8):
        for j in range(8):
            if i % 2 == j % 2 and data[y+i][x+j] == 'B':
                cnt += 1
            elif i % 2 != j % 2 and data[y+i][x+j] == 'W':
                cnt += 1
    answer = min(answer, cnt, 64-cnt)
print(answer)
