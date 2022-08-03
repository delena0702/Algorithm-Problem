import sys
def input(): return sys.stdin.readline().strip()

def update(idx, value):
    if values[idx] == value:
        return
    values[idx] = value

    value = 1 if value else -1
    while idx <= N:
        fw[idx] = fw[idx] + value
        idx = idx + (-idx & idx)

def sum(idx):
    retval = 0
    while idx:
        retval = retval + fw[idx]
        idx = idx - (-idx & idx)
    return retval

N = int(input())
values = [0] * (N + 1)
fw = [0] * (N + 1)
for i, num in enumerate(map(int, input().split())):
    update(i + 1, num % 2)

M = int(input())
for _ in range(M):
    q, l, r = map(int, input().split())
    if q == 1:
        update(l, r % 2)
    elif q == 2:
        print((r - l) - (sum(r) - sum(l - 1)) + 1)
    elif q == 3:
        print(sum(r) - sum(l - 1))