import sys

N = int(sys.stdin.readline())

for i in range(0, 16, 3):
    if N - i < 0 or i == 15:
        print(-1)
        break
    if (N - i) % 5 == 0:
        print(i//3 + (N-i)//5)
        break
