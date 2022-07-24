import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
data = [input() for _ in range(N)]    
data.sort(key=lambda x: (len(x), x))

for i in range(N):
    if i > 0 and data[i - 1] == data[i]:
        continue
    print(data[i])