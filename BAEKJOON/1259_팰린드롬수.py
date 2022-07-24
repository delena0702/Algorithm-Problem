import sys
def input(): return sys.stdin.readline().strip()


while True:
    num = input()
    if num == "0":
        break
    if num == num[::-1]:
        print("yes")
    else:
        print("no")
