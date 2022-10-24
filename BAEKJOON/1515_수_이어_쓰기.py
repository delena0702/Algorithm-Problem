import sys
def input(): return sys.stdin.readline().strip()

string = input()
i, j = 1, 0
while True:
    for ch in str(i):
        if j < len(string) and ch == string[j]:
            j += 1

    if j == len(string):
        print(i)
        break

    i += 1