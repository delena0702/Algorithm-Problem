def combine(n, k):
    answer = 1
    for i in range(k):
        answer = (answer * (n - i) * pow(1 + i, MOD - 2, MOD)) % MOD
    return answer

N = int(input())
MOD = 10007
print(combine(N + 9, 9))