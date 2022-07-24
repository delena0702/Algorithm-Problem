import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

aa, bb = 0, 0
count = 0
while aa < N and bb < N:
    if a[aa] == b[bb]:
        count += 1
        aa += 1
        bb += 1
    elif a[aa] > b[bb]:
        bb += 1
    else:
        aa += 1
print(N - count)