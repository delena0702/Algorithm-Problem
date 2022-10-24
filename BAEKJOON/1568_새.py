import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
answer = 0
while N:
    i = 1
    while True:
        if N - i < 0:
            break
        N -= i
        answer += 1
        i += 1
print(answer)