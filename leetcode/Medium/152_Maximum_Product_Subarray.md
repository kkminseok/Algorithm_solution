
**python**

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP = -11
        minP = 11
        result = -98765321
        for i in range(len(nums)):
            if nums[i] < 0 : 
                temp = maxP
                maxP = minP
                minP = temp
            maxP = max(nums[i],maxP * nums[i])
            minP = min(nums[i],minP * nums[i])
            result = max(maxP,result)
            
        return result
```

-----  

**c++**

```c++
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        if(nums.size()==0)
            return 0;
        int maxP = 1;
        int minP = 1;
        int result = INT_MIN;
        for(auto i =0 ; i<nums.size();++i)
        {
            if(nums[i]<0)
                swap(maxP,minP);
            maxP = max(nums[i],nums[i] * maxP);
            minP = min(nums[i],nums[i] * minP);
            result = max(result,maxP);
        }

    
        return result;
    }

};
```