import sys
def input(): return sys.stdin.readline().strip()

X, Y, W, S = map(int, input().split())
if W >= S:
    print(S * max(X, Y) + (W - S if (X + Y) % 2 else 0))
elif 2 * W >= S:
    print(S * min(X, Y) + W * abs(X - Y))
else:
    print(W * (X + Y))