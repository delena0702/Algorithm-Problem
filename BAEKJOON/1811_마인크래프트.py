import sys
def input(): return sys.stdin.readline().strip()

N, M, B = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

answer = [float('inf'), -1]
for height in range(max(map(lambda x: max(x), data)), min(map(lambda x: min(x), data)) - 1, -1):
    temp = 0
    blocks = B
    for i in range(N):
        for j in range(M):
            now = data[i][j]
            if now > height:
                temp = temp + 2 * (now - height)
            elif now < height:
                temp = temp + height - now
            blocks = blocks + now - height
    
    if blocks >= 0 and temp < answer[0]:
        answer[0] = temp
        answer[1] = height
print(*answer, sep=' ')