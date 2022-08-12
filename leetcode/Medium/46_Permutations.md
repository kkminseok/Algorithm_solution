```c++
class Solution {
public:
    
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        sort(nums.begin(),nums.end());
        do{
            vector<int> temp;
            for(int i =0;i<nums.size();++i)
                temp.push_back(nums[i]);
            result.push_back(temp); 
        }while(next_permutation(nums.begin(),nums.end()));
        
        
        return result;
    }
};
```