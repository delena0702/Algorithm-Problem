from math import sqrt
import sys
def input(): return sys.stdin.readline().strip()

SIZE = 5_000_000
is_prime = [i for i in range(SIZE + 1)]
for i in range(2, int(sqrt(SIZE + 1) + 1)):
    if i != is_prime[i]:
        continue
    for j in range(2 * i, SIZE + 1, i):
        if j == is_prime[j]:
            is_prime[j] = i

input()
for num in map(int, input().split()):
    while num != 1:
        print(is_prime[num], end=' ')
        num = num // is_prime[num]
    print()