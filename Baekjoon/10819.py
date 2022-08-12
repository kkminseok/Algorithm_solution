from itertools import permutations

n = int(input())
li = list(map(int, input().split()))
result_sum = 0
for result in permutations(li):
    tmp_sum = 0
    for i in range(n - 1):
        tmp_sum += abs(result[i] - result[i + 1])
    result_sum = max(result_sum, tmp_sum)
print(result_sum)
