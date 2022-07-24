import sys
def input(): return sys.stdin.readline().strip()


def xGCD(x, y, s, t):
    if y == 0:
        if x != 1:
            return -1
        return (t[0] + N) % N
    q = x // y
    return xGCD(y, x % y, (s[1], s[0] - q*s[1]), (t[1], t[0] - q*t[1]))


(N, A) = map(int, input().split())

print(f"{(N - A) % N} {xGCD(N, A, (1, 0), (0, 1))}")
