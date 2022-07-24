from math import log2
N, a, b = map(int, input().split())
print(int(log2((a - 1) ^ (b - 1))) + 1)