import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
cards = set(input().split())
M = int(input())
print(*map(lambda x: 1 if x in cards else 0, input().split()))