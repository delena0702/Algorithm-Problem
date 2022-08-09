import sys
def input(): return sys.stdin.readline().strip()


K, A, B = map(int, input().split())

if K == 0:
    print(B - A + 1)
else:
    s, e = K, K + 1 - (K % 2)
    answer = 0
    while s <= B:
        answer = answer + max(0, min(B, e) - max(A, s) + 1)
        s = s << 1
        e = (e << 1) | 1
    print(answer)
