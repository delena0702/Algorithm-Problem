M, N = int(input()), int(input())
is_prime = [True] * (N + 1)

for i in range(2, N + 1):
    if not is_prime[i]:
        continue
    for j in range(2 * i, N + 1, i):
        is_prime[j] = False
is_prime[1] = False

answer = [0, 0]
for i in range(M, N + 1):
    if not is_prime[i]:
        continue
    answer[0] += i
    if answer[1] == 0:
        answer[1] = i
if answer[0] == 0:
    print(-1)
else:
    print(*answer, sep='\n')