import sys
def input(): return sys.stdin.readline().strip()

K = int(input())
data = []
for _ in range(K):
    num = int(input())
    if num == 0:
        data.pop()
    else:
        data.append(num)
print(sum(data))