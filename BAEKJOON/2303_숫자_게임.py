from itertools import combinations
import sys
def input(): return sys.stdin.readline().strip()

def getKey(cards):
    answer = 0
    for card in combinations(cards, 3):
        answer = max(answer, sum(card) % 10)
    return answer

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
order = list(range(N))
order.sort(reverse=True, key=lambda i: (getKey(arr[i]), i))
print(order[0] + 1)