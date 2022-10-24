import sys
def input(): return sys.stdin.readline().strip()

N, M = map(int, input().split())

if N == 1:
    print(1)
elif N == 2:
    print(min((M + 1) // 2, 4))
else:
    if M <= 4:
        print(M)
    elif M <= 6:
        print(4)
    else:
        print(M - 2)