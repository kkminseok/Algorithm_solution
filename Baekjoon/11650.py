from operator import itemgetter
from sys import stdin

n = int(stdin.readline())

result = []

for i in range(n):
    data = tuple(map(int, stdin.readline().split()))
    result.append(data)

list.sort(result, key=itemgetter(0, 1))
for x, y in result:
    print(x, y)
