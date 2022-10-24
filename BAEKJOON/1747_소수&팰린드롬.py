import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
is_prime = [True] * 1003002
for i in range(2, 1003002):
    if not is_prime[i]:
        continue
    if i >= N and str(i) == str(i)[::-1]:
        print(i)
        break
    for j in range(2 * i, 1003002, i):
        is_prime[j] = False