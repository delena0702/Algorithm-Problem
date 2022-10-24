import sys
def input(): return sys.stdin.readline().strip()

string = input()[::-1]

arr = []
for i in range(2, len(string)):
    arr.append(string[i:])
arr.sort()

string = string[:-len(arr[0])]
answer = arr[0]

arr = []
for i in range(1, len(string)):
    arr.append(string[i:])
arr.sort()

answer = answer + arr[0] + string[:-len(arr[0])]
print(answer)