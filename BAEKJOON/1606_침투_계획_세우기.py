import sys
def input(): return sys.stdin.readline().strip()

x, y = map(int, input().split())
if x * y <= 0:
    a = max(abs(x), abs(y))
else:
    a = abs(x + y)
base = 3 * a ** 2 + 3 * a + 1
if base == 1:
    print(base)
    exit()

if x == a and -x < y <= 0:
    print(base + y)
elif y == -a and 0 < x <= -y:
    print(base - 2 * a + x)
elif x <= 0 and y < 0:
    print(base - 2 * a + x)
elif x == -a and 0 <= y < a:
    print(base - 3 * a - y)
elif y == a and -a <= x < 0:
    print(base - 5 * a - x)
else:
    print(base - 5 * a - x)