import sys
def input(): return sys.stdin.readline().strip()

sample = "SUN, MON, TUE, WED, THU, FRI, SAT".split(", ")
arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
psum = [0] * 12
for i in range(1, 12):
    psum[i] = psum[i - 1] + arr[i - 1]
x, y = map(int, input().split())
answer = (1 + psum[x - 1] + y - 1) % 7
print(sample[answer])