import sys
def input(): return sys.stdin.readline().strip()

T = int(input())
for _ in range(T):
    a, b, c = map(int, input().split())
    if (a + c) % 2:
        print("No")
        continue
    if a < c:
        print("No")
        continue
    if a == 0 and b % 2 and c == 0:
        print("No")
        continue
    print("Yes")