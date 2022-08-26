import sys
def input(): return sys.stdin.readline().strip()

N, M = map(int, input().split())
data = list(map(int, input().split()))
s, e = 0, -1
answer, psum = 0, 0

while True:
    if psum <= M:
        if psum == M:
            answer = answer + 1
        if e + 1 == N:
            break
        psum = psum + data[e + 1]
        e = e + 1
    else:
        psum = psum - data[s]
        s = s + 1
print(answer)