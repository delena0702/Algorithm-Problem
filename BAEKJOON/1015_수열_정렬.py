import sys
def input(): return sys.stdin.readline().strip()


N = int(input())
a = list(zip(map(int, input().split()), [i for i in range(N)]))
p = sorted([i for i in range(N)], key=lambda x: a[x])
answer = [0] * N
for i in range(N):
    answer[a[p[i]][1]] = i
for i in range(N):
    print(answer[i], end=' ')
