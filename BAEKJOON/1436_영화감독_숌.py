import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
for i in range(10 ** 10):
    if str(i).find("666") != -1:
        N = N - 1
        if N == 0:
            print(i)
            break