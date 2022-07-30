import sys
def input(): return sys.stdin.readline().strip()

C, L = float(input()), int(input())
print(C * sum(map(lambda x: x[0] * x[1], [list(map(float, input().split())) for _ in range(L)])))