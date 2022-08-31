import sys
def input(): return sys.stdin.readline().strip()

string = input()
stack, answer, pre = 0, 0, '_'
for ch in string:
    if ch == '(':
        stack = stack + 1
    else:
        stack = stack - 1
        answer = answer + (stack if pre == '(' else 1)
    pre = ch
print(answer)