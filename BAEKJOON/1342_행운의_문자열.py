from itertools import permutations
import sys
def input(): return sys.stdin.readline().strip()

string = input()
N = len(string)
answer = set()
for arr in permutations(string, N):
    for i in range(N - 1):
        if arr[i] == arr[i + 1]:
            break
    else:
        answer.add(str(arr))
print(len(answer))