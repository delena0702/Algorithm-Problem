import sys
input = sys.stdin.readline().strip()
input = '#'+'#'.join(input)+'#'
N = len(input)
a = [0]*N
(r, p) = (0, 0)
answer = 0

for i in range(N):
    a[i] = min([a[2*p-i], r-i]) if i <= r else 0

    while (i - a[i] - 1 >= 0 and i + a[i] + 1 < N and input[i-a[i]-1] == input[i+a[i]+1]):
        a[i] += 1

    if (r < i + a[i]):
        r = i + a[i]
        p = i

    answer += (a[i]+1)//2

print(answer)
