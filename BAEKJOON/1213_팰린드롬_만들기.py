from collections import defaultdict
import sys
def input(): return sys.stdin.readline().strip()

counter = defaultdict(int)
for ch in input():
    counter[ch] += 1

check = False
answer = ''
temp = ''
for ch, cnt in sorted(counter.items()):
    answer += ch * (cnt // 2)
    if cnt % 2:
        temp += ch

if len(temp) < 2:
    print(answer + temp + answer[::-1])
else:
    print("I'm Sorry Hansoo")