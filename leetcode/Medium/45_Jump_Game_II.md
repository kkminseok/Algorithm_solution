**python**
```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        counting = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(1,nums[i]+1):
                if i + j >= len(nums):
                    continue
                if counting[i+j] == 0 :
                    counting[i+j] = counting[i]+1
                    
        return counting[len(nums)-1]
```    

-----  

**c++**
        
```c++
class Solution {
public:
    int jump(vector<int>& nums) {
        vector<int> v(nums.size(),0);
        v[0] = 0;
        for(size_t i =0;i<nums.size()-1;++i)
        {
           for(int j = 1;j<=nums[i] ; ++j)
           {
               if(i+j >=nums.size())
                   continue;
               if(v[i+j]==0)
                   v[i+j] = v[i]+1;
           }
        }
        return v[v.size()-1];
        
    }
};
```