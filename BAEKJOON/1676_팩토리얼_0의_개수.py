N = int(input())
cases, cnt = [2, 5], [0, 0]
for i, case in enumerate(cases):
    n = N
    while n >= case:
        n = n // case
        cnt[i] = cnt[i] + n
print(min(cnt))