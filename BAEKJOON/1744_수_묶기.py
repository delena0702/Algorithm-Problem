import sys
def input(): return sys.stdin.readline().strip()

N, data = int(input()), [[], []]
for num in [int(input()) for _ in range(N)]:
    if num > 0:
        data[0].append(num)
    else:
        data[1].append(num)

data[0].sort(reverse=True)
data[1].sort()

answer = 0
for i in range(1, len(data[0]), 2):
    if data[0][i] == 1:
        answer += data[0][i] + data[0][i - 1]
    else:
        answer += data[0][i] * data[0][i - 1]
if len(data[0]) % 2:
    answer += data[0][-1]

for i in range(1, len(data[1]), 2):
    answer += data[1][i] * data[1][i - 1]
if len(data[1]) % 2:
    answer += data[1][-1]

print(answer)