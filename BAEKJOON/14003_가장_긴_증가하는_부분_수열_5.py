import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
data = list(map(int, input().split()))

answer = []
pre_node = [-1] * N
for i, num in enumerate(data):
    s, e = 0, len(answer)
    while s < e:
        m = (s + e) // 2
        if num <= data[answer[m]]:
            e = m
        else:
            s = m + 1
            
    if e == len(answer):
        answer.append(i)
    else:
        answer[e] = i
    if e:
        pre_node[i] = answer[e - 1]

for i in range(len(answer) - 2, -1, -1):
    answer[i] = pre_node[answer[i + 1]]

print(len(answer))
print(*map(lambda x: data[x], answer), sep=' ')