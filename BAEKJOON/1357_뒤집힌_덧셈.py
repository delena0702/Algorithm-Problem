import sys
def input(): return sys.stdin.readline().strip()

print(int(str(sum(map(lambda x: int(x[::-1]), input().split())))[::-1]))