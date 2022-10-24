from math import gcd
N, M, L = map(int, input().split())
print(N // gcd(N, L) * (M - 1))