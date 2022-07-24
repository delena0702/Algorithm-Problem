import sys
(N, K, D) = map(int, sys.stdin.readline().strip().split())
d, alg = [0]*N, [0]*N

for i in range(N):
    (M, d[i]) = map(int, sys.stdin.readline().strip().split())
    alg[i] = list(map(int, sys.stdin.readline().strip().split()))

order = [i for i in range(N)]
order.sort(key=lambda x: d[x])

count, visited = {}, set()
s, e = (-1, -1)
answer = 0
for here in range(N):
    if d[order[here]] in visited:
        continue
    visited.add(d[order[here]])

    for j in range(s, here):
        if s == -1: continue
        for k in alg[order[j]]:
            count[k] -= 1
            if count[k] == 0:
                del count[k]
    s = here

    while e + 1 < N and d[order[e+1]] <= d[order[here]] + D:
        e += 1
        for j in alg[order[e]]:
            count[j] = count[j] + 1 if j in count else 1

    inter = list(count.values()).count(e - s + 1)
    union = len(count)
    answer = max([answer, (union - inter)*(e - s + 1)])

    if (e == N-1):
        break
print(answer)