N, K = map(int, input().split())
now = N
while bin(now).count('1') > K:
    now = now + (-now & now)
print(now - N)