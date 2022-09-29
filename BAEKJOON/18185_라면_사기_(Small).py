import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
arr = list(map(int, input().split()))

answer = 0
for i in range(N - 2):
    if arr[i + 1] > arr[i + 2]:
        value = min(arr[i], arr[i + 1] - arr[i + 2])
        arr[i] -= value
        arr[i + 1] -= value
        answer += 5 * value

    value = min(arr[i], arr[i + 1], arr[i + 2])
    for j in range(i, i + 3):
        arr[j] -= value
    answer += 7 * value

    answer += 3 * arr[i]

minimum, maximum = min(arr[-1], arr[-2]), max(arr[-1], arr[-2])
answer += 5 * minimum + 3 * (maximum - minimum)

print(answer)
