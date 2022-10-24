import sys
def input(): return sys.stdin.readline().strip()

N, B, C = map(int, input().split())
arr = list(map(int, input().split()))

if B <= C:
    print(sum(arr) * B)
    exit()

answer = 0
for i in range(N - 2):
    if arr[i + 1] > arr[i + 2]:
        value = min(arr[i], arr[i + 1] - arr[i + 2])
        arr[i] -= value
        arr[i + 1] -= value
        answer += (B + C) * value

    value = min(arr[i], arr[i + 1], arr[i + 2])
    for j in range(i, i + 3):
        arr[j] -= value
    answer += (B + 2 * C) * value

    answer += B * arr[i]

minimum, maximum = min(arr[-1], arr[-2]), max(arr[-1], arr[-2])
answer += (B + C) * minimum + B * (maximum - minimum)
print(answer)
