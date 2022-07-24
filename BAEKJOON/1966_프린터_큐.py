import sys
def input(): return sys.stdin.readline().strip()

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    visited = [False] * N
    idx, now, last, cnt = 0, max(data), N - 1, 0
    
    while True:
        if not visited[idx] and now == data[idx]:
            visited[idx] = True
            cnt = cnt + 1
            last = idx

            if idx == M:
                print(cnt)
                break

        elif idx == last:
            now = now - 1

        idx = (idx + 1) % N
