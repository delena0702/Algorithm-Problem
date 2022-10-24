from datetime import datetime
import sys
def input(): return sys.stdin.readline().strip()

months = "0,January,February,March,April,May,June,July,August,September,October,November,December".split(',')
string = input().split()
Y = int(string[2])
M = months.index(string[0])
D = int(string[1][:-1])
h = int(string[3].split(":")[0])
m = int(string[3].split(":")[1])
print(100 * (datetime(Y, M, D, h, m) - datetime(Y, 1, 1, 0, 0)) / (datetime(Y + 1, 1, 1, 0, 0) - datetime(Y, 1, 1, 0, 0)))