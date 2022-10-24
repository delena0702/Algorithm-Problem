import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
arr = [int(input().split('.')[1]) for _ in range(N)]

for i in range(1, 1001):
    s = set()
    for j in range(i):
        s.add(1000 * j // i)
    
    for num in arr:
        if num not in s:
            break
    else:
        print(i)
        break