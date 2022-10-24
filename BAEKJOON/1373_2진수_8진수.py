import sys
def input(): return sys.stdin.readline().strip()

string = input()
N = len(string)
for i in range((N + 2) % 3 - 2, N, 3):
    print(int(string[max(i, 0):i + 3], 2), end='')