import sys
def input(): return sys.stdin.readline().strip()

while True:
    a, b, c = sorted(map(int, input().split()))

    if a == 0 and b == 0 and c == 0:
        break
    
    if a == 0:
        print("wrong")
    elif a ** 2 + b ** 2 == c ** 2:
        print("right")
    else:
        print("wrong")