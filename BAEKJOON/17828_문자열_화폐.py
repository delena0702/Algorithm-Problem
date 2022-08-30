import sys
def input(): return sys.stdin.readline().strip()


(N, X) = map(int, input().split())
(a, b) = divmod(X - N, 25)
if X == 26 * N:
    print('Z'*N)
elif N - a - 1 < 0 or a < 0:
    print('!')
else:
    print('A'*(N - a - 1)+chr(ord('A') + b) + 'Z'*a)
