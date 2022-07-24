import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
rank = [1] * N

for i in range(N):
    for j in range(N):
        if i != j and data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            rank[i] += 1

print(*rank, sep=' ')