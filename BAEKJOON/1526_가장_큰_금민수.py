import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
for i in range(N, 3, -1):
    for ch in str(i):
        if ch != '4' and ch != '7':
            break
    else:
        print(i)
        break