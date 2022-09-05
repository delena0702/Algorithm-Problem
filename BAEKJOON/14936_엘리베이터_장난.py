N, m = map(int, input().split())
answer = 1
t = [N, N // 2, (N + 1) // 2, (N + 2) // 3]
if t[0] <= m: answer += 1
if N > 1 and t[1] <= m: answer += 1
if N > 1 and t[2] <= m: answer += 1
if N > 2 and t[3] <= m: answer += 1
if N > 2 and t[3] + t[0] <= m: answer += 1
if N > 2 and t[3] + t[1] <= m: answer += 1
if N > 2 and t[3] + t[2] <= m: answer += 1
print(answer)