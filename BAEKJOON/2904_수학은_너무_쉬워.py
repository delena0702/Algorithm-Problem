import sys
def input(): return sys.stdin.readline().strip()

is_prime = [True] * (1_000_001)
primes = []
for i in range(2, 1_000_001):
    if not is_prime[i]:
        continue
    primes.append(i)
    for j in range(2 * i, 1_000_001, i):
        is_prime[j] = False

N, data = int(input()), list(map(int, input().split()))

count = [0] * (len(primes))
for num in data:
    for i, prime in enumerate(primes):
        if num == 1:
            break
        while num % prime == 0:
            num, count[i] = num // prime, count[i] + 1

answer = [1, 0]
for i in range(len(primes)):
    if count[i]:
        answer[0] = answer[0] * (primes[i] ** (count[i] // N))

for i, prime in enumerate(primes):
    for num in data:
        cnt = 0
        while num % prime == 0:
            num, cnt = num // prime, cnt + 1
        answer[1] = answer[1] + max(0, count[i] // N - cnt)

print(*answer, sep=' ')
