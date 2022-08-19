from sys import stdin
from collections import deque


def solution() -> None:
    n = int(stdin.readline())
    input_list = list(map(int, stdin.readline().split()))
    dp = [1] * n
    result = []
    size = 1
    data_dict = {1: deque([input_list[0]])}
    for i in range(n):
        for j in range(i - 1, -1, -1):
            if input_list[i] > input_list[j]:
                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    if dp[j] + 1 not in data_dict.keys():
                        data_dict[dp[j] + 1] = deque()
                        size = max(size, dp[j] + 1)
                    data_dict[dp[j] + 1].append(input_list[i])
            if j == 0 and dp[i] == 1:
                data_dict[1].append(input_list[i])

    max_num = data_dict[size][0]
    result.append(max_num)
    for i in range(size - 1, 0, -1):
        for data in data_dict[i]:
            if max_num > data:
                result.append(data)
                max_num = data
                break

    print(size)
    print(' '.join(map(str, result[::-1])))


solution()
