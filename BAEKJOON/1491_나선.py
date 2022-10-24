import sys
def input(): return sys.stdin.readline().strip()

N, M = map(int, input().split())
if N > M:
    if M % 2:
        print(N - M // 2 - 1, M // 2)
    else:
        print(M // 2 - 1, M // 2)
elif N < M:
    if N % 2:
        print(N // 2, M - N // 2 - 1)
    else:
        print(N // 2 - 1, N // 2)
else:
    if N % 2:
        print(N // 2, N // 2)
    else:
        print(N // 2 - 1, N // 2)