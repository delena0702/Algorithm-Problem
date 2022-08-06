def toNumber(ch):
    if ch >= 'A' and ch <= 'C': return 3
    if ch >= 'D' and ch <= 'F': return 4
    if ch >= 'G' and ch <= 'I': return 5
    if ch >= 'J' and ch <= 'L': return 6
    if ch >= 'M' and ch <= 'O': return 7
    if ch >= 'P' and ch <= 'S': return 8
    if ch >= 'T' and ch <= 'V': return 9
    if ch >= 'W' and ch <= 'Z': return 10

print(sum(map(toNumber, input())))