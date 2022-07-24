from math import sqrt
import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
if N == 1:
    print(1)
else:
    print(int(9 + sqrt(12 * N - 15)) // 6)