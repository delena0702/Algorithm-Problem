import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
print(*map(lambda x: f"{x[0]} {x[1]}", sorted([tuple(map(int, input().split())) for _ in range(N)])), sep='\n')
