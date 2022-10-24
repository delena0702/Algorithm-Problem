from re import A
import sys
def input(): return sys.stdin.readline().strip()

test_case = 0
while True:
    test_case += 1
    o, w = map(int, input().split())
    if o == 0 and w == 0:
        break

    while True:
        op, n = input().split()
        n = int(n)

        if op == '#':
            break
        if w <= 0:
            continue
        if op == 'F':
            w += n
        else:
            w -= n
            if w < 0:
                w = 0
    
    print(test_case, end=' ')
    if w == 0:
        print("RIP")
    elif o / 2 < w < 2 * o:
        print(":-)")
    else:
        print(":-(")