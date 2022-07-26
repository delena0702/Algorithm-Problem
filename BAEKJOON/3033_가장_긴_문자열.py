import sys
def input(): return sys.stdin.readline().strip()

getKey = lambda x: (rank[x], rank[min(L, x + d)])

L, data = int(input()), input() + "$"
sa = [i for i in range(L)]
rank = list(map(ord, data))
rank.append(0)
next_rank = [0] * (L + 1)

d = 1
while d < L:
    sa.sort(key=getKey)
    next_rank[sa[0]] = 1
    for i in range(1, L):
        next_rank[sa[i]] = next_rank[sa[i - 1]]
        if getKey(sa[i - 1]) < getKey(sa[i]):
            next_rank[sa[i]] = next_rank[sa[i]] + 1
    rank = next_rank[:]
    d = d << 1
    
isa = [0] * L
for i in range(L):
    isa[sa[i]] = i

length, lcp = 0, [0] * L
for i in range(L):
    k = isa[i]
    if k:
        j = sa[k - 1]
        while data[i + length] == data[j + length]:
            length = length + 1
        lcp[k] = length

        if length:
            length = length - 1
print(max(lcp))