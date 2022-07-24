import sys
def input(): return sys.stdin.readline().strip()


class LazySegTree:
    def __init__(self, size):
        self.size = size
        self.data = [0] * (4*size)
        self.lazy = [0] * (4*size)

    def sum(self, start, end):
        return self.__sum(start, end, 1, 1, self.size)

    def __sum(self, start, end, node, l, r):
        if r < start or end < l:
            return 0

        if self.lazy[node]:
            if l != r:
                self.lazy[2*node] += self.lazy[node]
                self.lazy[2*node+1] += self.lazy[node]
            self.data[node] += self.lazy[node]*(r - l + 1)
            self.lazy[node] = 0

        if start <= l and r <= end:
            return self.data[node]
        m = (l+r)//2
        return self.__sum(start, end, 2*node, l, m) + self.__sum(start, end, 2*node + 1, m + 1, r)

    def update(self, start, end, add_value):
        return self.__update(start, end, add_value, 1, 1, self.size)

    def __update(self, start, end, add_value, node, l, r):
        if r < start or end < l:
            return
        if start <= l and r <= end:
            self.lazy[node] += add_value
            return
        self.data[node] += (min(r, end) - max(l, start) + 1)*add_value
        m = (l+r)//2
        self.__update(start, end, add_value, 2*node, l, m)
        self.__update(start, end, add_value, 2*node+1, m+1, r)
        return


(N, M, K) = map(int, input().split())
lst = LazySegTree(N)
for i in range(1, N+1):
    lst.update(i, i, int(input()))

for i in range(M+K):
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        lst.update(arr[1], arr[2], arr[3])
    else:
        print(lst.sum(arr[1], arr[2]))
