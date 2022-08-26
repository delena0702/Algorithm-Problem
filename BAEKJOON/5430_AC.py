from collections import deque
import sys
def input(): return sys.stdin.readline().strip()

T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    if n:
        x = deque(map(int, input()[1:-1].split(',')))
    else:
        x, _ = deque(), input()

    reverse = False
    for query in p:
        if query == 'R':
            reverse = not reverse

        else:
            if not x:
                print("error")
                break

            if reverse:
                x.pop()
            else:
                x.popleft()
    else:
        print("[", end='')
        if reverse:
            print(*list(x)[::-1], sep=',', end='')
        else:
            print(*x, sep=',', end='')
        print("]")
