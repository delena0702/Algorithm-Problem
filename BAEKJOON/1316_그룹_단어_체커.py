import sys
def input(): return sys.stdin.readline().strip()

N, answer = int(input()), 0
for _ in range(N):
    check, pre = set(), ''

    for ch in input():
        if ch != pre:
            if ch in check:
                break
            check.add(ch)
        pre = ch
    else:
        answer = answer + 1

print(answer)
