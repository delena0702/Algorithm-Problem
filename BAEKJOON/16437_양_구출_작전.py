import sys
sys.setrecursionlimit(200000)
def input(): return sys.stdin.readline().strip()

N = int(input())
arr = [0, 0]
children = [[] for _ in range(N + 1)]
for i in range(2, N + 1):
    inp = input().split()
    arr.append(int(inp[1]) if inp[0] == 'S' else -int(inp[1]))
    children[int(inp[2])].append(i)

def dfs(here):
    retval = 0
    for there in children[here]:
        retval += dfs(there)
    return max(0, retval + arr[here])

print(dfs(1))