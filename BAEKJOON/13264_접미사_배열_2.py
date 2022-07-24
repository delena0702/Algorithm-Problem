import sys
def input(): return sys.stdin.readline().strip()

data = input()
N = len(data)
answer = [i for i in range(N)]
rank = [ord(ch) for ch in data] + [0]
next_rank = [0] * (N + 1)

d = 1
def getKey(x): return (rank[x], rank[min(N, x + d)])

while d < N:
    answer.sort(key=getKey)
    next_rank[answer[0]] = 1
    for i in range(1, N):
        next_rank[answer[i]] = next_rank[answer[i - 1]]
        if getKey(answer[i - 1]) != getKey(answer[i]):
            next_rank[answer[i]] = next_rank[answer[i]] + 1
    rank = next_rank[:]
    d = d << 1
print(*answer, sep='\n')