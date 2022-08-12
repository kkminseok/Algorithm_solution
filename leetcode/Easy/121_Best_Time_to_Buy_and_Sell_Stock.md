```c++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int result = 0;
        int minprice = INT_MAX;
        for(size_t i =0;i<prices.size();++i)
        {
            minprice= min(minprice,prices[i]);
            result = max(result, prices[i]-minprice);
        }
        
        return result;
    }
};
```