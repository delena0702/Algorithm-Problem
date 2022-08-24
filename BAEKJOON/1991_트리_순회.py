import sys
def input(): return sys.stdin.readline().strip()

def dfs(here):
    if here == '.':
        return
    answer[0].append(here)
    dfs(children[here][0])
    answer[1].append(here)
    dfs(children[here][1])
    answer[2].append(here)

N = int(input())

children = {}
for _ in range(N):
    parent, l, r = input().split()
    children[parent] = (l, r)

answer = [[] for _ in range(3)]
dfs('A')
for i in range(3):
    print(*answer[i], sep='')