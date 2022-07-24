import sys
def input(): return sys.stdin.readline().strip()


T = int(input())
for _ in range(T):
    (a, b) = map(int, input().split())
    a %= 10
    answer = 1

    temp = 1
    single = a
    while b:
        if b & temp:
            answer = answer * single % 10
            b -= temp
        single = (single**2) % 10
        temp *= 2
    print(answer if answer else 10)
