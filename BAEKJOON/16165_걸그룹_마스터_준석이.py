import sys
def input(): return sys.stdin.readline().strip()

N, M = map(int, input().split())
dic = [{}, {}]

for _ in range(N):
    title = input()
    cnt = int(input())

    dic[0][title] = []
    for _ in range(cnt):
        name = input()
        dic[0][title].append(name)
        dic[1][name] = title
    dic[0][title].sort()

for _ in range(M):
    name, type = input(), int(input())
    if type == 0:
        print(*dic[type][name], sep='\n')
    else:
        print(dic[type][name])
