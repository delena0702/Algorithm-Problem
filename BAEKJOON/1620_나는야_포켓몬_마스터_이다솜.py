import sys
def input(): return sys.stdin.readline().strip()

N, M = map(int, input().split())
dic = {}
for i in range(1, N + 1):
    name = input()
    dic[str(i)] = name
    dic[name] = i

for _ in range(M):
    print(dic[input()])