import sys
def input(): return sys.stdin.readline().strip()


N = int(input())
data = list(map(int, input().split()))

if N == 1 or N == 2 and data[0] != data[1]:
    print("A")
elif N == 2:
    print(data[0])
else:
    a, b = 0, 0
    if data[0] != data[1]:
        a = (data[2] - data[1]) // (data[1] - data[0])
    b = data[1] - a * data[0]

    for i in range(N - 1):
        if data[i + 1] != a * data[i] + b:
            print("B")
            break
    else:
        print(a * data[-1] + b)