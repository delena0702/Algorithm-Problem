import sys
def input(): return sys.stdin.readline().strip()


is_prime = [True] * 10001
for i in range(2, 10001):
    if not is_prime[i]:
        continue
    for j in range(2 * i, 10001, i):
        is_prime[j] = False

T = int(input())
for _ in range(T):
    N = int(input())
    for i in range(N // 2, 1, -1):
        if is_prime[i] and is_prime[N - i]:
            print(i, N - i, sep=' ')
            break
