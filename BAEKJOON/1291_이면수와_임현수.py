import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
is_prime = [0] * (N + 1)
is_prime[1] = 1
for i in range(2, N + 1):
    if is_prime[i]:
        continue
    is_prime[i] = i
    for j in range(2 * i, N + 1, i):
        is_prime[j] = i

temp, cnt = N, set()
while temp != is_prime[temp]:
    cnt.add(is_prime[temp])
    temp //= is_prime[temp]
cnt.add(temp)

answer = [False, False]

if N >= 6 and sum(map(int, str(N))) % 2:
    answer[0] = True
if N == 2 or N == 4 or len(cnt) % 2 == 0:
    answer[1] = True

if answer[0] and not answer[1]:
    print(1)
elif not answer[0] and answer[1]:
    print(2)
elif not answer[0] and not answer[1]:
    print(3)
elif answer[0] and answer[1]:
    print(4)