**python**

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [987654] * (amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i],dp[i-coins[j]]+1)
        return -1 if dp[amount] == 987654 else dp[amount]
```

-----  

**c++**

```c++
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        sort(coins.begin(),coins.end());
        int* dp = new int[amount+1];
        dp[0]=0;
        for(int i =1;i<amount+1;++i)
            dp[i]= 987654;
        
        for(int i =1;i<=amount; ++i)
        {
            for(int j = 0; j<coins.size();++j)
            {
                if(coins[j]<=i)
                    dp[i] = min(dp[i], dp[i -coins[j]] +1 );
            }
        }
        return dp[amount] == 987654 ? -1 : dp[amount];
    }
};
```