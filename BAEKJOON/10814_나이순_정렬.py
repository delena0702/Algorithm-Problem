import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
data = [0] * N
for i in range(N):
    arr = input().split()
    data[i] = (int(arr[0]), i, arr[1])
data.sort()

for i in range(N):
    print(data[i][0], data[i][2], sep=' ')