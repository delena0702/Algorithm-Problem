N, L = map(int, input().split())

for length in range(L, 101):
    if length % 2 == 0:
        if N % (length // 2) == 0 and (N // (length // 2)) % 2 == 1:
            pivot = N // (length // 2) // 2 - length // 2 + 1
            if pivot >= 0:
                print(*list(range(pivot, pivot + length)), sep=' ')
            else:
                print(-1)
            break
        
    else:
        if N % length == 0:
            pivot = N // length - length // 2
            if pivot >= 0:
                print(*list(range(pivot, pivot + length)), sep=' ')
            else:
                print(-1)
            break

    if length == 100:
        print(-1)