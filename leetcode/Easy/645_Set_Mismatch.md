**c++**

```c++
class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        
        bool* countnum = new bool[nums.size()+1];
        memset(countnum,false,sizeof(bool) * (nums.size()+1));
        vector<int> result;
        for(size_t i=0;i<nums.size();++i)
        {
            if(countnum[nums[i]])
                result.push_back(nums[i]);
            countnum[nums[i]]=true;
        }
        bool check =false;
        for(size_t i=1;i<nums.size()+1;++i)
        {
            if(!countnum[i])
            {
                result.push_back(i);
                break;
            }
        }
        
        return result;
        
    }
};
```



**python**


```python
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        countnum = [0] * (len(nums)+1)
        result = []
        for i in range(len(nums)):
            if(countnum[nums[i]]):
                result.append(nums[i])
            countnum[nums[i]]=1
        check = 0
        for i in range(1,len(nums)+1):
            if countnum[i] == 0:
                result.append(i)
                break
        return result
        
```