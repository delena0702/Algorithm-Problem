import sys
def input(): return sys.stdin.readline().strip()

N, M = map(int, input().split())
a = set([input() for _ in range(N)])
b = set([input() for _ in range(M)]).intersection(a)

print(len(b))
for name in sorted(b):
    print(name)