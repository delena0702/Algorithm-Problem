from math import gcd
import sys
def input(): return sys.stdin.readline().strip()

def get(idx):
    if uf[idx] == idx:
        return idx
    uf[idx] = get(uf[idx])
    return uf[idx]

N = int(input())

nodes = [1] * N
nnodes = [1] * N
uf = list(range(N))
for _ in range(N - 1):
    a, b, p, q = map(int, input().split())
    g = gcd(p, q) * gcd(nodes[a], nodes[b])
    nnodes = nodes[:]
    for i in range(N):
        if get(i) == get(a):
            nnodes[i] *= p * nodes[b] // g
    
    for i in range(N):
        if get(i) == get(b):
            nnodes[i] *= q * nodes[a] // g
    uf[get(a)] = uf[get(b)]
    nodes = nnodes

g = gcd(*nodes)
for i in range(N):
    print(nodes[i] // g, end=' ')