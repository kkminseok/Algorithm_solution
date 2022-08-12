**c++**


```c++
class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        int* buy = new int[prices.size()];
        int* sell = new int[prices.size()];
        buy[0] = -prices[0];
        sell[0] = 0;
        for(size_t i = 1;i<prices.size();++i)
        {
            buy[i] = max(buy[i-1],sell[i-1] - prices[i]);
            sell[i] = max(sell[i-1], buy[i-1] + prices[i]-fee);
        }

        return sell[prices.size()-1];
    }
};
```

-----  

**python**

```python
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        size = len(prices)
        buy = [0] * size
        sell = [0] * size
        buy[0] = -prices[0]
        sell[0] = 0
        for i in range(1,size):
            buy[i] = max(buy[i-1], sell[i-1] - prices[i])
            sell[i] = max(sell[i-1] , buy[i-1] + prices[i]-fee)
        return sell[size-1]
```