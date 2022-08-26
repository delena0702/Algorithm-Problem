from itertools import combinations
import sys
def input(): return sys.stdin.readline().strip()

while True:
    k, *data = map(int, input().split())
    if k == 0:
        break
    for arr in combinations(data, 6):
        print(*arr)
    print()