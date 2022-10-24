import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
if N == 1:
    print(1)
else:
    print(2 * (N - 1))