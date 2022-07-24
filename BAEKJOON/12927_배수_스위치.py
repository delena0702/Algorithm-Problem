import sys
def input(): return sys.stdin.readline().strip()


data = list(map(lambda x: x == 'Y', list(input())))
N = len(data)

answer = 0
for i in range(1, N+1):
    if not data[i-1]:
        continue
    for j in range(i, N+1, i):
        data[j-1] = not data[j-1]
    answer += 1
print(answer)
