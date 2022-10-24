import sys
def input(): return sys.stdin.readline().strip()

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break

    N = arr[0]
    answer = 1
    for i in range(N):
        a, b = arr[2 * i + 1], arr[2 * i + 2]
        answer = answer * a - b
    print(answer)