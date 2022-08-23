from sys import stdin


def solution() -> int:
    def init():
        num = int(stdin.readline())
        data_list = list(map(int, stdin.readline().split()))
        return num, data_list

    n, input_list = init()
    dp = [0] * n
    delete_dp = [0] * n
    dp[0] = delete_dp[0] = input_list[0]
    max_num = input_list[0]

    for i in range(1, n):
        delete_dp[i] = max(delete_dp[i - 1] + input_list[i], dp[i - 1])
        dp[i] = max(dp[i - 1] + input_list[i], input_list[i])
        max_num = max(max_num, dp[i], delete_dp[i])
    return max_num


result = solution()
print(result)
