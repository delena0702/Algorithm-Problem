import sys
def input(): return sys.stdin.readline().strip()

dr = [-1, -1, 0]
dc = [-1, 1, -1]
def dfs(r, c, bit_arr):
    global N, M, data, dp

    if r == N:
        return 0

    if bit_arr in dp[r][c]:
        return dp[r][c][bit_arr]
    
    nr, nc = divmod(r * M + c + 1, M)

    retval = dfs(nr, nc, ((1 << (M + 1)) - 1) & (bit_arr << 1))
    
    if data[r][c] == '.':
        check = True
        for i, idx in enumerate([M, M - 2, 0]):
            tr, tc = r + dr[i], c + dc[i]

            if tr < 0 or tr >= N or tc < 0 or tc >= M:
                continue
            
            if bit_arr & (1 << idx):
                check = False
                break

        if check:
            retval = max(retval, dfs(nr, nc, ((1 << (M + 1)) - 1) & (bit_arr << 1) | 1) + 1)
    
    dp[r][c][bit_arr] = retval
    return retval

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    dp = [[{} for _ in range(M)] for _ in range(N)]
    print(dfs(0, 0, 0))