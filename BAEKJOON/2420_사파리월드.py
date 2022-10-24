import sys
def input(): return sys.stdin.readline().strip()

N, M = map(int, input().split())
print(abs(N - M))