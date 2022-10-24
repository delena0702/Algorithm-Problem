import sys
def input(): return sys.stdin.readline().strip()

def combine(n, k):
    retval = 1
    for i in range(1, k + 1):
        retval = retval * (n - i + 1) // i
    return retval

N, M, K = map(int, input().split())
answer = 0
for i in range(K, M + 1):
    answer += combine(M, i) * combine(N - M, M - i)
print(answer / combine(N, M))