import sys
def input(): return sys.stdin.readline().strip()

N, M = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
a.difference_update(b)
a = list(a)
a.sort()
print(len(a))
print(*a)