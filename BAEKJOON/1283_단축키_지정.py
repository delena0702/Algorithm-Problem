import sys
def input(): return sys.stdin.readline().strip()


N = int(input())
arr = [input() for _ in range(N)]

check = set()

for string in arr:
    if len(string) == 0:
        print(string)
        continue

    if string[0].upper() not in check:
        check.add(string[0].upper())
        print(f"[{string[0]}]{string[1:]}")
        continue

    for i in range(1, len(string)):
        if string[i - 1] == ' ' and string[i] != ' ' and string[i].upper() not in check:
            check.add(string[i].upper())
            print(f"{string[:i]}[{string[i]}]{string[i + 1:]}")
            break
    else:
        for i in range(0, len(string)):
            if string[i] != ' ' and string[i].upper() not in check:
                check.add(string[i].upper())
                print(f"{string[:i]}[{string[i]}]{string[i + 1:]}")
                break
        else:
            print(string)
