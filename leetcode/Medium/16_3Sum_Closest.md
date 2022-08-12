**c++**

```c++
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        //tiem out
        int res = 0;
        int min = INT_MAX;
        for(int i = 0 ; i<nums.size()-2;++i){
            int sum = nums[i];
            for(int j = i+1; j< nums.size()-1; ++j){
                sum += nums[j];
                for(int k = j+1; k< nums.size();++k){
                    sum+=nums[k];
                    int temp = target-sum;
                    if(abs(min) > abs(temp))
                    {
                        min = temp;
                        res = sum;
                    }
                        
                    sum-=nums[k];
            }
                sum-=nums[j];
        }
    }
        return res;
    }
};
```