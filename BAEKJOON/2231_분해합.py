import sys
def input(): return sys.stdin.readline().strip()

N = int(input())

for i in range(1, N):
    if i + sum(map(int, str(i))) == N:
        print(i)
        break
else:
    print(0)