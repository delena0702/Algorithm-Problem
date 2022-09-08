N = input()
if sum(map(lambda x: int(x), N)) % 3:
    print(-1)
    exit()

answer = list(sorted(N, reverse=True))
if answer[-1] == '0':
    print(*answer, sep='')
else:
    print(-1)