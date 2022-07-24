import re
import sys
def input(): return sys.stdin.readline()

while True:
    string = input()
    if string == "." or string == ".\n":
        break
    string = re.sub(r"[^\(\)\[\]]", "", string)
    stack = []
    for ch in string:
        if ch == '(' or ch == '[':
            stack.append(ch)
        elif ch == ')':
            if len(stack) == 0 or stack[-1] != '(':
                print("no")
                break
            stack.pop()
        elif ch == ']':
            if len(stack) == 0 or stack[-1] != '[':
                print("no")
                break
            stack.pop()
    else:
        if len(stack) == 0:
            print("yes")
        else:
            print("no")