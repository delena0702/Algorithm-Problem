import sys
def input(): return sys.stdin.readline().strip()

def update(idx, value, node, s, e):
    if idx < s or e < idx:
        return
    segtree[node].append(value)
    m = (s + e) // 2
    if s < e:
        update(idx, value, 2 * node, s, m)
        update(idx, value, 2 * node + 1, m + 1, e)

def query(l, r, value, node, s, e):
    if e < l or r < s:
        return 0
    if not (l <= s and e <= r):
        m = (s + e) // 2
        return query(l, r, value, 2 * node, s, m) +\
            query(l, r, value, 2 * node + 1, m + 1, e)
    
    arr = segtree[node]
    st, en = 0, len(arr)
    while (st < en):
        mi = (st + en) // 2
        if value < arr[mi]:
            en = mi
        else:
            st = mi + 1
    return en

N, Q = map(int, input().split())
data = list(map(int, input().split()))
segtree = [[] for _ in range(4 * N)]
for i in range(N):
    update(i, data[i], 1, 0, N - 1)
for arr in segtree:
    arr.sort()

for _ in range(Q):
    i, j, k = map(int, input().split())
    s, e = -1000000000, 1000000000
    while s < e:
        m = (s + e) // 2
        if k <= query(i, j, m, 1, 1, N):
            e = m
        else:
            s = m + 1
    print(e)