from collections import defaultdict
import sys
def input(): return sys.stdin.readline().strip()


order = [(0, 'Z'), (2, 'W'), (4, 'U'), (6, 'X'), (8, 'G'),
         (1, 'O'), (3, 'H'), (5, 'F'), (7, 'S'), (9, 'E')]
words = "ZERO ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE".split()

T = int(input())
for test_case in range(T):
    counter = defaultdict(int)
    for ch in input():
        counter[ch] = counter[ch] + 1

    answer = [0] * 10
    for num, ch in order:
        cnt = counter[ch]
        answer[num] = cnt
        for ch in words[num]:
            counter[ch] = counter[ch] - cnt

    print(f"Case #{test_case + 1}: ", end='')
    for i, cnt in enumerate(answer):
        print(* [i] * cnt, sep='', end='')
    print()
