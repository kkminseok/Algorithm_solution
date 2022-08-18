from sys import stdin
from collections import deque

input_list = []

dp = deque([0, 1, 2, 4])
max_num = 0
mod = 1000000009


def init():
    def data_input():
        t = int(stdin.readline())

        for i in range(t):
            input_list.append(int(stdin.readline()))

    data_input()
    global max_num
    max_num = max(input_list)


def result():
    for i in range(4, max_num + 1):
        dp.append((dp[i - 1] + dp[i - 2] + dp[i - 3]) % mod)

    for data in input_list:
        print(dp[data])


def solution():
    init()
    result()


solution()
