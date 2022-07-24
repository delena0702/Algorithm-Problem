import sys
def input(): return sys.stdin.readline().strip()

for _ in range(3):
    N = int(input())

    answer = 0
    for i in range(N):
        answer = answer + int(input())

    if answer < 0:
        print('-')
    elif answer > 0:
        print('+')
    else:
        print('0')