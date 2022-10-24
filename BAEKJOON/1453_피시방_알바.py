import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
arr = list(map(int, input().split()))
print(N - len(set(arr)))