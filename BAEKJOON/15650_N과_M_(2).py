from itertools import combinations
import sys
def input(): return sys.stdin.readline().strip()

N, M = map(int, input().split())
for arr in combinations(range(1, N + 1), M):
    print(*arr)