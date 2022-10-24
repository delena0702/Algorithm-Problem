import sys
def input(): return sys.stdin.readline().strip()

string = input()
i = 0
while len(string) > 1:
    cnt = 0
    for ch in string:
        cnt += int(ch)
    string = str(cnt)
    i += 1
print(i, "NO" if int(string) % 3 else "YES", sep='\n')