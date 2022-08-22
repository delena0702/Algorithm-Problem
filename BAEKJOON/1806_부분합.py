import sys
sys.stdin = open("1.txt")
def input(): return sys.stdin.readline().strip()


def max_sum(idx):
    answer, psum = float('inf'), 0
    for i, num in enumerate(data):
        if i < idx:
            psum = psum + num
            if i == idx - 1:
                answer = psum
            continue
        psum = psum + num - data[i - idx]
        answer = max(answer, psum)
    return answer


N, S = map(int, input().split())
data = list(map(int, input().split()))

s, e = 1, N + 1
while s < e:
    m = (s + e) // 2
    if max_sum(m) >= S:
        e = m
    else:
        s = m + 1
print(e if e <= N else 0)
