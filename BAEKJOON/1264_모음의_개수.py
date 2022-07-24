import re
import sys
def input(): return sys.stdin.readline().strip()

regex = re.compile("[aeiou]", re.IGNORECASE)

while True:
    string = input()
    if string == "#":
        break
    print(len(regex.findall(string)))