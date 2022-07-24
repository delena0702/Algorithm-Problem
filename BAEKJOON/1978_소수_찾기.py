import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
data = list(map(int, input().split()))
isPrime = [True] * (1001)
isPrime[1] = False

for i in range(2, 1001):
    if not isPrime[i]:
        continue
    for j in range(i*2, 1001, i):
        isPrime[j] = False

print(list(map(lambda x: isPrime[x], data)).count(True))