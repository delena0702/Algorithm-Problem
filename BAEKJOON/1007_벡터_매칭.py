from itertools import combinations
from math import sqrt
import sys
def input(): return sys.stdin.readline().strip()

T = int(input())
for _ in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    answer = float('inf')
    for arr in combinations(range(N), N // 2):
        check = set(arr)
        x, y = 0, 0
        for i in range(N):
            if i in check:
                x += data[i][0]
                y += data[i][1]
            else:
                x -= data[i][0]
                y -= data[i][1]
        answer = min(answer, x ** 2 + y ** 2)
    print(sqrt(answer))