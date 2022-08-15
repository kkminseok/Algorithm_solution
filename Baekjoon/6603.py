from itertools import combinations
from sys import stdin

while True:
    data = list(map(str, stdin.readline().split()))
    if data[0] == '0':
        break
    new_data = list(combinations(data[1:], 6))
    for output in new_data:
        print(' '.join(list(output)), end="\n")
    print()
