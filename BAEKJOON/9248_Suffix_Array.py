import sys
def input(): return sys.stdin.readline().strip()


def getKey(x):
    return (rank[x], rank[min(N, x + d)])


data = input()
N = len(data)

data = data + "$"
sa = [i for i in range(N)]
rank = [ord(ch) for ch in data] + [0]
next_rank = [0] * (N + 1)

d = 1
while d < N:
    sa.sort(key=getKey)
    next_rank[sa[0]] = 1
    for i in range(1, N):
        next_rank[sa[i]] = next_rank[sa[i - 1]]
        if getKey(sa[i - 1]) < getKey(sa[i]):
            next_rank[sa[i]] = next_rank[sa[i]] + 1
    rank = next_rank[:]
    d = d << 1

isa = [0] * N
for i in range(N):
    isa[sa[i]] = i

k = 0
lcp = [-1] * N
for i in range(0, N):
    if isa[i] == 0:
        continue

    j = sa[isa[i] - 1]
    while data[i + k] == data[j + k]:
        k = k + 1

    lcp[isa[i]] = k
    k = max(0, k - 1)

print(*map(lambda x: x + 1, sa), sep=' ')
print("x", end=' ')
print(*map(lambda x: x, lcp[1:]), sep=' ')
