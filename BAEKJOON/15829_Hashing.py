import sys
def input(): return sys.stdin.readline().strip()

A, MOD = 31, 1234567891
L, data = int(input()), input()
answer = 0
for i in range(L - 1, -1, -1):
    answer = (answer * A + ord(data[i]) - ord('a') + 1) % MOD
print(answer)
