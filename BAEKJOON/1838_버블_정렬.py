import sys
def input(): return sys.stdin.readline().strip()


N = int(input())
data = list(map(int, input().split()))
dic, answer = {}, 0

for i, d in enumerate(sorted(data)):
	dic[d] = i

for i, d in enumerate(data):
	answer = max(answer, i - dic[d] if i - dic[d] > 0 else 0)

print(answer)
