import sys
def input(): return sys.stdin.readline().strip()

N, M = int(input()), int(input())
if M:
    ignore = set(input().split())
else:
    ignore = set()

answer = abs(N - 100)
for i in range(10 * (N + 1)):
    is_continue = False
    for ch in str(i):
        if ch in ignore:
            is_continue = True
            break
    if is_continue:
        continue
    answer = min(answer, len(str(i)) + abs(N - i))
print(answer)