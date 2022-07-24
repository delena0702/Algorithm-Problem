import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
print(*sorted([int(input()) for _ in range(N)]), sep='\n')