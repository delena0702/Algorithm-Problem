import sys
def input(): return sys.stdin.readline().strip()

T = int(input())
for _ in range(T):
    string = input()
    stack = 0
    for ch in string:
        if ch == '(':
            stack = stack + 1
        elif ch == ')':
            if stack == 0:
                print("NO")
                break
            stack = stack - 1
    else:
        if stack == 0:
            print("YES")
        else:
            print("NO")