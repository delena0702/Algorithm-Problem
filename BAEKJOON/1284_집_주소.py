import sys
def input(): return sys.stdin.readline().strip()

while True:
    N = input()

    if N == "0":
        break
    
    answer = 1
    for ch in N:
        if ch == '0': answer = answer + 5
        elif ch == '1': answer = answer + 3
        else: answer = answer + 4
    print(answer)