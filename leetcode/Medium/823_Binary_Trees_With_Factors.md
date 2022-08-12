**c++**

```c++
class Solution {
public:
    int numFactoredBinaryTrees(vector<int>& arr) {
        int mod = pow(10,9) + 7;
        sort(arr.begin(),arr.end());
        unordered_map<int,long> dp;
        long result = 0;
        for(size_t i =0;i<arr.size();++i)
        {
            dp[arr[i]] = 1;
            for(int j = 0 ; j<i;++j)
            {
                if(arr[i] % arr[j] == 0)
                    dp[arr[i]] = (dp[arr[i]] + dp[arr[j]] * dp[arr[i] /arr[j]]) %mod;
            }
            result =  (result + dp[arr[i]])%mod;
        }
        return result;
    }
};


```

-----

**python**

```python
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        dp ={}
        result = 0
        mod = pow(10,9) + 7
        arr.sort()
        
        for i in range(len(arr)):
            dp[arr[i]] = 1
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    if(arr[i]//arr[j]) in dp : 
                        dp[arr[i]] = (dp[arr[i]] + dp[arr[j]] *(dp[arr[i] // arr[j]])) %mod
                    else:
                        dp[arr[i]//arr[j]] =0
            result = (result+ dp[arr[i]]) %mod
        
        return result
```