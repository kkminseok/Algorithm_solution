**c++**

```c++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int* buy = new int[prices.size()];
        int* sell = new int[prices.size()];
        buy[0] = -prices[0];
        sell[0] = 0;
        int result = 0;
        for(int i =1;i<prices.size();++i){
            buy[i] = max(buy[i-1],sell[i-1] - prices[i]);
            sell[i] = max(sell[i-1],buy[i-1] + prices[i]);
            result = max(result,sell[i]);
        }
        return result;
    }
};
```