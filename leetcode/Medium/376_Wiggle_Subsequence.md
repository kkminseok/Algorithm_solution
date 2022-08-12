**c++**

```c++
class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        if(nums.size()==1)
            return 1;
        int* DP = new int [nums.size()];
        DP[0]=1;
        bool minusC = true;
        bool plusC = true;
        
        for(size_t i =1;i<nums.size();++i)
        {
            if(minusC && nums[i-1] < nums[i])
            {
                minusC= false;
                plusC= true;
                DP[i] = DP[i-1]+1;
            }
            else if(plusC && nums[i-1]>nums[i])
            {
                plusC = false;
                minusC = true;
                DP[i] = DP[i-1] + 1;
            }
            else
                DP[i] = DP[i-1];
        }
        
        return DP[nums.size()-1];
    }
};
```

----- 


**python**

```python
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return 1
        DP = [0] * len(nums)
        DP[0]= 1
        plusC = 1
        minusC = 1
        
        for i in range(1,len(nums)):
            if minusC==1 and nums[i] < nums[i-1] : 
                minusC = 0
                plusC = 1
                DP[i] = DP[i-1] + 1
            elif plusC==1 and nums[i] > nums[i-1] : 
                minusC = 1
                plusC = 0
                DP[i] = DP[i-1] + 1
            else :
                DP[i] =DP[i-1]
         
        return DP[len(nums)-1]
```