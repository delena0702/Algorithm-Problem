import sys
import re
def input(): return sys.stdin.readline().strip()

data = input()
r = re.compile("d2", flags=re.IGNORECASE)
print("D2" if r.search(data) else "unrated")