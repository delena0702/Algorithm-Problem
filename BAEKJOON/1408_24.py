import sys
def input(): return sys.stdin.readline().strip()

s = list(map(int, input().split(":")))
n = list(map(int, input().split(":")))
n[0] += 24

answer = [0, 0, 0]
for i in range(2, -1, -1):
    answer[i] = n[i] - s[i]
    while answer[i] < 0:
        n[i - 1] -= 1
        answer[i] += 60
answer[0] %= 24
print(f"{answer[0]:02d}:{answer[1]:02d}:{answer[2]:02d}")