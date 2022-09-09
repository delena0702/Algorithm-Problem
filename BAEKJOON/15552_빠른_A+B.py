import sys
def input(): return sys.stdin.readline().strip()

T = int(input())
for _ in range(T):
    print(sum(map(int, input().split())))