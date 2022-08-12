from itertools import permutations
from collections import deque

n = int(input())
travel_map = deque()
result_sum = 10e9

load = [i for i in range(1, n + 1)]
for i in range(n):
    tmp_li = deque(map(int, input().split()))
    travel_map.append(tmp_li)

for result in permutations(load):
    tmp_sum = 0
    judge = False
    for i in range(len(result) - 1):
        data = travel_map[result[i] - 1][result[i + 1] - 1]
        if data <= 0:
            judge = True
            break
        tmp_sum += data
    cycle_data = travel_map[result[i + 1] - 1][result[0] - 1]
    if cycle_data == 0 or judge:
        continue
    tmp_sum += cycle_data
    result_sum = min(result_sum, tmp_sum)
print(result_sum)
