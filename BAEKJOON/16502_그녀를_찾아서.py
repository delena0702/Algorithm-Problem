import sys
def input(): return sys.stdin.readline().strip()

def index(ch): return ord(ch) - ord('A')

T = int(input())
M = int(input())
data = [[0] * 4 for _ in range(4)]
for _ in range(M):
    a, b, p = input().split()
    data[index(a)][index(b)] = float(p)

answer = [25] * 4
for _ in range(T):
    next_answer = [0] * 4
    for i in range(4):
        for j in range(4):
            next_answer[i] += answer[j] * data[j][i]
    answer = next_answer
for i in range(4):
    print(f"{answer[i]:.2f}")