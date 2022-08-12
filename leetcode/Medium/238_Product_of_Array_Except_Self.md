**python**

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        result = [1] * size
        for i in range(1,size):
            result[i] = result[i-1] * nums[i-1]
        right = 1
        for i in range(size-1,-1,-1):
            result[i] *= right
            right *= nums[i]
        return result
```

----- 

**c++**

```c++
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(n);
        result[0] = 1;
         for(size_t i =1;i<n;++i)
         {
             result[i] = result[i-1] * nums[i-1];
         }
        int right = 1;
        for(int i = n-1; i>=0;--i)
        {
            result[i] *= right;
            right *= nums[i];
        }
        return result;   
    }
};
```