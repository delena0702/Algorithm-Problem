import sys
def input(): return sys.stdin.readline().strip()

dx = [0, 1, -1]
dy = [1, 0, 0]

while True:
    N, M = map(int, input().split())
    if N == 0:
        break
    data = [input() for _ in range(N)]

    x, y = -1, 0
    for i in range(0, M):
        if data[0][i] == 'S':
            x = i
            break
    
    px, py, pi, ppi = -1, -1, -1, -1
    answer = 1
    while True:
        for i in range(3):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if nx == px and ny == py:
                continue
            if data[ny][nx] != 'S':
                continue

            if pi or (i == 0 or i == ppi):
                answer = answer + 1
            else:
                ppi = i
            
            px, py, pi = x, y, i
            x, y = nx, ny
            break
        
        else:
            break
    
    print(answer)