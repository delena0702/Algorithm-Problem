import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
data = []
for _ in range(N):
    x, y = map(int, input().split())
    data.append((y, x))
data.sort()
print(*map(lambda x: f"{x[1]} {x[0]}", data), sep='\n')