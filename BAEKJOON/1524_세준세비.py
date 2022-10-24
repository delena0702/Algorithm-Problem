import sys
def input(): return sys.stdin.readline().strip()

T = int(input())
for _ in range(T):
    input()
    N, M = map(int, input().split())
    arr = []
    for num in list(map(int, input().split())):
        arr.append((num, 1))
    for num in list(map(int, input().split())):
        arr.append((num, 0))
    arr.sort(reverse=True)

    print("S" if arr[0][1] == 1 else "B")