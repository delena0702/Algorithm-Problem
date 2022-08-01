import sys
def input(): return sys.stdin.readline().strip()

def get(idx):
    retval = 0
    while idx:
        retval = retval + fenwick[idx]
        idx = idx - (-idx & idx)
    return retval

def update(idx):
    while idx <= N:
        fenwick[idx] = fenwick[idx] + 1
        idx = idx + (-idx & idx)

N = int(input())
data = input().split()
dic = {}
for i in range(N):
    dic[data[i]] = i

fenwick = [0] * (N + 1)
answer = 0
for i, key in enumerate(input().split()):
    answer = answer + i - get(dic[key] + 1)
    update(dic[key] + 1)
print(answer)