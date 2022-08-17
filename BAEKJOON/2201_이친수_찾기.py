import sys
def input(): return sys.stdin.readline().strip()


K = int(input())

if K <= 2:
    print(bin(K)[2:])
    exit()

dp, psum = [1, 1], [1, 2]
i = 2
while True:
    dp.append(psum[i - 2] + 1)
    psum.append(psum[i - 1] + dp[i])
    if K <= psum[i]:
        break
    i = i + 1

answer = 0
remain = K
while remain:
    # Lower Bound
    s, e = 0, len(dp)
    while s < e:
        m = (s + e) // 2
        if psum[m] >= remain:
            e = m
        else:
            s = m + 1

    answer = answer | (1 << s)
    if s:
        remain = remain - psum[s - 1] - 1
    else:
        remain = 0

print(bin(answer)[2:])
