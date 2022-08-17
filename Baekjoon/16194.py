from sys import stdin

n = int(stdin.readline())


def make_dp(size: int) -> list:
    return [0 for _ in range(size + 1)]


def soultion(dp: list, price: list) -> None:
    for i in range(1, len(price) + 1):
        dp[i] = price[i - 1]
        for j in range(1, (i // 2) + 1):
            dp[i] = min(dp[i], dp[j] + dp[i - j])
    print(dp[n])


price = list(map(int, stdin.readline().split()))

dp = make_dp(len(price))
dp[1] = price[0]
soultion(dp, price)
