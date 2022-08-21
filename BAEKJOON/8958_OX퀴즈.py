import sys
def input(): return sys.stdin.readline().strip()

T = int(input())
for _ in range(T):
    string = input()
    answer, cnt = 0, 0
    for ch in string:
        if ch == 'O':
            answer, cnt = answer + cnt + 1, cnt + 1
        else:
            cnt = 0
    print(answer)