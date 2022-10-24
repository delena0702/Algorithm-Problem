import sys
def input(): return sys.stdin.readline().strip()

x, cnt = int(input()), int(input())
if x == 1:
    print(8 * cnt)
elif x == 5:
    print(8 * cnt + 4)
else:
    if cnt % 2 == 0:
        print(8 * (cnt // 2) + x - 1)
    else:
        print(8 * (cnt // 2) - x + 9)