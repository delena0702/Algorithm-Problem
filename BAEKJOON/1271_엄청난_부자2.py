import sys
def input(): return sys.stdin.readline().strip()

N, M = map(int, input().split())
print(N // M)
print(N % M)