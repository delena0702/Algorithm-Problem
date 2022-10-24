from math import ceil, floor, sqrt, log
import sys
def input(): return sys.stdin.readline().strip()

A, B = map(int, input().split())
N = int(sqrt(B)) + 1

is_prime = [True] * (N + 1)
answer = 0
for i in range(2, N + 1):
    if not is_prime[i]:
        continue
    answer += floor(log(B, i)) - max(ceil(log(A, i)), 2) + 1
    for j in range(2 * i, N + 1, i):
        is_prime[j] = False
print(answer)