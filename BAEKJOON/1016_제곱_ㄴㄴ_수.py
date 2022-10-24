from math import sqrt
import sys
def input(): return sys.stdin.readline().strip()

l, h = map(int, input().split())
N = h - l + 1
data = [True] * N

for i in range(2, int(sqrt(h)) + 1):
    d = i ** 2
    low = ((l - 1) // d + 1) * d - l
    for j in range(low, N, d):
        data[j] = False
print(data.count(True))