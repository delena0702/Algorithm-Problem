import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
arr = [int(input()) for _ in range(N)]
print(sum(arr) - N + 1)