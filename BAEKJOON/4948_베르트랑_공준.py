from math import sqrt
import sys
def input(): return sys.stdin.readline().strip()

def update(idx):
    while idx <= SIZE:
        fw[idx] = fw[idx] + 1
        idx = idx + (-idx & idx)

def get(idx):
    retval = 0
    while idx:
        retval = retval + fw[idx]
        idx = idx - (-idx & idx)
    return retval

SIZE = 123_456 * 2
is_prime = [True] * (SIZE + 1)
for i in range(2, int(sqrt(SIZE)) + 1):
    if not is_prime[i]:
        continue
    for j in range(2 * i, SIZE + 1, i):
        is_prime[j] = False

fw = [0] * (SIZE + 1)
for i in range(2, SIZE + 1):
    if is_prime[i]:
        update(i)

while True:
    N = int(input())
    if N == 0:
        break
    print(get(2 * N) - get(N))
