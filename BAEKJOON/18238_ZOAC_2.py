import sys
def input(): return sys.stdin.readline().strip()


data, answer = "A" + input(), 0
for i in range(len(data) - 1):
    d = abs(ord(data[i+1]) - ord(data[i]))
    answer += min(d, 26 - d)
print(answer)
