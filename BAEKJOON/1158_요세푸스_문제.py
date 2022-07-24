import sys
def input(): return sys.stdin.readline().strip()

(N, K) = map(int, input().split())
data = [i for i in range(1, N + 1)]
ind, answer = K - 1, []
while True:
    answer.append(data.pop(ind))
    if not data: break
    ind = (ind + K - 1) % len(data)

print(f"<{', '.join(map(str, answer))}>")