import sys
def input(): return sys.stdin.readline().strip()


N = int(input())
answer = [int(input()) for _ in range(N)]
next, stack, now, result = 1, [], 0, ''

while now < N and next <= answer[now]:
    while next <= answer[now]:
        stack.append(next)
        next += 1
        result += '+\n'

    while stack and stack[-1] == answer[now]:
        stack.pop()
        now += 1
        result += '-\n'

print(result if now == N else 'NO')
