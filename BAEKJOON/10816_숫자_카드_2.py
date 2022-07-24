from collections import Counter
import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
query = list(map(int, input().split()))
counter = Counter(cards)

for num in query:
    print(counter[num], end=' ')