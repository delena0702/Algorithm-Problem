N, m, M, T, R = map(int, input().split())

count, now, answer = 0, m, 0
while True:
    if N == answer:
        print(count)
        break

    if count and now == m and answer == 0:
        print(-1)
        break

    if now + T <= M:
        now = now + T
        answer = answer + 1
    else:
        now = max(now - R, m)
    
    count = count + 1