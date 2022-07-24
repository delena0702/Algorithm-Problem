import sys
def input(): return sys.stdin.readline().strip()


class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.data = [0] * (size + 1)

    def sum(self, index):
        retval = 0
        while index:
            retval += self.data[index]
            index -= (-index & index)
        return retval

    def update(self, index, add_value):
        while index <= self.size:
            self.data[index] += add_value
            index += -index & index


N = int(input())
fw = FenwickTree(N)
for (i, n) in enumerate(map(int, input().split())):
    fw.update(i + 1, n)
    fw.update(i + 2, -n)

M = int(input())
for i in range(M):
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        fw.update(arr[1], arr[3])
        fw.update(arr[2] + 1, -arr[3])
    else:
        print(fw.sum(arr[1]))
