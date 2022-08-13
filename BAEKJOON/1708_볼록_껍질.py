from functools import cmp_to_key
import sys
def input(): return sys.stdin.readline().strip()
def sub(a, b): return (a[0] - b[0], a[1] - b[1])
def ccw(a, b): return a[0] * b[1] - a[1] * b[0]

N = int(input())
data = [tuple(map(int, input().split())) for _ in range(N)]

pivot = min(data)
queue = list(filter(lambda x: x != pivot, data))

def cmp(a, b):
    a, b = sub(a, pivot), sub(b, pivot)
    cp = -ccw(a, b)
    if cp:
        return cp
    return a[0] ** 2 + a[1] ** 2 - b[0] ** 2 - b[1] ** 2

queue.sort(key=cmp_to_key(cmp))
stack = [pivot]
for p in queue:
    while len(stack) >= 2 and ccw(sub(stack[-1], stack[-2]), sub(p, stack[-1])) <= 0:
        stack.pop()
    stack.append(p)
print(len(stack))