```python
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return n
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        answer = 0
        for i in range(1,n+1):
            if i % 2 == 0:
                dp[i] = dp[i//2]
            else:
                dp[i] = dp[i//2] + dp[i//2 + 1]
            answer = max(answer,dp[i])
        return answer
```