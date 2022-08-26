import sys
def input(): return sys.stdin.readline().strip()

C = int(input())
for _ in range(C):
    N, *arr = map(int, input().split())
    aver = sum(arr) / N
    k = len(list(filter(lambda x: x > aver, arr)))
    print(f"{k / N * 100:.3f}%")