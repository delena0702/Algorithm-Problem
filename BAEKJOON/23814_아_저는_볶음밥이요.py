D = int(input())
N, M, K = map(int, input().split())
target, answer = (N + M + K) // D, 0

if N // D + M // D + K // D == target:
    answer = max(answer, K)
if (K - (-N % D)) >= 0 and (N + (-N % D)) // D + M // D + (K - (-N % D)) // D == target:
    answer = max(answer, K - (-N % D))
if (K - (-M % D)) >= 0 and N // D + (M + (-M % D)) // D + (K - (-M % D)) // D == target:
    answer = max(answer, K - (-M % D))
if (K - (-N % D) - (-M % D)) >= 0 and (N + (-N % D)) // D + (M + (-M % D)) // D + (K - (-N % D) - (-M % D)) // D == target:
    answer = max(answer, K - (-N % D) - (-M % D))
print(answer)