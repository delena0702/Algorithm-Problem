import sys
def input(): return sys.stdin.readline().strip()

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.data = [0] * (size + 1)
    
    def sum(self, index):
        index += 1
        retval = 0
        while index:
            retval += self.data[index]
            index -= (-index&index)
        return retval
    
    def update(self, index, add_value):
        index += 1
        while index <= self.size:
            self.data[index] += add_value
            index += -index&index

data = FenwickTree(100000)

(N, T) = map(int, input().split())
for _ in range(N):
    K = int(input())
    for _ in range(K):
        (S, E) = map(int, input().split())
        data.update(S, 1)
        data.update(E, -1)

s, e = 0, -1

max_value = sum_value = sum([data.sum(i) for i in range(T)])
max_end = T-1
for i in range(T, 100000):
    sum_value += data.sum(i) - data.sum(i-T)
    if (max_value < sum_value):
        max_value = sum_value
        max_end = i
print(max_end - T + 1, max_end + 1)
