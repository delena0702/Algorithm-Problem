from math import sqrt
import sys
def input(): return sys.stdin.readline().strip()

D, H, W = map(int, input().split())
k = sqrt((D ** 2) / (W ** 2 + H ** 2))
print(int(k * H), int(k * W))