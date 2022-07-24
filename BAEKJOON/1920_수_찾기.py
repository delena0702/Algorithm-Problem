import sys
def input(): return sys.stdin.readline().strip()

input()
cnt = set(list(map(int, input().split())))
input()
for num in map(int, input().split()):
    print(1 if num in cnt else 0)