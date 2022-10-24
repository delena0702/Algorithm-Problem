import sys
def input(): return sys.stdin.readline().strip()

eng = "zero one two three four five six seven eight nine".split()

M, N = map(int, input().split())
arr = []
for i in range(M, N + 1):
    result = []
    for ch in str(i):
        result.append(eng[int(ch)])
    arr.append((' '.join(result), i))
arr.sort()

for i in range(len(arr)):
    print(arr[i][1], end=' ')
    if i % 10 == 9:
        print()