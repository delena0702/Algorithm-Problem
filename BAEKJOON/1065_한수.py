N, answer = int(input()), 0

for num in range(1, N + 1):
    arr = list(map(int, str(num)))
    if len(arr) <= 2:
        answer = answer + 1
        continue

    d = arr[1] - arr[0]
    for i in range(1, len(arr) - 1):
        if arr[i + 1] - arr[i] != d:
            break
    else:
        answer = answer + 1
        pass

print(answer)