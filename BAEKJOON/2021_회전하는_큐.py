import sys
def input(): return sys.stdin.readline().strip()


(N, M) = map(int, input().split())
fw, data = [0] * (N + 1), list(map(int, input().split()))


def fw_sum(n):
    retval = 0
    while n:
        retval += fw[n]
        n -= -n & n
    return retval


def fw_update(n):
    while n <= N:
        fw[n] += 1
        n += -n & n


here, answer = 1, 0
for (i, next) in enumerate(data):
    data[i] -= fw_sum(next)
    fw_update(next)
    answer += min(abs(data[i] - here), N - i - abs(data[i] - here))
    here = data[i]
print(answer)