import re
regex = re.compile('^(100+1+|01)+$')
for _ in range(int(input())):
    print("YES" if regex.match(input()) else "NO")
