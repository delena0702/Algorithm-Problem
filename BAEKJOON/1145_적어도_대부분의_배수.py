from math import lcm
from itertools import combinations
print(min(map(lambda x: lcm(*x), combinations(map(int, input().split()), 3))))