import sys
N = int(sys.stdin.readline().strip())
K = int(sys.stdin.readline().strip())

data = list(map(int, sys.stdin.readline().strip().split()))
data.sort()

data2 = [data[i + 1] - data[i] for i in range(N - 1)]
data2.sort()

print(sum(data2[:N-K]))