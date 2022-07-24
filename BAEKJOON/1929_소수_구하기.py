M, N = map(int, input().split())
is_prime = [True] * (N + 1)

for i in range(2, N + 1):
    if is_prime[i]:
        if i >= M:
            print(i)

        j = i * 2
        while j <= N:
            is_prime[j] = False
            j = j + i
