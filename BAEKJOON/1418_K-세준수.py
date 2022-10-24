import sys
def input(): return sys.stdin.readline().strip()

N, K = int(input()), int(input())

is_prime = [True] * (N + 1)
data = [True] * (N + 1)
data[0] = False
for i in range(2, N + 1):
    if not is_prime[i]:
        continue
    for j in range(2 * i, N + 1, i):
        is_prime[j] = False

    if i <= K:
        continue
    for j in range(i, N + 1, i):
        data[j] = False

print(data.count(True))